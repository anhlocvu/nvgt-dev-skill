#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NVGT API Extractor
==================
Trích xuất toàn bộ API của NVGT từ mã nguồn:
1. Core Engine API -> nvgt_api_reference.md
2. Standard Libraries API -> nvgt_libraries_api.md
3. Plugins API -> nvgt_plugins_api.md

Tác giả: Vũ Anh Lộc (LC Boy) & Antigravity
"""

import os
import sys
import re
import glob
import argparse
import subprocess
from pathlib import Path

# Đảm bảo in UTF-8 không bị lỗi trên Windows console (cp1252)
if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

# ==============================================================================
# Helper Functions: String & Source Cleaning
# ==============================================================================

def clean_cpp_source(text: str) -> str:
    """Loại bỏ chú thích block và line của C++ nhưng giữ nguyên cấu trúc dòng."""
    text = re.sub(r'/\*.*?\*/', lambda m: '\n' * m.group(0).count('\n'), text, flags=re.DOTALL)
    text = re.sub(r'//[^\n]*', '', text)
    return text

def clean_angelscript_source(text: str) -> str:
    """Loại bỏ chú thích của AngelScript."""
    text = re.sub(r'/\*.*?\*/', lambda m: '\n' * m.group(0).count('\n'), text, flags=re.DOTALL)
    text = re.sub(r'//[^\n]*', '', text)
    return text

# Regex cho chuỗi literal C++ (hỗ trợ _O("..."), _("..."), nối chuỗi liền nhau "a" "b")
STRING_LITERAL_REGEX = r'(?:_O\s*\(\s*|_O_UNCHECKED\s*\(\s*|_\s*\(\s*|std::string\s*\(\s*|string\s*\(\s*)?((?:\s*"(?:[^"\\]|\\.)*"\s*)+)(?:\s*\))?'

def parse_cpp_string_literal(lit_str: str) -> str:
    """Bóc tách và unescape chuỗi literal C++ chuẩn xác."""
    if not lit_str:
        return ""
    parts = []
    for m in re.finditer(r'"((?:[^"\\]|\\.)*)"', lit_str):
        raw = m.group(1)
        # Unescape escaped quotes và backslashes
        unescaped = raw.replace(r'\"', '"').replace(r'\\', '\\')
        parts.append(unescaped)
    return "".join(parts).strip()

def extract_dump_strings(line: str) -> list:
    """Bóc tách các chuỗi trong dòng dump của AngelScript có hỗ trợ escape \\" và \\\\."""
    matches = re.findall(r'"((?:[^"\\]|\\.)*)"', line)
    return [m.replace(r'\"', '"').replace(r'\\', '\\') for m in matches]

def extract_param_types(params_str: str) -> str:
    """Tách danh sách kiểu tham số bỏ tên biến và giá trị mặc định để chuẩn hóa khóa."""
    params = []
    current = ""
    depth = 0
    for ch in params_str:
        if ch in '<(':
            depth += 1
            current += ch
        elif ch in '>)':
            depth -= 1
            current += ch
        elif ch == ',' and depth == 0:
            params.append(current.strip())
            current = ""
        else:
            current += ch
    if current.strip():
        params.append(current.strip())

    types = []
    for p in params:
        p = p.split('=')[0].strip()
        p = re.sub(r'array<([a-zA-Z0-9_]+)>', r'\1[]', p)
        p = re.sub(r'&\s+(in|out|inout)\b', r'&\1', p)
        p = p.replace('@+', '@')
        tokens = p.split()
        if len(tokens) > 1 and not tokens[-1].endswith('&') and not tokens[-1].endswith('@') and not tokens[-1].endswith(']'):
            if re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', tokens[-1]):
                p = " ".join(tokens[:-1])
        types.append(p)
    return ", ".join(types)

def canonical_func_key(sig: str) -> str:
    """Tạo khóa chuẩn hóa để nhận diện và loại bỏ hàm trùng lặp."""
    sig = sig.strip()
    m = re.match(r'^(.*?)\s*([a-zA-Z0-9_]+)\s*\((.*?)\)(.*)$', sig)
    if not m:
        # Chuẩn hóa biến/thuộc tính
        s = re.sub(r'&\s+(in|out|inout)\b', r'&\1', sig)
        s = re.sub(r'array<([a-zA-Z0-9_]+)>', r'\1[]', s)
        return " ".join(s.split())
    ret_type, name, params, suffix = m.groups()
    ret_type = re.sub(r'array<([a-zA-Z0-9_]+)>', r'\1[]', ret_type)
    ret_type = ret_type.replace('@+', '@').strip()
    param_types = extract_param_types(params)
    suffix = " ".join(suffix.split())
    return f"{ret_type} {name}({param_types}){suffix}"

def deduplicate_signatures(signatures):
    """
    Loại bỏ trùng lặp ngữ nghĩa giữa các signature (ví dụ giữa bản C++ tĩnh và bản runtime dump),
    ưu tiên giữ lại signature có đầy đủ tên tham số, giá trị mặc định, @+...
    """
    sig_map = {}
    for sig in signatures:
        key = canonical_func_key(sig)
        if key not in sig_map:
            sig_map[key] = sig
        else:
            existing = sig_map[key]
            # Điểm đánh giá: có tham số, có default value, có @+, dài hơn
            score_new = len(sig) + (25 if '=' in sig else 0) + (10 if '@+' in sig else 0) + (10 if '[]' in sig else 0)
            score_exist = len(existing) + (25 if '=' in existing else 0) + (10 if '@+' in existing else 0) + (10 if '[]' in existing else 0)
            if score_new > score_exist:
                sig_map[key] = sig
    return set(sig_map.values())


# ==============================================================================
# 1. C++ API Extractor (Core Engine & Plugins)
# ==============================================================================

class CppApiExtractor:
    """Trích xuất API AngelScript được đăng ký từ mã nguồn C++ (engine->Register...)."""

    def __init__(self, include_dirs=None):
        self.include_dirs = include_dirs or []
        self.global_functions = set()
        self.global_properties = set()
        self.classes = {}       # class_name -> {'behaviours': set(), 'properties': set(), 'methods': set()}
        self.enums = {}         # enum_name -> set(values)
        self.interfaces = {}    # intf_name -> set(methods)
        self.typedefs = {}      # type_name -> original_type

        # Compile regular expressions
        self.re_glob_fn  = re.compile(r'RegisterGlobalFunction\s*\(\s*' + STRING_LITERAL_REGEX)
        self.re_glob_pr  = re.compile(r'RegisterGlobalProperty\s*\(\s*' + STRING_LITERAL_REGEX)
        self.re_obj_type = re.compile(r'RegisterObjectType\s*\(\s*' + STRING_LITERAL_REGEX)
        self.re_obj_mthd = re.compile(r'RegisterObjectMethod\s*\(\s*' + STRING_LITERAL_REGEX + r'\s*,\s*' + STRING_LITERAL_REGEX)
        self.re_obj_prop = re.compile(r'RegisterObjectProperty\s*\(\s*' + STRING_LITERAL_REGEX + r'\s*,\s*' + STRING_LITERAL_REGEX)
        self.re_obj_beh  = re.compile(r'RegisterObjectBehaviour\s*\(\s*' + STRING_LITERAL_REGEX + r'\s*,\s*(\w+)\s*,\s*' + STRING_LITERAL_REGEX)
        self.re_intf     = re.compile(r'RegisterInterface\s*\(\s*' + STRING_LITERAL_REGEX)
        self.re_intf_m   = re.compile(r'RegisterInterfaceMethod\s*\(\s*' + STRING_LITERAL_REGEX + r'\s*,\s*' + STRING_LITERAL_REGEX)
        self.re_enum     = re.compile(r'RegisterEnum\s*\(\s*' + STRING_LITERAL_REGEX)
        self.re_enum_val = re.compile(r'RegisterEnumValue\s*\(\s*' + STRING_LITERAL_REGEX + r'\s*,\s*' + STRING_LITERAL_REGEX)
        self.re_funcdef  = re.compile(r'RegisterFuncdef\s*\(\s*' + STRING_LITERAL_REGEX)
        self.re_typedef  = re.compile(r'RegisterTypedef\s*\(\s*' + STRING_LITERAL_REGEX + r'\s*,\s*' + STRING_LITERAL_REGEX)

    def _ensure_class(self, cls_name: str):
        if cls_name not in self.classes:
            self.classes[cls_name] = {'behaviours': set(), 'properties': set(), 'methods': set()}

    def scan_directory(self, directory: str, recursive: bool = True):
        """Quét toàn bộ file .cpp và .h trong thư mục."""
        pattern_cpp = os.path.join(directory, "**", "*.cpp") if recursive else os.path.join(directory, "*.cpp")
        pattern_h   = os.path.join(directory, "**", "*.h") if recursive else os.path.join(directory, "*.h")
        pattern_mm  = os.path.join(directory, "**", "*.mm") if recursive else os.path.join(directory, "*.mm")

        file_list = glob.glob(pattern_cpp, recursive=recursive) + \
                    glob.glob(pattern_h, recursive=recursive) + \
                    glob.glob(pattern_mm, recursive=recursive)

        for path in file_list:
            self.scan_file(path)

    def scan_file(self, filepath: str):
        """Phân tích một file mã nguồn C++ cụ thể."""
        try:
            with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                content = clean_cpp_source(f.read())
        except Exception:
            return

        # 1. Global Functions
        for m in self.re_glob_fn.finditer(content):
            fn = parse_cpp_string_literal(m.group(1))
            if fn and '(' in fn:
                self.global_functions.add(fn)

        # 2. Funcdefs (Thêm vào global functions dạng `funcdef ...`)
        for m in self.re_funcdef.finditer(content):
            fd = parse_cpp_string_literal(m.group(1))
            if fd:
                if not fd.startswith("funcdef "):
                    fd = "funcdef " + fd
                self.global_functions.add(fd)

        # 3. Global Properties
        for m in self.re_glob_pr.finditer(content):
            pr = parse_cpp_string_literal(m.group(1))
            if pr and '(' not in pr:
                self.global_properties.add(pr)

        # 4. Object Types
        for m in self.re_obj_type.finditer(content):
            cls = parse_cpp_string_literal(m.group(1))
            if cls:
                self._ensure_class(cls)

        # 5. Interfaces
        for m in self.re_intf.finditer(content):
            intf = parse_cpp_string_literal(m.group(1))
            if intf:
                self._ensure_class(intf)

        # 6. Object Methods
        for m in self.re_obj_mthd.finditer(content):
            cls = parse_cpp_string_literal(m.group(1))
            decl = parse_cpp_string_literal(m.group(2))
            if cls and decl:
                self._ensure_class(cls)
                self.classes[cls]['methods'].add(decl)

        # 7. Interface Methods
        for m in self.re_intf_m.finditer(content):
            intf = parse_cpp_string_literal(m.group(1))
            decl = parse_cpp_string_literal(m.group(2))
            if intf and decl:
                self._ensure_class(intf)
                self.classes[intf]['methods'].add(decl)

        # 8. Object Properties
        for m in self.re_obj_prop.finditer(content):
            cls = parse_cpp_string_literal(m.group(1))
            decl = parse_cpp_string_literal(m.group(2))
            if cls and decl:
                self._ensure_class(cls)
                self.classes[cls]['properties'].add(decl)

        # 9. Object Behaviours (Constructors, Factories, Operators...)
        for m in self.re_obj_beh.finditer(content):
            cls = parse_cpp_string_literal(m.group(1))
            beh = m.group(2).strip()
            decl = parse_cpp_string_literal(m.group(3))
            if cls and decl:
                self._ensure_class(cls)
                # Bỏ qua các destructor nội bộ (DESTRUCT, RELEASE, ADDREF)
                if 'DESTRUCT' not in beh and 'RELEASE' not in beh and 'ADDREF' not in beh:
                    self.classes[cls]['behaviours'].add(decl)

        # 10. Enums
        for m in self.re_enum.finditer(content):
            en = parse_cpp_string_literal(m.group(1))
            if en and en not in self.enums:
                self.enums[en] = set()

        # 11. Enum Values
        for m in self.re_enum_val.finditer(content):
            en = parse_cpp_string_literal(m.group(1))
            v = parse_cpp_string_literal(m.group(2))
            if en and v:
                if en not in self.enums:
                    self.enums[en] = set()
                self.enums[en].add(v)

        # 12. Typedefs
        for m in self.re_typedef.finditer(content):
            name = parse_cpp_string_literal(m.group(1))
            orig = parse_cpp_string_literal(m.group(2))
            if name and orig:
                self.typedefs[name] = orig

    def try_runtime_engine_dump(self, nvgt_executable: str = "nvgt"):
        """
        Nếu máy có sẵn binary `nvgt` (hoặc c:\\nvgt\\nvgt.exe), ta thực hiện một lệnh dump nhanh
        từ AngelScript runtime để bổ sung các kiểu template khởi tạo động (như atomic_int, mutex).
        """
        script_code = """
        void main() {
            file f;
            if (f.open("_temp_dump.txt", "w")) {
                script_dump_engine_configuration(f);
                f.close();
            }
        }
        """
        temp_script = "_temp_dump.nvgt"
        temp_output = "_temp_dump.txt"
        try:
            with open(temp_script, "w", encoding="utf-8") as f:
                f.write(script_code)

            cmd = [nvgt_executable, temp_script]
            res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=10)
            if os.path.exists(temp_output):
                self._merge_runtime_dump(temp_output)
        except Exception:
            pass
        finally:
            if os.path.exists(temp_script):
                try: os.remove(temp_script)
                except Exception: pass
            if os.path.exists(temp_output):
                try: os.remove(temp_output)
                except Exception: pass

    def _merge_runtime_dump(self, dump_file: str):
        """Hòa nhập dữ liệu từ runtime dump vào kết quả quét tĩnh để không sót bất kỳ kiểu template nào."""
        try:
            with open(dump_file, "r", encoding="utf-8", errors="ignore") as f:
                lines = f.readlines()
        except Exception:
            return

        current_enum = None
        for line in lines:
            line = line.strip()
            if not line or line.startswith("//"):
                continue

            # Enums
            if line.startswith("enum "):
                current_enum = line[5:].strip()
                if current_enum not in self.enums:
                    self.enums[current_enum] = set()
            elif line.startswith("enumval "):
                parts = line.split()
                if len(parts) >= 3:
                    ename = parts[1]
                    eval_name = parts[2]
                    if ename not in self.enums:
                        self.enums[ename] = set()
                    self.enums[ename].add(eval_name)

            # Object types
            elif line.startswith("objtype "):
                strs = extract_dump_strings(line)
                if strs:
                    cls = strs[0]
                    self._ensure_class(cls)

            # Object methods
            elif line.startswith("objmthd "):
                strs = extract_dump_strings(line)
                if len(strs) >= 2:
                    cls, decl = strs[0], strs[1]
                    self._ensure_class(cls)
                    self.classes[cls]['methods'].add(decl)

            # Object properties
            elif line.startswith("objprop "):
                strs = extract_dump_strings(line)
                if len(strs) >= 2:
                    cls, decl = strs[0], strs[1]
                    self._ensure_class(cls)
                    self.classes[cls]['properties'].add(decl)

            # Object behaviours
            elif line.startswith("objbeh "):
                strs = extract_dump_strings(line)
                if len(strs) >= 2:
                    cls, decl = strs[0], strs[1]
                    # Lọc các hàm nội bộ $beh, destructors
                    if not decl.startswith("void $beh") and not decl.startswith("bool $beh") and not decl.startswith("int $beh"):
                        self._ensure_class(cls)
                        self.classes[cls]['behaviours'].add(decl)

            # Global functions
            elif line.startswith("func "):
                strs = extract_dump_strings(line)
                if strs:
                    self.global_functions.add(strs[0])

            # Global properties
            elif line.startswith("prop "):
                strs = extract_dump_strings(line)
                if strs:
                    self.global_properties.add(strs[0])


# ==============================================================================
# 2. AngelScript Extractor (Standard Libraries .nvgt)
# ==============================================================================

class AngelScriptExtractor:
    """Phân tích cú pháp sâu mã nguồn AngelScript (.nvgt) cho thư viện chuẩn."""

    @staticmethod
    def _strip_blocks(code: str) -> str:
        """Xóa trắng nội dung class, enum, interface, funcdef để lấy các khai báo toàn cục (depth 0)."""
        # Blank out enums, interfaces, funcdefs
        patterns = [
            re.compile(r'(?:shared\s+)?enum\s+\w+\s*\{[^}]*\}', re.MULTILINE),
            re.compile(r'(?:shared\s+)?interface\s+\w+(?:\s*:[^{]+)?\s*\{[^}]*\}', re.MULTILINE),
            re.compile(r'funcdef\s+[^;]+;', re.MULTILINE)
        ]
        for p in patterns:
            code = p.sub(lambda m: ' ' * len(m.group(0)), code)

        # Blank out class blocks bằng bộ đếm ngoặc nhọn
        class_header = re.compile(r'(?:shared\s+)?(?:abstract\s+)?class\s+\w+(?:\s*:[^{]+)?\s*\{')
        while True:
            m = class_header.search(code)
            if not m:
                break
            start_brace = m.end() - 1
            depth = 0
            end_brace = -1
            in_str = False
            str_q = ''
            i = start_brace
            while i < len(code):
                ch = code[i]
                if in_str:
                    if ch == '\\':
                        i += 2
                        continue
                    elif ch == str_q:
                        in_str = False
                else:
                    if ch in ('"', "'"):
                        in_str = True
                        str_q = ch
                    elif ch == '{':
                        depth += 1
                    elif ch == '}':
                        depth -= 1
                        if depth == 0:
                            end_brace = i
                            break
                i += 1
            if end_brace != -1:
                total_len = end_brace - m.start() + 1
                code = code[:m.start()] + (' ' * total_len) + code[end_brace+1:]
            else:
                break
        return code

    @classmethod
    def parse_file(cls, filepath: str) -> dict:
        """Trích xuất toàn bộ thành phần API của một file .nvgt."""
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            raw_code = f.read()

        code = clean_angelscript_source(raw_code)

        result = {
            'enums': {},             # enum_name -> [values]
            'interfaces': {},        # intf_name -> [methods]
            'classes': {},           # class_name -> {'constructors': [], 'methods': [], 'properties': []}
            'funcdefs': [],          # [signature]
            'global_functions': [],  # [signature]
            'global_properties': []  # [signature]
        }

        # 1. Enums
        enum_pattern = re.compile(r'(?:shared\s+)?enum\s+(\w+)\s*\{([^}]*)\}', re.MULTILINE)
        for m in enum_pattern.finditer(code):
            ename = m.group(1)
            body = m.group(2)
            vals = []
            for line in body.split(','):
                v = line.strip()
                if v:
                    val_ident = v.split('=')[0].strip()
                    if val_ident:
                        vals.append(val_ident)
            result['enums'][ename] = vals

        # 2. Funcdefs
        funcdef_pattern = re.compile(r'funcdef\s+([^;]+);')
        for m in funcdef_pattern.finditer(code):
            result['funcdefs'].append(f"funcdef {m.group(1).strip()}")

        # 3. Interfaces
        intf_pattern = re.compile(r'(?:shared\s+)?interface\s+(\w+)(?:\s*:[^{]+)?\s*\{([^}]*)\}', re.MULTILINE)
        for m in intf_pattern.finditer(code):
            iname = m.group(1)
            body = m.group(2)
            methods = []
            for stmt in body.split(';'):
                s = " ".join(stmt.split()).strip()
                if s:
                    methods.append(s)
            result['interfaces'][iname] = methods

        # 4. Classes (Duyệt theo cặp ngoặc nhọn {})
        class_header_pattern = re.compile(r'(?:shared\s+)?(?:abstract\s+)?class\s+(\w+)(?:\s*:[^{]+)?\s*\{')
        for m in class_header_pattern.finditer(code):
            cname = m.group(1)
            start_pos = m.end() - 1
            depth = 0
            end_pos = -1
            in_str = False
            str_q = ''
            idx = start_pos
            while idx < len(code):
                ch = code[idx]
                if in_str:
                    if ch == '\\':
                        idx += 2
                        continue
                    elif ch == str_q:
                        in_str = False
                else:
                    if ch in ('"', "'"):
                        in_str = True
                        str_q = ch
                    elif ch == '{':
                        depth += 1
                    elif ch == '}':
                        depth -= 1
                        if depth == 0:
                            end_pos = idx
                            break
                idx += 1

            if end_pos != -1:
                class_body = code[start_pos+1:end_pos]
                result['classes'][cname] = cls._parse_class_body(cname, class_body)

        # 5. Top-level Functions & Properties
        top_code = cls._strip_blocks(code)
        funcs, props = cls._extract_top_statements(top_code)
        result['global_functions'] = funcs
        result['global_properties'] = props

        return result

    @classmethod
    def _parse_class_body(cls, class_name: str, body: str) -> dict:
        info = {'constructors': [], 'methods': [], 'properties': []}
        idx = 0
        current_stmt = ""
        depth = 0
        in_str = False
        str_q = ''

        while idx < len(body):
            ch = body[idx]
            if in_str:
                if ch == '\\':
                    idx += 2
                    continue
                elif ch == str_q:
                    in_str = False
                current_stmt += ch
            else:
                if ch in ('"', "'"):
                    in_str = True
                    str_q = ch
                    current_stmt += ch
                elif ch == '{':
                    if depth == 0:
                        header = " ".join(current_stmt.split()).strip()
                        if header:
                            cls._categorize_class_member(class_name, header, info)
                        current_stmt = ""
                    depth += 1
                elif ch == '}':
                    depth -= 1
                    if depth == 0:
                        current_stmt = ""
                elif ch == ';':
                    if depth == 0:
                        stmt = " ".join(current_stmt.split()).strip()
                        if stmt:
                            cls._categorize_class_member(class_name, stmt, info)
                        current_stmt = ""
                else:
                    if depth == 0:
                        current_stmt += ch
            idx += 1

        return info

    @classmethod
    def _categorize_class_member(cls, class_name: str, decl: str, info: dict):
        decl = re.sub(r'\s+', ' ', decl).strip()
        if not decl:
            return
        # Destructor
        if decl.startswith(f"~{class_name}"):
            return
        # Constructor
        if decl.startswith(f"{class_name}(") or decl.startswith(f"{class_name} ("):
            info['constructors'].append(decl)
            return
        # Method: có dấu ngoặc tròn ()
        if '(' in decl and ')' in decl:
            info['methods'].append(decl)
        else:
            # Property / Field
            info['properties'].append(decl)

    @classmethod
    def _extract_top_statements(cls, top_code: str):
        funcs = []
        props = []
        idx = 0
        current_stmt = ""
        depth = 0
        in_str = False
        str_q = ''

        while idx < len(top_code):
            ch = top_code[idx]
            if in_str:
                if ch == '\\':
                    idx += 2
                    continue
                elif ch == str_q:
                    in_str = False
                current_stmt += ch
            else:
                if ch in ('"', "'"):
                    in_str = True
                    str_q = ch
                    current_stmt += ch
                elif ch == '{':
                    if depth == 0:
                        header = " ".join(current_stmt.split()).strip()
                        header = re.sub(r'#(?:if|ifdef|ifndef|else|endif|include|pragma)[^\n]*', '', header).strip()
                        if header and '(' in header and ')' in header:
                            funcs.append(header)
                        current_stmt = ""
                    depth += 1
                elif ch == '}':
                    depth -= 1
                    if depth == 0:
                        current_stmt = ""
                elif ch == ';':
                    if depth == 0:
                        stmt = " ".join(current_stmt.split()).strip()
                        stmt = re.sub(r'#(?:if|ifdef|ifndef|else|endif|include|pragma)[^\n]*', '', stmt).strip()
                        if stmt:
                            if '(' in stmt and ')' in stmt:
                                funcs.append(stmt)
                            else:
                                props.append(stmt)
                        current_stmt = ""
                else:
                    if depth == 0:
                        current_stmt += ch
            idx += 1

        return funcs, props


# ==============================================================================
# 3. Markdown Document Generators
# ==============================================================================

class MarkdownGenerator:
    """Định dạng và xuất 3 file Markdown theo phong cách chuẩn mực của NVGT."""

    @staticmethod
    def generate_core_api_markdown(extractor: CppApiExtractor, output_path: str):
        """Tạo file nvgt_api_reference.md (Core Engine)."""
        lines = []
        lines.append("# NVGT API Reference (Core Engine)\n")
        lines.append("This document contains the API definitions automatically extracted from the NVGT C++ source code.\n")

        # 1. Global Functions
        lines.append("## Global Functions")
        unique_funcs = deduplicate_signatures(extractor.global_functions)
        for fn in sorted(unique_funcs, key=str.casefold):
            lines.append(f"- `{fn}`")
        lines.append("")

        # 2. Global Properties
        lines.append("## Global Properties")
        unique_props = deduplicate_signatures(extractor.global_properties)
        for pr in sorted(unique_props, key=str.casefold):
            lines.append(f"- `{pr}`")
        lines.append("")

        # 3. Classes
        lines.append("## Classes")
        for cls_name in sorted(extractor.classes.keys(), key=str.casefold):
            data = extractor.classes[cls_name]
            lines.append(f"### Class `{cls_name}`")

            # Behaviours / Constructors
            behs = deduplicate_signatures(data['behaviours'])
            if behs:
                lines.append("##### Behaviours / Constructors")
                for beh in sorted(behs, key=str.casefold):
                    lines.append(f"- `{beh}`")

            # Properties
            props = deduplicate_signatures(data['properties'])
            if props:
                lines.append("##### Properties")
                for prop in sorted(props, key=str.casefold):
                    lines.append(f"- `{prop}`")

            # Methods
            mthds = deduplicate_signatures(data['methods'])
            if mthds:
                lines.append("##### Methods")
                for mthd in sorted(mthds, key=str.casefold):
                    lines.append(f"- `{mthd}`")

            lines.append("")

        # 4. Enums
        lines.append("## Enums")
        for enum_name in sorted(extractor.enums.keys(), key=str.casefold):
            lines.append(f"### Enum `{enum_name}`")
            vals = extractor.enums[enum_name]
            for v in sorted(vals, key=str.casefold):
                lines.append(f"- `{v}`")
            lines.append("")

        with open(output_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines).strip() + "\n")

    @staticmethod
    def generate_libraries_markdown(libraries: dict, output_path: str):
        """Tạo file nvgt_libraries_api.md (Standard Libraries .nvgt)."""
        lines = []
        lines.append("# NVGT Standard Libraries & Plugins API Reference\n")
        lines.append("> **IMPORTANT NOTE:** These syntaxes belong to standard libraries (includes) and plugins. To use them, you MUST include the corresponding file at the top of your script. Example:")
        lines.append('> `#include "sound_pool.nvgt"`\n')

        for lib_name in sorted(libraries.keys(), key=str.casefold):
            data = libraries[lib_name]
            lines.append("---")
            lines.append(f"## Library: `{lib_name}`")
            lines.append(f'**Syntax to use:** `#include "{lib_name}"`\n')

            # Global Functions
            if data['global_functions'] or data['funcdefs']:
                lines.append("### Global Functions")
                all_funcs = sorted(list(data['global_functions']) + list(data['funcdefs']), key=str.casefold)
                for fn in all_funcs:
                    lines.append(f"- `{fn}`")
                lines.append("")

            # Global Properties
            if data['global_properties']:
                lines.append("### Global Properties")
                for prop in sorted(data['global_properties'], key=str.casefold):
                    lines.append(f"- `{prop}`")
                lines.append("")

            # Classes
            if data['classes']:
                lines.append("### Classes")
                for cls_name in sorted(data['classes'].keys(), key=str.casefold):
                    cdata = data['classes'][cls_name]
                    lines.append(f"#### Class `{cls_name}`")
                    # Gộp constructors, properties, methods theo phong cách thư viện
                    items = []
                    for ctor in sorted(cdata['constructors'], key=str.casefold):
                        items.append(ctor)
                    for pr in sorted(cdata['properties'], key=str.casefold):
                        items.append(pr)
                    for m in sorted(cdata['methods'], key=str.casefold):
                        items.append(m)

                    for item in items:
                        lines.append(f"- `{item}`")
                    lines.append("")

            # Interfaces
            if data['interfaces']:
                lines.append("### Interfaces")
                for iname in sorted(data['interfaces'].keys(), key=str.casefold):
                    lines.append(f"#### Interface `{iname}`")
                    for m in sorted(data['interfaces'][iname], key=str.casefold):
                        lines.append(f"- `{m}`")
                    lines.append("")

            # Enums
            if data['enums']:
                lines.append("### Enums")
                for ename in sorted(data['enums'].keys(), key=str.casefold):
                    lines.append(f"#### Enum `{ename}`")
                    for val in sorted(data['enums'][ename], key=str.casefold):
                        lines.append(f"- `{val}`")
                    lines.append("")

        with open(output_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines).strip() + "\n")

    @staticmethod
    def generate_plugins_markdown(plugins: dict, output_path: str):
        """Tạo file nvgt_plugins_api.md (C++ Plugins)."""
        lines = []
        lines.append("# NVGT Plugins API Reference\n")
        lines.append("> **IMPORTANT NOTE:** These syntaxes belong to NVGT plugins written in C++. To use them, you MUST include the pragma directive at the top of your script. Example:")
        lines.append('> `#pragma plugin("plugin_name")`\n')

        for plugin_name in sorted(plugins.keys(), key=str.casefold):
            pdata = plugins[plugin_name]
            lines.append("---")
            lines.append(f"## Plugin: `{plugin_name}`")
            lines.append(f'**Syntax to use:** `#pragma plugin("{plugin_name}")`\n')

            # Global Functions
            if pdata['global_functions']:
                lines.append("### Global Functions")
                unique_fn = deduplicate_signatures(pdata['global_functions'])
                for fn in sorted(unique_fn, key=str.casefold):
                    lines.append(f"- `{fn}`")
                lines.append("")

            # Global Properties
            if pdata['global_properties']:
                lines.append("### Global Properties")
                unique_pr = deduplicate_signatures(pdata['global_properties'])
                for prop in sorted(unique_pr, key=str.casefold):
                    lines.append(f"- `{prop}`")
                lines.append("")

            # Classes
            if pdata['classes']:
                lines.append("### Classes")
                for cls_name in sorted(pdata['classes'].keys(), key=str.casefold):
                    cdata = pdata['classes'][cls_name]
                    lines.append(f"#### Class `{cls_name}`")

                    behs = deduplicate_signatures(cdata['behaviours'])
                    if behs:
                        lines.append("##### Behaviours / Constructors")
                        for beh in sorted(behs, key=str.casefold):
                            lines.append(f"- `{beh}`")

                    props = deduplicate_signatures(cdata['properties'])
                    if props:
                        lines.append("##### Properties")
                        for prop in sorted(props, key=str.casefold):
                            lines.append(f"- `{prop}`")

                    mthds = deduplicate_signatures(cdata['methods'])
                    if mthds:
                        lines.append("##### Methods")
                        for m in sorted(mthds, key=str.casefold):
                            lines.append(f"- `{m}`")

                    lines.append("")

            # Enums
            if pdata['enums']:
                lines.append("### Enums")
                for ename in sorted(pdata['enums'].keys(), key=str.casefold):
                    lines.append(f"#### Enum `{ename}`")
                    for val in sorted(pdata['enums'][ename], key=str.casefold):
                        lines.append(f"- `{val}`")
                    lines.append("")

        with open(output_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines).strip() + "\n")


# ==============================================================================
# 4. Main Controller & Orchestrator
# ==============================================================================

def main():
    parser = argparse.ArgumentParser(description="NVGT API Extractor - Soi từng ngóc ngách mã nguồn NVGT để xuất bộ API hoàn chỉnh")
    parser.add_argument("--nvgt-dir", default=None, help="Đường dẫn đến thư mục chứa mã nguồn NVGT (mặc định tự tìm 'nvgt' hoặc thư mục hiện tại)")
    parser.add_argument("--output-dir", default=".", help="Thư mục xuất 3 file markdown (mặc định: thư mục hiện tại)")
    parser.add_argument("--skip-runtime-dump", action="store_true", help="Bỏ qua bước thử dump runtime từ nvgt.exe")
    args = parser.parse_args()

    # Xác định thư mục nvgt
    nvgt_dir = args.nvgt_dir
    if not nvgt_dir:
        if os.path.exists("nvgt") and os.path.isdir("nvgt"):
            nvgt_dir = "nvgt"
        elif os.path.exists("src") and os.path.isdir("src"):
            nvgt_dir = "."
        else:
            print("Lỗi: Không tìm thấy thư mục mã nguồn NVGT. Vui lòng truyền qua --nvgt-dir.")
            sys.exit(1)

    nvgt_dir = os.path.abspath(nvgt_dir)
    output_dir = os.path.abspath(args.output_dir)
    os.makedirs(output_dir, exist_ok=True)

    print(f"==================================================")
    print(f"  NVGT API Extractor - Đang khởi chạy...")
    print(f"  Thư mục NVGT:   {nvgt_dir}")
    print(f"  Thư mục đầu ra: {output_dir}")
    print(f"==================================================\n")

    # --------------------------------------------------------------------------
    # BƯỚC 1: Trích xuất Core Engine API -> nvgt_api_reference.md
    # --------------------------------------------------------------------------
    print("[1/3] Đang quét mã nguồn Core Engine (C++)...")
    core_extractor = CppApiExtractor()

    src_dir = os.path.join(nvgt_dir, "src")
    addon_dir = os.path.join(nvgt_dir, "ASAddon")

    if os.path.exists(src_dir):
        core_extractor.scan_directory(src_dir)
    if os.path.exists(addon_dir):
        core_extractor.scan_directory(addon_dir)

    # Thử runtime dump nếu nvgt khả dụng trên hệ thống
    if not args.skip_runtime_dump:
        for nvgt_bin in ["nvgt", "c:\\nvgt\\nvgt.exe"]:
            try:
                core_extractor.try_runtime_engine_dump(nvgt_bin)
                break
            except Exception:
                pass

    core_out_file = os.path.join(output_dir, "nvgt_api_reference.md")
    MarkdownGenerator.generate_core_api_markdown(core_extractor, core_out_file)

    print(f"  -> Hoàn thành nvgt_api_reference.md:")
    print(f"     + Global Functions:  {len(core_extractor.global_functions)}")
    print(f"     + Global Properties: {len(core_extractor.global_properties)}")
    print(f"     + Classes:           {len(core_extractor.classes)}")
    print(f"     + Enums:             {len(core_extractor.enums)}")
    print(f"     + Kích thước:        {os.path.getsize(core_out_file):,} bytes\n")

    # --------------------------------------------------------------------------
    # BƯỚC 2: Trích xuất Standard Libraries API -> nvgt_libraries_api.md
    # --------------------------------------------------------------------------
    print("[2/3] Đang quét các thư viện chuẩn AngelScript (.nvgt)...")
    libraries_data = {}
    include_dir = os.path.join(nvgt_dir, "release", "include")
    if not os.path.exists(include_dir):
        # Dự phòng tìm thư mục include khác nếu có
        for inc_cand in [os.path.join(nvgt_dir, "include"), os.path.join(nvgt_dir, "ASAddon", "include")]:
            if os.path.exists(inc_cand):
                include_dir = inc_cand
                break

    if os.path.exists(include_dir):
        nvgt_files = sorted(glob.glob(os.path.join(include_dir, "*.nvgt")))
        for fpath in nvgt_files:
            lib_name = os.path.basename(fpath)
            libraries_data[lib_name] = AngelScriptExtractor.parse_file(fpath)

    lib_out_file = os.path.join(output_dir, "nvgt_libraries_api.md")
    MarkdownGenerator.generate_libraries_markdown(libraries_data, lib_out_file)

    total_lib_funcs = sum(len(d['global_functions']) + len(d['funcdefs']) for d in libraries_data.values())
    total_lib_classes = sum(len(d['classes']) for d in libraries_data.values())
    total_lib_enums = sum(len(d['enums']) for d in libraries_data.values())
    print(f"  -> Hoàn thành nvgt_libraries_api.md:")
    print(f"     + Số thư viện:       {len(libraries_data)}")
    print(f"     + Tổng Classes:      {total_lib_classes}")
    print(f"     + Tổng Functions:    {total_lib_funcs}")
    print(f"     + Tổng Enums:        {total_lib_enums}")
    print(f"     + Kích thước:        {os.path.getsize(lib_out_file):,} bytes\n")

    # --------------------------------------------------------------------------
    # BƯỚC 3: Trích xuất Plugins API -> nvgt_plugins_api.md
    # --------------------------------------------------------------------------
    print("[3/3] Đang quét tất cả Plugins (official + extra + integrated)...")
    plugins_data = {}

    plugin_search_paths = [
        os.path.join(nvgt_dir, "plugin"),
        os.path.join(nvgt_dir, "extra", "plugin", "integrated"),
        os.path.join(nvgt_dir, "extra", "plugin", "external"),
    ]

    for base_p in plugin_search_paths:
        if not os.path.exists(base_p):
            continue
        for entry in os.listdir(base_p):
            pdir = os.path.join(base_p, entry)
            if not os.path.isdir(pdir):
                continue
            # Kiểm tra xem có file source c++ không
            cpp_files = glob.glob(os.path.join(pdir, "**", "*.cpp"), recursive=True)
            if not cpp_files:
                continue

            plugin_name = entry
            p_extractor = CppApiExtractor()
            p_extractor.scan_directory(pdir)

            if p_extractor.classes or p_extractor.global_functions or p_extractor.global_properties or p_extractor.enums:
                plugins_data[plugin_name] = {
                    'classes': p_extractor.classes,
                    'global_functions': p_extractor.global_functions,
                    'global_properties': p_extractor.global_properties,
                    'enums': p_extractor.enums,
                }

    plugin_out_file = os.path.join(output_dir, "nvgt_plugins_api.md")
    MarkdownGenerator.generate_plugins_markdown(plugins_data, plugin_out_file)

    total_p_funcs = sum(len(d['global_functions']) for d in plugins_data.values())
    total_p_classes = sum(len(d['classes']) for d in plugins_data.values())
    total_p_enums = sum(len(d['enums']) for d in plugins_data.values())
    print(f"  -> Hoàn thành nvgt_plugins_api.md:")
    print(f"     + Số Plugins:        {len(plugins_data)} ({', '.join(sorted(plugins_data.keys()))})")
    print(f"     + Tổng Classes:      {total_p_classes}")
    print(f"     + Tổng Functions:    {total_p_funcs}")
    print(f"     + Tổng Enums:        {total_p_enums}")
    print(f"     + Kích thước:        {os.path.getsize(plugin_out_file):,} bytes\n")

    print("==================================================")
    print("  ĐÃ XUẤT THÀNH CÔNG TOÀN BỘ 3 FILE API REFERENCE!")
    print("==================================================")

if __name__ == "__main__":
    main()
