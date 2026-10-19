# NVGT API Reference (Core Engine)

This document contains the API definitions automatically extracted from the NVGT C++ source code.

## Global Functions
- `aabb aabb_create_from_triangle(const vector[]@ points)`
- `ARCHITECTURE get_PROCESSOR_ARCHITECTURE() property`
- `audio_engine@+ get_sound_default_engine() property`
- `audio_error_state get_SOUNDSYSTEM_LAST_ERROR() property`
- `bool android_request_permission(const string&in permission, android_permission_request_callback@ callback = null, const string&in callback_data = "")`
- `bool android_show_toast(const string&in message, int duration, int gravity = -1, int x_offset = 0, int y_offset = 0)`
- `bool boxes_intersect(float minx1, float maxx1, float miny1, float maxy1, float r1, float minx2, float maxx2, float miny2, float maxy2, float r2)`
- `bool chdir(const string& in directory)`
- `bool clipboard_set_raw_text(const string& in text)`
- `bool clipboard_set_text(const string& in text)`
- `bool close_to(double a, double b, double epsilon = 0.0000000001)`
- `bool close_to(float a, float b, float epsilon = 0.00001f)`
- `bool datetime_is_leap_year(int year)`
- `bool datetime_is_valid(int year, int month, int day, int hour = 0, int minute = 0, int second = 0, int millisecond = 0, int microsecond = 0)`
- `bool datetime_is_valid_format(const string&in datetime)`
- `bool datetime_is_valid_format_string(const string&in fmt)`
- `bool destroy_window()`
- `bool directory_create(const string& in path)`
- `bool directory_delete(const string& in path, bool recursive = true)`
- `bool directory_exists(const string& in path)`
- `bool environment_variable_exists(const string&in variable)`
- `bool file_copy(const string& in source, const string& in destination, bool overwrite)`
- `bool file_delete(const string& in path)`
- `bool file_exists(const string& in path)`
- `bool file_hard_link(const string& in source, const string&in destination)`
- `bool file_move(const string& in source, const string& in destination)`
- `bool file_put_contents(const string&in filename, const string&in contents, bool append = false)`
- `bool file_touch(const string& in path, const timestamp& in new_time = timestamp())`
- `bool fnmatch(const string& in text, const string& in pattern)`
- `bool focus_window()`
- `bool get_cursor_visible() property`
- `bool get_KEYBOARD_AVAILABLE() property`
- `bool get_MOUSE_AVAILABLE() property`
- `bool get_mouse_grab() property`
- `bool get_SCREEN_KEYBOARD_SUPPORTED() property`
- `bool get_SCREEN_READER_AVAILABLE() property`
- `bool get_SCRIPT_COMPILED() property`
- `bool get_sound_3d_attenuator_enabled(int attenuator_id)`
- `bool get_sound_3d_panner_enabled(int panner_id)`
- `bool get_sound_global_hrtf() property`
- `bool get_system_is_chromebook() property`
- `bool get_system_is_DeX_mode() property`
- `bool get_system_is_mobile() property`
- `bool get_system_is_tablet() property`
- `bool get_system_is_unix() property`
- `bool get_system_is_windows() property`
- `bool get_thread_is_main() property`
- `bool hide_window()`
- `bool http_credentials_is_basic(const http_request&in request)`
- `bool http_credentials_is_basic(const string&in header)`
- `bool http_credentials_is_digest(const http_request&in request)`
- `bool http_credentials_is_digest(const string&in header)`
- `bool http_credentials_is_ntlm(const http_request&in request)`
- `bool http_credentials_is_ntlm(const string&in header)`
- `bool http_credentials_is_proxy_basic(const http_request&in request)`
- `bool http_credentials_is_proxy_digest(const http_request&in request)`
- `bool http_credentials_is_proxy_ntlm(const http_request&in request)`
- `bool info_box(const string& in title, const string& in caption, const string& in text, uint64 flags = 0)`
- `bool install_keyhook()`
- `bool insure_key_up(int key)`
- `bool is_console_available()`
- `bool is_debugger_present()`
- `bool is_finite(double x)`
- `bool is_finite(float x)`
- `bool is_greater(double x, double y)`
- `bool is_greater(float x, float y)`
- `bool is_greater_equal(double x, double y)`
- `bool is_greater_equal(float x, float y)`
- `bool is_inf(double x)`
- `bool is_inf(float x)`
- `bool is_less(double x, double y)`
- `bool is_less(float x, float y)`
- `bool is_less_equal(double x, double y)`
- `bool is_less_equal(float x, float y)`
- `bool is_less_greater(double x, double y)`
- `bool is_less_greater(float x, float y)`
- `bool is_nan(double x)`
- `bool is_nan(float x)`
- `bool is_negative(double x)`
- `bool is_negative(float x)`
- `bool is_normal(double x)`
- `bool is_normal(float x)`
- `bool is_screen_keyboard_shown()`
- `bool is_unordered(double x, double y)`
- `bool is_unordered(float x, float y)`
- `bool is_window_active()`
- `bool is_window_hidden()`
- `bool key_down(int key)`
- `bool key_pressed(int key)`
- `bool key_released(int key)`
- `bool key_repeating(int key)`
- `bool key_up(int key)`
- `bool mouse_down(uint8 button)`
- `bool mouse_pressed(uint8 button)`
- `bool mouse_released(uint8 button)`
- `bool mouse_up(uint8 button)`
- `bool natural_number_sort(const string&in string1, const string&in string2)`
- `bool parse_ip_address(const string&in addr_in, ip_address&out addr_out)`
- `bool random_bool(int percent = 50)`
- `bool random_set_state(const string& in state)`
- `bool regexp_match(const string&in text, const string&in pattern, int options = RE_UTF8)`
- `bool regexp_search(const string&in text, const string&in pattern, int options = RE_UTF8)`
- `bool run(const string& in filename, const string& in arguments, bool wait_for_completion, bool background)`
- `bool screen_reader_braille(const string &in text)`
- `bool screen_reader_braille(const string&in text)`
- `bool screen_reader_has_braille()`
- `bool screen_reader_has_speech()`
- `bool screen_reader_is_speaking()`
- `bool screen_reader_output(const string &in text, bool interrupt = true)`
- `bool screen_reader_output(const string&in text, bool interrupt = true)`
- `bool screen_reader_silence()`
- `bool screen_reader_speak(const string &in text, bool interrupt = true)`
- `bool screen_reader_speak(const string&in text, bool interrupt = true)`
- `bool sdl_set_hint(const string&in hint, const string&in value, int priority = SDL_HINT_NORMAL)`
- `bool set_application_name(const string& in name)`
- `bool set_key_name(int key, const string&in name)`
- `bool set_linux_thread_priority(int64 thread_id, int priority)`
- `bool set_linux_thread_priority_and_policy(int64 thread_id, int priority, int policy)`
- `bool set_sound_global_hrtf(bool enabled)`
- `bool set_window_fullscreen(bool fullscreen)`
- `bool simulate_key_down(int key)`
- `bool simulate_key_up(int key)`
- `bool sound_set_listener_position(const vector&in position, uint listener_index = 0)`
- `bool sound_set_listener_position(float x, float y, float z, uint listener_index = 0)`
- `bool sound_set_spatialization(int panner, int attenuator, bool disable_previous = false, bool set_default = true)`
- `bool start_text_input()`
- `bool stop_text_input()`
- `bool text_input_active()`
- `bool thread_sleep(uint ms)`
- `bool urlopen(const string &in url)`
- `bool urlopen(const string&in url)`
- `bool utf8valid(const string&in text, bool ban_ascii_special = true)`
- `bool validate_email_address(const string &in address)`
- `bool validate_email_address(const string&in address)`
- `const string[]@+ get_sound_input_devices() property`
- `const string[]@+ get_sound_output_devices() property`
- `datastream@ get_cerr() property`
- `datastream@ get_cin() property`
- `datastream@ get_cout() property`
- `datetime@ parse_datetime(const string&in fmt, const string&in str, int& tzd)`
- `datetime@ parse_datetime(const string&in fmt, const string&in str, int&inout tzd)`
- `datetime@ parse_datetime(const string&in str, int& tzd)`
- `datetime@ parse_datetime(const string&in str, int&inout tzd)`
- `dictionary@ deserialize(const string& in data)`
- `dns_host_entry dns_resolve(const string&in address)`
- `dns_host_entry system_dns_host_entry()`
- `double abs(double v)`
- `double acos(double x)`
- `double acosh(double x)`
- `double asin(double x)`
- `double asinh(double x)`
- `double atan(double x)`
- `double atan2(double y, double x)`
- `double atanh(double x)`
- `double bytes_to_double(const string&in data)`
- `double calculate_gamma(double x)`
- `double calculate_lgamma(double x)`
- `double cbrt(double a)`
- `double ceil(double x)`
- `double copysign(double mag, double sgn)`
- `double cos(double x)`
- `double cosh(double x)`
- `double dmax(double a, double b)`
- `double dmin(double a, double b)`
- `double erf(double x)`
- `double erfc(double x)`
- `double exp(double a)`
- `double exp2(double a)`
- `double expm1(double a)`
- `double fdim(double a, double b)`
- `double floor(double x)`
- `double fma(double a, double b, double c)`
- `double fmod(double a, double b)`
- `double fpFromIEEE(uint64 raw)`
- `double frexp(double x, int& out exp)`
- `double hypot(double a, double b)`
- `double hypot(double a, double b, double c)`
- `double ldexp(double x, int exp)`
- `double lerp(double a, double b, double c)`
- `double log(double a)`
- `double log10(double a)`
- `double log1p(double a)`
- `double log2(double a)`
- `double logb(double x)`
- `double modf(double num, double& out iptr)`
- `double nearbyint(double x)`
- `double nextafter(double from, double to)`
- `double nexttoward(double from, double to)`
- `double parse_double(const string &in number)`
- `double parse_double(const string&in number)`
- `double pow(double a, double b)`
- `double remainder(double a, double b)`
- `double remquo(double a, double b, int& out quo)`
- `double rint(double x)`
- `double round(double number, int place)`
- `double scalbn(double x, int exp)`
- `double scalbn(double x, int64 exp)`
- `double sin(double x)`
- `double sinh(double x)`
- `double sqrt(double a)`
- `double tan(double x)`
- `double tanh(double x)`
- `double tinyexpr(const string &in expression)`
- `double tinyexpr(const string&in expression)`
- `double trunc(double x)`
- `float absf(float v)`
- `float acosf(float x)`
- `float acosh(float x)`
- `float asinf(float x)`
- `float asinh(float x)`
- `float atan2f(float y, float x)`
- `float atanf(float x)`
- `float atanh(float x)`
- `float bytes_to_float(const string&in data)`
- `float calculate_gamma(float x)`
- `float calculate_lgamma(float x)`
- `float cbrt(float a)`
- `float ceilf(float x)`
- `float clamp(float value, float min, float max)`
- `float copysign(float mag, float sgn)`
- `float cosf(float x)`
- `float cosh(float x)`
- `float erf(float x)`
- `float erfc(float x)`
- `float exp(float a)`
- `float exp2(float a)`
- `float expm1(float a)`
- `float fdim(float a, float b)`
- `float floorf(float x)`
- `float fma(float a, float b, float c)`
- `float fmax(float a, float b)`
- `float fmin(float a, float b)`
- `float fmod(float a, float b)`
- `float fp_from_IEEE(uint raw)`
- `float frexp(float x, int& out exp)`
- `float get_sound_master_volume() property`
- `float hypot(float a, float b)`
- `float hypot(float a, float b, float c)`
- `float ldexp(float x, int exp)`
- `float lerp(float a, float b, float c)`
- `float log10(float a)`
- `float log1p(float a)`
- `float log2(float a)`
- `float logb(float x)`
- `float logf(float a)`
- `float modf(float num, float& out iptr)`
- `float nearbyint(float x)`
- `float nextafter(float from, float to)`
- `float nexttoward(float from, double to)`
- `float parse_float(const string &in number)`
- `float parse_float(const string&in number)`
- `float powf(float a, float b)`
- `float random_float()`
- `float remainder(float a, float b)`
- `float remquo(float a, float b, int& out quo)`
- `float rint(float x)`
- `float scalbn(float x, int exp)`
- `float scalbn(float x, int64 exp)`
- `float sinf(float x)`
- `float sinh(float x)`
- `float sqrtf(float a)`
- `float tanf(float x)`
- `float tanh(float x)`
- `float trunc(float x)`
- `funcdef bool array<T>::less(const T&in if_handle_then_const a, const T&in if_handle_then_const b)`
- `funcdef bool coordinate_map_filter_callback(coordinate_map_area@ area)`
- `funcdef float physics_raycast_callback(const raycast_info&in info)`
- `funcdef int pathfinder_callback(int x, int y, int z, any@ callback_data = null)`
- `funcdef int pathfinder_callback_ex(int x, int y, int z, int parent_x, int parent_y, int parent_z, any@ callback_data = null)`
- `funcdef int pathfinder_callback_legacy(int x, int y, int parent_x, int parent_y, string user_data)`
- `funcdef uint timer_callback(string timer_id, string user_data)`
- `funcdef void android_permission_request_callback(string permission, bool granted, string user_data)`
- `funcdef void audio_engine_processing_callback(audio_engine@ engine, memory_buffer<float>& data, uint64 frames)`
- `funcdef void coroutine(dictionary@ args)`
- `funcdef void physics_collision_callback(const physics_collision_callback_data& data)`
- `funcdef void physics_overlap_callback(const physics_overlap_callback_data& data)`
- `funcdef void system_tray_callback(system_tray_menu_item@ item)`
- `funcdef void thread_callback(dictionary@ args)`
- `game_window@ show_window(const string& in title, uint flags = 0)`
- `game_window@+ get_window() property`
- `graphic@ create_surface(int width, int height, pixel_format pixel_format)`
- `graphic@ load_bmp(const string&in file)`
- `graphic@ load_bmp(const string&in file, const pack_interface@ pack_file)`
- `graphic@ load_png(const string&in file)`
- `graphic@ load_png(const string&in file, const pack_interface@ pack_file)`
- `graphic@ load_surface(const string&in file)`
- `graphic@ load_surface(const string&in file, const pack_interface@ pack_file)`
- `int alert(const string &in title, const string &in text, bool can_cancel = false, uint flags = 0)`
- `int alert(const string&in title, const string&in text, bool can_cancel = false, uint flags = 0)`
- `int bit_width(const uint x)`
- `int bit_width(const uint16 x)`
- `int bit_width(const uint32 x)`
- `int bit_width(const uint64 x)`
- `int bit_width(const uint8 x)`
- `int clamp(int value, int min, int max)`
- `int count_leading_ones(uint x)`
- `int count_leading_ones(uint16 x)`
- `int count_leading_ones(uint32 x)`
- `int count_leading_ones(uint64 x)`
- `int count_leading_ones(uint8 x)`
- `int count_leading_zeroes(uint x)`
- `int count_leading_zeroes(uint16 x)`
- `int count_leading_zeroes(uint32 x)`
- `int count_leading_zeroes(uint64 x)`
- `int count_leading_zeroes(uint8 x)`
- `int count_trailing_ones(uint x)`
- `int count_trailing_ones(uint16 x)`
- `int count_trailing_ones(uint32 x)`
- `int count_trailing_ones(uint64 x)`
- `int count_trailing_ones(uint8 x)`
- `int count_trailing_zeroes(uint x)`
- `int count_trailing_zeroes(uint16 x)`
- `int count_trailing_zeroes(uint32 x)`
- `int count_trailing_zeroes(uint64 x)`
- `int count_trailing_zeroes(uint8 x)`
- `int datetime_days_of_month(int year, int month)`
- `int fpclassify(double x)`
- `int fpclassify(float x)`
- `int get_ANDROID_SDK_VERSION() property`
- `int get_call_stack_size() property`
- `int get_DATE_DAY() property`
- `int get_DATE_MONTH() property`
- `int get_DATE_WEEKDAY() property`
- `int get_DATE_YEAR() property`
- `int get_exception_line()`
- `int get_garbage_collect_auto_frequency() property`
- `int get_garbage_collect_mode() property`
- `int get_key_code(const string&in name)`
- `int get_last_error()`
- `int get_SCRIPT_CURRENT_LINE() property`
- `int get_sound_default_3d_attenuator() property`
- `int get_sound_default_3d_panner() property`
- `int get_sound_output_device() property`
- `int get_TIME_HOUR() property`
- `int get_TIME_MINUTE() property`
- `int get_TIME_SECOND() property`
- `int get_TIMEZONE_BASE_OFFSET() property`
- `int get_TIMEZONE_DST_OFFSET() property`
- `int get_TIMEZONE_OFFSET() property`
- `int get_window_height()`
- `int get_window_width()`
- `int ilogb(double x)`
- `int ilogb(float x)`
- `int joystick_count(bool gamepads_only = true)`
- `int message_box(const string& in title, const string& in message, string[]@+ buttons, uint flags = 0)`
- `int popcount(uint x)`
- `int popcount(uint16 x)`
- `int popcount(uint32 x)`
- `int popcount(uint64 x)`
- `int popcount(uint8 x)`
- `int question(const string& in title, const string& in text, bool can_cancel = false, uint flags = 0)`
- `int random(int min, int max)`
- `int total_keys_down()`
- `int utf8next(const string&in text, int cursor)`
- `int utf8prev(const string&in text, int cursor)`
- `int utf8size(const string&in character)`
- `int64 file_get_size(const string& in path)`
- `int64 parse_int(const string &in str, uint base = 10, uint &out byteCount = 0)`
- `int64 parse_int(const string&in str, uint base = 10, uint&out byteCount = 0)`
- `int64 random64(int64 min, int64 max)`
- `int[]@ keys_down()`
- `int[]@ keys_pressed()`
- `int[]@ keys_released()`
- `ip_address broadcast_ip_address()`
- `ip_address wildcard_ip_address(ip_address_family family)`
- `ip_address wildcard_ip_address(spec::ip_address_family family)`
- `key_modifier get_keyboard_modifiers() property`
- `mail_message@ parse_email_message(const string &in data)`
- `mail_message@ parse_email_message(const string&in data)`
- `matrix3x3 get_IDENTITY_MATRIX() property`
- `OPERATING_SYSTEM get_OS() property`
- `pack_interface@ get_sound_default_pack() property`
- `physics_convex_mesh@ physics_convex_mesh_create(physics_vertex_data@ vertex_data)`
- `physics_convex_mesh@ physics_convex_mesh_create_from_polygon(physics_polygon_data@ polygon_data)`
- `physics_default_logger@ physics_default_logger_create()`
- `physics_height_field@ physics_height_field_create(int nb_columns, int nb_rows, double[]@ height_data, float integer_height_scale = 1.0f)`
- `physics_height_field@ physics_height_field_create(int nb_columns, int nb_rows, float[]@ height_data, float integer_height_scale = 1.0f)`
- `physics_height_field@ physics_height_field_create(int nb_columns, int nb_rows, int[]@ height_data, float integer_height_scale = 1.0f)`
- `physics_logger@ physics_logger_get_current()`
- `physics_transform get_IDENTITY_TRANSFORM() property`
- `physics_transform transforms_interpolate()`
- `physics_triangle_mesh@ physics_triangle_mesh_create(physics_triangle_data@ triangle_data)`
- `process@ run(const string[]& in args, int flags = 0, const string& in workdir = "")`
- `quaternion get_IDENTITY_QUATERNION() property`
- `quaternion quaternion_from_euler_angles(const vector& angles)`
- `quaternion quaternion_from_euler_angles(const vector&inout angles)`
- `quaternion quaternion_from_euler_angles(float angle_x, float angle_y, float angle_z)`
- `quaternion quaternion_slerp(const quaternion& q1, const quaternion& q2, float t)`
- `quaternion quaternion_slerp(const quaternion&inout q1, const quaternion&inout q2, float t)`
- `random_interface@ get_default_random()`
- `script_module@ script_get_module(const string&in name, int mode = 1)`
- `sound@ sound_play(const string&in path, const vector&in position = vector(FLOAT_MAX, FLOAT_MAX, FLOAT_MAX), float volume = 0.0, float pan = 0.0, float pitch = 100.0, mixer@ mix = null, const pack_interface@ pack_file = sound_default_pack, bool autoplay = true)`
- `sound@ sound_play(const string&in path, const vector&in position = vector(FLOAT_MAX, FLOAT_MAX, FLOAT_MAX), float volume = 0.0, float pan = 0.0, float pitch = 100.0, mixer@+ mix = null, const pack_interface@+ pack_file = sound_default_pack, bool autoplay = true)`
- `spec::ip_address dns_resolve_single(const string&in address)`
- `string ascii_to_character(uint8 character_code)`
- `string clipboard_get_text()`
- `string cwdir()`
- `string DIRECTORY_PREFERENCES(const string&in company_name, const string&in application_name)`
- `string double_to_bytes(double number)`
- `string expand_environment_variables(const string& in text)`
- `string file_get_contents(const string&in filename)`
- `string float_to_bytes(float number)`
- `string font_tag_to_string(uint tag)`
- `string format_float(double val, const string &in options = "", uint width = 0, uint precision = 0)`
- `string format_float(double val, const string&in options = "", uint width = 0, uint precision = 0)`
- `string format_int(int64 val, const string &in options = "", uint width = 0)`
- `string format_int(int64 val, const string&in options = "", uint width = 0)`
- `string format_uint(uint64 val, const string &in options = "", uint width = 0)`
- `string format_uint(uint64 val, const string&in options = "", uint width = 0)`
- `string generate_profile(bool reset = true)`
- `string generate_system_fingerprint(const string&in application_id = "")`
- `string generate_system_fingerprint_legacy1(const string&in application_id = "")`
- `string get_call_stack() property`
- `string get_characters()`
- `string get_COMMAND_LINE() property`
- `string get_DATE_MONTH_NAME() property`
- `string get_DATE_WEEKDAY_NAME() property`
- `string get_DIRECTORY_APPDATA() property`
- `string get_DIRECTORY_COMMON_APPDATA() property`
- `string get_DIRECTORY_HOME() property`
- `string get_DIRECTORY_LOCAL_APPDATA() property`
- `string get_DIRECTORY_TEMP() property`
- `string get_exception_file()`
- `string get_exception_function()`
- `string get_exception_info()`
- `string get_function_signature(?&in)`
- `string get_key_name(int key)`
- `string get_keyboard_name(uint id)`
- `string get_mouse_name(uint id)`
- `string get_preferences_path(const string&in company_name, const string&in application_name)`
- `string get_SCRIPT_CURRENT_FILE() property`
- `string get_SCRIPT_CURRENT_FUNCTION() property`
- `string get_SCRIPT_EXECUTABLE() property`
- `string get_SCRIPT_MAIN_PATH() property`
- `string get_SOUNDSYSTEM_LAST_ERROR_TEXT() property`
- `string get_system_node_id() property`
- `string get_system_node_name() property`
- `string get_TIMEZONE_DST_NAME() property`
- `string get_TIMEZONE_NAME() property`
- `string get_TIMEZONE_STANDARD_NAME() property`
- `string get_touch_device_name(uint64 device_id)`
- `string get_window_text()`
- `string getExceptionInfo()`
- `string hex_to_string(const string& in hex)`
- `string html_entities_decode(const string&in input)`
- `string http_status_reason(http_status status)`
- `string input_box(const string& in title, const string& in caption, const string& in default_value = '', uint64 flags = 0)`
- `string join(const array<string> &in arr, const string &in delimiter, int start = 0, int count = -1)`
- `string join(const array<string>&in arr, const string&in delimiter, int start = 0, int count = -1)`
- `string number_to_words(int64 number, bool include_and = true)`
- `string open_file_dialog(const string &in filters = "", const string&in default_location = "")`
- `string open_file_dialog(const string&in filters = "", const string&in default_location = "")`
- `string physics_logger_get_category_name(physics_logger_category category)`
- `string physics_logger_get_level_name(physics_logger_level level)`
- `string random_bytes(uint count)`
- `string random_character(const string& in min, const string& in max)`
- `string random_get_state()`
- `string read_environment_variable(const string&in variable, const string&in default_value = "")`
- `string regexp_replace(const string&in text, const string&in pattern, const string&in replacement, int options = RE_UTF8)`
- `string save_file_dialog(const string &in filters = "", const string&in default_location = "")`
- `string save_file_dialog(const string&in filters = "", const string&in default_location = "")`
- `string screen_reader_detect()`
- `string sdl_get_hint(const string&in hint)`
- `string select_folder_dialog(const string&in default_location = "")`
- `string string_aes_decrypt(const string&in ciphertext, string key)`
- `string string_aes_encrypt(const string&in plaintext, string key)`
- `string string_base32_decode(const string& in encoded)`
- `string string_base32_encode(const string& in binary)`
- `string string_base32_normalize(const string& in base32encoded)`
- `string string_base64_decode(const string& in encoded, string_base64_options options = STRING_BASE64_PADLESS)`
- `string string_base64_encode(const string& in binary, string_base64_options options = STRING_BASE64_DEFAULT)`
- `string string_create_from_pointer(uint64 ptr, uint64 length)`
- `string string_deflate(const string& in data, int compression_level = 9)`
- `string string_hash_md5(const string& in data, bool binary = false)`
- `string string_hash_sha1(const string& in data, bool binary = false)`
- `string string_hash_sha224(const string& in data, bool binary = false)`
- `string string_hash_sha256(const string& in data, bool binary = false)`
- `string string_hash_sha384(const string& in data, bool binary = false)`
- `string string_hash_sha512(const string& in data, bool binary = false)`
- `string string_inflate(const string& in deflated)`
- `string string_recode(const string&in text, const string&in in_encoding, const string&in out_encoding, int&out error_count = void)`
- `string string_to_hex(const string& in binary)`
- `string url_decode(const string&in url, bool plus_as_space = true)`
- `string url_encode(const string&in url, const string&in reserved = "")`
- `string url_get(const string&in url, http_response&out response = void)`
- `string url_post(const string&in url, const string&in data, http_response&out response = void)`
- `string url_request(const string&in method, const string&in url, const string&in data = "", http_response&out response = void)`
- `string[]@ find_directories(const string& in pattern)`
- `string[]@ find_files(const string& in pattern)`
- `string[]@ get_preferred_locales()`
- `string[]@ glob(const string& in pattern, glob_options options = GLOB_DEFAULT)`
- `system_power_state system_power_info(int&out seconds = void, int&out percent = void)`
- `text_font@ get_font(const string&in name, float size, uint style = FONT_STYLE_NORMAL, bool allow_caching = true)`
- `thread@+ get_thread_current() property`
- `thread_pool& get_thread_pool_default() property`
- `timestamp file_get_date_created(const string& in path)`
- `timestamp file_get_date_modified(const string& in path)`
- `timestamp timestamp_from_UTC_time(int64 UTC)`
- `touch_device_type get_touch_device_type(uint64 device_id)`
- `touch_finger[]@ query_touch_device(uint64 device_id = 0)`
- `uint adler32(const string& in data)`
- `uint crc32(const string& in data)`
- `uint font_string_to_tag(const string&in str)`
- `uint fp_to_IEEE(float fp)`
- `uint get_PROCESSOR_COUNT() property`
- `uint HOTP(const string& in key, uint64 counter, uint digits = 6)`
- `uint random_seed()`
- `uint string_distance(const string&in string1, const string&in string2, uint insert_cost = 1, uint delete_cost = 1, uint replace_cost = 1)`
- `uint thread_current_id()`
- `uint64 fpToIEEE(double fp)`
- `uint64 get_process_id()`
- `uint64 get_SYSTEM_PERFORMANCE_COUNTER() property`
- `uint64 get_SYSTEM_PERFORMANCE_FREQUENCY() property`
- `uint64 get_TIME_STAMP() property`
- `uint64 get_TIME_SYSTEM_RUNNING_MILLISECONDS() property`
- `uint64 get_window_os_handle()`
- `uint64 idle_ticks()`
- `uint64 memory_allocate(uint64 size)`
- `uint64 memory_allocate_units(uint64 unit_size, uint64 unit_count)`
- `uint64 memory_reallocate(uint64 ptr, uint64 size)`
- `uint64 microticks(bool secure = false)`
- `uint64 nanoticks()`
- `uint64 parseUInt(const string &in str, uint base = 10, uint &out byteCount = 0)`
- `uint64 parseUInt(const string&in str, uint base = 10, uint&out byteCount = 0)`
- `uint64 random_seed64()`
- `uint64 secure_ticks()`
- `uint64 ticks(bool secure = false)`
- `uint64[]@ get_touch_devices()`
- `uint8 character_to_ascii(const string&in character)`
- `uint[]@ get_keyboards()`
- `uint[]@ get_mice()`
- `uuid uuid_create_from_name(const uuid&in namespace_id, const string&in name)`
- `uuid uuid_create_from_name_sha1(const uuid&in namespace_id, const string&in name)`
- `uuid uuid_generate()`
- `uuid uuid_generate_random()`
- `uuid uuid_generate_time()`
- `uuid uuid_generate_time_v6()`
- `uuid uuid_generate_time_v7()`
- `uuid uuid_namespace_dns()`
- `uuid uuid_namespace_oid()`
- `uuid uuid_namespace_url()`
- `uuid uuid_namespace_x500()`
- `var@ parse_json(const string&in payload)`
- `var@ parse_json(datastream@+ stream)`
- `vector rotate(const vector&in point, const vector&in origin, double theta, bool maintain_z = true)`
- `vector sound_get_listener_position(uint listener_index = 0)`
- `void acquire_exclusive_lock()`
- `void acquire_shared_lock()`
- `void android_send_back_button()`
- `void assert(bool expression, const string&in fail_text = "")`
- `void atomic_thread_fence(memory_order order)`
- `void c_debug_break()`
- `void c_debug_break(const string&in message)`
- `void c_debug_message(const string&in message)`
- `void create_coroutine(coroutine @+ func, dictionary @+ args)`
- `void create_coroutine(coroutine@ func, dictionary@ args)`
- `void debug_add_file_breakpoint(const string&in filename, int line)`
- `void debug_add_func_breakpoint(const string&in function_name)`
- `void debug_break()`
- `void exit(int retcode = 0)`
- `void garbage_collect(bool full = true)`
- `void http_credentials_extract(const spec::uri&in uri, string&out username, string&out password)`
- `void http_credentials_extract(const string&in user_info, string&out username, string&out password)`
- `void memory_free(uint64 ptr)`
- `void mouse_update()`
- `void nanosleep(uint64 ns)`
- `void next_keyboard_layout()`
- `void physics_box_shape_destroy(physics_box_shape@ shape)`
- `void physics_capsule_shape_destroy(physics_capsule_shape@ shape)`
- `void physics_concave_mesh_shape_destroy(physics_concave_mesh_shape@ shape)`
- `void physics_convex_mesh_destroy(physics_convex_mesh@ mesh)`
- `void physics_convex_mesh_shape_destroy(physics_convex_mesh_shape@ shape)`
- `void physics_default_logger_destroy(physics_default_logger@ logger)`
- `void physics_height_field_destroy(physics_height_field@ height_field)`
- `void physics_height_field_shape_destroy(physics_height_field_shape@ shape)`
- `void physics_logger_set_current(physics_logger@ logger)`
- `void physics_shape_destroy(physics_collision_shape@ shape)`
- `void physics_sphere_shape_destroy(physics_sphere_shape@ shape)`
- `void physics_triangle_mesh_destroy(physics_triangle_mesh@ mesh)`
- `void physics_triangle_shape_compute_smooth_triangle_mesh_contact(const physics_collision_shape &in shape1, const physics_collision_shape &in shape2, vector & local_contact_point_shape1, vector & local_contact_point_shape2, const physics_transform &in shape1_to_world, const physics_transform &in shape2_to_world, float penitration_depth, vector & out_smooth_vertex_normal)`
- `void physics_triangle_shape_compute_smooth_triangle_mesh_contact(const physics_collision_shape&in shape1, const physics_collision_shape&in shape2, vector&inout local_contact_point_shape1, vector&inout local_contact_point_shape2, const physics_transform&in shape1_to_world, const physics_transform&in shape2_to_world, float penitration_depth, vector&inout out_smooth_vertex_normal)`
- `void physics_world_destroy(physics_world& world)`
- `void physics_world_destroy(physics_world&inout world)`
- `void print(`
- `void print(const ?&in = null, const ?&in = null, const ?&in = null, const ?&in = null, const ?&in = null, const ?&in = null, const ?&in = null, const ?&in = null, const ?&in = null, const ?&in = null, const ?&in = null, const ?&in = null, const ?&in = null, const ?&in = null, const ?&in = null, const ?&in = null)`
- `void printf(const string &in format,`
- `void printf(const string&in format, const ?&in = null, const ?&in = null, const ?&in = null, const ?&in = null, const ?&in = null, const ?&in = null, const ?&in = null, const ?&in = null, const ?&in = null, const ?&in = null, const ?&in = null, const ?&in = null, const ?&in = null, const ?&in = null, const ?&in = null, const ?&in = null)`
- `void println(`
- `void println(const ?&in = null, const ?&in = null, const ?&in = null, const ?&in = null, const ?&in = null, const ?&in = null, const ?&in = null, const ?&in = null, const ?&in = null, const ?&in = null, const ?&in = null, const ?&in = null, const ?&in = null, const ?&in = null, const ?&in = null, const ?&in = null)`
- `void refresh_window()`
- `void release_exclusive_lock()`
- `void release_shared_lock()`
- `void reset_keyboard()`
- `void reset_profiler()`
- `void script_dump_engine_configuration(datastream@+ output)`
- `void set_cursor_visible(bool state) property`
- `void set_default_random(random_generator@+ generator)`
- `void set_default_random(random_interface@ generator)`
- `void set_garbage_collect_auto_frequency(int frequency) property`
- `void set_garbage_collect_mode(int mode) property`
- `void set_keyboard_modifiers(key_modifier modifier) property`
- `void set_mouse_grab(bool grabbed) property`
- `void set_sound_3d_attenuator_enabled(int attenuator_id, bool enabled)`
- `void set_sound_3d_panner_enabled(int panner_id, bool enabled)`
- `void set_sound_default_3d_attenuator(int attenuator_id)`
- `void set_sound_default_3d_panner(int panner_id)`
- `void set_sound_default_decryption_key(const string& in key) property`
- `void set_sound_default_engine(audio_engine@ engine) property`
- `void set_sound_default_pack(pack_interface@+ storage) property`
- `void set_sound_master_volume(float db) property`
- `void set_sound_output_device(int device) property`
- `void sleep(uint milliseconds)`
- `void start_profiling()`
- `void stop_profiling()`
- `void thread_yield()`
- `void throw(const string &in message)`
- `void throw(const string&in message)`
- `void uninstall_keyhook()`
- `void wait(int ms)`
- `void write_environment_variable(const string&in variable, const string&in value)`
- `void yield()`

## Global Properties
- `bool speedhack_protection`
- `const atomic_flag memory_scan_detected`
- `const atomic_flag speed_hack_detected`
- `const bool profiler_is_running`
- `const double DOUBLE_EPSILON`
- `const double DOUBLE_MAX`
- `const double DOUBLE_MIN_NORMALIZED`
- `const double DOUBLE_NEG_EPSILON`
- `const float EPSILON`
- `const float FLOAT_EPSILON`
- `const float FLOAT_MAX`
- `const float FLOAT_MIN_NORMALIZED`
- `const float FLOAT_NEG_EPSILON`
- `const float MOUSE_ABSOLUTE_X`
- `const float MOUSE_ABSOLUTE_Y`
- `const float MOUSE_ABSOLUTE_Z`
- `const float MOUSE_X`
- `const float MOUSE_Y`
- `const float MOUSE_Z`
- `const int DOUBLE_EPSILON_EXPONENT`
- `const int DOUBLE_EXPONENT_BITS`
- `const int DOUBLE_GUARD_DIGITS`
- `const int DOUBLE_MANTISSA_DIGITS`
- `const int DOUBLE_MAX_EXPONENT`
- `const int DOUBLE_MIN_EXPONENT`
- `const int DOUBLE_NEG_EPSILON_EXPONENT`
- `const int DOUBLE_RADIX`
- `const int DOUBLE_ROUNDING_MODE`
- `const int FLOAT_EPSILON_EXPONENT`
- `const int FLOAT_EXPONENT_BITS`
- `const int FLOAT_GUARD_DIGITS`
- `const int FLOAT_MANTISSA_DIGITS`
- `const int FLOAT_MAX_EXPONENT`
- `const int FLOAT_MIN_EXPONENT`
- `const int FLOAT_NEG_EPSILON_EXPONENT`
- `const int FLOAT_RADIX`
- `const int FLOAT_ROUNDING_MODE`
- `const int HTTP_UNKNOWN_CONTENT_LENGTH`
- `const int NVGT_VERSION_MAJOR`
- `const int NVGT_VERSION_MINOR`
- `const int NVGT_VERSION_PATCH`
- `const int64 DAYS`
- `const int64 HOURS`
- `const int64 MICROSECONDS`
- `const int64 MILLISECONDS`
- `const int64 MINUTES`
- `const int64 SECONDS`
- `const string DATE_TIME_FORMAT_ASCTIME`
- `const string DATE_TIME_FORMAT_HTTP`
- `const string DATE_TIME_FORMAT_ISO8601`
- `const string DATE_TIME_FORMAT_ISO8601_FRAC`
- `const string DATE_TIME_FORMAT_RFC1036`
- `const string DATE_TIME_FORMAT_RFC1123`
- `const string DATE_TIME_FORMAT_RFC822`
- `const string DATE_TIME_FORMAT_RFC850`
- `const string DATE_TIME_FORMAT_SORTABLE`
- `const string DATE_TIME_REGEX_ASCTIME`
- `const string DATE_TIME_REGEX_HTTP`
- `const string DATE_TIME_REGEX_ISO8601`
- `const string DATE_TIME_REGEX_RFC1036`
- `const string DATE_TIME_REGEX_RFC1123`
- `const string DATE_TIME_REGEX_RFC822`
- `const string DATE_TIME_REGEX_RFC850`
- `const string DATE_TIME_REGEX_SORTABLE`
- `const string HTTP_1_0`
- `const string HTTP_1_1`
- `const string HTTP_CHUNKED_TRANSFER_ENCODING`
- `const string HTTP_DELETE`
- `const string HTTP_GET`
- `const string HTTP_HEAD`
- `const string HTTP_IDENTITY_TRANSFER_ENCODING`
- `const string HTTP_OPTIONS`
- `const string HTTP_PATCH`
- `const string HTTP_POST`
- `const string HTTP_PUT`
- `const string HTTP_UNKNOWN_CONTENT_TYPE`
- `const string last_exception_call_stack`
- `const string NEWLINE_CR`
- `const string NEWLINE_CRLF`
- `const string NEWLINE_DEFAULT`
- `const string NEWLINE_LF`
- `const string NVGT_VERSION`
- `const string NVGT_VERSION_BUILD_TIME`
- `const string NVGT_VERSION_COMMIT_HASH`
- `const string NVGT_VERSION_TYPE`
- `const string PLATFORM`
- `const string PLATFORM_ARCHITECTURE`
- `const string PLATFORM_DISPLAY_NAME`
- `const string PLATFORM_VERSION`
- `const string[]@ ARGS`
- `const timestamp SCRIPT_BUILD_TIME`
- `const uint NVGT_VERSION_BUILD_TIMESTAMP`
- `engine_character_event on_characters`
- `engine_key_event on_key_press`
- `engine_key_event on_key_release`
- `engine_key_event on_key_repeat`
- `engine_touch_event on_touch_finger_cancel`
- `engine_touch_event on_touch_finger_down`
- `engine_touch_event on_touch_finger_up`
- `engine_touch_motion_event on_touch_finger_move`
- `mixer@ sound_default_mixer`
- `uint64 timer_default_accuracy`

## Classes
### Class `aabb`
##### Behaviours / Constructors
- `void aabb()`
- `void aabb(const vector&in min, const vector&in max)`
- `void f()`
- `void f(const vector&in min, const vector&in max)`
##### Methods
- `bool contains(const aabb&in aabb) const`
- `bool contains(const vector&in point, float epsilon = EPSILON) const`
- `bool raycast(const ray&in ray, vector&out hit_point)`
- `bool test_collision(const aabb&in aabb) const`
- `bool test_collision_triangle_aabb(const vector[]@ points) const`
- `bool test_ray_intersect(const vector&in ray_origin, const vector&in ray_direction, float ray_max_fraction)`
- `const vector& get_max() const property`
- `const vector& get_min() const property`
- `float get_volume() const property`
- `vector get_center() const property`
- `vector get_extent() const property`
- `void apply_scale(const vector&in scale)`
- `void inflate(float x, float y, float z)`
- `void inflate_with_point(const vector&in point)`
- `void merge(const aabb&in aabb1, const aabb&in aabb2)`
- `void merge_with(const aabb&in aabb)`
- `void set_max(const vector&in max) property`
- `void set_min(const vector&in min) property`

### Class `any`
##### Behaviours / Constructors
- `any@ any()`
- `any@ any(?&in value)`
- `any@ any(const double&in value)`
- `any@ any(const int64&in value)`
- `any@ f()`
- `any@ f(?&in value)`
- `any@ f(?&in value) explicit`
- `any@ f(const double&in value)`
- `any@ f(const double&in value) explicit`
- `any@ f(const int64&in value)`
- `any@ f(const int64&in value) explicit`
- `bool f()`
- `int f()`
- `void f()`
- `void f(int&in)`
##### Methods
- `any &opAssign(any&in other)`
- `any& opAssign(any&in other)`
- `bool retrieve(?&out value)`
- `bool retrieve(?&out value) const`
- `bool retrieve(double&out value)`
- `bool retrieve(double&out value) const`
- `bool retrieve(int64&out value)`
- `bool retrieve(int64&out value) const`
- `void store(?&in value)`
- `void store(const double&in value)`
- `void store(const int64&in value)`

### Class `array<class T>`

### Class `array<T>`
##### Behaviours / Constructors
- `array<T>@ $list(int&in type, int&in list) { repeat T }`
- `array<T>@ array(int&in)`
- `array<T>@ array(int&in, uint length)`
- `array<T>@ array(int&in, uint length, const T&in value)`
- `array<T>@ f(int&in type, int&in list) {repeat T}`
- `array<T>@ f(int&in)`
- `array<T>@ f(int&in, uint length) explicit`
- `array<T>@ f(int&in, uint length, const T &in value)`
- `bool f()`
- `bool f(int&in, bool&out)`
- `int f()`
- `void f()`
- `void f(int&in)`
##### Methods
- `array<T> &opAssign(const array<T>&in other)`
- `array<T>& opAssign(const array<T>&in other)`
- `bool empty() const`
- `bool is_empty() const`
- `bool opEquals(const array<T>&in other) const`
- `bool opForEnd(int64 iterator) const`
- `const T &opForValue0(int64 index) const`
- `const T &opIndex(int64 index) const`
- `const T& opForValue0(int64 index) const`
- `const T& opIndex(int64 index) const`
- `const T& random() const`
- `const T& random(const random_gamerand&in generator) const`
- `const T& random(const random_pcg&in generator) const`
- `const T& random(const random_well&in generator) const`
- `const T& random(const random_xorshift&in generator) const`
- `const T& random(random_gamerand@ generator) const`
- `const T& random(random_generator@ rng) const`
- `const T& random(random_interface@ rng) const`
- `const T& random(random_pcg@ generator) const`
- `const T& random(random_well@ generator) const`
- `const T& random(random_xorshift@ generator) const`
- `int find(const T&in if_handle_then_const value) const`
- `int find(const T&in value) const`
- `int find(uint startAt, const T&in if_handle_then_const value) const`
- `int find(uint startAt, const T&in value) const`
- `int find_by_ref(const T&in if_handle_then_const value) const`
- `int find_by_ref(const T&in value) const`
- `int find_by_ref(uint startAt, const T&in if_handle_then_const value) const`
- `int find_by_ref(uint startAt, const T&in value) const`
- `int64 opForBegin() const`
- `int64 opForNext(int64 iterator) const`
- `int64 opForValue1(int64 index) const`
- `T &back()`
- `T &front()`
- `T &opIndex(int64 index)`
- `T& back()`
- `T& front()`
- `T& opIndex(int64 index)`
- `uint get_length() const property`
- `uint length() const`
- `uint size() const`
- `void erase(uint index)`
- `void extend(const array<T>& arr)`
- `void extend(const array<T>&inout arr)`
- `void insert(uint index, const array<T>& arr)`
- `void insert(uint index, const array<T>&inout arr)`
- `void insert(uint index, const T&in value)`
- `void insert_at(uint index, const array<T>& arr)`
- `void insert_at(uint index, const array<T>&inout arr)`
- `void insert_at(uint index, const T&in value)`
- `void insert_last(const T&in value)`
- `void pop_back()`
- `void push_back(const T&in value)`
- `void remove_at(uint index)`
- `void remove_last()`
- `void remove_range(uint start, uint count)`
- `void reserve(uint length)`
- `void resize(uint length)`
- `void reverse()`
- `void set_length(uint length) property`
- `void shuffle()`
- `void shuffle(random_gamerand@ generator)`
- `void shuffle(random_generator@+ rng)`
- `void shuffle(random_interface@ rng)`
- `void shuffle(random_pcg@ generator)`
- `void shuffle(random_well@ generator)`
- `void shuffle(random_xorshift@ generator)`
- `void sort(array<T>::less&in callback, uint startAt = 0, uint count = uint(-1))`
- `void sort(const less &in callback, uint startAt = 0, uint count = uint(-1))`
- `void sort_ascending()`
- `void sort_ascending(uint startAt, uint count)`
- `void sort_descending()`
- `void sort_descending(uint startAt, uint count)`

### Class `asset_decryptor`
##### Behaviours / Constructors
- `asset_decryptor@ asset_decryptor()`
- `asset_decryptor@ asset_decryptor(datastream@ stream, const string&in key, const string&in encoding = "", int byteorder = 1)`
##### Properties
- `bool autoflush`
- `bool binary`
- `bool skip_eof`
- `bool sync_rw_cursors`
##### Methods
- `asset_decryptor& opShl(double value)`
- `asset_decryptor& opShl(float value)`
- `asset_decryptor& opShl(int value)`
- `asset_decryptor& opShl(int16 value)`
- `asset_decryptor& opShl(int64 value)`
- `asset_decryptor& opShl(int8 value)`
- `asset_decryptor& opShl(string value)`
- `asset_decryptor& opShl(uint value)`
- `asset_decryptor& opShl(uint16 value)`
- `asset_decryptor& opShl(uint64 value)`
- `asset_decryptor& opShl(uint8 value)`
- `asset_decryptor& opShr(double&out value)`
- `asset_decryptor& opShr(float&out value)`
- `asset_decryptor& opShr(int&out value)`
- `asset_decryptor& opShr(int16&out value)`
- `asset_decryptor& opShr(int64&out value)`
- `asset_decryptor& opShr(int8&out value)`
- `asset_decryptor& opShr(string&out value)`
- `asset_decryptor& opShr(uint&out value)`
- `asset_decryptor& opShr(uint16&out value)`
- `asset_decryptor& opShr(uint64&out value)`
- `asset_decryptor& opShr(uint8&out value)`
- `asset_decryptor& write_double(double value)`
- `asset_decryptor& write_float(float value)`
- `asset_decryptor& write_int(int value)`
- `asset_decryptor& write_int16(int16 value)`
- `asset_decryptor& write_int64(int64 value)`
- `asset_decryptor& write_int8(int8 value)`
- `asset_decryptor& write_string(string value)`
- `asset_decryptor& write_uint(uint value)`
- `asset_decryptor& write_uint16(uint16 value)`
- `asset_decryptor& write_uint64(uint64 value)`
- `asset_decryptor& write_uint8(uint8 value)`
- `bool close(bool close_all = false)`
- `bool close_all()`
- `bool get_active() const property`
- `bool get_bad() const property`
- `bool get_eof() const property`
- `bool get_fail() const property`
- `bool get_good() const property`
- `bool open(datastream@ stream, const string&in key, const string&in encoding = "", int byteorder = 1)`
- `bool rseek(uint64 offset)`
- `bool rseek_end(uint64 offset = 0)`
- `bool rseek_relative(int64 offset)`
- `bool seek(uint64 offset)`
- `bool seek_end(uint64 offset = 0)`
- `bool seek_relative(int64 offset)`
- `bool wseek(uint64 offset)`
- `bool wseek_end(uint64 offset = 0)`
- `bool wseek_relative(int64 offset)`
- `datastream@ opImplCast()`
- `double read_double()`
- `float read_float()`
- `int read_int()`
- `int16 read_int16()`
- `int64 get_pos() const property`
- `int64 get_rpos() const property`
- `int64 get_wpos() const property`
- `int64 read_int64()`
- `int8 read_int8()`
- `string read(uint count = 0)`
- `string read_line()`
- `string read_string()`
- `string read_until(const string&in text, bool require_full)`
- `uint read_uint()`
- `uint write(const string&in data)`
- `uint16 read_uint16()`
- `uint64 get_available() const property`
- `uint64 read_7bit_encoded()`
- `uint64 read_uint64()`
- `uint8 read_uint8()`
- `void flush()`
- `void read_7bit_encoded(uint64&out integer)`
- `void write_7bit_encoded(uint64 integer)`

### Class `asset_encryptor`
##### Behaviours / Constructors
- `asset_encryptor@ asset_encryptor()`
- `asset_encryptor@ asset_encryptor(datastream@ stream, string&in key, const string&in encoding = "", int byteorder = 1)`
##### Properties
- `bool autoflush`
- `bool binary`
- `bool skip_eof`
- `bool sync_rw_cursors`
##### Methods
- `asset_encryptor& opShl(double value)`
- `asset_encryptor& opShl(float value)`
- `asset_encryptor& opShl(int value)`
- `asset_encryptor& opShl(int16 value)`
- `asset_encryptor& opShl(int64 value)`
- `asset_encryptor& opShl(int8 value)`
- `asset_encryptor& opShl(string value)`
- `asset_encryptor& opShl(uint value)`
- `asset_encryptor& opShl(uint16 value)`
- `asset_encryptor& opShl(uint64 value)`
- `asset_encryptor& opShl(uint8 value)`
- `asset_encryptor& opShr(double&out value)`
- `asset_encryptor& opShr(float&out value)`
- `asset_encryptor& opShr(int&out value)`
- `asset_encryptor& opShr(int16&out value)`
- `asset_encryptor& opShr(int64&out value)`
- `asset_encryptor& opShr(int8&out value)`
- `asset_encryptor& opShr(string&out value)`
- `asset_encryptor& opShr(uint&out value)`
- `asset_encryptor& opShr(uint16&out value)`
- `asset_encryptor& opShr(uint64&out value)`
- `asset_encryptor& opShr(uint8&out value)`
- `asset_encryptor& write_double(double value)`
- `asset_encryptor& write_float(float value)`
- `asset_encryptor& write_int(int value)`
- `asset_encryptor& write_int16(int16 value)`
- `asset_encryptor& write_int64(int64 value)`
- `asset_encryptor& write_int8(int8 value)`
- `asset_encryptor& write_string(string value)`
- `asset_encryptor& write_uint(uint value)`
- `asset_encryptor& write_uint16(uint16 value)`
- `asset_encryptor& write_uint64(uint64 value)`
- `asset_encryptor& write_uint8(uint8 value)`
- `bool close(bool close_all = false)`
- `bool close_all()`
- `bool get_active() const property`
- `bool get_bad() const property`
- `bool get_eof() const property`
- `bool get_fail() const property`
- `bool get_good() const property`
- `bool open(datastream@ stream, string&in key, const string&in encoding = "", int byteorder = 1)`
- `bool rseek(uint64 offset)`
- `bool rseek_end(uint64 offset = 0)`
- `bool rseek_relative(int64 offset)`
- `bool seek(uint64 offset)`
- `bool seek_end(uint64 offset = 0)`
- `bool seek_relative(int64 offset)`
- `bool wseek(uint64 offset)`
- `bool wseek_end(uint64 offset = 0)`
- `bool wseek_relative(int64 offset)`
- `datastream@ opImplCast()`
- `double read_double()`
- `float read_float()`
- `int read_int()`
- `int16 read_int16()`
- `int64 get_pos() const property`
- `int64 get_rpos() const property`
- `int64 get_wpos() const property`
- `int64 read_int64()`
- `int8 read_int8()`
- `string read(uint count = 0)`
- `string read_line()`
- `string read_string()`
- `string read_until(const string&in text, bool require_full)`
- `uint read_uint()`
- `uint write(const string&in data)`
- `uint16 read_uint16()`
- `uint64 get_available() const property`
- `uint64 read_7bit_encoded()`
- `uint64 read_uint64()`
- `uint8 read_uint8()`
- `void flush()`
- `void read_7bit_encoded(uint64&out integer)`
- `void write_7bit_encoded(uint64 integer)`

### Class `async<class T>`

### Class `async<T>`
##### Behaviours / Constructors
- `async<T>@ async(int&in)`
- `async<T>@ async(int&in, const ?&in)`
- `async<T>@ async(int&in, const ?&in, const ?&in)`
- `async<T>@ async(int&in, const ?&in, const ?&in, const ?&in)`
- `async<T>@ async(int&in, const ?&in, const ?&in, const ?&in, const ?&in)`
- `async<T>@ async(int&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in)`
- `async<T>@ async(int&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in)`
- `async<T>@ async(int&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in)`
- `async<T>@ async(int&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in)`
- `async<T>@ async(int&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in)`
- `async<T>@ async(int&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in)`
- `async<T>@ async(int&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in)`
- `async<T>@ async(int&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in)`
- `async<T>@ async(int&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in)`
- `async<T>@ async(int&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in)`
- `async<T>@ async(int&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in)`
- `async<T>@ async(int&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in, const ?&in)`
- `async<T>@ f(int&in)`
##### Methods
- `bool get_complete() const property`
- `bool get_failed() const property`
- `bool try_wait(uint ms)`
- `const T& get_value() property`
- `string get_exception() const property`
- `void wait()`

### Class `atomic_bool`
##### Behaviours / Constructors
- `void atomic_bool()`
##### Methods
- `bool compare_exchange_strong(bool&inout expected, bool desired, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `bool compare_exchange_strong(bool&inout expected, bool desired, memory_order success, memory_order failure)`
- `bool compare_exchange_weak(bool&inout expected, bool desired, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `bool compare_exchange_weak(bool&inout expected, bool desired, memory_order success, memory_order failure)`
- `bool exchange(bool desired, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `bool get_is_always_lock_free() property`
- `bool is_lock_free() const`
- `bool load(memory_order order = MEMORY_ORDER_SEQ_CST) const`
- `bool opAssign(bool val)`
- `bool opImplConv() const`
- `void notify_all()`
- `void notify_one()`
- `void store(bool val, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `void wait(bool old, memory_order order = MEMORY_ORDER_SEQ_CST) const`

### Class `atomic_double`
##### Behaviours / Constructors
- `void atomic_double()`
##### Methods
- `bool compare_exchange_strong(double&inout expected, double desired, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `bool compare_exchange_strong(double&inout expected, double desired, memory_order success, memory_order failure)`
- `bool compare_exchange_weak(double&inout expected, double desired, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `bool compare_exchange_weak(double&inout expected, double desired, memory_order success, memory_order failure)`
- `bool get_is_always_lock_free() property`
- `bool is_lock_free() const`
- `double exchange(double desired, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `double fetch_add(double arg, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `double fetch_sub(double arg, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `double load(memory_order order = MEMORY_ORDER_SEQ_CST) const`
- `double opAddAssign(double arg)`
- `double opAssign(double val)`
- `double opImplConv() const`
- `double opSubAssign(double arg)`
- `void notify_all()`
- `void notify_one()`
- `void store(double val, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `void wait(double old, memory_order order = MEMORY_ORDER_SEQ_CST) const`

### Class `atomic_flag`
##### Behaviours / Constructors
- `void atomic_flag()`
- `void f()`
##### Methods
- `bool test(memory_order order = MEMORY_ORDER_SEQ_CST) const`
- `bool test_and_set(memory_order order = MEMORY_ORDER_SEQ_CST)`
- `void clear(memory_order order = MEMORY_ORDER_SEQ_CST)`
- `void notify_all()`
- `void notify_one()`
- `void wait(bool old, memory_order order = MEMORY_ORDER_SEQ_CST) const`

### Class `atomic_float`
##### Behaviours / Constructors
- `void atomic_float()`
##### Methods
- `bool compare_exchange_strong(float&inout expected, float desired, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `bool compare_exchange_strong(float&inout expected, float desired, memory_order success, memory_order failure)`
- `bool compare_exchange_weak(float&inout expected, float desired, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `bool compare_exchange_weak(float&inout expected, float desired, memory_order success, memory_order failure)`
- `bool get_is_always_lock_free() property`
- `bool is_lock_free() const`
- `float exchange(float desired, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `float fetch_add(float arg, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `float fetch_sub(float arg, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `float load(memory_order order = MEMORY_ORDER_SEQ_CST) const`
- `float opAddAssign(float arg)`
- `float opAssign(float val)`
- `float opImplConv() const`
- `float opSubAssign(float arg)`
- `void notify_all()`
- `void notify_one()`
- `void store(float val, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `void wait(float old, memory_order order = MEMORY_ORDER_SEQ_CST) const`

### Class `atomic_int`
##### Behaviours / Constructors
- `void atomic_int()`
##### Methods
- `bool compare_exchange_strong(int&inout expected, int desired, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `bool compare_exchange_strong(int&inout expected, int desired, memory_order success, memory_order failure)`
- `bool compare_exchange_weak(int&inout expected, int desired, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `bool compare_exchange_weak(int&inout expected, int desired, memory_order success, memory_order failure)`
- `bool get_is_always_lock_free() property`
- `bool is_lock_free() const`
- `int exchange(int desired, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `int fetch_add(int arg, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `int fetch_and(int arg, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `int fetch_or(int arg, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `int fetch_sub(int arg, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `int fetch_xor(int arg, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `int load(memory_order order = MEMORY_ORDER_SEQ_CST) const`
- `int opAddAssign(int arg)`
- `int opAndAssign(int arg)`
- `int opAssign(int val)`
- `int opImplConv() const`
- `int opOrAssign(int arg)`
- `int opPostDec(int arg)`
- `int opPostInc(int arg)`
- `int opPreDec()`
- `int opPreInc()`
- `int opSubAssign(int arg)`
- `int opXorAssign(int arg)`
- `void notify_all()`
- `void notify_one()`
- `void store(int val, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `void wait(int old, memory_order order = MEMORY_ORDER_SEQ_CST) const`

### Class `atomic_int16`
##### Behaviours / Constructors
- `void atomic_int16()`
##### Methods
- `bool compare_exchange_strong(int16&inout expected, int16 desired, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `bool compare_exchange_strong(int16&inout expected, int16 desired, memory_order success, memory_order failure)`
- `bool compare_exchange_weak(int16&inout expected, int16 desired, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `bool compare_exchange_weak(int16&inout expected, int16 desired, memory_order success, memory_order failure)`
- `bool get_is_always_lock_free() property`
- `bool is_lock_free() const`
- `int16 exchange(int16 desired, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `int16 fetch_add(int16 arg, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `int16 fetch_and(int16 arg, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `int16 fetch_or(int16 arg, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `int16 fetch_sub(int16 arg, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `int16 fetch_xor(int16 arg, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `int16 load(memory_order order = MEMORY_ORDER_SEQ_CST) const`
- `int16 opAddAssign(int16 arg)`
- `int16 opAndAssign(int16 arg)`
- `int16 opAssign(int16 val)`
- `int16 opImplConv() const`
- `int16 opOrAssign(int16 arg)`
- `int16 opPostDec(int16 arg)`
- `int16 opPostInc(int16 arg)`
- `int16 opPreDec()`
- `int16 opPreInc()`
- `int16 opSubAssign(int16 arg)`
- `int16 opXorAssign(int16 arg)`
- `void notify_all()`
- `void notify_one()`
- `void store(int16 val, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `void wait(int16 old, memory_order order = MEMORY_ORDER_SEQ_CST) const`

### Class `atomic_int32`
##### Behaviours / Constructors
- `void atomic_int32()`
##### Methods
- `bool compare_exchange_strong(int&inout expected, int desired, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `bool compare_exchange_strong(int&inout expected, int desired, memory_order success, memory_order failure)`
- `bool compare_exchange_weak(int&inout expected, int desired, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `bool compare_exchange_weak(int&inout expected, int desired, memory_order success, memory_order failure)`
- `bool get_is_always_lock_free() property`
- `bool is_lock_free() const`
- `int exchange(int desired, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `int fetch_add(int arg, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `int fetch_and(int arg, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `int fetch_or(int arg, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `int fetch_sub(int arg, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `int fetch_xor(int arg, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `int load(memory_order order = MEMORY_ORDER_SEQ_CST) const`
- `int opAddAssign(int arg)`
- `int opAndAssign(int arg)`
- `int opAssign(int val)`
- `int opImplConv() const`
- `int opOrAssign(int arg)`
- `int opPostDec(int arg)`
- `int opPostInc(int arg)`
- `int opPreDec()`
- `int opPreInc()`
- `int opSubAssign(int arg)`
- `int opXorAssign(int arg)`
- `void notify_all()`
- `void notify_one()`
- `void store(int val, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `void wait(int old, memory_order order = MEMORY_ORDER_SEQ_CST) const`

### Class `atomic_int64`
##### Behaviours / Constructors
- `void atomic_int64()`
##### Methods
- `bool compare_exchange_strong(int64&inout expected, int64 desired, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `bool compare_exchange_strong(int64&inout expected, int64 desired, memory_order success, memory_order failure)`
- `bool compare_exchange_weak(int64&inout expected, int64 desired, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `bool compare_exchange_weak(int64&inout expected, int64 desired, memory_order success, memory_order failure)`
- `bool get_is_always_lock_free() property`
- `bool is_lock_free() const`
- `int64 exchange(int64 desired, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `int64 fetch_add(int64 arg, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `int64 fetch_and(int64 arg, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `int64 fetch_or(int64 arg, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `int64 fetch_sub(int64 arg, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `int64 fetch_xor(int64 arg, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `int64 load(memory_order order = MEMORY_ORDER_SEQ_CST) const`
- `int64 opAddAssign(int64 arg)`
- `int64 opAndAssign(int64 arg)`
- `int64 opAssign(int64 val)`
- `int64 opImplConv() const`
- `int64 opOrAssign(int64 arg)`
- `int64 opPostDec(int64 arg)`
- `int64 opPostInc(int64 arg)`
- `int64 opPreDec()`
- `int64 opPreInc()`
- `int64 opSubAssign(int64 arg)`
- `int64 opXorAssign(int64 arg)`
- `void notify_all()`
- `void notify_one()`
- `void store(int64 val, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `void wait(int64 old, memory_order order = MEMORY_ORDER_SEQ_CST) const`

### Class `atomic_int8`
##### Behaviours / Constructors
- `void atomic_int8()`
##### Methods
- `bool compare_exchange_strong(int8&inout expected, int8 desired, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `bool compare_exchange_strong(int8&inout expected, int8 desired, memory_order success, memory_order failure)`
- `bool compare_exchange_weak(int8&inout expected, int8 desired, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `bool compare_exchange_weak(int8&inout expected, int8 desired, memory_order success, memory_order failure)`
- `bool get_is_always_lock_free() property`
- `bool is_lock_free() const`
- `int8 exchange(int8 desired, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `int8 fetch_add(int8 arg, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `int8 fetch_and(int8 arg, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `int8 fetch_or(int8 arg, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `int8 fetch_sub(int8 arg, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `int8 fetch_xor(int8 arg, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `int8 load(memory_order order = MEMORY_ORDER_SEQ_CST) const`
- `int8 opAddAssign(int8 arg)`
- `int8 opAndAssign(int8 arg)`
- `int8 opAssign(int8 val)`
- `int8 opImplConv() const`
- `int8 opOrAssign(int8 arg)`
- `int8 opPostDec(int8 arg)`
- `int8 opPostInc(int8 arg)`
- `int8 opPreDec()`
- `int8 opPreInc()`
- `int8 opSubAssign(int8 arg)`
- `int8 opXorAssign(int8 arg)`
- `void notify_all()`
- `void notify_one()`
- `void store(int8 val, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `void wait(int8 old, memory_order order = MEMORY_ORDER_SEQ_CST) const`

### Class `atomic_signed_lock_free`
##### Behaviours / Constructors
- `void atomic_signed_lock_free()`
##### Methods
- `bool compare_exchange_strong(int64&inout expected, int64 desired, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `bool compare_exchange_strong(int64&inout expected, int64 desired, memory_order success, memory_order failure)`
- `bool compare_exchange_weak(int64&inout expected, int64 desired, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `bool compare_exchange_weak(int64&inout expected, int64 desired, memory_order success, memory_order failure)`
- `bool get_is_always_lock_free() property`
- `bool is_lock_free() const`
- `int64 exchange(int64 desired, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `int64 fetch_add(int64 arg, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `int64 fetch_and(int64 arg, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `int64 fetch_or(int64 arg, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `int64 fetch_sub(int64 arg, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `int64 fetch_xor(int64 arg, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `int64 load(memory_order order = MEMORY_ORDER_SEQ_CST) const`
- `int64 opAddAssign(int64 arg)`
- `int64 opAndAssign(int64 arg)`
- `int64 opAssign(int64 val)`
- `int64 opImplConv() const`
- `int64 opOrAssign(int64 arg)`
- `int64 opPostDec(int64 arg)`
- `int64 opPostInc(int64 arg)`
- `int64 opPreDec()`
- `int64 opPreInc()`
- `int64 opSubAssign(int64 arg)`
- `int64 opXorAssign(int64 arg)`
- `void notify_all()`
- `void notify_one()`
- `void store(int64 val, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `void wait(int64 old, memory_order order = MEMORY_ORDER_SEQ_CST) const`

### Class `atomic_uint`
##### Behaviours / Constructors
- `void atomic_uint()`
##### Methods
- `bool compare_exchange_strong(uint&inout expected, uint desired, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `bool compare_exchange_strong(uint&inout expected, uint desired, memory_order success, memory_order failure)`
- `bool compare_exchange_weak(uint&inout expected, uint desired, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `bool compare_exchange_weak(uint&inout expected, uint desired, memory_order success, memory_order failure)`
- `bool get_is_always_lock_free() property`
- `bool is_lock_free() const`
- `uint exchange(uint desired, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `uint fetch_add(uint arg, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `uint fetch_and(uint arg, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `uint fetch_or(uint arg, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `uint fetch_sub(uint arg, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `uint fetch_xor(uint arg, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `uint load(memory_order order = MEMORY_ORDER_SEQ_CST) const`
- `uint opAddAssign(uint arg)`
- `uint opAndAssign(uint arg)`
- `uint opAssign(uint val)`
- `uint opImplConv() const`
- `uint opOrAssign(uint arg)`
- `uint opPostDec(uint arg)`
- `uint opPostInc(uint arg)`
- `uint opPreDec()`
- `uint opPreInc()`
- `uint opSubAssign(uint arg)`
- `uint opXorAssign(uint arg)`
- `void notify_all()`
- `void notify_one()`
- `void store(uint val, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `void wait(uint old, memory_order order = MEMORY_ORDER_SEQ_CST) const`

### Class `atomic_uint16`
##### Behaviours / Constructors
- `void atomic_uint16()`
##### Methods
- `bool compare_exchange_strong(uint16&inout expected, uint16 desired, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `bool compare_exchange_strong(uint16&inout expected, uint16 desired, memory_order success, memory_order failure)`
- `bool compare_exchange_weak(uint16&inout expected, uint16 desired, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `bool compare_exchange_weak(uint16&inout expected, uint16 desired, memory_order success, memory_order failure)`
- `bool get_is_always_lock_free() property`
- `bool is_lock_free() const`
- `uint16 exchange(uint16 desired, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `uint16 fetch_add(uint16 arg, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `uint16 fetch_and(uint16 arg, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `uint16 fetch_or(uint16 arg, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `uint16 fetch_sub(uint16 arg, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `uint16 fetch_xor(uint16 arg, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `uint16 load(memory_order order = MEMORY_ORDER_SEQ_CST) const`
- `uint16 opAddAssign(uint16 arg)`
- `uint16 opAndAssign(uint16 arg)`
- `uint16 opAssign(uint16 val)`
- `uint16 opImplConv() const`
- `uint16 opOrAssign(uint16 arg)`
- `uint16 opPostDec(uint16 arg)`
- `uint16 opPostInc(uint16 arg)`
- `uint16 opPreDec()`
- `uint16 opPreInc()`
- `uint16 opSubAssign(uint16 arg)`
- `uint16 opXorAssign(uint16 arg)`
- `void notify_all()`
- `void notify_one()`
- `void store(uint16 val, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `void wait(uint16 old, memory_order order = MEMORY_ORDER_SEQ_CST) const`

### Class `atomic_uint32`
##### Behaviours / Constructors
- `void atomic_uint32()`
##### Methods
- `bool compare_exchange_strong(uint&inout expected, uint desired, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `bool compare_exchange_strong(uint&inout expected, uint desired, memory_order success, memory_order failure)`
- `bool compare_exchange_weak(uint&inout expected, uint desired, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `bool compare_exchange_weak(uint&inout expected, uint desired, memory_order success, memory_order failure)`
- `bool get_is_always_lock_free() property`
- `bool is_lock_free() const`
- `uint exchange(uint desired, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `uint fetch_add(uint arg, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `uint fetch_and(uint arg, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `uint fetch_or(uint arg, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `uint fetch_sub(uint arg, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `uint fetch_xor(uint arg, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `uint load(memory_order order = MEMORY_ORDER_SEQ_CST) const`
- `uint opAddAssign(uint arg)`
- `uint opAndAssign(uint arg)`
- `uint opAssign(uint val)`
- `uint opImplConv() const`
- `uint opOrAssign(uint arg)`
- `uint opPostDec(uint arg)`
- `uint opPostInc(uint arg)`
- `uint opPreDec()`
- `uint opPreInc()`
- `uint opSubAssign(uint arg)`
- `uint opXorAssign(uint arg)`
- `void notify_all()`
- `void notify_one()`
- `void store(uint val, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `void wait(uint old, memory_order order = MEMORY_ORDER_SEQ_CST) const`

### Class `atomic_uint64`
##### Behaviours / Constructors
- `void atomic_uint64()`
##### Methods
- `bool compare_exchange_strong(uint64&inout expected, uint64 desired, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `bool compare_exchange_strong(uint64&inout expected, uint64 desired, memory_order success, memory_order failure)`
- `bool compare_exchange_weak(uint64&inout expected, uint64 desired, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `bool compare_exchange_weak(uint64&inout expected, uint64 desired, memory_order success, memory_order failure)`
- `bool get_is_always_lock_free() property`
- `bool is_lock_free() const`
- `uint64 exchange(uint64 desired, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `uint64 fetch_add(uint64 arg, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `uint64 fetch_and(uint64 arg, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `uint64 fetch_or(uint64 arg, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `uint64 fetch_sub(uint64 arg, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `uint64 fetch_xor(uint64 arg, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `uint64 load(memory_order order = MEMORY_ORDER_SEQ_CST) const`
- `uint64 opAddAssign(uint64 arg)`
- `uint64 opAndAssign(uint64 arg)`
- `uint64 opAssign(uint64 val)`
- `uint64 opImplConv() const`
- `uint64 opOrAssign(uint64 arg)`
- `uint64 opPostDec(uint64 arg)`
- `uint64 opPostInc(uint64 arg)`
- `uint64 opPreDec()`
- `uint64 opPreInc()`
- `uint64 opSubAssign(uint64 arg)`
- `uint64 opXorAssign(uint64 arg)`
- `void notify_all()`
- `void notify_one()`
- `void store(uint64 val, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `void wait(uint64 old, memory_order order = MEMORY_ORDER_SEQ_CST) const`

### Class `atomic_uint8`
##### Behaviours / Constructors
- `void atomic_uint8()`
##### Methods
- `bool compare_exchange_strong(uint8&inout expected, uint8 desired, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `bool compare_exchange_strong(uint8&inout expected, uint8 desired, memory_order success, memory_order failure)`
- `bool compare_exchange_weak(uint8&inout expected, uint8 desired, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `bool compare_exchange_weak(uint8&inout expected, uint8 desired, memory_order success, memory_order failure)`
- `bool get_is_always_lock_free() property`
- `bool is_lock_free() const`
- `uint8 exchange(uint8 desired, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `uint8 fetch_add(uint8 arg, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `uint8 fetch_and(uint8 arg, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `uint8 fetch_or(uint8 arg, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `uint8 fetch_sub(uint8 arg, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `uint8 fetch_xor(uint8 arg, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `uint8 load(memory_order order = MEMORY_ORDER_SEQ_CST) const`
- `uint8 opAddAssign(uint8 arg)`
- `uint8 opAndAssign(uint8 arg)`
- `uint8 opAssign(uint8 val)`
- `uint8 opImplConv() const`
- `uint8 opOrAssign(uint8 arg)`
- `uint8 opPostDec(uint8 arg)`
- `uint8 opPostInc(uint8 arg)`
- `uint8 opPreDec()`
- `uint8 opPreInc()`
- `uint8 opSubAssign(uint8 arg)`
- `uint8 opXorAssign(uint8 arg)`
- `void notify_all()`
- `void notify_one()`
- `void store(uint8 val, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `void wait(uint8 old, memory_order order = MEMORY_ORDER_SEQ_CST) const`

### Class `atomic_unsigned_lock_free`
##### Behaviours / Constructors
- `void atomic_unsigned_lock_free()`
##### Methods
- `bool compare_exchange_strong(uint64&inout expected, uint64 desired, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `bool compare_exchange_strong(uint64&inout expected, uint64 desired, memory_order success, memory_order failure)`
- `bool compare_exchange_weak(uint64&inout expected, uint64 desired, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `bool compare_exchange_weak(uint64&inout expected, uint64 desired, memory_order success, memory_order failure)`
- `bool get_is_always_lock_free() property`
- `bool is_lock_free() const`
- `uint64 exchange(uint64 desired, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `uint64 fetch_add(uint64 arg, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `uint64 fetch_and(uint64 arg, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `uint64 fetch_or(uint64 arg, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `uint64 fetch_sub(uint64 arg, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `uint64 fetch_xor(uint64 arg, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `uint64 load(memory_order order = MEMORY_ORDER_SEQ_CST) const`
- `uint64 opAddAssign(uint64 arg)`
- `uint64 opAndAssign(uint64 arg)`
- `uint64 opAssign(uint64 val)`
- `uint64 opImplConv() const`
- `uint64 opOrAssign(uint64 arg)`
- `uint64 opPostDec(uint64 arg)`
- `uint64 opPostInc(uint64 arg)`
- `uint64 opPreDec()`
- `uint64 opPreInc()`
- `uint64 opSubAssign(uint64 arg)`
- `uint64 opXorAssign(uint64 arg)`
- `void notify_all()`
- `void notify_one()`
- `void store(uint64 val, memory_order order = MEMORY_ORDER_SEQ_CST)`
- `void wait(uint64 old, memory_order order = MEMORY_ORDER_SEQ_CST) const`

### Class `audio_band_pass_filter`
##### Behaviours / Constructors
- `audio_band_pass_filter@ audio_band_pass_filter(double cutoff_frequency, uint order, audio_engine@ engine = sound_default_engine)`
- `audio_band_pass_filter@ f(double cutoff_frequency, uint order, audio_engine@+ engine = sound_default_engine)`
##### Methods
- `audio_node@ opImplCast()`
- `audio_node_state get_state()`
- `audio_node_state get_state_by_time(uint64 global_time)`
- `audio_node_state get_state_by_time_range(uint64 global_time_begin, uint64 global_time_end)`
- `bool attach_output_bus(uint output_bus, audio_node@ destination, uint destination_input_bus)`
- `bool detach_all_output_buses()`
- `bool detach_output_bus(uint bus)`
- `bool set_output_bus_volume(uint bus, float volume)`
- `bool set_state(audio_node_state state)`
- `bool set_state_time(audio_node_state state, uint64 time)`
- `bool set_time(uint64 local_time)`
- `double get_cutoff_frequency() const property`
- `float get_output_bus_volume(uint bus)`
- `uint get_input_bus_count() const property`
- `uint get_input_channels(uint bus) const`
- `uint get_order() const property`
- `uint get_output_bus_count() const property`
- `uint get_output_channels(uint bus) const`
- `uint64 get_state_time(audio_node_state state)`
- `uint64 get_time() const`
- `void set_cutoff_frequency(double frequency) property`
- `void set_order(uint order) property`

### Class `audio_data_source`
##### Methods
- `array<float>@ read(uint64 frame_count = 0)`
- `audio_data_source@ get_current() const property`
- `audio_data_source@ get_next() const property`
- `audio_decoder@ opCast()`
- `audio_node@ opImplCast()`
- `audio_node_state get_state()`
- `audio_node_state get_state_by_time(uint64 global_time)`
- `audio_node_state get_state_by_time_range(uint64 global_time_begin, uint64 global_time_end)`
- `audio_ring_buffer@ opCast()`
- `bool attach_output_bus(uint output_bus, audio_node@ destination, uint destination_input_bus)`
- `bool detach_all_output_buses()`
- `bool detach_output_bus(uint bus)`
- `bool get_active() const property`
- `bool get_looping() const property`
- `bool seek_frames(uint64 frame_index)`
- `bool seek_milliseconds(float ms)`
- `bool set_current(audio_data_source@ new_current)`
- `bool set_loop_point(uint64 start_frame, uint64 end_frame)`
- `bool set_looping(bool looping)`
- `bool set_next(audio_data_source@ new_next)`
- `bool set_output_bus_volume(uint bus, float volume)`
- `bool set_range(uint64 start_frame, uint64 end_frame)`
- `bool set_state(audio_node_state state)`
- `bool set_state_time(audio_node_state state, uint64 time)`
- `bool set_time(uint64 local_time)`
- `float get_cursor_milliseconds() const property`
- `float get_length_milliseconds() const property`
- `float get_output_bus_volume(uint bus)`
- `float skip_milliseconds(float ms)`
- `microphone@ opCast()`
- `uint get_advised_read_frame_count() const property`
- `uint get_channels() const property`
- `uint get_input_bus_count() const property`
- `uint get_input_channels(uint bus) const`
- `uint get_output_bus_count() const property`
- `uint get_output_channels(uint bus) const`
- `uint get_sample_rate() const property`
- `uint64 get_cursor_frames() const property`
- `uint64 get_length_frames() const property`
- `uint64 get_state_time(audio_node_state state)`
- `uint64 get_time() const`
- `uint64 skip_frames(uint64 frame_count)`
- `void get_loop_point(uint64&out start_frame, uint64&out end_frame) const`
- `void get_range(uint64&out start_frame, uint64&out end_frame) const`

### Class `audio_decoder`
##### Behaviours / Constructors
- `audio_decoder@ audio_decoder(audio_engine@ engine = sound_default_engine)`
- `audio_decoder@ d(audio_engine@+ engine = sound_default_engine)`
##### Methods
- `array<float>@ read(uint64 frame_count = 0)`
- `audio_data_source@ get_current() const property`
- `audio_data_source@ get_next() const property`
- `audio_data_source@ opImplCast()`
- `audio_node@ opImplCast()`
- `audio_node_state get_state()`
- `audio_node_state get_state_by_time(uint64 global_time)`
- `audio_node_state get_state_by_time_range(uint64 global_time_begin, uint64 global_time_end)`
- `bool attach_output_bus(uint output_bus, audio_node@ destination, uint destination_input_bus)`
- `bool close()`
- `bool detach_all_output_buses()`
- `bool detach_output_bus(uint bus)`
- `bool get_active() const property`
- `bool get_looping() const property`
- `bool open(const string&in filename, const pack_interface@+ pack_file = sound_default_pack, uint sample_rate = 0, uint channels = 0)`
- `bool open(datastream@ stream, uint sample_rate = 0, uint channels = 0)`
- `bool seek_frames(uint64 frame_index)`
- `bool seek_milliseconds(float ms)`
- `bool set_current(audio_data_source@ new_current)`
- `bool set_loop_point(uint64 start_frame, uint64 end_frame)`
- `bool set_looping(bool looping)`
- `bool set_next(audio_data_source@ new_next)`
- `bool set_output_bus_volume(uint bus, float volume)`
- `bool set_range(uint64 start_frame, uint64 end_frame)`
- `bool set_state(audio_node_state state)`
- `bool set_state_time(audio_node_state state, uint64 time)`
- `bool set_time(uint64 local_time)`
- `float get_cursor_milliseconds() const property`
- `float get_length_milliseconds() const property`
- `float get_output_bus_volume(uint bus)`
- `float skip_milliseconds(float ms)`
- `uint get_advised_read_frame_count() const property`
- `uint get_channels() const property`
- `uint get_input_bus_count() const property`
- `uint get_input_channels(uint bus) const`
- `uint get_output_bus_count() const property`
- `uint get_output_channels(uint bus) const`
- `uint get_sample_rate() const property`
- `uint64 get_cursor_frames() const property`
- `uint64 get_length_frames() const property`
- `uint64 get_state_time(audio_node_state state)`
- `uint64 get_time() const`
- `uint64 skip_frames(uint64 frame_count)`
- `void get_loop_point(uint64&out start_frame, uint64&out end_frame) const`
- `void get_range(uint64&out start_frame, uint64&out end_frame) const`

### Class `audio_delay_node`
##### Behaviours / Constructors
- `audio_delay_node@ audio_delay_node(uint delay_in_frames, float decay, audio_engine@ engine = sound_default_engine)`
- `audio_delay_node@ d(uint delay_in_frames, float decay, audio_engine@+ engine = sound_default_engine)`
##### Methods
- `audio_node@ opImplCast()`
- `audio_node_state get_state()`
- `audio_node_state get_state_by_time(uint64 global_time)`
- `audio_node_state get_state_by_time_range(uint64 global_time_begin, uint64 global_time_end)`
- `bool attach_output_bus(uint output_bus, audio_node@ destination, uint destination_input_bus)`
- `bool detach_all_output_buses()`
- `bool detach_output_bus(uint bus)`
- `bool set_output_bus_volume(uint bus, float volume)`
- `bool set_state(audio_node_state state)`
- `bool set_state_time(audio_node_state state, uint64 time)`
- `bool set_time(uint64 local_time)`
- `float get_decay() const property`
- `float get_dry() const property`
- `float get_output_bus_volume(uint bus)`
- `float get_wet() const property`
- `uint get_input_bus_count() const property`
- `uint get_input_channels(uint bus) const`
- `uint get_output_bus_count() const property`
- `uint get_output_channels(uint bus) const`
- `uint64 get_state_time(audio_node_state state)`
- `uint64 get_time() const`
- `void set_decay(float decay) property`
- `void set_dry(float dry) property`
- `void set_wet(float wet) property`

### Class `audio_encoder`
##### Methods
- `audio_node@ opImplCast()`
- `audio_node_state get_state()`
- `audio_node_state get_state_by_time(uint64 global_time)`
- `audio_node_state get_state_by_time_range(uint64 global_time_begin, uint64 global_time_end)`
- `audio_opus_encoder@ opCast()`
- `audio_wav_encoder@ opCast()`
- `bool attach_output_bus(uint output_bus, audio_node@ destination, uint destination_input_bus)`
- `bool close()`
- `bool detach_all_output_buses()`
- `bool detach_output_bus(uint bus)`
- `bool get_active() const property`
- `bool open(const string&in filename, uint sample_rate, uint channels, uint flags = AUDIO_ENCODER_DEFAULTS)`
- `bool open(datastream@ stream, uint sample_rate, uint channels, uint flags = AUDIO_ENCODER_DEFAULTS)`
- `bool open(uint sample_rate, uint channels, uint flags = AUDIO_ENCODER_DEFAULTS)`
- `bool set_output_bus_volume(uint bus, float volume)`
- `bool set_state(audio_node_state state)`
- `bool set_state_time(audio_node_state state, uint64 time)`
- `bool set_time(uint64 local_time)`
- `float get_output_bus_volume(uint bus)`
- `string get_format() const property`
- `string read()`
- `uint get_channels() const property`
- `uint get_default_open_flags() const property`
- `uint get_input_bus_count() const property`
- `uint get_input_channels(uint bus) const`
- `uint get_output_bus_count() const property`
- `uint get_output_channels(uint bus) const`
- `uint get_sample_rate() const property`
- `uint write(const array<float>@ frames)`
- `uint write(const memory_buffer<float>&inout frames)`
- `uint64 get_frames_written() const property`
- `uint64 get_state_time(audio_node_state state)`
- `uint64 get_time() const`

### Class `audio_engine`
##### Behaviours / Constructors
- `audio_engine@ audio_engine(int flags, int sample_rate = 0, int channels = 0)`
- `audio_engine@ e(int flags, int sample_rate = 0, int channels = 0)`
##### Methods
- `audio_engine_processing_callback@+ get_processing_callback() const property`
- `audio_node@ opImplCast()`
- `audio_node@+ get_endpoint() const property`
- `audio_node_state get_state()`
- `audio_node_state get_state_by_time(uint64 global_time)`
- `audio_node_state get_state_by_time_range(uint64 global_time_begin, uint64 global_time_end)`
- `bool attach_output_bus(uint output_bus, audio_node@ destination, uint destination_input_bus)`
- `bool detach_all_output_buses()`
- `bool detach_output_bus(uint bus)`
- `bool get_listener_enabled(int index) const`
- `bool set_device(int device)`
- `bool set_gain(float gain)`
- `bool set_output_bus_volume(uint bus, float volume)`
- `bool set_state(audio_node_state state)`
- `bool set_state_time(audio_node_state state, uint64 time)`
- `bool set_time(uint64 local_time)`
- `bool set_time_in_frames(uint64 time_frames)`
- `bool set_time_in_milliseconds(uint64 time_ms)`
- `bool set_volume(float volume)`
- `bool start()`
- `bool stop()`
- `float get_gain() const property`
- `float get_output_bus_volume(uint bus)`
- `float get_volume() const property`
- `float[]@ read(uint64 frame_count)`
- `int find_closest_listener(const vector&in position) const`
- `int find_closest_listener(float x, float y, float z) const`
- `int get_channels() const property`
- `int get_device() const`
- `int get_flags() const property`
- `int get_sample_rate() const property`
- `mixer@ mixer()`
- `sound@ play(const string&in path, const vector&in position = vector(FLOAT_MAX, FLOAT_MAX, FLOAT_MAX), float volume = 0.0, float pan = 0.0, float pitch = 100.0, mixer@ mix = null, const pack_interface@ pack_file = sound_default_pack, bool autoplay = true)`
- `sound@ play(const string&in path, const vector&in position = vector(FLOAT_MAX, FLOAT_MAX, FLOAT_MAX), float volume = 0.0, float pan = 0.0, float pitch = 100.0, mixer@+ mix = null, const pack_interface@+ pack_file = sound_default_pack, bool autoplay = true)`
- `sound@ sound()`
- `uint get_input_bus_count() const property`
- `uint get_input_channels(uint bus) const`
- `uint get_listener_count() const property`
- `uint get_output_bus_count() const property`
- `uint get_output_channels(uint bus) const`
- `uint64 get_state_time(audio_node_state state)`
- `uint64 get_time() const`
- `uint64 get_time_in_frames() const property`
- `uint64 get_time_in_milliseconds() const property`
- `vector get_listener_direction(int index) const`
- `vector get_listener_position(int index) const`
- `vector get_listener_velocity(int index) const`
- `vector get_listener_world_up(int index) const`
- `void get_listener_cone(int index, float&out inner_radians, float&out outer_radians, float&out outer_gain) const`
- `void set_listener_cone(int index, float inner_radians, float outer_radians, float outer_gain)`
- `void set_listener_direction(int index, const vector&in direction)`
- `void set_listener_direction(int index, float x, float y, float z)`
- `void set_listener_enabled(int index, bool enabled)`
- `void set_listener_position(int index, const vector&in position)`
- `void set_listener_position(int index, float x, float y, float z)`
- `void set_listener_velocity(int index, const vector&in velocity)`
- `void set_listener_velocity(int index, float x, float y, float z)`
- `void set_listener_world_up(int index, const vector&in world_up)`
- `void set_listener_world_up(int index, float x, float y, float z)`
- `void set_processing_callback(audio_engine_processing_callback@ cb) property`

### Class `audio_freeverb_node`
##### Behaviours / Constructors
- `audio_freeverb_node@ audio_freeverb_node(audio_engine@ engine = sound_default_engine)`
- `audio_freeverb_node@ n(audio_engine@+ engine = sound_default_engine)`
##### Methods
- `audio_node@ opImplCast()`
- `audio_node_state get_state()`
- `audio_node_state get_state_by_time(uint64 global_time)`
- `audio_node_state get_state_by_time_range(uint64 global_time_begin, uint64 global_time_end)`
- `bool attach_output_bus(uint output_bus, audio_node@ destination, uint destination_input_bus)`
- `bool detach_all_output_buses()`
- `bool detach_output_bus(uint bus)`
- `bool get_frozen() const property`
- `bool set_output_bus_volume(uint bus, float volume)`
- `bool set_state(audio_node_state state)`
- `bool set_state_time(audio_node_state state, uint64 time)`
- `bool set_time(uint64 local_time)`
- `float get_damping() const property`
- `float get_dry() const property`
- `float get_input_width() const property`
- `float get_output_bus_volume(uint bus)`
- `float get_room_size() const property`
- `float get_wet() const property`
- `float get_width() const property`
- `uint get_input_bus_count() const property`
- `uint get_input_channels(uint bus) const`
- `uint get_output_bus_count() const property`
- `uint get_output_channels(uint bus) const`
- `uint64 get_state_time(audio_node_state state)`
- `uint64 get_time() const`
- `void set_damping(float damping) property`
- `void set_dry(float dry) property`
- `void set_frozen(bool frozen) property`
- `void set_input_width(float width) property`
- `void set_room_size(float size) property`
- `void set_wet(float wet) property`
- `void set_width(float width) property`

### Class `audio_high_pass_filter`
##### Behaviours / Constructors
- `audio_high_pass_filter@ audio_high_pass_filter(double cutoff_frequency, uint order, audio_engine@ engine = sound_default_engine)`
- `audio_high_pass_filter@ f(double cutoff_frequency, uint order, audio_engine@+ engine = sound_default_engine)`
##### Methods
- `audio_node@ opImplCast()`
- `audio_node_state get_state()`
- `audio_node_state get_state_by_time(uint64 global_time)`
- `audio_node_state get_state_by_time_range(uint64 global_time_begin, uint64 global_time_end)`
- `bool attach_output_bus(uint output_bus, audio_node@ destination, uint destination_input_bus)`
- `bool detach_all_output_buses()`
- `bool detach_output_bus(uint bus)`
- `bool set_output_bus_volume(uint bus, float volume)`
- `bool set_state(audio_node_state state)`
- `bool set_state_time(audio_node_state state, uint64 time)`
- `bool set_time(uint64 local_time)`
- `double get_cutoff_frequency() const property`
- `float get_output_bus_volume(uint bus)`
- `uint get_input_bus_count() const property`
- `uint get_input_channels(uint bus) const`
- `uint get_order() const property`
- `uint get_output_bus_count() const property`
- `uint get_output_channels(uint bus) const`
- `uint64 get_state_time(audio_node_state state)`
- `uint64 get_time() const`
- `void set_cutoff_frequency(double frequency) property`
- `void set_order(uint order) property`

### Class `audio_high_shelf_filter`
##### Behaviours / Constructors
- `audio_high_shelf_filter@ audio_high_shelf_filter(double gain_db, double q, double frequency, audio_engine@ engine = sound_default_engine)`
- `audio_high_shelf_filter@ f(double gain_db, double q, double frequency, audio_engine@+ engine = sound_default_engine)`
##### Methods
- `audio_node@ opImplCast()`
- `audio_node_state get_state()`
- `audio_node_state get_state_by_time(uint64 global_time)`
- `audio_node_state get_state_by_time_range(uint64 global_time_begin, uint64 global_time_end)`
- `bool attach_output_bus(uint output_bus, audio_node@ destination, uint destination_input_bus)`
- `bool detach_all_output_buses()`
- `bool detach_output_bus(uint bus)`
- `bool set_output_bus_volume(uint bus, float volume)`
- `bool set_state(audio_node_state state)`
- `bool set_state_time(audio_node_state state, uint64 time)`
- `bool set_time(uint64 local_time)`
- `double get_frequency() const property`
- `double get_gain() const property`
- `double get_q() const property`
- `float get_output_bus_volume(uint bus)`
- `uint get_input_bus_count() const property`
- `uint get_input_channels(uint bus) const`
- `uint get_output_bus_count() const property`
- `uint get_output_channels(uint bus) const`
- `uint64 get_state_time(audio_node_state state)`
- `uint64 get_time() const`
- `void set_frequency(double frequency) property`
- `void set_gain(double gain) property`
- `void set_q(double q) property`

### Class `audio_low_pass_filter`
##### Behaviours / Constructors
- `audio_low_pass_filter@ audio_low_pass_filter(double cutoff_frequency, uint order, audio_engine@ engine = sound_default_engine)`
- `audio_low_pass_filter@ f(double cutoff_frequency, uint order, audio_engine@+ engine = sound_default_engine)`
##### Methods
- `audio_node@ opImplCast()`
- `audio_node_state get_state()`
- `audio_node_state get_state_by_time(uint64 global_time)`
- `audio_node_state get_state_by_time_range(uint64 global_time_begin, uint64 global_time_end)`
- `bool attach_output_bus(uint output_bus, audio_node@ destination, uint destination_input_bus)`
- `bool detach_all_output_buses()`
- `bool detach_output_bus(uint bus)`
- `bool set_output_bus_volume(uint bus, float volume)`
- `bool set_state(audio_node_state state)`
- `bool set_state_time(audio_node_state state, uint64 time)`
- `bool set_time(uint64 local_time)`
- `double get_cutoff_frequency() const property`
- `float get_output_bus_volume(uint bus)`
- `uint get_input_bus_count() const property`
- `uint get_input_channels(uint bus) const`
- `uint get_order() const property`
- `uint get_output_bus_count() const property`
- `uint get_output_channels(uint bus) const`
- `uint64 get_state_time(audio_node_state state)`
- `uint64 get_time() const`
- `void set_cutoff_frequency(double frequency) property`
- `void set_order(uint order) property`

### Class `audio_low_shelf_filter`
##### Behaviours / Constructors
- `audio_low_shelf_filter@ audio_low_shelf_filter(double gain_db, double q, double frequency, audio_engine@ engine = sound_default_engine)`
- `audio_low_shelf_filter@ f(double gain_db, double q, double frequency, audio_engine@+ engine = sound_default_engine)`
##### Methods
- `audio_node@ opImplCast()`
- `audio_node_state get_state()`
- `audio_node_state get_state_by_time(uint64 global_time)`
- `audio_node_state get_state_by_time_range(uint64 global_time_begin, uint64 global_time_end)`
- `bool attach_output_bus(uint output_bus, audio_node@ destination, uint destination_input_bus)`
- `bool detach_all_output_buses()`
- `bool detach_output_bus(uint bus)`
- `bool set_output_bus_volume(uint bus, float volume)`
- `bool set_state(audio_node_state state)`
- `bool set_state_time(audio_node_state state, uint64 time)`
- `bool set_time(uint64 local_time)`
- `double get_frequency() const property`
- `double get_gain() const property`
- `double get_q() const property`
- `float get_output_bus_volume(uint bus)`
- `uint get_input_bus_count() const property`
- `uint get_input_channels(uint bus) const`
- `uint get_output_bus_count() const property`
- `uint get_output_channels(uint bus) const`
- `uint64 get_state_time(audio_node_state state)`
- `uint64 get_time() const`
- `void set_frequency(double frequency) property`
- `void set_gain(double gain) property`
- `void set_q(double q) property`

### Class `audio_node`
##### Methods
- `audio_band_pass_filter@ opCast()`
- `audio_data_source@ opCast()`
- `audio_decoder@ opCast()`
- `audio_delay_node@ opCast()`
- `audio_encoder@ opCast()`
- `audio_engine@ opCast()`
- `audio_freeverb_node@ opCast()`
- `audio_high_pass_filter@ opCast()`
- `audio_high_shelf_filter@ opCast()`
- `audio_low_pass_filter@ opCast()`
- `audio_low_shelf_filter@ opCast()`
- `audio_node_chain@ opCast()`
- `audio_node_state get_state()`
- `audio_node_state get_state_by_time(uint64 global_time)`
- `audio_node_state get_state_by_time_range(uint64 global_time_begin, uint64 global_time_end)`
- `audio_notch_filter@ opCast()`
- `audio_opus_encoder@ opCast()`
- `audio_peak_filter@ opCast()`
- `audio_ring_buffer@ opCast()`
- `audio_splitter_node@ opCast()`
- `audio_wav_encoder@ opCast()`
- `bool attach_output_bus(uint output_bus, audio_node@ destination, uint destination_input_bus)`
- `bool detach_all_output_buses()`
- `bool detach_output_bus(uint bus)`
- `bool set_output_bus_volume(uint bus, float volume)`
- `bool set_state(audio_node_state state)`
- `bool set_state_time(audio_node_state state, uint64 time)`
- `bool set_time(uint64 local_time)`
- `float get_output_bus_volume(uint bus)`
- `microphone@ opCast()`
- `mixer@ opCast()`
- `phonon_binaural_node@ opCast()`
- `reverb3d@ opCast()`
- `sound@ opCast()`
- `uint get_input_bus_count() const property`
- `uint get_input_channels(uint bus) const`
- `uint get_output_bus_count() const property`
- `uint get_output_channels(uint bus) const`
- `uint64 get_state_time(audio_node_state state)`
- `uint64 get_time() const`

### Class `audio_node_chain`
##### Behaviours / Constructors
- `audio_node_chain@ audio_node_chain(audio_node@ source = null, audio_node@ endpoint = null, audio_engine@ engine = sound_default_engine)`
- `audio_node_chain@ c(audio_node@+ source = null, audio_node@+ endpoint = null, audio_engine@+ engine = sound_default_engine)`
##### Methods
- `audio_node@ opImplCast()`
- `audio_node@+ get_endpoint() const property`
- `audio_node@+ get_first() const property`
- `audio_node@+ get_last() const property`
- `audio_node@+ opIndex(uint index) const`
- `audio_node_state get_state()`
- `audio_node_state get_state_by_time(uint64 global_time)`
- `audio_node_state get_state_by_time_range(uint64 global_time_begin, uint64 global_time_end)`
- `bool add_node(audio_node@+ node, audio_node@+ after = null, uint input_bus_index = 0)`
- `bool add_node(audio_node@+ node, int after, uint input_bus_index = 0)`
- `bool attach_output_bus(uint output_bus, audio_node@ destination, uint destination_input_bus)`
- `bool clear(bool detach_nodes = true)`
- `bool detach_all_output_buses()`
- `bool detach_output_bus(uint bus)`
- `bool remove_node(audio_node@+ node)`
- `bool remove_node(uint index)`
- `bool set_output_bus_volume(uint bus, float volume)`
- `bool set_state(audio_node_state state)`
- `bool set_state_time(audio_node_state state, uint64 time)`
- `bool set_time(uint64 local_time)`
- `float get_output_bus_volume(uint bus)`
- `int find(audio_node@+ node) const`
- `uint get_input_bus_count() const property`
- `uint get_input_channels(uint bus) const`
- `uint get_node_count() const property`
- `uint get_output_bus_count() const property`
- `uint get_output_channels(uint bus) const`
- `uint64 get_state_time(audio_node_state state)`
- `uint64 get_time() const`
- `void set_endpoint(audio_node@+ endpoint, uint input_bus_index = 0)`

### Class `audio_notch_filter`
##### Behaviours / Constructors
- `audio_notch_filter@ audio_notch_filter(double q, double frequency, audio_engine@ engine = sound_default_engine)`
- `audio_notch_filter@ f(double q, double frequency, audio_engine@+ engine = sound_default_engine)`
##### Methods
- `audio_node@ opImplCast()`
- `audio_node_state get_state()`
- `audio_node_state get_state_by_time(uint64 global_time)`
- `audio_node_state get_state_by_time_range(uint64 global_time_begin, uint64 global_time_end)`
- `bool attach_output_bus(uint output_bus, audio_node@ destination, uint destination_input_bus)`
- `bool detach_all_output_buses()`
- `bool detach_output_bus(uint bus)`
- `bool set_output_bus_volume(uint bus, float volume)`
- `bool set_state(audio_node_state state)`
- `bool set_state_time(audio_node_state state, uint64 time)`
- `bool set_time(uint64 local_time)`
- `double get_frequency() const property`
- `double get_q() const property`
- `float get_output_bus_volume(uint bus)`
- `uint get_input_bus_count() const property`
- `uint get_input_channels(uint bus) const`
- `uint get_output_bus_count() const property`
- `uint get_output_channels(uint bus) const`
- `uint64 get_state_time(audio_node_state state)`
- `uint64 get_time() const`
- `void set_frequency(double frequency) property`
- `void set_q(double q) property`

### Class `audio_opus_encoder`
##### Behaviours / Constructors
- `audio_opus_encoder@ audio_opus_encoder(audio_engine@ engine = sound_default_engine)`
- `audio_opus_encoder@ e(audio_engine@+ engine = sound_default_engine)`
##### Methods
- `audio_encoder@ opImplCast()`
- `audio_node@ opImplCast()`
- `audio_node_state get_state()`
- `audio_node_state get_state_by_time(uint64 global_time)`
- `audio_node_state get_state_by_time_range(uint64 global_time_begin, uint64 global_time_end)`
- `bool attach_output_bus(uint output_bus, audio_node@ destination, uint destination_input_bus)`
- `bool close()`
- `bool detach_all_output_buses()`
- `bool detach_output_bus(uint bus)`
- `bool get_active() const property`
- `bool get_cvbr() const property`
- `bool get_dtx() const property`
- `bool get_vbr() const property`
- `bool open(const string&in filename, uint sample_rate, uint channels, uint flags = AUDIO_ENCODER_DEFAULTS)`
- `bool open(datastream@ stream, uint sample_rate, uint channels, uint flags = AUDIO_ENCODER_DEFAULTS)`
- `bool open(uint sample_rate, uint channels, uint flags = AUDIO_ENCODER_DEFAULTS)`
- `bool set_output_bus_volume(uint bus, float volume)`
- `bool set_state(audio_node_state state)`
- `bool set_state_time(audio_node_state state, uint64 time)`
- `bool set_time(uint64 local_time)`
- `float get_output_bus_volume(uint bus)`
- `int get_application() const property`
- `int get_bitrate() const property`
- `int get_complexity() const property`
- `int get_packet_loss_percent() const property`
- `int get_signal_type() const property`
- `string get_format() const property`
- `string read()`
- `uint get_channels() const property`
- `uint get_default_open_flags() const property`
- `uint get_input_bus_count() const property`
- `uint get_input_channels(uint bus) const`
- `uint get_output_bus_count() const property`
- `uint get_output_channels(uint bus) const`
- `uint get_sample_rate() const property`
- `uint write(const array<float>@ frames)`
- `uint write(const memory_buffer<float>&inout frames)`
- `uint64 get_frames_written() const property`
- `uint64 get_state_time(audio_node_state state)`
- `uint64 get_time() const`
- `void set_application(int application) property`
- `void set_bitrate(int bitrate) property`
- `void set_complexity(int complexity) property`
- `void set_cvbr(bool enabled) property`
- `void set_dtx(bool enabled) property`
- `void set_packet_loss_percent(int percent) property`
- `void set_signal_type(int signal_type) property`
- `void set_vbr(bool enabled) property`

### Class `audio_peak_filter`
##### Behaviours / Constructors
- `audio_peak_filter@ audio_peak_filter(double gain_db, double q, double frequency, audio_engine@ engine = sound_default_engine)`
- `audio_peak_filter@ f(double gain_db, double q, double frequency, audio_engine@+ engine = sound_default_engine)`
##### Methods
- `audio_node@ opImplCast()`
- `audio_node_state get_state()`
- `audio_node_state get_state_by_time(uint64 global_time)`
- `audio_node_state get_state_by_time_range(uint64 global_time_begin, uint64 global_time_end)`
- `bool attach_output_bus(uint output_bus, audio_node@ destination, uint destination_input_bus)`
- `bool detach_all_output_buses()`
- `bool detach_output_bus(uint bus)`
- `bool set_output_bus_volume(uint bus, float volume)`
- `bool set_state(audio_node_state state)`
- `bool set_state_time(audio_node_state state, uint64 time)`
- `bool set_time(uint64 local_time)`
- `double get_frequency() const property`
- `double get_gain() const property`
- `double get_q() const property`
- `float get_output_bus_volume(uint bus)`
- `uint get_input_bus_count() const property`
- `uint get_input_channels(uint bus) const`
- `uint get_output_bus_count() const property`
- `uint get_output_channels(uint bus) const`
- `uint64 get_state_time(audio_node_state state)`
- `uint64 get_time() const`
- `void set_frequency(double frequency) property`
- `void set_gain(double gain) property`
- `void set_q(double q) property`

### Class `audio_ring_buffer`
##### Behaviours / Constructors
- `audio_ring_buffer@ audio_ring_buffer(uint channels, uint size, audio_engine@ engine = sound_default_engine)`
- `audio_ring_buffer@ r(uint channels, uint size, audio_engine@+ engine = sound_default_engine)`
##### Methods
- `array<float>@ read(uint64 frame_count = 0)`
- `audio_data_source@ get_current() const property`
- `audio_data_source@ get_next() const property`
- `audio_data_source@ opImplCast()`
- `audio_node@ opImplCast()`
- `audio_node_state get_state()`
- `audio_node_state get_state_by_time(uint64 global_time)`
- `audio_node_state get_state_by_time_range(uint64 global_time_begin, uint64 global_time_end)`
- `bool attach_output_bus(uint output_bus, audio_node@ destination, uint destination_input_bus)`
- `bool detach_all_output_buses()`
- `bool detach_output_bus(uint bus)`
- `bool get_active() const property`
- `bool get_looping() const property`
- `bool seek_frames(uint64 frame_index)`
- `bool seek_milliseconds(float ms)`
- `bool set_current(audio_data_source@ new_current)`
- `bool set_loop_point(uint64 start_frame, uint64 end_frame)`
- `bool set_looping(bool looping)`
- `bool set_next(audio_data_source@ new_next)`
- `bool set_output_bus_volume(uint bus, float volume)`
- `bool set_range(uint64 start_frame, uint64 end_frame)`
- `bool set_state(audio_node_state state)`
- `bool set_state_time(audio_node_state state, uint64 time)`
- `bool set_time(uint64 local_time)`
- `float get_cursor_milliseconds() const property`
- `float get_length_milliseconds() const property`
- `float get_output_bus_volume(uint bus)`
- `float skip_milliseconds(float ms)`
- `microphone@ opCast()`
- `uint get_advised_read_frame_count() const property`
- `uint get_available_read() const property`
- `uint get_available_write() const property`
- `uint get_channels() const property`
- `uint get_input_bus_count() const property`
- `uint get_input_channels(uint bus) const`
- `uint get_output_bus_count() const property`
- `uint get_output_channels(uint bus) const`
- `uint get_sample_rate() const property`
- `uint write(const array<float>@ frames)`
- `uint write(const memory_buffer<float>&inout frames)`
- `uint64 get_cursor_frames() const property`
- `uint64 get_length_frames() const property`
- `uint64 get_state_time(audio_node_state state)`
- `uint64 get_time() const`
- `uint64 skip_frames(uint64 frame_count)`
- `void get_loop_point(uint64&out start_frame, uint64&out end_frame) const`
- `void get_range(uint64&out start_frame, uint64&out end_frame) const`
- `void reset()`

### Class `audio_splitter_node`
##### Behaviours / Constructors
- `audio_splitter_node@ audio_splitter_node(audio_engine@ engine, int channels)`
- `audio_splitter_node@ n(audio_engine@+ engine, int channels)`
##### Methods
- `audio_node@ opImplCast()`
- `audio_node_state get_state()`
- `audio_node_state get_state_by_time(uint64 global_time)`
- `audio_node_state get_state_by_time_range(uint64 global_time_begin, uint64 global_time_end)`
- `bool attach_output_bus(uint output_bus, audio_node@ destination, uint destination_input_bus)`
- `bool detach_all_output_buses()`
- `bool detach_output_bus(uint bus)`
- `bool set_output_bus_volume(uint bus, float volume)`
- `bool set_state(audio_node_state state)`
- `bool set_state_time(audio_node_state state, uint64 time)`
- `bool set_time(uint64 local_time)`
- `float get_output_bus_volume(uint bus)`
- `uint get_input_bus_count() const property`
- `uint get_input_channels(uint bus) const`
- `uint get_output_bus_count() const property`
- `uint get_output_channels(uint bus) const`
- `uint64 get_state_time(audio_node_state state)`
- `uint64 get_time() const`

### Class `audio_wav_encoder`
##### Behaviours / Constructors
- `audio_wav_encoder@ audio_wav_encoder(audio_engine@ engine = sound_default_engine)`
- `audio_wav_encoder@ e(audio_engine@+ engine = sound_default_engine)`
##### Methods
- `audio_encoder@ opImplCast()`
- `audio_format get_wav_format() const property`
- `audio_node@ opImplCast()`
- `audio_node_state get_state()`
- `audio_node_state get_state_by_time(uint64 global_time)`
- `audio_node_state get_state_by_time_range(uint64 global_time_begin, uint64 global_time_end)`
- `bool attach_output_bus(uint output_bus, audio_node@ destination, uint destination_input_bus)`
- `bool close()`
- `bool detach_all_output_buses()`
- `bool detach_output_bus(uint bus)`
- `bool get_active() const property`
- `bool open(const string&in filename, uint sample_rate, uint channels, uint flags = AUDIO_ENCODER_DEFAULTS)`
- `bool open(datastream@ stream, uint sample_rate, uint channels, uint flags = AUDIO_ENCODER_DEFAULTS)`
- `bool open(uint sample_rate, uint channels, uint flags = AUDIO_ENCODER_DEFAULTS)`
- `bool set_output_bus_volume(uint bus, float volume)`
- `bool set_state(audio_node_state state)`
- `bool set_state_time(audio_node_state state, uint64 time)`
- `bool set_time(uint64 local_time)`
- `float get_output_bus_volume(uint bus)`
- `string get_format() const property`
- `string read()`
- `uint get_channels() const property`
- `uint get_default_open_flags() const property`
- `uint get_input_bus_count() const property`
- `uint get_input_channels(uint bus) const`
- `uint get_output_bus_count() const property`
- `uint get_output_channels(uint bus) const`
- `uint get_sample_rate() const property`
- `uint write(const array<float>@ frames)`
- `uint write(const memory_buffer<float>&inout frames)`
- `uint64 get_frames_written() const property`
- `uint64 get_state_time(audio_node_state state)`
- `uint64 get_time() const`

### Class `base32_decoder`
##### Behaviours / Constructors
- `base32_decoder@ base32_decoder()`
- `base32_decoder@ base32_decoder(datastream@ stream, const string&in encoding = "", int byteorder = 1)`
##### Properties
- `bool autoflush`
- `bool binary`
- `bool skip_eof`
- `bool sync_rw_cursors`
##### Methods
- `base32_decoder& opShl(double value)`
- `base32_decoder& opShl(float value)`
- `base32_decoder& opShl(int value)`
- `base32_decoder& opShl(int16 value)`
- `base32_decoder& opShl(int64 value)`
- `base32_decoder& opShl(int8 value)`
- `base32_decoder& opShl(string value)`
- `base32_decoder& opShl(uint value)`
- `base32_decoder& opShl(uint16 value)`
- `base32_decoder& opShl(uint64 value)`
- `base32_decoder& opShl(uint8 value)`
- `base32_decoder& opShr(double&out value)`
- `base32_decoder& opShr(float&out value)`
- `base32_decoder& opShr(int&out value)`
- `base32_decoder& opShr(int16&out value)`
- `base32_decoder& opShr(int64&out value)`
- `base32_decoder& opShr(int8&out value)`
- `base32_decoder& opShr(string&out value)`
- `base32_decoder& opShr(uint&out value)`
- `base32_decoder& opShr(uint16&out value)`
- `base32_decoder& opShr(uint64&out value)`
- `base32_decoder& opShr(uint8&out value)`
- `base32_decoder& write_double(double value)`
- `base32_decoder& write_float(float value)`
- `base32_decoder& write_int(int value)`
- `base32_decoder& write_int16(int16 value)`
- `base32_decoder& write_int64(int64 value)`
- `base32_decoder& write_int8(int8 value)`
- `base32_decoder& write_string(string value)`
- `base32_decoder& write_uint(uint value)`
- `base32_decoder& write_uint16(uint16 value)`
- `base32_decoder& write_uint64(uint64 value)`
- `base32_decoder& write_uint8(uint8 value)`
- `bool close(bool close_all = false)`
- `bool close_all()`
- `bool get_active() const property`
- `bool get_bad() const property`
- `bool get_eof() const property`
- `bool get_fail() const property`
- `bool get_good() const property`
- `bool open(datastream@ stream, const string&in encoding = "", int byteorder = 1)`
- `bool rseek(uint64 offset)`
- `bool rseek_end(uint64 offset = 0)`
- `bool rseek_relative(int64 offset)`
- `bool seek(uint64 offset)`
- `bool seek_end(uint64 offset = 0)`
- `bool seek_relative(int64 offset)`
- `bool wseek(uint64 offset)`
- `bool wseek_end(uint64 offset = 0)`
- `bool wseek_relative(int64 offset)`
- `datastream@ opImplCast()`
- `double read_double()`
- `float read_float()`
- `int read_int()`
- `int16 read_int16()`
- `int64 get_pos() const property`
- `int64 get_rpos() const property`
- `int64 get_wpos() const property`
- `int64 read_int64()`
- `int8 read_int8()`
- `string read(uint count = 0)`
- `string read_line()`
- `string read_string()`
- `string read_until(const string&in text, bool require_full)`
- `uint read_uint()`
- `uint write(const string&in data)`
- `uint16 read_uint16()`
- `uint64 get_available() const property`
- `uint64 read_7bit_encoded()`
- `uint64 read_uint64()`
- `uint8 read_uint8()`
- `void flush()`
- `void read_7bit_encoded(uint64&out integer)`
- `void write_7bit_encoded(uint64 integer)`

### Class `base32_encoder`
##### Behaviours / Constructors
- `base32_encoder@ base32_encoder()`
- `base32_encoder@ base32_encoder(datastream@ stream, bool padding = true, const string&in encoding = "", int byteorder = 1)`
##### Properties
- `bool autoflush`
- `bool binary`
- `bool skip_eof`
- `bool sync_rw_cursors`
##### Methods
- `base32_encoder& opShl(double value)`
- `base32_encoder& opShl(float value)`
- `base32_encoder& opShl(int value)`
- `base32_encoder& opShl(int16 value)`
- `base32_encoder& opShl(int64 value)`
- `base32_encoder& opShl(int8 value)`
- `base32_encoder& opShl(string value)`
- `base32_encoder& opShl(uint value)`
- `base32_encoder& opShl(uint16 value)`
- `base32_encoder& opShl(uint64 value)`
- `base32_encoder& opShl(uint8 value)`
- `base32_encoder& opShr(double&out value)`
- `base32_encoder& opShr(float&out value)`
- `base32_encoder& opShr(int&out value)`
- `base32_encoder& opShr(int16&out value)`
- `base32_encoder& opShr(int64&out value)`
- `base32_encoder& opShr(int8&out value)`
- `base32_encoder& opShr(string&out value)`
- `base32_encoder& opShr(uint&out value)`
- `base32_encoder& opShr(uint16&out value)`
- `base32_encoder& opShr(uint64&out value)`
- `base32_encoder& opShr(uint8&out value)`
- `base32_encoder& write_double(double value)`
- `base32_encoder& write_float(float value)`
- `base32_encoder& write_int(int value)`
- `base32_encoder& write_int16(int16 value)`
- `base32_encoder& write_int64(int64 value)`
- `base32_encoder& write_int8(int8 value)`
- `base32_encoder& write_string(string value)`
- `base32_encoder& write_uint(uint value)`
- `base32_encoder& write_uint16(uint16 value)`
- `base32_encoder& write_uint64(uint64 value)`
- `base32_encoder& write_uint8(uint8 value)`
- `bool close(bool close_all = false)`
- `bool close_all()`
- `bool get_active() const property`
- `bool get_bad() const property`
- `bool get_eof() const property`
- `bool get_fail() const property`
- `bool get_good() const property`
- `bool open(datastream@ stream, bool padding = true, const string&in encoding = "", int byteorder = 1)`
- `bool rseek(uint64 offset)`
- `bool rseek_end(uint64 offset = 0)`
- `bool rseek_relative(int64 offset)`
- `bool seek(uint64 offset)`
- `bool seek_end(uint64 offset = 0)`
- `bool seek_relative(int64 offset)`
- `bool wseek(uint64 offset)`
- `bool wseek_end(uint64 offset = 0)`
- `bool wseek_relative(int64 offset)`
- `datastream@ opImplCast()`
- `double read_double()`
- `float read_float()`
- `int read_int()`
- `int16 read_int16()`
- `int64 get_pos() const property`
- `int64 get_rpos() const property`
- `int64 get_wpos() const property`
- `int64 read_int64()`
- `int8 read_int8()`
- `string read(uint count = 0)`
- `string read_line()`
- `string read_string()`
- `string read_until(const string&in text, bool require_full)`
- `uint read_uint()`
- `uint write(const string&in data)`
- `uint16 read_uint16()`
- `uint64 get_available() const property`
- `uint64 read_7bit_encoded()`
- `uint64 read_uint64()`
- `uint8 read_uint8()`
- `void flush()`
- `void read_7bit_encoded(uint64&out integer)`
- `void write_7bit_encoded(uint64 integer)`

### Class `base64_decoder`
##### Behaviours / Constructors
- `base64_decoder@ base64_decoder()`
- `base64_decoder@ base64_decoder(datastream@ stream, int options = 0, const string&in encoding = "", int byteorder = 1)`
##### Properties
- `bool autoflush`
- `bool binary`
- `bool skip_eof`
- `bool sync_rw_cursors`
##### Methods
- `base64_decoder& opShl(double value)`
- `base64_decoder& opShl(float value)`
- `base64_decoder& opShl(int value)`
- `base64_decoder& opShl(int16 value)`
- `base64_decoder& opShl(int64 value)`
- `base64_decoder& opShl(int8 value)`
- `base64_decoder& opShl(string value)`
- `base64_decoder& opShl(uint value)`
- `base64_decoder& opShl(uint16 value)`
- `base64_decoder& opShl(uint64 value)`
- `base64_decoder& opShl(uint8 value)`
- `base64_decoder& opShr(double&out value)`
- `base64_decoder& opShr(float&out value)`
- `base64_decoder& opShr(int&out value)`
- `base64_decoder& opShr(int16&out value)`
- `base64_decoder& opShr(int64&out value)`
- `base64_decoder& opShr(int8&out value)`
- `base64_decoder& opShr(string&out value)`
- `base64_decoder& opShr(uint&out value)`
- `base64_decoder& opShr(uint16&out value)`
- `base64_decoder& opShr(uint64&out value)`
- `base64_decoder& opShr(uint8&out value)`
- `base64_decoder& write_double(double value)`
- `base64_decoder& write_float(float value)`
- `base64_decoder& write_int(int value)`
- `base64_decoder& write_int16(int16 value)`
- `base64_decoder& write_int64(int64 value)`
- `base64_decoder& write_int8(int8 value)`
- `base64_decoder& write_string(string value)`
- `base64_decoder& write_uint(uint value)`
- `base64_decoder& write_uint16(uint16 value)`
- `base64_decoder& write_uint64(uint64 value)`
- `base64_decoder& write_uint8(uint8 value)`
- `bool close(bool close_all = false)`
- `bool close_all()`
- `bool get_active() const property`
- `bool get_bad() const property`
- `bool get_eof() const property`
- `bool get_fail() const property`
- `bool get_good() const property`
- `bool open(datastream@ stream, int options = 0, const string&in encoding = "", int byteorder = 1)`
- `bool rseek(uint64 offset)`
- `bool rseek_end(uint64 offset = 0)`
- `bool rseek_relative(int64 offset)`
- `bool seek(uint64 offset)`
- `bool seek_end(uint64 offset = 0)`
- `bool seek_relative(int64 offset)`
- `bool wseek(uint64 offset)`
- `bool wseek_end(uint64 offset = 0)`
- `bool wseek_relative(int64 offset)`
- `datastream@ opImplCast()`
- `double read_double()`
- `float read_float()`
- `int read_int()`
- `int16 read_int16()`
- `int64 get_pos() const property`
- `int64 get_rpos() const property`
- `int64 get_wpos() const property`
- `int64 read_int64()`
- `int8 read_int8()`
- `string read(uint count = 0)`
- `string read_line()`
- `string read_string()`
- `string read_until(const string&in text, bool require_full)`
- `uint read_uint()`
- `uint write(const string&in data)`
- `uint16 read_uint16()`
- `uint64 get_available() const property`
- `uint64 read_7bit_encoded()`
- `uint64 read_uint64()`
- `uint8 read_uint8()`
- `void flush()`
- `void read_7bit_encoded(uint64&out integer)`
- `void write_7bit_encoded(uint64 integer)`

### Class `base64_encoder`
##### Behaviours / Constructors
- `base64_encoder@ base64_encoder()`
- `base64_encoder@ base64_encoder(datastream@ stream, int options = 0, const string&in encoding = "", int byteorder = 1)`
##### Properties
- `bool autoflush`
- `bool binary`
- `bool skip_eof`
- `bool sync_rw_cursors`
##### Methods
- `base64_encoder& opShl(double value)`
- `base64_encoder& opShl(float value)`
- `base64_encoder& opShl(int value)`
- `base64_encoder& opShl(int16 value)`
- `base64_encoder& opShl(int64 value)`
- `base64_encoder& opShl(int8 value)`
- `base64_encoder& opShl(string value)`
- `base64_encoder& opShl(uint value)`
- `base64_encoder& opShl(uint16 value)`
- `base64_encoder& opShl(uint64 value)`
- `base64_encoder& opShl(uint8 value)`
- `base64_encoder& opShr(double&out value)`
- `base64_encoder& opShr(float&out value)`
- `base64_encoder& opShr(int&out value)`
- `base64_encoder& opShr(int16&out value)`
- `base64_encoder& opShr(int64&out value)`
- `base64_encoder& opShr(int8&out value)`
- `base64_encoder& opShr(string&out value)`
- `base64_encoder& opShr(uint&out value)`
- `base64_encoder& opShr(uint16&out value)`
- `base64_encoder& opShr(uint64&out value)`
- `base64_encoder& opShr(uint8&out value)`
- `base64_encoder& write_double(double value)`
- `base64_encoder& write_float(float value)`
- `base64_encoder& write_int(int value)`
- `base64_encoder& write_int16(int16 value)`
- `base64_encoder& write_int64(int64 value)`
- `base64_encoder& write_int8(int8 value)`
- `base64_encoder& write_string(string value)`
- `base64_encoder& write_uint(uint value)`
- `base64_encoder& write_uint16(uint16 value)`
- `base64_encoder& write_uint64(uint64 value)`
- `base64_encoder& write_uint8(uint8 value)`
- `bool close(bool close_all = false)`
- `bool close_all()`
- `bool get_active() const property`
- `bool get_bad() const property`
- `bool get_eof() const property`
- `bool get_fail() const property`
- `bool get_good() const property`
- `bool open(datastream@ stream, int options = 0, const string&in encoding = "", int byteorder = 1)`
- `bool rseek(uint64 offset)`
- `bool rseek_end(uint64 offset = 0)`
- `bool rseek_relative(int64 offset)`
- `bool seek(uint64 offset)`
- `bool seek_end(uint64 offset = 0)`
- `bool seek_relative(int64 offset)`
- `bool wseek(uint64 offset)`
- `bool wseek_end(uint64 offset = 0)`
- `bool wseek_relative(int64 offset)`
- `datastream@ opImplCast()`
- `double read_double()`
- `float read_float()`
- `int read_int()`
- `int16 read_int16()`
- `int64 get_pos() const property`
- `int64 get_rpos() const property`
- `int64 get_wpos() const property`
- `int64 read_int64()`
- `int8 read_int8()`
- `string read(uint count = 0)`
- `string read_line()`
- `string read_string()`
- `string read_until(const string&in text, bool require_full)`
- `uint read_uint()`
- `uint write(const string&in data)`
- `uint16 read_uint16()`
- `uint64 get_available() const property`
- `uint64 read_7bit_encoded()`
- `uint64 read_uint64()`
- `uint8 read_uint8()`
- `void flush()`
- `void read_7bit_encoded(uint64&out integer)`
- `void write_7bit_encoded(uint64 integer)`

### Class `calendar`
##### Behaviours / Constructors
- `calendar@ calendar()`
- `calendar@ calendar(const calendar&in other)`
- `calendar@ calendar(const datetime&in value)`
- `calendar@ calendar(double julian_day)`
- `calendar@ calendar(int year, int month, int day, int hour = 0, int minute = 0, int second = 0, int millisecond = 0, int microsecond = 0)`
- `calendar@ f()`
- `calendar@ f(const calendar&in other)`
- `calendar@ f(const datetime&in value)`
- `calendar@ f(double julian_day)`
- `calendar@ f(int year, int month, int day, int hour = 0, int minute = 0, int second = 0, int millisecond = 0, int microsecond = 0)`
##### Methods
- `bool add_days(int amount)`
- `bool add_hours(int amount)`
- `bool add_minutes(int amount)`
- `bool add_months(int amount)`
- `bool add_seconds(int amount)`
- `bool add_years(int amount)`
- `bool get_AM() const property`
- `bool get_leap_year()`
- `bool get_PM() const property`
- `bool get_valid() const property`
- `bool opEquals(const calendar&in other) const`
- `calendar& opAddAssign(const timespan&in value)`
- `calendar& opAssign(const calendar&in other)`
- `calendar& opAssign(const timestamp&in value)`
- `calendar& opAssign(double julian_day)`
- `calendar& opSubAssign(const timespan&in value)`
- `calendar& set(int year, int month, int day, int hour = 0, int minute = 0, int second = 0, int millisecond = 0, int microsecond = 0)`
- `calendar@ opAdd(const timespan&in value) const`
- `calendar@ opSub(const timespan&in value) const`
- `datetime@ get_UTC() const property`
- `double diff_years(const calendar&in other)`
- `double get_julian_day() const property`
- `int get_day() const property`
- `int get_hour() const property`
- `int get_hour12() const property`
- `int get_microsecond() const property`
- `int get_millisecond() const property`
- `int get_minute() const property`
- `int get_month() const property`
- `int get_second() const property`
- `int get_tzd() const property`
- `int get_weekday() const property`
- `int get_year() const property`
- `int get_yearday() const property`
- `int opCmp(const calendar&in other) const`
- `int week(int first_day_of_week = 1) const`
- `int64 diff_days(const calendar&in other)`
- `int64 diff_hours(const calendar&in other)`
- `int64 diff_minutes(const calendar&in other)`
- `int64 diff_months(const calendar&in other)`
- `int64 diff_seconds(const calendar&in other)`
- `int64 get_UTC_time() const property`
- `string format(const string&in fmt)`
- `string get_month_name() const property`
- `string get_weekday_name() const property`
- `timespan opSub(const calendar&in other) const`
- `timestamp get_timestamp() const property`
- `void reset()`

### Class `combination`
##### Behaviours / Constructors
- `combination@ combination()`
- `combination@ f()`
##### Methods
- `bool generate_all_combinations(int items, int min_size, int max_size)`
- `bool generate_all_combinations(int items, int size)`
- `bool generate_permutations(int items)`
- `bool generate_unique_combinations(int items, int min_size, int max_size)`
- `bool generate_unique_combinations(int items, int size)`
- `bool get_active() property`
- `bool next(int[]@+ list)`
- `void reset()`

### Class `complex`
##### Behaviours / Constructors
- `void $list(const int&in) { float, float }`
- `void complex()`
- `void complex(const complex&in other)`
- `void complex(float real)`
- `void complex(float real, float imaginary)`
- `void f()`
- `void f(const complex &in other)`
- `void f(const int &in) {float, float}`
- `void f(float real)`
- `void f(float real, float imaginary)`
##### Properties
- `float i`
- `float r`
##### Methods
- `bool opEquals(const complex &in other) const`
- `bool opEquals(const complex&in other) const`
- `complex &opAddAssign(const complex &in other)`
- `complex &opDivAssign(const complex &in other)`
- `complex &opMulAssign(const complex &in other)`
- `complex &opSubAssign(const complex &in other)`
- `complex get_ir() const property`
- `complex get_ri() const property`
- `complex opAdd(const complex &in other) const`
- `complex opAdd(const complex&in other) const`
- `complex opDiv(const complex &in other) const`
- `complex opDiv(const complex&in other) const`
- `complex opMul(const complex &in other) const`
- `complex opMul(const complex&in other) const`
- `complex opSub(const complex &in other) const`
- `complex opSub(const complex&in other) const`
- `complex& opAddAssign(const complex&in other)`
- `complex& opDivAssign(const complex&in other)`
- `complex& opMulAssign(const complex&in other)`
- `complex& opSubAssign(const complex&in other)`
- `float abs() const`
- `void set_ir(const complex &in value) property`
- `void set_ir(const complex&in value) property`
- `void set_ri(const complex &in value) property`
- `void set_ri(const complex&in value) property`

### Class `const_weakref<class T>`

### Class `const_weakref<T>`
##### Behaviours / Constructors
- `bool f(int&in, bool&out)`
- `void const_weakref()`
- `void const_weakref(int&in)`
- `void const_weakref(int&in, const T@ object)`
- `void f(int&in)`
- `void f(int&in, const T@+ object) explicit`
##### Methods
- `bool opEquals(const const_weakref<T> &in other) const`
- `bool opEquals(const const_weakref<T>&in other) const`
- `bool opEquals(const T@+ object) const`
- `bool opEquals(const weakref<T> &in other) const`
- `bool opEquals(const weakref<T>&in other) const`
- `const T@ get() const`
- `const T@ opImplCast() const`
- `const_weakref<T> &opAssign(const const_weakref<T> &in other)`
- `const_weakref<T> &opHndlAssign(const const_weakref<T> &in other)`
- `const_weakref<T> &opHndlAssign(const T@ object)`
- `const_weakref<T> &opHndlAssign(const weakref<T> &in other)`
- `const_weakref<T>& opAssign(const const_weakref<T>&in other)`
- `const_weakref<T>& opHndlAssign(const const_weakref<T>&in other)`
- `const_weakref<T>& opHndlAssign(const T@ object)`
- `const_weakref<T>& opHndlAssign(const weakref<T>&in other)`

### Class `coordinate_map`
##### Behaviours / Constructors
- `coordinate_map @m()`
- `coordinate_map@ coordinate_map()`
##### Methods
- `array<coordinate_map_area@>@ get_areas(float minx, float maxx, float miny, float maxy, float minz, float maxz, float d = 0.0, coordinate_map_filter_callback@ filter_callback = null, int64 required_flags = 0, int64 excluded_flags = 0) const`
- `array<coordinate_map_area@>@ get_areas(float x, float y, float z, float d = 0.0, coordinate_map_filter_callback@ filter_callback = null, int64 required_flags = 0, int64 excluded_flags = 0) const`
- `coordinate_map_area@ add_area(float minx, float maxx, float miny, float maxy, float minz, float maxz, float rotation, any@ primary_data, const string&in data1, const string&in data2, const string&in data3, int priority, int64 flags = 0)`
- `coordinate_map_area@ get_area(float x, float y, float z, int priority = -1, float d = 0.0, coordinate_map_filter_callback@ filter_callback = null, int64 required_flags = 0, int64 excluded_flags = 0) const`
- `coordinate_map_area@[]@ get_areas(float minx, float maxx, float miny, float maxy, float minz, float maxz, float d = 0.0, coordinate_map_filter_callback@ filter_callback = null, int64 required_flags = 0, int64 excluded_flags = 0) const`
- `coordinate_map_area@[]@ get_areas(float x, float y, float z, float d = 0.0, coordinate_map_filter_callback@ filter_callback = null, int64 required_flags = 0, int64 excluded_flags = 0) const`
- `void reset()`

### Class `coordinate_map_area`
##### Properties
- `any@ primary_data`
- `const bool framed`
- `const coordinate_map@ map`
- `const float maxx`
- `const float maxy`
- `const float maxz`
- `const float minx`
- `const float miny`
- `const float minz`
- `const float rotation`
- `const int priority`
- `const string data1`
- `const string data2`
- `const string data3`
- `int64 flags`
##### Methods
- `bool is_in_area(float x, float y, float z, float d = 0.0, coordinate_map_filter_callback@+ filter_callback = null, int64 required_flags = 0, int64 excluded_flags = 0) const`
- `void reframe()`
- `void set(float minx, float maxx, float miny, float maxy, float minz, float maxz, float theta)`
- `void set_area(float minx, float maxx, float miny, float maxy, float minz, float maxz)`
- `void set_rotation(float theta)`
- `void unframe()`

### Class `counting_reader`
##### Behaviours / Constructors
- `counting_reader@ counting_reader()`
- `counting_reader@ counting_reader(datastream@ stream, const string&in encoding = "", int byteorder = 1)`
##### Properties
- `bool autoflush`
- `bool binary`
- `bool skip_eof`
- `bool sync_rw_cursors`
##### Methods
- `bool close(bool close_all = false)`
- `bool close_all()`
- `bool get_active() const property`
- `bool get_bad() const property`
- `bool get_eof() const property`
- `bool get_fail() const property`
- `bool get_good() const property`
- `bool open(datastream@ stream, const string&in encoding = "", int byteorder = 1)`
- `bool rseek(uint64 offset)`
- `bool rseek_end(uint64 offset = 0)`
- `bool rseek_relative(int64 offset)`
- `bool seek(uint64 offset)`
- `bool seek_end(uint64 offset = 0)`
- `bool seek_relative(int64 offset)`
- `bool wseek(uint64 offset)`
- `bool wseek_end(uint64 offset = 0)`
- `bool wseek_relative(int64 offset)`
- `counting_reader& opShl(double value)`
- `counting_reader& opShl(float value)`
- `counting_reader& opShl(int value)`
- `counting_reader& opShl(int16 value)`
- `counting_reader& opShl(int64 value)`
- `counting_reader& opShl(int8 value)`
- `counting_reader& opShl(string value)`
- `counting_reader& opShl(uint value)`
- `counting_reader& opShl(uint16 value)`
- `counting_reader& opShl(uint64 value)`
- `counting_reader& opShl(uint8 value)`
- `counting_reader& opShr(double&out value)`
- `counting_reader& opShr(float&out value)`
- `counting_reader& opShr(int&out value)`
- `counting_reader& opShr(int16&out value)`
- `counting_reader& opShr(int64&out value)`
- `counting_reader& opShr(int8&out value)`
- `counting_reader& opShr(string&out value)`
- `counting_reader& opShr(uint&out value)`
- `counting_reader& opShr(uint16&out value)`
- `counting_reader& opShr(uint64&out value)`
- `counting_reader& opShr(uint8&out value)`
- `counting_reader& write_double(double value)`
- `counting_reader& write_float(float value)`
- `counting_reader& write_int(int value)`
- `counting_reader& write_int16(int16 value)`
- `counting_reader& write_int64(int64 value)`
- `counting_reader& write_int8(int8 value)`
- `counting_reader& write_string(string value)`
- `counting_reader& write_uint(uint value)`
- `counting_reader& write_uint16(uint16 value)`
- `counting_reader& write_uint64(uint64 value)`
- `counting_reader& write_uint8(uint8 value)`
- `datastream@ opImplCast()`
- `double read_double()`
- `float read_float()`
- `int read_int()`
- `int16 read_int16()`
- `int64 get_chars() property`
- `int64 get_current_line() property`
- `int64 get_lines() property`
- `int64 get_pos() const property`
- `int64 get_rpos() const property`
- `int64 get_wpos() const property`
- `int64 read_int64()`
- `int8 read_int8()`
- `string read(uint count = 0)`
- `string read_line()`
- `string read_string()`
- `string read_until(const string&in text, bool require_full)`
- `uint read_uint()`
- `uint write(const string&in data)`
- `uint16 read_uint16()`
- `uint64 get_available() const property`
- `uint64 read_7bit_encoded()`
- `uint64 read_uint64()`
- `uint8 read_uint8()`
- `void add_chars(int64 count)`
- `void add_lines(int64 count)`
- `void add_pos(int64 count)`
- `void flush()`
- `void read_7bit_encoded(uint64&out integer)`
- `void reset()`
- `void set_current_line(int64 line)`
- `void write_7bit_encoded(uint64 integer)`

### Class `counting_writer`
##### Behaviours / Constructors
- `counting_writer@ counting_writer()`
- `counting_writer@ counting_writer(datastream@ stream, const string&in encoding = "", int byteorder = 1)`
##### Properties
- `bool autoflush`
- `bool binary`
- `bool skip_eof`
- `bool sync_rw_cursors`
##### Methods
- `bool close(bool close_all = false)`
- `bool close_all()`
- `bool get_active() const property`
- `bool get_bad() const property`
- `bool get_eof() const property`
- `bool get_fail() const property`
- `bool get_good() const property`
- `bool open(datastream@ stream, const string&in encoding = "", int byteorder = 1)`
- `bool rseek(uint64 offset)`
- `bool rseek_end(uint64 offset = 0)`
- `bool rseek_relative(int64 offset)`
- `bool seek(uint64 offset)`
- `bool seek_end(uint64 offset = 0)`
- `bool seek_relative(int64 offset)`
- `bool wseek(uint64 offset)`
- `bool wseek_end(uint64 offset = 0)`
- `bool wseek_relative(int64 offset)`
- `counting_writer& opShl(double value)`
- `counting_writer& opShl(float value)`
- `counting_writer& opShl(int value)`
- `counting_writer& opShl(int16 value)`
- `counting_writer& opShl(int64 value)`
- `counting_writer& opShl(int8 value)`
- `counting_writer& opShl(string value)`
- `counting_writer& opShl(uint value)`
- `counting_writer& opShl(uint16 value)`
- `counting_writer& opShl(uint64 value)`
- `counting_writer& opShl(uint8 value)`
- `counting_writer& opShr(double&out value)`
- `counting_writer& opShr(float&out value)`
- `counting_writer& opShr(int&out value)`
- `counting_writer& opShr(int16&out value)`
- `counting_writer& opShr(int64&out value)`
- `counting_writer& opShr(int8&out value)`
- `counting_writer& opShr(string&out value)`
- `counting_writer& opShr(uint&out value)`
- `counting_writer& opShr(uint16&out value)`
- `counting_writer& opShr(uint64&out value)`
- `counting_writer& opShr(uint8&out value)`
- `counting_writer& write_double(double value)`
- `counting_writer& write_float(float value)`
- `counting_writer& write_int(int value)`
- `counting_writer& write_int16(int16 value)`
- `counting_writer& write_int64(int64 value)`
- `counting_writer& write_int8(int8 value)`
- `counting_writer& write_string(string value)`
- `counting_writer& write_uint(uint value)`
- `counting_writer& write_uint16(uint16 value)`
- `counting_writer& write_uint64(uint64 value)`
- `counting_writer& write_uint8(uint8 value)`
- `datastream@ opImplCast()`
- `double read_double()`
- `float read_float()`
- `int read_int()`
- `int16 read_int16()`
- `int64 get_chars() property`
- `int64 get_current_line() property`
- `int64 get_lines() property`
- `int64 get_pos() const property`
- `int64 get_rpos() const property`
- `int64 get_wpos() const property`
- `int64 read_int64()`
- `int8 read_int8()`
- `string read(uint count = 0)`
- `string read_line()`
- `string read_string()`
- `string read_until(const string&in text, bool require_full)`
- `uint read_uint()`
- `uint write(const string&in data)`
- `uint16 read_uint16()`
- `uint64 get_available() const property`
- `uint64 read_7bit_encoded()`
- `uint64 read_uint64()`
- `uint8 read_uint8()`
- `void add_chars(int64 count)`
- `void add_lines(int64 count)`
- `void add_pos(int64 count)`
- `void flush()`
- `void read_7bit_encoded(uint64&out integer)`
- `void reset()`
- `void set_current_line(int64 line)`
- `void write_7bit_encoded(uint64 integer)`

### Class `datastream`
##### Behaviours / Constructors
- `datastream@ d(const string&in initial_data = "")`
- `datastream@ d(const string&in initial_data, const string&in encoding, int byteorder = STREAM_BYTE_ORDER_NATIVE)`
- `datastream@ datastream(const string&in initial_data = "")`
- `datastream@ datastream(const string&in initial_data, const string&in encoding, int byteorder = STREAM_BYTE_ORDER_NATIVE)`
##### Properties
- `bool autoflush`
- `bool binary`
- `bool skip_eof`
- `bool sync_rw_cursors`
##### Methods
- `asset_decryptor@ opCast()`
- `asset_encryptor@ opCast()`
- `base32_decoder@ opCast()`
- `base32_encoder@ opCast()`
- `base64_decoder@ opCast()`
- `base64_encoder@ opCast()`
- `bool close(bool close_all = false)`
- `bool close_all()`
- `bool get_active() const property`
- `bool get_bad() const property`
- `bool get_eof() const property`
- `bool get_fail() const property`
- `bool get_good() const property`
- `bool open(const string&in initial_data = "", const string&in encoding = "", int byteorder = STREAM_BYTE_ORDER_NATIVE)`
- `bool rseek(uint64 offset)`
- `bool rseek_end(uint64 offset = 0)`
- `bool rseek_relative(int64 offset)`
- `bool seek(uint64 offset)`
- `bool seek_end(uint64 offset = 0)`
- `bool seek_relative(int64 offset)`
- `bool wseek(uint64 offset)`
- `bool wseek_end(uint64 offset = 0)`
- `bool wseek_relative(int64 offset)`
- `counting_reader@ opCast()`
- `counting_writer@ opCast()`
- `datastream& opShl(double value)`
- `datastream& opShl(float value)`
- `datastream& opShl(int value)`
- `datastream& opShl(int16 value)`
- `datastream& opShl(int64 value)`
- `datastream& opShl(int8 value)`
- `datastream& opShl(string value)`
- `datastream& opShl(uint value)`
- `datastream& opShl(uint16 value)`
- `datastream& opShl(uint64 value)`
- `datastream& opShl(uint8 value)`
- `datastream& opShr(double&out value)`
- `datastream& opShr(float&out value)`
- `datastream& opShr(int&out value)`
- `datastream& opShr(int16&out value)`
- `datastream& opShr(int64&out value)`
- `datastream& opShr(int8&out value)`
- `datastream& opShr(string&out value)`
- `datastream& opShr(uint&out value)`
- `datastream& opShr(uint16&out value)`
- `datastream& opShr(uint64&out value)`
- `datastream& opShr(uint8&out value)`
- `datastream& write_double(double value)`
- `datastream& write_float(float value)`
- `datastream& write_int(int value)`
- `datastream& write_int16(int16 value)`
- `datastream& write_int64(int64 value)`
- `datastream& write_int8(int8 value)`
- `datastream& write_string(string value)`
- `datastream& write_uint(uint value)`
- `datastream& write_uint16(uint16 value)`
- `datastream& write_uint64(uint64 value)`
- `datastream& write_uint8(uint8 value)`
- `datastream@ opCast()`
- `deflating_reader@ opCast()`
- `deflating_writer@ opCast()`
- `discarding_writer@ opCast()`
- `double read_double()`
- `duplicating_reader@ opCast()`
- `duplicating_writer@ opCast()`
- `file@ opCast()`
- `float read_float()`
- `hex_decoder@ opCast()`
- `hex_encoder@ opCast()`
- `inflating_reader@ opCast()`
- `inflating_writer@ opCast()`
- `int read_int()`
- `int16 read_int16()`
- `int64 get_pos() const property`
- `int64 get_rpos() const property`
- `int64 get_wpos() const property`
- `int64 read_int64()`
- `int8 read_int8()`
- `line_converting_reader@ opCast()`
- `line_converting_writer@ opCast()`
- `memory_reader@ opCast()`
- `memory_writer@ opCast()`
- `random_reader@ opCast()`
- `string read(uint count = 0)`
- `string read_line()`
- `string read_string()`
- `string read_until(const string&in text, bool require_full)`
- `string str()`
- `uint read_uint()`
- `uint write(const string&in data)`
- `uint16 read_uint16()`
- `uint64 get_available() const property`
- `uint64 read_7bit_encoded()`
- `uint64 read_uint64()`
- `uint8 read_uint8()`
- `void flush()`
- `void read_7bit_encoded(uint64&out integer)`
- `void str(const string&in new_data)`
- `void write_7bit_encoded(uint64 integer)`

### Class `datetime`
##### Behaviours / Constructors
- `datetime@ datetime()`
- `datetime@ datetime(const datetime&in other)`
- `datetime@ datetime(const timestamp&in timestamp)`
- `datetime@ datetime(double julian_day)`
- `datetime@ datetime(int year, int month, int day, int hour = 0, int minute = 0, int second = 0, int millisecond = 0, int microsecond = 0)`
- `datetime@ f()`
- `datetime@ f(const datetime&in other)`
- `datetime@ f(const timestamp&in timestamp)`
- `datetime@ f(double julian_day)`
- `datetime@ f(int year, int month, int day, int hour = 0, int minute = 0, int second = 0, int millisecond = 0, int microsecond = 0)`
##### Methods
- `bool add_days(int amount)`
- `bool add_hours(int amount)`
- `bool add_minutes(int amount)`
- `bool add_months(int amount)`
- `bool add_seconds(int amount)`
- `bool add_years(int amount)`
- `bool get_AM() const property`
- `bool get_leap_year()`
- `bool get_PM() const property`
- `bool get_valid() const property`
- `bool opEquals(const datetime&in other) const`
- `datetime& opAddAssign(const timespan&in value)`
- `datetime& opAssign(const datetime&in other)`
- `datetime& opAssign(const timestamp&in value)`
- `datetime& opAssign(double julian_day)`
- `datetime& opSubAssign(const timespan&in value)`
- `datetime& set(int year, int month, int day, int hour = 0, int minute = 0, int second = 0, int millisecond = 0, int microsecond = 0)`
- `datetime@ opAdd(const timespan&in value) const`
- `datetime@ opSub(const timespan&in value) const`
- `double diff_years(const datetime&in other)`
- `double get_julian_day() const property`
- `int get_day() const property`
- `int get_hour() const property`
- `int get_hour12() const property`
- `int get_microsecond() const property`
- `int get_millisecond() const property`
- `int get_minute() const property`
- `int get_month() const property`
- `int get_second() const property`
- `int get_weekday() const property`
- `int get_year() const property`
- `int get_yearday() const property`
- `int opCmp(const datetime&in other) const`
- `int week(int first_day_of_week = 1) const`
- `int64 diff_days(const datetime&in other)`
- `int64 diff_hours(const datetime&in other)`
- `int64 diff_minutes(const datetime&in other)`
- `int64 diff_months(const datetime&in other)`
- `int64 diff_seconds(const datetime&in other)`
- `int64 get_UTC_time() const property`
- `string format(const string&in fmt, int tzd = 0xffff)`
- `string get_month_name() const property`
- `string get_weekday_name() const property`
- `timespan opSub(const datetime&in other) const`
- `timestamp get_timestamp() const property`
- `void make_local(int timezone_offset)`
- `void make_UTC(int timezone_offset)`
- `void reset()`

### Class `deflating_reader`
##### Behaviours / Constructors
- `deflating_reader@ deflating_reader()`
- `deflating_reader@ deflating_reader(datastream@ stream, compression_method compression = COMPRESSION_METHOD_ZLIB, int level = 9, const string&in encoding = "", int byteorder = 1)`
##### Properties
- `bool autoflush`
- `bool binary`
- `bool skip_eof`
- `bool sync_rw_cursors`
##### Methods
- `bool close(bool close_all = false)`
- `bool close_all()`
- `bool get_active() const property`
- `bool get_bad() const property`
- `bool get_eof() const property`
- `bool get_fail() const property`
- `bool get_good() const property`
- `bool open(datastream@ stream, compression_method compression = COMPRESSION_METHOD_ZLIB, int level = 9, const string&in encoding = "", int byteorder = 1)`
- `bool rseek(uint64 offset)`
- `bool rseek_end(uint64 offset = 0)`
- `bool rseek_relative(int64 offset)`
- `bool seek(uint64 offset)`
- `bool seek_end(uint64 offset = 0)`
- `bool seek_relative(int64 offset)`
- `bool wseek(uint64 offset)`
- `bool wseek_end(uint64 offset = 0)`
- `bool wseek_relative(int64 offset)`
- `datastream@ opImplCast()`
- `deflating_reader& opShl(double value)`
- `deflating_reader& opShl(float value)`
- `deflating_reader& opShl(int value)`
- `deflating_reader& opShl(int16 value)`
- `deflating_reader& opShl(int64 value)`
- `deflating_reader& opShl(int8 value)`
- `deflating_reader& opShl(string value)`
- `deflating_reader& opShl(uint value)`
- `deflating_reader& opShl(uint16 value)`
- `deflating_reader& opShl(uint64 value)`
- `deflating_reader& opShl(uint8 value)`
- `deflating_reader& opShr(double&out value)`
- `deflating_reader& opShr(float&out value)`
- `deflating_reader& opShr(int&out value)`
- `deflating_reader& opShr(int16&out value)`
- `deflating_reader& opShr(int64&out value)`
- `deflating_reader& opShr(int8&out value)`
- `deflating_reader& opShr(string&out value)`
- `deflating_reader& opShr(uint&out value)`
- `deflating_reader& opShr(uint16&out value)`
- `deflating_reader& opShr(uint64&out value)`
- `deflating_reader& opShr(uint8&out value)`
- `deflating_reader& write_double(double value)`
- `deflating_reader& write_float(float value)`
- `deflating_reader& write_int(int value)`
- `deflating_reader& write_int16(int16 value)`
- `deflating_reader& write_int64(int64 value)`
- `deflating_reader& write_int8(int8 value)`
- `deflating_reader& write_string(string value)`
- `deflating_reader& write_uint(uint value)`
- `deflating_reader& write_uint16(uint16 value)`
- `deflating_reader& write_uint64(uint64 value)`
- `deflating_reader& write_uint8(uint8 value)`
- `double read_double()`
- `float read_float()`
- `int read_int()`
- `int16 read_int16()`
- `int64 get_pos() const property`
- `int64 get_rpos() const property`
- `int64 get_wpos() const property`
- `int64 read_int64()`
- `int8 read_int8()`
- `string read(uint count = 0)`
- `string read_line()`
- `string read_string()`
- `string read_until(const string&in text, bool require_full)`
- `uint read_uint()`
- `uint write(const string&in data)`
- `uint16 read_uint16()`
- `uint64 get_available() const property`
- `uint64 read_7bit_encoded()`
- `uint64 read_uint64()`
- `uint8 read_uint8()`
- `void flush()`
- `void read_7bit_encoded(uint64&out integer)`
- `void write_7bit_encoded(uint64 integer)`

### Class `deflating_writer`
##### Behaviours / Constructors
- `deflating_writer@ deflating_writer()`
- `deflating_writer@ deflating_writer(datastream@ stream, compression_method compression = COMPRESSION_METHOD_ZLIB, int level = 9, const string&in encoding = "", int byteorder = 1)`
##### Properties
- `bool autoflush`
- `bool binary`
- `bool skip_eof`
- `bool sync_rw_cursors`
##### Methods
- `bool close(bool close_all = false)`
- `bool close_all()`
- `bool get_active() const property`
- `bool get_bad() const property`
- `bool get_eof() const property`
- `bool get_fail() const property`
- `bool get_good() const property`
- `bool open(datastream@ stream, compression_method compression = COMPRESSION_METHOD_ZLIB, int level = 9, const string&in encoding = "", int byteorder = 1)`
- `bool rseek(uint64 offset)`
- `bool rseek_end(uint64 offset = 0)`
- `bool rseek_relative(int64 offset)`
- `bool seek(uint64 offset)`
- `bool seek_end(uint64 offset = 0)`
- `bool seek_relative(int64 offset)`
- `bool wseek(uint64 offset)`
- `bool wseek_end(uint64 offset = 0)`
- `bool wseek_relative(int64 offset)`
- `datastream@ opImplCast()`
- `deflating_writer& opShl(double value)`
- `deflating_writer& opShl(float value)`
- `deflating_writer& opShl(int value)`
- `deflating_writer& opShl(int16 value)`
- `deflating_writer& opShl(int64 value)`
- `deflating_writer& opShl(int8 value)`
- `deflating_writer& opShl(string value)`
- `deflating_writer& opShl(uint value)`
- `deflating_writer& opShl(uint16 value)`
- `deflating_writer& opShl(uint64 value)`
- `deflating_writer& opShl(uint8 value)`
- `deflating_writer& opShr(double&out value)`
- `deflating_writer& opShr(float&out value)`
- `deflating_writer& opShr(int&out value)`
- `deflating_writer& opShr(int16&out value)`
- `deflating_writer& opShr(int64&out value)`
- `deflating_writer& opShr(int8&out value)`
- `deflating_writer& opShr(string&out value)`
- `deflating_writer& opShr(uint&out value)`
- `deflating_writer& opShr(uint16&out value)`
- `deflating_writer& opShr(uint64&out value)`
- `deflating_writer& opShr(uint8&out value)`
- `deflating_writer& write_double(double value)`
- `deflating_writer& write_float(float value)`
- `deflating_writer& write_int(int value)`
- `deflating_writer& write_int16(int16 value)`
- `deflating_writer& write_int64(int64 value)`
- `deflating_writer& write_int8(int8 value)`
- `deflating_writer& write_string(string value)`
- `deflating_writer& write_uint(uint value)`
- `deflating_writer& write_uint16(uint16 value)`
- `deflating_writer& write_uint64(uint64 value)`
- `deflating_writer& write_uint8(uint8 value)`
- `double read_double()`
- `float read_float()`
- `int read_int()`
- `int16 read_int16()`
- `int64 get_pos() const property`
- `int64 get_rpos() const property`
- `int64 get_wpos() const property`
- `int64 read_int64()`
- `int8 read_int8()`
- `string read(uint count = 0)`
- `string read_line()`
- `string read_string()`
- `string read_until(const string&in text, bool require_full)`
- `uint read_uint()`
- `uint write(const string&in data)`
- `uint16 read_uint16()`
- `uint64 get_available() const property`
- `uint64 read_7bit_encoded()`
- `uint64 read_uint64()`
- `uint8 read_uint8()`
- `void flush()`
- `void read_7bit_encoded(uint64&out integer)`
- `void write_7bit_encoded(uint64 integer)`

### Class `dictionary`
##### Behaviours / Constructors
- `bool f()`
- `dictionary @f(int &in) {repeat {string, ?}}`
- `dictionary@ $list(int&in) { repeat { string, ? } }`
- `dictionary@ dictionary()`
- `dictionary@ f()`
- `int f()`
- `void f()`
- `void f(int&in)`
##### Methods
- `array<string> @get_keys() const`
- `array<string>@ get_keys() const`
- `bool delete(const string &in key)`
- `bool delete(const string&in key)`
- `bool empty() const`
- `bool exists(const string &in key) const`
- `bool exists(const string&in key) const`
- `bool get(const string &in key, ?&out value) const`
- `bool get(const string &in key, double&out value) const`
- `bool get(const string &in key, int64&out value) const`
- `bool get(const string&in key, ?&out value) const`
- `bool get(const string&in key, double&out value) const`
- `bool get(const string&in key, int64&out value) const`
- `bool is_empty() const`
- `bool opForEnd(dictionaryIter @+ iter) const`
- `bool opForEnd(dictionaryIter@ iter) const`
- `const dictionaryValue &opForValue0(dictionaryIter @+ iter) const`
- `const dictionaryValue &opIndex(const string &in key) const`
- `const dictionaryValue& opForValue0(dictionaryIter@ iter) const`
- `const dictionaryValue& opIndex(const string&in key) const`
- `const string &opForValue1(dictionaryIter @+ iter) const`
- `const string& opForValue1(dictionaryIter@ iter) const`
- `dictionary &opAssign(const dictionary &in other)`
- `dictionary& opAssign(const dictionary&in other)`
- `dictionaryIter @+ opForNext(dictionaryIter @+ iter) const`
- `dictionaryIter @opForBegin() const`
- `dictionaryIter@ opForBegin() const`
- `dictionaryIter@ opForNext(dictionaryIter@ iter) const`
- `dictionaryValue &opIndex(const string &in key)`
- `dictionaryValue& opIndex(const string&in key)`
- `string serialize()`
- `uint get_size() const`
- `uint size() const`
- `void clear()`
- `void delete_all()`
- `void erase(const string &in key)`
- `void erase(const string&in key)`
- `void set(const string &in key, const ?&in value)`
- `void set(const string &in key, const double&in value)`
- `void set(const string &in key, const int64&in value)`
- `void set(const string&in key, const ?&in value)`
- `void set(const string&in key, const double&in value)`
- `void set(const string&in key, const int64&in value)`

### Class `dictionaryIter`

### Class `dictionaryValue`
##### Behaviours / Constructors
- `void dictionaryValue()`
- `void f()`
- `void f(int&in)`
##### Methods
- `dictionaryValue &opAssign(const ?&in value)`
- `dictionaryValue &opAssign(const dictionaryValue &in other)`
- `dictionaryValue &opAssign(double value)`
- `dictionaryValue &opAssign(int64 value)`
- `dictionaryValue &opHndlAssign(const ?&in value)`
- `dictionaryValue &opHndlAssign(const dictionaryValue &in other)`
- `dictionaryValue& opAssign(const ?&in value)`
- `dictionaryValue& opAssign(const dictionaryValue&in other)`
- `dictionaryValue& opAssign(double value)`
- `dictionaryValue& opAssign(int64 value)`
- `dictionaryValue& opHndlAssign(const ?&in value)`
- `dictionaryValue& opHndlAssign(const dictionaryValue&in other)`
- `double opConv()`
- `int64 opConv()`
- `void opCast(?&out value)`
- `void opConv(?&out value)`

### Class `discarding_writer`
##### Behaviours / Constructors
- `discarding_writer@ discarding_writer(const string&in encoding = "", int byteorder = 1)`
##### Properties
- `bool autoflush`
- `bool binary`
- `bool skip_eof`
- `bool sync_rw_cursors`
##### Methods
- `bool close(bool close_all = false)`
- `bool close_all()`
- `bool get_active() const property`
- `bool get_bad() const property`
- `bool get_eof() const property`
- `bool get_fail() const property`
- `bool get_good() const property`
- `bool open(const string&in encoding = "", int byteorder = 1)`
- `bool rseek(uint64 offset)`
- `bool rseek_end(uint64 offset = 0)`
- `bool rseek_relative(int64 offset)`
- `bool seek(uint64 offset)`
- `bool seek_end(uint64 offset = 0)`
- `bool seek_relative(int64 offset)`
- `bool wseek(uint64 offset)`
- `bool wseek_end(uint64 offset = 0)`
- `bool wseek_relative(int64 offset)`
- `datastream@ opImplCast()`
- `discarding_writer& opShl(double value)`
- `discarding_writer& opShl(float value)`
- `discarding_writer& opShl(int value)`
- `discarding_writer& opShl(int16 value)`
- `discarding_writer& opShl(int64 value)`
- `discarding_writer& opShl(int8 value)`
- `discarding_writer& opShl(string value)`
- `discarding_writer& opShl(uint value)`
- `discarding_writer& opShl(uint16 value)`
- `discarding_writer& opShl(uint64 value)`
- `discarding_writer& opShl(uint8 value)`
- `discarding_writer& opShr(double&out value)`
- `discarding_writer& opShr(float&out value)`
- `discarding_writer& opShr(int&out value)`
- `discarding_writer& opShr(int16&out value)`
- `discarding_writer& opShr(int64&out value)`
- `discarding_writer& opShr(int8&out value)`
- `discarding_writer& opShr(string&out value)`
- `discarding_writer& opShr(uint&out value)`
- `discarding_writer& opShr(uint16&out value)`
- `discarding_writer& opShr(uint64&out value)`
- `discarding_writer& opShr(uint8&out value)`
- `discarding_writer& write_double(double value)`
- `discarding_writer& write_float(float value)`
- `discarding_writer& write_int(int value)`
- `discarding_writer& write_int16(int16 value)`
- `discarding_writer& write_int64(int64 value)`
- `discarding_writer& write_int8(int8 value)`
- `discarding_writer& write_string(string value)`
- `discarding_writer& write_uint(uint value)`
- `discarding_writer& write_uint16(uint16 value)`
- `discarding_writer& write_uint64(uint64 value)`
- `discarding_writer& write_uint8(uint8 value)`
- `double read_double()`
- `float read_float()`
- `int read_int()`
- `int16 read_int16()`
- `int64 get_pos() const property`
- `int64 get_rpos() const property`
- `int64 get_wpos() const property`
- `int64 read_int64()`
- `int8 read_int8()`
- `string read(uint count = 0)`
- `string read_line()`
- `string read_string()`
- `string read_until(const string&in text, bool require_full)`
- `uint read_uint()`
- `uint write(const string&in data)`
- `uint16 read_uint16()`
- `uint64 get_available() const property`
- `uint64 read_7bit_encoded()`
- `uint64 read_uint64()`
- `uint8 read_uint8()`
- `void flush()`
- `void read_7bit_encoded(uint64&out integer)`
- `void write_7bit_encoded(uint64 integer)`

### Class `dns_host_entry`
##### Behaviours / Constructors
- `void dns_host_entry()`
- `void dns_host_entry(const dns_host_entry&in other)`
- `void f()`
- `void f(const dns_host_entry&in other)`
##### Methods
- `array<spec::ip_address>@ get_addresses() const`
- `const string& get_name() const property`
- `dns_host_entry& opAssign(const dns_host_entry&in e)`
- `spec::ip_address[]@ get_addresses() const`
- `string[]@ get_aliases() const`

### Class `duplicating_reader`
##### Behaviours / Constructors
- `duplicating_reader@ duplicating_reader()`
- `duplicating_reader@ duplicating_reader(datastream@ stream, const string&in encoding = "", int byteorder = 1)`
##### Properties
- `bool autoflush`
- `bool binary`
- `bool skip_eof`
- `bool sync_rw_cursors`
##### Methods
- `bool close(bool close_all = false)`
- `bool close_all()`
- `bool get_active() const property`
- `bool get_bad() const property`
- `bool get_eof() const property`
- `bool get_fail() const property`
- `bool get_good() const property`
- `bool open(datastream@ stream, const string&in encoding = "", int byteorder = 1)`
- `bool rseek(uint64 offset)`
- `bool rseek_end(uint64 offset = 0)`
- `bool rseek_relative(int64 offset)`
- `bool seek(uint64 offset)`
- `bool seek_end(uint64 offset = 0)`
- `bool seek_relative(int64 offset)`
- `bool wseek(uint64 offset)`
- `bool wseek_end(uint64 offset = 0)`
- `bool wseek_relative(int64 offset)`
- `datastream@ opImplCast()`
- `double read_double()`
- `duplicating_reader& opShl(double value)`
- `duplicating_reader& opShl(float value)`
- `duplicating_reader& opShl(int value)`
- `duplicating_reader& opShl(int16 value)`
- `duplicating_reader& opShl(int64 value)`
- `duplicating_reader& opShl(int8 value)`
- `duplicating_reader& opShl(string value)`
- `duplicating_reader& opShl(uint value)`
- `duplicating_reader& opShl(uint16 value)`
- `duplicating_reader& opShl(uint64 value)`
- `duplicating_reader& opShl(uint8 value)`
- `duplicating_reader& opShr(double&out value)`
- `duplicating_reader& opShr(float&out value)`
- `duplicating_reader& opShr(int&out value)`
- `duplicating_reader& opShr(int16&out value)`
- `duplicating_reader& opShr(int64&out value)`
- `duplicating_reader& opShr(int8&out value)`
- `duplicating_reader& opShr(string&out value)`
- `duplicating_reader& opShr(uint&out value)`
- `duplicating_reader& opShr(uint16&out value)`
- `duplicating_reader& opShr(uint64&out value)`
- `duplicating_reader& opShr(uint8&out value)`
- `duplicating_reader& write_double(double value)`
- `duplicating_reader& write_float(float value)`
- `duplicating_reader& write_int(int value)`
- `duplicating_reader& write_int16(int16 value)`
- `duplicating_reader& write_int64(int64 value)`
- `duplicating_reader& write_int8(int8 value)`
- `duplicating_reader& write_string(string value)`
- `duplicating_reader& write_uint(uint value)`
- `duplicating_reader& write_uint16(uint16 value)`
- `duplicating_reader& write_uint64(uint64 value)`
- `duplicating_reader& write_uint8(uint8 value)`
- `duplicating_reader@ add(datastream@ stream)`
- `duplicating_reader@ opAdd(datastream@ stream)`
- `duplicating_reader@ opAddAssign(datastream@ stream)`
- `float read_float()`
- `int read_int()`
- `int16 read_int16()`
- `int64 get_pos() const property`
- `int64 get_rpos() const property`
- `int64 get_wpos() const property`
- `int64 read_int64()`
- `int8 read_int8()`
- `string read(uint count = 0)`
- `string read_line()`
- `string read_string()`
- `string read_until(const string&in text, bool require_full)`
- `uint read_uint()`
- `uint write(const string&in data)`
- `uint16 read_uint16()`
- `uint64 get_available() const property`
- `uint64 read_7bit_encoded()`
- `uint64 read_uint64()`
- `uint8 read_uint8()`
- `void flush()`
- `void read_7bit_encoded(uint64&out integer)`
- `void write_7bit_encoded(uint64 integer)`

### Class `duplicating_writer`
##### Behaviours / Constructors
- `duplicating_writer@ duplicating_writer(const string&in encoding = "", int byteorder = 1)`
- `duplicating_writer@ duplicating_writer(datastream@ stream, const string&in encoding = "", int byteorder = 1)`
##### Properties
- `bool autoflush`
- `bool binary`
- `bool skip_eof`
- `bool sync_rw_cursors`
##### Methods
- `bool close(bool close_all = false)`
- `bool close_all()`
- `bool get_active() const property`
- `bool get_bad() const property`
- `bool get_eof() const property`
- `bool get_fail() const property`
- `bool get_good() const property`
- `bool open(const string&in encoding = "", int byteorder = 1)`
- `bool open(datastream@ stream, const string&in encoding = "", int byteorder = 1)`
- `bool rseek(uint64 offset)`
- `bool rseek_end(uint64 offset = 0)`
- `bool rseek_relative(int64 offset)`
- `bool seek(uint64 offset)`
- `bool seek_end(uint64 offset = 0)`
- `bool seek_relative(int64 offset)`
- `bool wseek(uint64 offset)`
- `bool wseek_end(uint64 offset = 0)`
- `bool wseek_relative(int64 offset)`
- `datastream@ opImplCast()`
- `double read_double()`
- `duplicating_writer& opShl(double value)`
- `duplicating_writer& opShl(float value)`
- `duplicating_writer& opShl(int value)`
- `duplicating_writer& opShl(int16 value)`
- `duplicating_writer& opShl(int64 value)`
- `duplicating_writer& opShl(int8 value)`
- `duplicating_writer& opShl(string value)`
- `duplicating_writer& opShl(uint value)`
- `duplicating_writer& opShl(uint16 value)`
- `duplicating_writer& opShl(uint64 value)`
- `duplicating_writer& opShl(uint8 value)`
- `duplicating_writer& opShr(double&out value)`
- `duplicating_writer& opShr(float&out value)`
- `duplicating_writer& opShr(int&out value)`
- `duplicating_writer& opShr(int16&out value)`
- `duplicating_writer& opShr(int64&out value)`
- `duplicating_writer& opShr(int8&out value)`
- `duplicating_writer& opShr(string&out value)`
- `duplicating_writer& opShr(uint&out value)`
- `duplicating_writer& opShr(uint16&out value)`
- `duplicating_writer& opShr(uint64&out value)`
- `duplicating_writer& opShr(uint8&out value)`
- `duplicating_writer& write_double(double value)`
- `duplicating_writer& write_float(float value)`
- `duplicating_writer& write_int(int value)`
- `duplicating_writer& write_int16(int16 value)`
- `duplicating_writer& write_int64(int64 value)`
- `duplicating_writer& write_int8(int8 value)`
- `duplicating_writer& write_string(string value)`
- `duplicating_writer& write_uint(uint value)`
- `duplicating_writer& write_uint16(uint16 value)`
- `duplicating_writer& write_uint64(uint64 value)`
- `duplicating_writer& write_uint8(uint8 value)`
- `duplicating_writer@ add(datastream@ stream)`
- `duplicating_writer@ opAdd(datastream@ stream)`
- `duplicating_writer@ opAddAssign(datastream@ stream)`
- `float read_float()`
- `int read_int()`
- `int16 read_int16()`
- `int64 get_pos() const property`
- `int64 get_rpos() const property`
- `int64 get_wpos() const property`
- `int64 read_int64()`
- `int8 read_int8()`
- `string read(uint count = 0)`
- `string read_line()`
- `string read_string()`
- `string read_until(const string&in text, bool require_full)`
- `uint read_uint()`
- `uint write(const string&in data)`
- `uint16 read_uint16()`
- `uint64 get_available() const property`
- `uint64 read_7bit_encoded()`
- `uint64 read_uint64()`
- `uint8 read_uint8()`
- `void flush()`
- `void read_7bit_encoded(uint64&out integer)`
- `void write_7bit_encoded(uint64 integer)`

### Class `engine_character_event`
##### Methods
- `bool insert(engine_character_event_callback@ listener, int index = -1)`
- `bool insert(engine_character_event_listener@ listener, int index = -1)`
- `bool insert(engine_character_event_passthrough_callback@ listener, int index = -1)`
- `bool opAddAssign(engine_character_event_callback@ listener)`
- `bool opAddAssign(engine_character_event_listener@ listener)`
- `bool opAddAssign(engine_character_event_passthrough_callback@ listener)`
- `bool opSubAssign(engine_character_event_callback@ listener)`
- `bool opSubAssign(engine_character_event_listener@ listener)`
- `bool opSubAssign(engine_character_event_passthrough_callback@ listener)`
- `bool remove(engine_character_event_callback@ listener)`
- `bool remove(engine_character_event_listener@ listener)`
- `bool remove(engine_character_event_passthrough_callback@ listener)`
- `bool remove(uint index)`
- `int find(engine_character_event_callback@ listener) const`
- `int find(engine_character_event_listener@ listener) const`
- `int find(engine_character_event_passthrough_callback@ listener) const`
- `uint get_count() const property`
- `void clear()`
- `void opCall(string character)`

### Class `engine_key_event`
##### Methods
- `bool insert(engine_key_event_callback@ listener, int index = -1)`
- `bool insert(engine_key_event_listener@ listener, int index = -1)`
- `bool insert(engine_key_event_passthrough_callback@ listener, int index = -1)`
- `bool opAddAssign(engine_key_event_callback@ listener)`
- `bool opAddAssign(engine_key_event_listener@ listener)`
- `bool opAddAssign(engine_key_event_passthrough_callback@ listener)`
- `bool opSubAssign(engine_key_event_callback@ listener)`
- `bool opSubAssign(engine_key_event_listener@ listener)`
- `bool opSubAssign(engine_key_event_passthrough_callback@ listener)`
- `bool remove(engine_key_event_callback@ listener)`
- `bool remove(engine_key_event_listener@ listener)`
- `bool remove(engine_key_event_passthrough_callback@ listener)`
- `bool remove(uint index)`
- `int find(engine_key_event_callback@ listener) const`
- `int find(engine_key_event_listener@ listener) const`
- `int find(engine_key_event_passthrough_callback@ listener) const`
- `uint get_count() const property`
- `void clear()`
- `void opCall(int key)`

### Class `engine_touch_event`
##### Methods
- `bool insert(engine_touch_event_callback@ listener, int index = -1)`
- `bool insert(engine_touch_event_listener@ listener, int index = -1)`
- `bool insert(engine_touch_event_passthrough_callback@ listener, int index = -1)`
- `bool opAddAssign(engine_touch_event_callback@ listener)`
- `bool opAddAssign(engine_touch_event_listener@ listener)`
- `bool opAddAssign(engine_touch_event_passthrough_callback@ listener)`
- `bool opSubAssign(engine_touch_event_callback@ listener)`
- `bool opSubAssign(engine_touch_event_listener@ listener)`
- `bool opSubAssign(engine_touch_event_passthrough_callback@ listener)`
- `bool remove(engine_touch_event_callback@ listener)`
- `bool remove(engine_touch_event_listener@ listener)`
- `bool remove(engine_touch_event_passthrough_callback@ listener)`
- `bool remove(uint index)`
- `int find(engine_touch_event_callback@ listener) const`
- `int find(engine_touch_event_listener@ listener) const`
- `int find(engine_touch_event_passthrough_callback@ listener) const`
- `uint get_count() const property`
- `void clear()`
- `void opCall(uint64 device, const touch_finger&inout finger)`

### Class `engine_touch_motion_event`
##### Methods
- `bool insert(engine_touch_motion_event_callback@ listener, int index = -1)`
- `bool insert(engine_touch_motion_event_listener@ listener, int index = -1)`
- `bool insert(engine_touch_motion_event_passthrough_callback@ listener, int index = -1)`
- `bool opAddAssign(engine_touch_motion_event_callback@ listener)`
- `bool opAddAssign(engine_touch_motion_event_listener@ listener)`
- `bool opAddAssign(engine_touch_motion_event_passthrough_callback@ listener)`
- `bool opSubAssign(engine_touch_motion_event_callback@ listener)`
- `bool opSubAssign(engine_touch_motion_event_listener@ listener)`
- `bool opSubAssign(engine_touch_motion_event_passthrough_callback@ listener)`
- `bool remove(engine_touch_motion_event_callback@ listener)`
- `bool remove(engine_touch_motion_event_listener@ listener)`
- `bool remove(engine_touch_motion_event_passthrough_callback@ listener)`
- `bool remove(uint index)`
- `int find(engine_touch_motion_event_callback@ listener) const`
- `int find(engine_touch_motion_event_listener@ listener) const`
- `int find(engine_touch_motion_event_passthrough_callback@ listener) const`
- `uint get_count() const property`
- `void clear()`
- `void opCall(uint64 device, const touch_finger&inout finger, float relative_x, float relative_y)`

### Class `fast_mutex`
##### Behaviours / Constructors
- `fast_mutex@ fast_mutex()`
##### Methods
- `bool try_lock()`
- `bool try_lock(uint milliseconds)`
- `void lock()`
- `void lock(uint milliseconds)`
- `void unlock()`

### Class `fast_mutex_lock`
##### Behaviours / Constructors
- `void fast_mutex_lock()`
- `void fast_mutex_lock(fast_mutex@ target)`
- `void fast_mutex_lock(fast_mutex@ target, uint milliseconds)`
##### Methods
- `void unlock()`

### Class `file`
##### Behaviours / Constructors
- `file@ d(const string&in path, const string&in mode, const string&in encoding = "", int byteorder = 1)`
- `file@ file()`
- `file@ file(const string&in path, const string&in mode, const string&in encoding = "", int byteorder = 1)`
##### Properties
- `bool autoflush`
- `bool binary`
- `bool skip_eof`
- `bool sync_rw_cursors`
##### Methods
- `bool close(bool close_all = false)`
- `bool close_all()`
- `bool get_active() const property`
- `bool get_bad() const property`
- `bool get_eof() const property`
- `bool get_fail() const property`
- `bool get_good() const property`
- `bool open(const string&in path, const string&in mode, const string&in encoding = "", int byteorder = 1)`
- `bool rseek(uint64 offset)`
- `bool rseek_end(uint64 offset = 0)`
- `bool rseek_relative(int64 offset)`
- `bool seek(uint64 offset)`
- `bool seek_end(uint64 offset = 0)`
- `bool seek_relative(int64 offset)`
- `bool wseek(uint64 offset)`
- `bool wseek_end(uint64 offset = 0)`
- `bool wseek_relative(int64 offset)`
- `datastream@ opImplCast()`
- `double read_double()`
- `file& opShl(double value)`
- `file& opShl(float value)`
- `file& opShl(int value)`
- `file& opShl(int16 value)`
- `file& opShl(int64 value)`
- `file& opShl(int8 value)`
- `file& opShl(string value)`
- `file& opShl(uint value)`
- `file& opShl(uint16 value)`
- `file& opShl(uint64 value)`
- `file& opShl(uint8 value)`
- `file& opShr(double&out value)`
- `file& opShr(float&out value)`
- `file& opShr(int&out value)`
- `file& opShr(int16&out value)`
- `file& opShr(int64&out value)`
- `file& opShr(int8&out value)`
- `file& opShr(string&out value)`
- `file& opShr(uint&out value)`
- `file& opShr(uint16&out value)`
- `file& opShr(uint64&out value)`
- `file& opShr(uint8&out value)`
- `file& write_double(double value)`
- `file& write_float(float value)`
- `file& write_int(int value)`
- `file& write_int16(int16 value)`
- `file& write_int64(int64 value)`
- `file& write_int8(int8 value)`
- `file& write_string(string value)`
- `file& write_uint(uint value)`
- `file& write_uint16(uint16 value)`
- `file& write_uint64(uint64 value)`
- `file& write_uint8(uint8 value)`
- `float read_float()`
- `int read_int()`
- `int16 read_int16()`
- `int64 get_pos() const property`
- `int64 get_rpos() const property`
- `int64 get_wpos() const property`
- `int64 read_int64()`
- `int8 read_int8()`
- `string read(uint count = 0)`
- `string read_line()`
- `string read_string()`
- `string read_until(const string&in text, bool require_full)`
- `uint read_uint()`
- `uint write(const string&in data)`
- `uint16 read_uint16()`
- `uint64 get_available() const property`
- `uint64 get_size() const property`
- `uint64 read_7bit_encoded()`
- `uint64 read_uint64()`
- `uint8 read_uint8()`
- `void flush()`
- `void read_7bit_encoded(uint64&out integer)`
- `void write_7bit_encoded(uint64 integer)`

### Class `ftp_client`
##### Behaviours / Constructors
- `ftp_client@ ftp_client(const string&in host, uint16 port = 21, const string&in username = "", const string&in password = "", uint16 active_data_port = 0)`
- `ftp_client@ ftp_client(uint16 active_data_port = 0)`
##### Methods
- `bool get_is_logged_in() const property`
- `bool get_is_open() const property`
- `bool get_is_secure() const property`
- `bool get_passive() const property`
- `const string& get_welcome_message() const property`
- `datastream@ begin_download(const string&in path, const string&in encoding = "", int byteorder = STREAM_BYTE_ORDER_NATIVE)`
- `datastream@ begin_list(const string&in path = "", bool extended = false, const string&in encoding = "", int byteorder = STREAM_BYTE_ORDER_NATIVE)`
- `datastream@ begin_upload(const string&in path, const string&in encoding = "", int byteorder = STREAM_BYTE_ORDER_NATIVE)`
- `ftp_file_type get_file_type() const property`
- `int send_command(const string&in command, const string&in argument, string&inout response)`
- `int send_command(const string&in command, string&inout response)`
- `string get_working_directory()`
- `string system_type()`
- `void abort()`
- `void cdup()`
- `void close()`
- `void create_directory(const string&in path)`
- `void end_download()`
- `void end_list()`
- `void end_upload()`
- `void login(const string&in username, const string&in password)`
- `void logout()`
- `void open(const string&in host, uint16 port, const string&in username = "", const string&in password = "")`
- `void remove(const string&in path)`
- `void remove_directory(const string&in path)`
- `void rename(const string&in source, const string&in destination)`
- `void set_file_type(ftp_file_type type)`
- `void set_passive(bool passive, bool use_rfc1738 = true)`
- `void set_working_directory(const string&in path)`

### Class `game_window`
##### Behaviours / Constructors
- `game_window@ f(const string&in title, uint w, uint h, uint flags = 0)`
- `game_window@ game_window(const string&in title, uint w, uint h, uint flags = 0)`
##### Methods
- `bool clear(uint r, uint g, uint b)`
- `bool destroy_surface()`
- `bool flash(uint operation)`
- `bool get_aspect_ratio(float&out min_aspect, float&out max_aspect) const`
- `bool get_borders_size(int&out top, int&out left, int&out bottom, int&out right) const`
- `bool get_has_surface() const property`
- `bool get_keyboard_grab() const property`
- `bool get_maximum_size(int&out w, int&out h) const`
- `bool get_minimum_size(int&out w, int&out h) const`
- `bool get_mouse_grab() const property`
- `bool get_position(int&out x, int&out y) const`
- `bool get_size(int&out w, int&out h) const`
- `bool get_size_in_pixels(int&out w, int&out h) const`
- `bool get_surface_vsync(int&out vsync) const`
- `bool hide()`
- `bool maximize()`
- `bool minimize()`
- `bool present()`
- `bool raise()`
- `bool render_graphic(graphic@+ gfx, float x, float y)`
- `bool restore()`
- `bool set_always_on_top(bool on_top)`
- `bool set_aspect_ratio(float min_aspect, float max_aspect)`
- `bool set_bordered(bool bordered)`
- `bool set_fill_document(bool fill)`
- `bool set_focusable(bool focusable)`
- `bool set_fullscreen(bool fullscreen)`
- `bool set_icon(graphic@+ icon)`
- `bool set_keyboard_grab(bool grabbed)`
- `bool set_maximum_size(int w, int h)`
- `bool set_minimum_size(int w, int h)`
- `bool set_modal(bool modal)`
- `bool set_mouse_grab(bool grabbed)`
- `bool set_opacity(float opacity)`
- `bool set_position(int x, int y)`
- `bool set_progress_state(uint state)`
- `bool set_progress_value(float value)`
- `bool set_resizable(bool resizable)`
- `bool set_size(int w, int h)`
- `bool set_surface_vsync(int vsync)`
- `bool set_title(const string&in title)`
- `bool show()`
- `bool show_system_menu(int x, int y)`
- `bool sync()`
- `bool update_surface()`
- `float get_display_scale() const property`
- `float get_opacity() const property`
- `float get_pixel_density() const property`
- `float get_progress_value() const property`
- `graphics_renderer@+ get_renderer() property`
- `string get_title() const property`
- `text_font@+ get_font() property`
- `uint get_id() const property`
- `uint get_pixel_format() const property`
- `uint get_progress_state() const property`
- `uint64 get_flags() const property`
- `uint64 get_native_window() const property`
- `uint64 measure_text(const string&in text) const`
- `uint64 measure_text_wrapped(const string&in text, int wrap_width) const`
- `void draw_circle(float cx, float cy, int radius, uint r, uint g, uint b, bool filled = false)`
- `void draw_line(float x1, float y1, float x2, float y2, uint r, uint g, uint b)`
- `void draw_menu(string[]@+ items, float x, float y)`
- `void draw_rect(float x, float y, float w, float h, uint r, uint g, uint b, bool filled = false)`
- `void draw_text(const string&in text, float x, float y, uint r, uint g, uint b)`
- `void draw_text_wrapped(const string&in text, float x, float y, int wrap_width, uint r, uint g, uint b)`
- `void set_font(text_font@+ font) property`

### Class `graphic`
##### Methods
- `blend_mode get_blend_mode() const`
- `bool flip(flip_mode mode)`
- `bool get_color_mod(uint&out r, uint&out g, uint&out b) const`
- `bool get_is_valid() const property`
- `bool lock()`
- `bool save_bmp(const string&in file) const`
- `bool save_png(const string&in file) const`
- `bool set_alpha_mod(uint alpha)`
- `bool set_blend_mode(blend_mode mode)`
- `bool set_color_mod(uint r, uint g, uint b)`
- `bool set_rle(bool enabled)`
- `graphic@ convert(pixel_format pixel_format) const`
- `graphic@ duplicate() const`
- `int get_height() const property`
- `int get_pitch() const property`
- `int get_width() const property`
- `uint get_alpha_mod() const`
- `void unlock()`

### Class `graphics_renderer`
##### Behaviours / Constructors
- `graphics_renderer@ f()`
- `graphics_renderer@ graphics_renderer()`
##### Methods
- `blend_mode get_draw_blend_mode() const property`
- `bool clear()`
- `bool draw_line(float x1, float y1, float x2, float y2)`
- `bool draw_point(float x, float y)`
- `bool draw_rect(float x, float y, float w, float h)`
- `bool fill_rect(float x, float y, float w, float h)`
- `bool flush()`
- `bool get_clip_enabled() const property`
- `bool get_clip_rect(int&out x, int&out y, int&out w, int&out h) const`
- `bool get_current_output_size(int&out w, int&out h) const`
- `bool get_draw_color(uint&out r, uint&out g, uint&out b, uint&out a) const`
- `bool get_is_valid() const property`
- `bool get_logical_presentation(int&out w, int&out h, renderer_logical_presentation&out mode) const`
- `bool get_output_size(int&out w, int&out h) const`
- `bool get_scale(float&out sx, float&out sy) const`
- `bool get_viewport(int&out x, int&out y, int&out w, int&out h) const`
- `bool get_viewport_set() const property`
- `bool get_vsync(int&out vsync) const`
- `bool present()`
- `bool render_graphic(graphic@+ gfx, float dst_x, float dst_y)`
- `bool render_graphic(graphic@+ gfx, float src_x, float src_y, float src_w, float src_h, float dst_x, float dst_y, float dst_w, float dst_h)`
- `bool render_texture(graphics_texture@+ tex, float dst_x, float dst_y)`
- `bool render_texture(graphics_texture@+ tex, float src_x, float src_y, float src_w, float src_h, float dst_x, float dst_y, float dst_w, float dst_h)`
- `bool set_clip_rect(int x, int y, int w, int h)`
- `bool set_color_scale(float scale)`
- `bool set_draw_blend_mode(blend_mode mode)`
- `bool set_draw_color(uint r, uint g, uint b, uint a)`
- `bool set_logical_presentation(int w, int h, renderer_logical_presentation mode)`
- `bool set_scale(float sx, float sy)`
- `bool set_viewport(int x, int y, int w, int h)`
- `bool set_vsync(int vsync)`
- `float get_color_scale() const property`
- `graphics_texture@ create_texture(graphic@+ gfx)`
- `string get_name() const property`

### Class `graphics_texture`
##### Methods
- `blend_mode get_blend_mode() const`
- `bool get_color_mod(uint&out r, uint&out g, uint&out b) const`
- `bool get_is_valid() const property`
- `bool set_alpha_mod(uint alpha)`
- `bool set_blend_mode(blend_mode mode)`
- `bool set_color_mod(uint r, uint g, uint b)`
- `int get_height() const property`
- `int get_width() const property`
- `uint get_alpha_mod() const`

### Class `grid<class T>`

### Class `grid<T>`
##### Behaviours / Constructors
- `bool f()`
- `bool f(int&in, bool&out)`
- `grid<T>@ $list(int&in type, int&in list) { repeat { repeat_same T } }`
- `grid<T>@ f(int&in type)`
- `grid<T>@ f(int&in type, int&in list) {repeat {repeat_same T}}`
- `grid<T>@ f(int&in type, uint width, uint height)`
- `grid<T>@ f(int&in type, uint width, uint height, const T &in value)`
- `grid<T>@ grid(int&in type)`
- `grid<T>@ grid(int&in type, uint width, uint height)`
- `grid<T>@ grid(int&in type, uint width, uint height, const T&in value)`
- `int f()`
- `void f()`
- `void f(int&in)`
##### Methods
- `const T &opIndex(uint x, uint y) const`
- `const T& opIndex(uint x, uint y) const`
- `T &opIndex(uint x, uint y)`
- `T& opIndex(uint x, uint y)`
- `uint height() const`
- `uint width() const`
- `void resize(uint width, uint height)`

### Class `hex_decoder`
##### Behaviours / Constructors
- `hex_decoder@ hex_decoder()`
- `hex_decoder@ hex_decoder(datastream@ stream, const string&in encoding = "", int byteorder = 1)`
##### Properties
- `bool autoflush`
- `bool binary`
- `bool skip_eof`
- `bool sync_rw_cursors`
##### Methods
- `bool close(bool close_all = false)`
- `bool close_all()`
- `bool get_active() const property`
- `bool get_bad() const property`
- `bool get_eof() const property`
- `bool get_fail() const property`
- `bool get_good() const property`
- `bool open(datastream@ stream, const string&in encoding = "", int byteorder = 1)`
- `bool rseek(uint64 offset)`
- `bool rseek_end(uint64 offset = 0)`
- `bool rseek_relative(int64 offset)`
- `bool seek(uint64 offset)`
- `bool seek_end(uint64 offset = 0)`
- `bool seek_relative(int64 offset)`
- `bool wseek(uint64 offset)`
- `bool wseek_end(uint64 offset = 0)`
- `bool wseek_relative(int64 offset)`
- `datastream@ opImplCast()`
- `double read_double()`
- `float read_float()`
- `hex_decoder& opShl(double value)`
- `hex_decoder& opShl(float value)`
- `hex_decoder& opShl(int value)`
- `hex_decoder& opShl(int16 value)`
- `hex_decoder& opShl(int64 value)`
- `hex_decoder& opShl(int8 value)`
- `hex_decoder& opShl(string value)`
- `hex_decoder& opShl(uint value)`
- `hex_decoder& opShl(uint16 value)`
- `hex_decoder& opShl(uint64 value)`
- `hex_decoder& opShl(uint8 value)`
- `hex_decoder& opShr(double&out value)`
- `hex_decoder& opShr(float&out value)`
- `hex_decoder& opShr(int&out value)`
- `hex_decoder& opShr(int16&out value)`
- `hex_decoder& opShr(int64&out value)`
- `hex_decoder& opShr(int8&out value)`
- `hex_decoder& opShr(string&out value)`
- `hex_decoder& opShr(uint&out value)`
- `hex_decoder& opShr(uint16&out value)`
- `hex_decoder& opShr(uint64&out value)`
- `hex_decoder& opShr(uint8&out value)`
- `hex_decoder& write_double(double value)`
- `hex_decoder& write_float(float value)`
- `hex_decoder& write_int(int value)`
- `hex_decoder& write_int16(int16 value)`
- `hex_decoder& write_int64(int64 value)`
- `hex_decoder& write_int8(int8 value)`
- `hex_decoder& write_string(string value)`
- `hex_decoder& write_uint(uint value)`
- `hex_decoder& write_uint16(uint16 value)`
- `hex_decoder& write_uint64(uint64 value)`
- `hex_decoder& write_uint8(uint8 value)`
- `int read_int()`
- `int16 read_int16()`
- `int64 get_pos() const property`
- `int64 get_rpos() const property`
- `int64 get_wpos() const property`
- `int64 read_int64()`
- `int8 read_int8()`
- `string read(uint count = 0)`
- `string read_line()`
- `string read_string()`
- `string read_until(const string&in text, bool require_full)`
- `uint read_uint()`
- `uint write(const string&in data)`
- `uint16 read_uint16()`
- `uint64 get_available() const property`
- `uint64 read_7bit_encoded()`
- `uint64 read_uint64()`
- `uint8 read_uint8()`
- `void flush()`
- `void read_7bit_encoded(uint64&out integer)`
- `void write_7bit_encoded(uint64 integer)`

### Class `hex_encoder`
##### Behaviours / Constructors
- `hex_encoder@ hex_encoder()`
- `hex_encoder@ hex_encoder(datastream@ stream, const string&in encoding = "", int byteorder = 1)`
##### Properties
- `bool autoflush`
- `bool binary`
- `bool skip_eof`
- `bool sync_rw_cursors`
##### Methods
- `bool close(bool close_all = false)`
- `bool close_all()`
- `bool get_active() const property`
- `bool get_bad() const property`
- `bool get_eof() const property`
- `bool get_fail() const property`
- `bool get_good() const property`
- `bool open(datastream@ stream, const string&in encoding = "", int byteorder = 1)`
- `bool rseek(uint64 offset)`
- `bool rseek_end(uint64 offset = 0)`
- `bool rseek_relative(int64 offset)`
- `bool seek(uint64 offset)`
- `bool seek_end(uint64 offset = 0)`
- `bool seek_relative(int64 offset)`
- `bool wseek(uint64 offset)`
- `bool wseek_end(uint64 offset = 0)`
- `bool wseek_relative(int64 offset)`
- `datastream@ opImplCast()`
- `double read_double()`
- `float read_float()`
- `hex_encoder& opShl(double value)`
- `hex_encoder& opShl(float value)`
- `hex_encoder& opShl(int value)`
- `hex_encoder& opShl(int16 value)`
- `hex_encoder& opShl(int64 value)`
- `hex_encoder& opShl(int8 value)`
- `hex_encoder& opShl(string value)`
- `hex_encoder& opShl(uint value)`
- `hex_encoder& opShl(uint16 value)`
- `hex_encoder& opShl(uint64 value)`
- `hex_encoder& opShl(uint8 value)`
- `hex_encoder& opShr(double&out value)`
- `hex_encoder& opShr(float&out value)`
- `hex_encoder& opShr(int&out value)`
- `hex_encoder& opShr(int16&out value)`
- `hex_encoder& opShr(int64&out value)`
- `hex_encoder& opShr(int8&out value)`
- `hex_encoder& opShr(string&out value)`
- `hex_encoder& opShr(uint&out value)`
- `hex_encoder& opShr(uint16&out value)`
- `hex_encoder& opShr(uint64&out value)`
- `hex_encoder& opShr(uint8&out value)`
- `hex_encoder& write_double(double value)`
- `hex_encoder& write_float(float value)`
- `hex_encoder& write_int(int value)`
- `hex_encoder& write_int16(int16 value)`
- `hex_encoder& write_int64(int64 value)`
- `hex_encoder& write_int8(int8 value)`
- `hex_encoder& write_string(string value)`
- `hex_encoder& write_uint(uint value)`
- `hex_encoder& write_uint16(uint16 value)`
- `hex_encoder& write_uint64(uint64 value)`
- `hex_encoder& write_uint8(uint8 value)`
- `int read_int()`
- `int16 read_int16()`
- `int64 get_pos() const property`
- `int64 get_rpos() const property`
- `int64 get_wpos() const property`
- `int64 read_int64()`
- `int8 read_int8()`
- `string read(uint count = 0)`
- `string read_line()`
- `string read_string()`
- `string read_until(const string&in text, bool require_full)`
- `uint read_uint()`
- `uint write(const string&in data)`
- `uint16 read_uint16()`
- `uint64 get_available() const property`
- `uint64 read_7bit_encoded()`
- `uint64 read_uint64()`
- `uint8 read_uint8()`
- `void flush()`
- `void read_7bit_encoded(uint64&out integer)`
- `void write_7bit_encoded(uint64 integer)`

### Class `http`
##### Behaviours / Constructors
- `http@ f()`
- `http@ http()`
##### Methods
- `bool connect(const spec::uri&in url, const string&in body, const name_value_collection@+ headers = null, const http_credentials@+ creds = null)`
- `bool delete(const spec::uri&in url, const string&in body, const name_value_collection@+ headers = null, const http_credentials@+ creds = null)`
- `bool get(const spec::uri&in url, const name_value_collection@+ headers = null, const http_credentials@+ creds = null)`
- `bool get_complete() property`
- `bool get_keepalive() const property`
- `bool get_running() property`
- `bool head(const spec::uri&in url, const name_value_collection@+ headers = null, const http_credentials@+ creds = null)`
- `bool options(const spec::uri&in url, const string&in body, const name_value_collection@+ headers = null, const http_credentials@+ creds = null)`
- `bool patch(const spec::uri&in url, const string&in body, const name_value_collection@+ headers = null, const http_credentials@+ creds = null)`
- `bool post(const spec::uri&in url, const string&in body, const name_value_collection@+ headers = null, const http_credentials@+ creds = null)`
- `bool put(const spec::uri&in url, const string&in body, const name_value_collection@+ headers = null, const http_credentials@+ creds = null)`
- `bool trace(const spec::uri&in url, const string&in body, const name_value_collection@+ headers = null, const http_credentials@+ creds = null)`
- `const uuid& get_uuid() const property`
- `float get_progress() property`
- `http_response@ get_response_headers() property`
- `int get_status_code() property`
- `spec::uri get_url() property`
- `string get_response_body() property`
- `string get_user_agent() const property`
- `string opIndex(const string&in key)`
- `string request()`
- `uint get_connect_timeout() const property`
- `uint get_keepalive_timeout() const property`
- `uint get_max_retries() const property`
- `uint get_receive_timeout() const property`
- `uint get_retry_delay() const property`
- `uint get_send_timeout() const property`
- `void reset(bool configuration = false)`
- `void set_connect_timeout(uint timeout) property`
- `void set_keepalive(bool enabled) property`
- `void set_keepalive_timeout(uint timeout) property`
- `void set_max_retries(uint retries) property`
- `void set_receive_timeout(uint timeout) property`
- `void set_retry_delay(uint delay = 0) property`
- `void set_send_timeout(uint timeout) property`
- `void set_user_agent(const string&in agent = "") property`
- `void wait()`

### Class `http_client`
##### Behaviours / Constructors
- `http_client@ http_client(const string&in host, uint16 port = 80)`
##### Methods
- `bool get_connected() const property`
- `bool get_keep_alive() const property`
- `bool get_secure() const property`
- `bool peek_response(http_response&inout response)`
- `const string& get_host() const property`
- `datastream@ receive_response(http_response&inout response, const string&in encoding = "", int byteorder = STREAM_BYTE_ORDER_NATIVE)`
- `datastream@ send_request(http_request&inout request, const string&in encoding = "", int byteorder = STREAM_BYTE_ORDER_NATIVE)`
- `https_client@ opCast()`
- `timespan get_keep_alive_timeout() const property`
- `timespan get_receive_timeout() const property`
- `timespan get_send_timeout() const property`
- `uint16 get_port() const property`
- `void abort()`
- `void flush_request()`
- `void reset()`
- `void set_host(const string&in host) property`
- `void set_keep_alive(bool enabled) property`
- `void set_keep_alive_timeout(const timespan&in timeout) property`
- `void set_port(uint16 port) property`
- `void set_receive_timeout(const timespan&in timeout) property`
- `void set_send_timeout(const timespan&in timeout) property`

### Class `http_credentials`
##### Behaviours / Constructors
- `http_credentials@ f()`
- `http_credentials@ f(const string&in username, const string&in password)`
- `http_credentials@ http_credentials()`
- `http_credentials@ http_credentials(const string&in username, const string&in password)`
##### Methods
- `bool get_empty() const property`
- `string get_host() const property`
- `string get_password() const property`
- `string get_username() const property`
- `void authenticate(http_request& request, const http_response&in response)`
- `void authenticate(http_request&inout request, const http_response&in response)`
- `void clear()`
- `void from_uri(const spec::uri&in uri)`
- `void from_user_info(const string&in user_info)`
- `void proxy_authenticate(http_request& request, const http_response&in response)`
- `void proxy_authenticate(http_request&inout request, const http_response&in response)`
- `void set_host(const string&in host) property`
- `void set_password(const string&in password) property`
- `void set_username(const string&in username) property`
- `void update_auth_info(http_request& request)`
- `void update_auth_info(http_request&inout request)`
- `void update_proxy_auth_info(http_request& request)`
- `void update_proxy_auth_info(http_request&inout request)`

### Class `http_request`
##### Behaviours / Constructors
- `http_request@ $list(int&in) { repeat { string, string } }`
- `http_request@ http_request()`
- `http_request@ http_request(const http_request&in other)`
- `http_request@ http_request(const string&in method, const string&in uri, const string&in version = HTTP_1_1)`
##### Methods
- `bool empty() const`
- `bool exists(const string&in name) const`
- `bool get_auto_decode() const property`
- `bool get_chunked_transfer_encoding() const property`
- `bool get_expect_continue() const property`
- `bool get_has_content_length() const property`
- `bool get_has_credentials() const property`
- `bool get_has_proxy_credentials() const property`
- `bool get_keep_alive() const property`
- `bool has_token(const string&in name, const string&in token)`
- `bool read(datastream@ stream)`
- `bool write(datastream@ stream) const`
- `const string& get(const string&in name, const string&in default_value = "") const`
- `const string& get_host() const property`
- `const string& get_method() const property`
- `const string& get_opIndex(const string&in name) const property`
- `const string& get_uri() const property`
- `const string& get_version() const property`
- `const string& name_at(uint index) const`
- `const string& value_at(uint index) const`
- `http_request& opAssign(const http_request&in other)`
- `int get_field_limit() const property`
- `int get_name_length_limit() const property`
- `int get_value_length_limit() const property`
- `int64 get_content_length() const property`
- `internet_message_header@ opImplCast()`
- `string get_content_type() const property`
- `string get_decoded(const string&in name, const string&in default_value = "")`
- `string get_transfer_encoding() const property`
- `uint64 size() const`
- `void add(const string&in name, const string&in value)`
- `void clear()`
- `void erase(const string&in name)`
- `void get_cookies(name_value_collection&inout cookies) const`
- `void get_credentials(string&inout scheme, string&inout auth_info) const`
- `void get_proxy_credentials(string&inout scheme, string&inout auth_info) const`
- `void remove_credentials()`
- `void remove_proxy_credentials()`
- `void secure_erase(const string&in name)`
- `void set(const string&in name, const string&in value)`
- `void set_auto_decode(bool enabled) property`
- `void set_chunked_transfer_encoding(bool enabled) property`
- `void set_content_length(int64 length) property`
- `void set_content_type(const string&in media_type) property`
- `void set_cookies(const name_value_collection&inout cookies)`
- `void set_credentials(const string&in scheme, const string&in auth_info)`
- `void set_expect_continue(bool expect) property`
- `void set_field_limit(int limit) property`
- `void set_host(const string&in host) property`
- `void set_host(const string&in host, uint16 port) property`
- `void set_keep_alive(bool enabled) property`
- `void set_method(const string&in method) property`
- `void set_name_length_limit(int limit) property`
- `void set_opIndex(const string&in name, const string&in value) property`
- `void set_proxy_credentials(const string&in scheme, const string&in auth_info)`
- `void set_transfer_encoding(const string&in encoding) property`
- `void set_uri(const string&in uri) property`
- `void set_value_length_limit(int limit) property`
- `void set_version(const string&in version) property`

### Class `http_response`
##### Behaviours / Constructors
- `http_response@ $list(int&in) { repeat { string, string } }`
- `http_response@ http_response()`
- `http_response@ http_response(const http_response&in other)`
- `http_response@ http_response(const string&in version, http_status status)`
- `http_response@ http_response(const string&in version, http_status status, const string&in reason)`
- `http_response@ http_response(http_status status)`
- `http_response@ http_response(http_status status, const string&in reason)`
##### Methods
- `bool empty() const`
- `bool exists(const string&in name) const`
- `bool get_auto_decode() const property`
- `bool get_chunked_transfer_encoding() const property`
- `bool get_has_content_length() const property`
- `bool get_keep_alive() const property`
- `bool has_token(const string&in name, const string&in token)`
- `bool read(datastream@ stream)`
- `bool write(datastream@ stream) const`
- `const string& get(const string&in name, const string&in default_value = "") const`
- `const string& get_opIndex(const string&in name) const property`
- `const string& get_reason() const property`
- `const string& get_version() const property`
- `const string& name_at(uint index) const`
- `const string& value_at(uint index) const`
- `http_response& opAssign(const http_response&in other)`
- `http_status get_status() const property`
- `int get_field_limit() const property`
- `int get_name_length_limit() const property`
- `int get_value_length_limit() const property`
- `int64 get_content_length() const property`
- `internet_message_header@ opImplCast()`
- `string get_content_type() const property`
- `string get_decoded(const string&in name, const string&in default_value = "")`
- `string get_transfer_encoding() const property`
- `uint64 size() const`
- `void add(const string&in name, const string&in value)`
- `void clear()`
- `void erase(const string&in name)`
- `void secure_erase(const string&in name)`
- `void set(const string&in name, const string&in value)`
- `void set_auto_decode(bool enabled) property`
- `void set_chunked_transfer_encoding(bool enabled) property`
- `void set_content_length(int64 length) property`
- `void set_content_type(const string&in media_type) property`
- `void set_field_limit(int limit) property`
- `void set_keep_alive(bool enabled) property`
- `void set_name_length_limit(int limit) property`
- `void set_opIndex(const string&in name, const string&in value) property`
- `void set_reason(const string&in reason) property`
- `void set_status(const string&in status)`
- `void set_status(http_status status) property`
- `void set_status_and_reason(http_status status)`
- `void set_status_and_reason(http_status status, const string&in reason)`
- `void set_transfer_encoding(const string&in encoding) property`
- `void set_value_length_limit(int limit) property`
- `void set_version(const string&in version) property`

### Class `https_client`
##### Behaviours / Constructors
- `https_client@ https_client(const string&in host, uint16 port = 443)`
##### Methods
- `bool get_connected() const property`
- `bool get_keep_alive() const property`
- `bool get_secure() const property`
- `bool peek_response(http_response&inout response)`
- `const string& get_host() const property`
- `datastream@ receive_response(http_response&inout response, const string&in encoding = "", int byteorder = STREAM_BYTE_ORDER_NATIVE)`
- `datastream@ send_request(http_request&inout request, const string&in encoding = "", int byteorder = STREAM_BYTE_ORDER_NATIVE)`
- `http_client@ opImplCast()`
- `timespan get_keep_alive_timeout() const property`
- `timespan get_receive_timeout() const property`
- `timespan get_send_timeout() const property`
- `uint16 get_port() const property`
- `void abort()`
- `void flush_request()`
- `void reset()`
- `void set_host(const string&in host) property`
- `void set_keep_alive(bool enabled) property`
- `void set_keep_alive_timeout(const timespan&in timeout) property`
- `void set_port(uint16 port) property`
- `void set_receive_timeout(const timespan&in timeout) property`
- `void set_send_timeout(const timespan&in timeout) property`

### Class `inflating_reader`
##### Behaviours / Constructors
- `inflating_reader@ inflating_reader()`
- `inflating_reader@ inflating_reader(datastream@ stream, compression_method compression = COMPRESSION_METHOD_ZLIB, const string&in encoding = "", int byteorder = 1)`
##### Properties
- `bool autoflush`
- `bool binary`
- `bool skip_eof`
- `bool sync_rw_cursors`
##### Methods
- `bool close(bool close_all = false)`
- `bool close_all()`
- `bool get_active() const property`
- `bool get_bad() const property`
- `bool get_eof() const property`
- `bool get_fail() const property`
- `bool get_good() const property`
- `bool open(datastream@ stream, compression_method compression = COMPRESSION_METHOD_ZLIB, const string&in encoding = "", int byteorder = 1)`
- `bool rseek(uint64 offset)`
- `bool rseek_end(uint64 offset = 0)`
- `bool rseek_relative(int64 offset)`
- `bool seek(uint64 offset)`
- `bool seek_end(uint64 offset = 0)`
- `bool seek_relative(int64 offset)`
- `bool wseek(uint64 offset)`
- `bool wseek_end(uint64 offset = 0)`
- `bool wseek_relative(int64 offset)`
- `datastream@ opImplCast()`
- `double read_double()`
- `float read_float()`
- `inflating_reader& opShl(double value)`
- `inflating_reader& opShl(float value)`
- `inflating_reader& opShl(int value)`
- `inflating_reader& opShl(int16 value)`
- `inflating_reader& opShl(int64 value)`
- `inflating_reader& opShl(int8 value)`
- `inflating_reader& opShl(string value)`
- `inflating_reader& opShl(uint value)`
- `inflating_reader& opShl(uint16 value)`
- `inflating_reader& opShl(uint64 value)`
- `inflating_reader& opShl(uint8 value)`
- `inflating_reader& opShr(double&out value)`
- `inflating_reader& opShr(float&out value)`
- `inflating_reader& opShr(int&out value)`
- `inflating_reader& opShr(int16&out value)`
- `inflating_reader& opShr(int64&out value)`
- `inflating_reader& opShr(int8&out value)`
- `inflating_reader& opShr(string&out value)`
- `inflating_reader& opShr(uint&out value)`
- `inflating_reader& opShr(uint16&out value)`
- `inflating_reader& opShr(uint64&out value)`
- `inflating_reader& opShr(uint8&out value)`
- `inflating_reader& write_double(double value)`
- `inflating_reader& write_float(float value)`
- `inflating_reader& write_int(int value)`
- `inflating_reader& write_int16(int16 value)`
- `inflating_reader& write_int64(int64 value)`
- `inflating_reader& write_int8(int8 value)`
- `inflating_reader& write_string(string value)`
- `inflating_reader& write_uint(uint value)`
- `inflating_reader& write_uint16(uint16 value)`
- `inflating_reader& write_uint64(uint64 value)`
- `inflating_reader& write_uint8(uint8 value)`
- `int read_int()`
- `int16 read_int16()`
- `int64 get_pos() const property`
- `int64 get_rpos() const property`
- `int64 get_wpos() const property`
- `int64 read_int64()`
- `int8 read_int8()`
- `string read(uint count = 0)`
- `string read_line()`
- `string read_string()`
- `string read_until(const string&in text, bool require_full)`
- `uint read_uint()`
- `uint write(const string&in data)`
- `uint16 read_uint16()`
- `uint64 get_available() const property`
- `uint64 read_7bit_encoded()`
- `uint64 read_uint64()`
- `uint8 read_uint8()`
- `void flush()`
- `void read_7bit_encoded(uint64&out integer)`
- `void write_7bit_encoded(uint64 integer)`

### Class `inflating_writer`
##### Behaviours / Constructors
- `inflating_writer@ inflating_writer()`
- `inflating_writer@ inflating_writer(datastream@ stream, compression_method compression = COMPRESSION_METHOD_ZLIB, const string&in encoding = "", int byteorder = 1)`
##### Properties
- `bool autoflush`
- `bool binary`
- `bool skip_eof`
- `bool sync_rw_cursors`
##### Methods
- `bool close(bool close_all = false)`
- `bool close_all()`
- `bool get_active() const property`
- `bool get_bad() const property`
- `bool get_eof() const property`
- `bool get_fail() const property`
- `bool get_good() const property`
- `bool open(datastream@ stream, compression_method compression = COMPRESSION_METHOD_ZLIB, const string&in encoding = "", int byteorder = 1)`
- `bool rseek(uint64 offset)`
- `bool rseek_end(uint64 offset = 0)`
- `bool rseek_relative(int64 offset)`
- `bool seek(uint64 offset)`
- `bool seek_end(uint64 offset = 0)`
- `bool seek_relative(int64 offset)`
- `bool wseek(uint64 offset)`
- `bool wseek_end(uint64 offset = 0)`
- `bool wseek_relative(int64 offset)`
- `datastream@ opImplCast()`
- `double read_double()`
- `float read_float()`
- `inflating_writer& opShl(double value)`
- `inflating_writer& opShl(float value)`
- `inflating_writer& opShl(int value)`
- `inflating_writer& opShl(int16 value)`
- `inflating_writer& opShl(int64 value)`
- `inflating_writer& opShl(int8 value)`
- `inflating_writer& opShl(string value)`
- `inflating_writer& opShl(uint value)`
- `inflating_writer& opShl(uint16 value)`
- `inflating_writer& opShl(uint64 value)`
- `inflating_writer& opShl(uint8 value)`
- `inflating_writer& opShr(double&out value)`
- `inflating_writer& opShr(float&out value)`
- `inflating_writer& opShr(int&out value)`
- `inflating_writer& opShr(int16&out value)`
- `inflating_writer& opShr(int64&out value)`
- `inflating_writer& opShr(int8&out value)`
- `inflating_writer& opShr(string&out value)`
- `inflating_writer& opShr(uint&out value)`
- `inflating_writer& opShr(uint16&out value)`
- `inflating_writer& opShr(uint64&out value)`
- `inflating_writer& opShr(uint8&out value)`
- `inflating_writer& write_double(double value)`
- `inflating_writer& write_float(float value)`
- `inflating_writer& write_int(int value)`
- `inflating_writer& write_int16(int16 value)`
- `inflating_writer& write_int64(int64 value)`
- `inflating_writer& write_int8(int8 value)`
- `inflating_writer& write_string(string value)`
- `inflating_writer& write_uint(uint value)`
- `inflating_writer& write_uint16(uint16 value)`
- `inflating_writer& write_uint64(uint64 value)`
- `inflating_writer& write_uint8(uint8 value)`
- `int read_int()`
- `int16 read_int16()`
- `int64 get_pos() const property`
- `int64 get_rpos() const property`
- `int64 get_wpos() const property`
- `int64 read_int64()`
- `int8 read_int8()`
- `string read(uint count = 0)`
- `string read_line()`
- `string read_string()`
- `string read_until(const string&in text, bool require_full)`
- `uint read_uint()`
- `uint write(const string&in data)`
- `uint16 read_uint16()`
- `uint64 get_available() const property`
- `uint64 read_7bit_encoded()`
- `uint64 read_uint64()`
- `uint8 read_uint8()`
- `void flush()`
- `void read_7bit_encoded(uint64&out integer)`
- `void write_7bit_encoded(uint64 integer)`

### Class `internet_message_header`
##### Behaviours / Constructors
- `internet_message_header@ $list(int&in) { repeat { string, string } }`
- `internet_message_header@ internet_message_header()`
- `internet_message_header@ internet_message_header(const internet_message_header&in other)`
##### Methods
- `bool empty() const`
- `bool exists(const string&in name) const`
- `bool get_auto_decode() const property`
- `bool has_token(const string&in name, const string&in token)`
- `bool read(datastream@ stream)`
- `bool write(datastream@ stream) const`
- `const string& get(const string&in name, const string&in default_value = "") const`
- `const string& get_opIndex(const string&in name) const property`
- `const string& name_at(uint index) const`
- `const string& value_at(uint index) const`
- `http_request@ opCast()`
- `http_response@ opCast()`
- `int get_field_limit() const property`
- `int get_name_length_limit() const property`
- `int get_value_length_limit() const property`
- `internet_message_header& opAssign(const internet_message_header&in other)`
- `name_value_collection@ opImplCast()`
- `string get_decoded(const string&in name, const string&in default_value = "")`
- `uint64 size() const`
- `void add(const string&in name, const string&in value)`
- `void clear()`
- `void erase(const string&in name)`
- `void secure_erase(const string&in name)`
- `void set(const string&in name, const string&in value)`
- `void set_auto_decode(bool enabled) property`
- `void set_field_limit(int limit) property`
- `void set_name_length_limit(int limit) property`
- `void set_opIndex(const string&in name, const string&in value) property`
- `void set_value_length_limit(int limit) property`

### Class `ip_address`
##### Behaviours / Constructors
- `void f()`
- `void f(const ip_address&in other)`
- `void f(const string&in addr)`
- `void f(const string&in addr, ip_address_family family)`
- `void f(ip_address_family family)`
- `void ip_address()`
- `void ip_address(const spec::ip_address&in other)`
- `void ip_address(const string&in addr)`
- `void ip_address(const string&in addr, spec::ip_address_family family)`
- `void ip_address(spec::ip_address_family family)`
##### Methods
- `bool get_is_broadcast() const property`
- `bool get_is_global_multicast() const property`
- `bool get_is_IPV4_compatible() const property`
- `bool get_is_IPV4_mapped() const property`
- `bool get_is_link_local() const property`
- `bool get_is_link_local_multicast() const property`
- `bool get_is_loopback() const property`
- `bool get_is_multicast() const property`
- `bool get_is_node_local_multicast() const property`
- `bool get_is_org_local_multicast() const property`
- `bool get_is_site_local() const property`
- `bool get_is_site_local_multicast() const property`
- `bool get_is_unicast() const property`
- `bool get_is_v4() const property`
- `bool get_is_v6() const property`
- `bool get_is_well_known_multicast() const property`
- `bool get_is_wildcard() const property`
- `bool opEquals(const ip_address&in addr) const`
- `bool opEquals(const spec::ip_address&in addr) const`
- `int opCmp(const ip_address&in other)`
- `int opCmp(const spec::ip_address&in other)`
- `ip_address opAnd(const ip_address&in addr) const`
- `ip_address opCom() const`
- `ip_address opOr(const ip_address&in addr) const`
- `ip_address opXor(const ip_address&in addr) const`
- `ip_address& opAssign(const ip_address&in addr)`
- `ip_address_family get_family() const property`
- `spec::ip_address opAnd(const spec::ip_address&in addr) const`
- `spec::ip_address opCom() const`
- `spec::ip_address opOr(const spec::ip_address&in addr) const`
- `spec::ip_address opXor(const spec::ip_address&in addr) const`
- `spec::ip_address& opAssign(const spec::ip_address&in addr)`
- `spec::ip_address_family get_family() const property`
- `string opImplConv() const`
- `uint get_prefix_length() const property`
- `uint get_scope() const property`
- `void mask(const ip_address&in mask)`
- `void mask(const ip_address&in mask, const ip_address&in set)`
- `void mask(const spec::ip_address&in mask)`
- `void mask(const spec::ip_address&in mask, const spec::ip_address&in set)`

### Class `joystick`
##### Behaviours / Constructors
- `joystick@ f()`
- `joystick@ joystick()`
##### Methods
- `bool button_down(int button)`
- `bool button_pressed(int button)`
- `bool button_released(int button)`
- `bool button_up(int button)`
- `bool get_active() const property`
- `bool get_can_vibrate() const property`
- `bool get_can_vibrate_triggers() const property`
- `bool get_has_led() const property`
- `bool get_has_r_x() const property`
- `bool get_has_r_y() const property`
- `bool get_has_r_z() const property`
- `bool get_has_x() const property`
- `bool get_has_y() const property`
- `bool get_has_z() const property`
- `bool pov_centered(int pov)`
- `bool refresh_joystick_list()`
- `bool set(int index)`
- `bool set_led(uint8 red, uint8 green, uint8 blue)`
- `bool vibrate(uint16 low_frequency, uint16 high_frequency, int duration)`
- `bool vibrate_triggers(uint16 left, uint16 right, int duration)`
- `int get_a_slider_1() const property`
- `int get_a_slider_2() const property`
- `int get_a_x() const property`
- `int get_a_y() const property`
- `int get_a_z() const property`
- `int get_ar_x() const property`
- `int get_ar_y() const property`
- `int get_ar_z() const property`
- `int get_f_slider_1() const property`
- `int get_f_slider_2() const property`
- `int get_f_x() const property`
- `int get_f_y() const property`
- `int get_f_z() const property`
- `int get_fr_x() const property`
- `int get_fr_y() const property`
- `int get_fr_z() const property`
- `int get_pov_1() const property`
- `int get_pov_2() const property`
- `int get_pov_3() const property`
- `int get_pov_4() const property`
- `int get_preferred_joystick() const property`
- `int get_r_x() const property`
- `int get_r_y() const property`
- `int get_r_z() const property`
- `int get_slider_1() const property`
- `int get_slider_2() const property`
- `int get_touchpads() const property`
- `int get_v_slider_1() const property`
- `int get_v_slider_2() const property`
- `int get_v_x() const property`
- `int get_v_y() const property`
- `int get_v_z() const property`
- `int get_vr_x() const property`
- `int get_vr_y() const property`
- `int get_vr_z() const property`
- `int get_x() const property`
- `int get_y() const property`
- `int get_z() const property`
- `int[]@ buttons_down()`
- `int[]@ buttons_pressed()`
- `int[]@ buttons_released()`
- `int[]@ buttons_up()`
- `joystick_power_info get_power_info() const property`
- `string get_name() const property`
- `string get_serial() const property`
- `string[]@ list_joysticks()`
- `uint get_buttons() const property`
- `uint get_joysticks() const property`
- `uint get_povs() const property`
- `uint get_sliders() const property`
- `uint get_type() const property`
- `void set_preferred_joystick(int index) property`

### Class `joystick_power_info`
##### Behaviours / Constructors
- `void f()`
- `void f(const joystick_power_info&in other)`
- `void f(int state, int percentage)`
- `void joystick_power_info()`
- `void joystick_power_info(const joystick_power_info&in other)`
- `void joystick_power_info(int state, int percentage)`
##### Properties
- `int percentage`
- `int state`
##### Methods
- `string get_state_name() const property`
- `string opConv() const`
- `string opImplConv() const`
- `string to_string() const`

### Class `json_array`
##### Behaviours / Constructors
- `json_array @a()`
- `json_array @a(json_array@+ other)`
- `json_array@ $list(int&in) { repeat var@ }`
- `json_array@ f(int&in) {repeat var@}`
- `json_array@ json_array()`
- `json_array@ json_array(json_array@ other)`
##### Methods
- `bool get_empty() property`
- `bool get_escape_unicode() property`
- `bool is_array(uint index)`
- `bool is_null(uint index)`
- `bool is_object(uint index)`
- `json_array& extend(const json_array@+ array)`
- `json_array& opAssign(json_array@+ other)`
- `json_array@ get_array(uint index) const`
- `json_object@ get_object(uint index) const`
- `string stringify(uint indent = 0, int step = -1)`
- `uint length()`
- `uint size()`
- `var@ get_opIndex(uint index) property`
- `var@ opCall(const string&in path) const`
- `void add(const var&in value)`
- `void clear()`
- `void remove(uint index)`
- `void set_escape_unicode(bool value) property`
- `void set_opIndex(uint index, const var&in value) property`
- `void stringify(datastream@+ stream, uint indent = 0, int step = -1)`

### Class `json_object`
##### Behaviours / Constructors
- `json_object @o()`
- `json_object @o(json_object@+ other)`
- `json_object@ $list(int&in) { repeat { string, var@ } }`
- `json_object@ f(int&in) {repeat {string, var@}}`
- `json_object@ json_object()`
- `json_object@ json_object(json_object@ other)`
##### Methods
- `bool exists(const string&in key) const`
- `bool get_escape_unicode() const property`
- `bool is_array(const string&in key) const`
- `bool is_null(const string&in key) const`
- `bool is_object(const string&in key) const`
- `json_array@ get_array(const string&in key) const`
- `json_object& opAssign(json_object@+ other)`
- `json_object@ get_object(const string&in key) const`
- `string stringify(uint indent = 0, int step = -1) const`
- `string[]@ get_keys() const`
- `uint size() const`
- `var@ get(const string&in key, var@ default_value = null) const`
- `var@ get_opIndex(const string&in key) const property`
- `var@ opCall(const string&in path, var@ default_value = null) const`
- `void clear()`
- `void remove(const string&in key)`
- `void set(const string&in key, const var&in value)`
- `void set_escape_unicode(bool value) property`
- `void set_opIndex(const string&in key, const var&in value) property`
- `void stringify(datastream@+ stream, uint indent = 0, int step = -1) const`

### Class `library`
##### Behaviours / Constructors
- `library @l()`
- `library@ library()`
##### Methods
- `bool get_active() const property`
- `bool load(const string&in filename)`
- `bool unload()`
- `library_function@ get(const string&in sig)`
- `var@ call(const string&in sig, ?&in...)`

### Class `library_function`
##### Methods
- `bool get_valid() const property`
- `string get_error() const property`
- `var@ opCall(?&in...)`

### Class `line_converting_reader`
##### Behaviours / Constructors
- `line_converting_reader@ line_converting_reader()`
- `line_converting_reader@ line_converting_reader(datastream@ stream, const string&in line_ending = spec::NEWLINE_DEFAULT, const string&in encoding = "", int byteorder = 1)`
##### Properties
- `bool autoflush`
- `bool binary`
- `bool skip_eof`
- `bool sync_rw_cursors`
##### Methods
- `bool close(bool close_all = false)`
- `bool close_all()`
- `bool get_active() const property`
- `bool get_bad() const property`
- `bool get_eof() const property`
- `bool get_fail() const property`
- `bool get_good() const property`
- `bool open(datastream@ stream, const string&in line_ending = spec::NEWLINE_DEFAULT, const string&in encoding = "", int byteorder = 1)`
- `bool rseek(uint64 offset)`
- `bool rseek_end(uint64 offset = 0)`
- `bool rseek_relative(int64 offset)`
- `bool seek(uint64 offset)`
- `bool seek_end(uint64 offset = 0)`
- `bool seek_relative(int64 offset)`
- `bool wseek(uint64 offset)`
- `bool wseek_end(uint64 offset = 0)`
- `bool wseek_relative(int64 offset)`
- `datastream@ opImplCast()`
- `double read_double()`
- `float read_float()`
- `int read_int()`
- `int16 read_int16()`
- `int64 get_pos() const property`
- `int64 get_rpos() const property`
- `int64 get_wpos() const property`
- `int64 read_int64()`
- `int8 read_int8()`
- `line_converting_reader& opShl(double value)`
- `line_converting_reader& opShl(float value)`
- `line_converting_reader& opShl(int value)`
- `line_converting_reader& opShl(int16 value)`
- `line_converting_reader& opShl(int64 value)`
- `line_converting_reader& opShl(int8 value)`
- `line_converting_reader& opShl(string value)`
- `line_converting_reader& opShl(uint value)`
- `line_converting_reader& opShl(uint16 value)`
- `line_converting_reader& opShl(uint64 value)`
- `line_converting_reader& opShl(uint8 value)`
- `line_converting_reader& opShr(double&out value)`
- `line_converting_reader& opShr(float&out value)`
- `line_converting_reader& opShr(int&out value)`
- `line_converting_reader& opShr(int16&out value)`
- `line_converting_reader& opShr(int64&out value)`
- `line_converting_reader& opShr(int8&out value)`
- `line_converting_reader& opShr(string&out value)`
- `line_converting_reader& opShr(uint&out value)`
- `line_converting_reader& opShr(uint16&out value)`
- `line_converting_reader& opShr(uint64&out value)`
- `line_converting_reader& opShr(uint8&out value)`
- `line_converting_reader& write_double(double value)`
- `line_converting_reader& write_float(float value)`
- `line_converting_reader& write_int(int value)`
- `line_converting_reader& write_int16(int16 value)`
- `line_converting_reader& write_int64(int64 value)`
- `line_converting_reader& write_int8(int8 value)`
- `line_converting_reader& write_string(string value)`
- `line_converting_reader& write_uint(uint value)`
- `line_converting_reader& write_uint16(uint16 value)`
- `line_converting_reader& write_uint64(uint64 value)`
- `line_converting_reader& write_uint8(uint8 value)`
- `string read(uint count = 0)`
- `string read_line()`
- `string read_string()`
- `string read_until(const string&in text, bool require_full)`
- `uint read_uint()`
- `uint write(const string&in data)`
- `uint16 read_uint16()`
- `uint64 get_available() const property`
- `uint64 read_7bit_encoded()`
- `uint64 read_uint64()`
- `uint8 read_uint8()`
- `void flush()`
- `void read_7bit_encoded(uint64&out integer)`
- `void write_7bit_encoded(uint64 integer)`

### Class `line_converting_writer`
##### Behaviours / Constructors
- `line_converting_writer@ line_converting_writer()`
- `line_converting_writer@ line_converting_writer(datastream@ stream, const string&in line_ending = spec::NEWLINE_DEFAULT, const string&in encoding = "", int byteorder = 1)`
##### Properties
- `bool autoflush`
- `bool binary`
- `bool skip_eof`
- `bool sync_rw_cursors`
##### Methods
- `bool close(bool close_all = false)`
- `bool close_all()`
- `bool get_active() const property`
- `bool get_bad() const property`
- `bool get_eof() const property`
- `bool get_fail() const property`
- `bool get_good() const property`
- `bool open(datastream@ stream, const string&in line_ending = spec::NEWLINE_DEFAULT, const string&in encoding = "", int byteorder = 1)`
- `bool rseek(uint64 offset)`
- `bool rseek_end(uint64 offset = 0)`
- `bool rseek_relative(int64 offset)`
- `bool seek(uint64 offset)`
- `bool seek_end(uint64 offset = 0)`
- `bool seek_relative(int64 offset)`
- `bool wseek(uint64 offset)`
- `bool wseek_end(uint64 offset = 0)`
- `bool wseek_relative(int64 offset)`
- `datastream@ opImplCast()`
- `double read_double()`
- `float read_float()`
- `int read_int()`
- `int16 read_int16()`
- `int64 get_pos() const property`
- `int64 get_rpos() const property`
- `int64 get_wpos() const property`
- `int64 read_int64()`
- `int8 read_int8()`
- `line_converting_writer& opShl(double value)`
- `line_converting_writer& opShl(float value)`
- `line_converting_writer& opShl(int value)`
- `line_converting_writer& opShl(int16 value)`
- `line_converting_writer& opShl(int64 value)`
- `line_converting_writer& opShl(int8 value)`
- `line_converting_writer& opShl(string value)`
- `line_converting_writer& opShl(uint value)`
- `line_converting_writer& opShl(uint16 value)`
- `line_converting_writer& opShl(uint64 value)`
- `line_converting_writer& opShl(uint8 value)`
- `line_converting_writer& opShr(double&out value)`
- `line_converting_writer& opShr(float&out value)`
- `line_converting_writer& opShr(int&out value)`
- `line_converting_writer& opShr(int16&out value)`
- `line_converting_writer& opShr(int64&out value)`
- `line_converting_writer& opShr(int8&out value)`
- `line_converting_writer& opShr(string&out value)`
- `line_converting_writer& opShr(uint&out value)`
- `line_converting_writer& opShr(uint16&out value)`
- `line_converting_writer& opShr(uint64&out value)`
- `line_converting_writer& opShr(uint8&out value)`
- `line_converting_writer& write_double(double value)`
- `line_converting_writer& write_float(float value)`
- `line_converting_writer& write_int(int value)`
- `line_converting_writer& write_int16(int16 value)`
- `line_converting_writer& write_int64(int64 value)`
- `line_converting_writer& write_int8(int8 value)`
- `line_converting_writer& write_string(string value)`
- `line_converting_writer& write_uint(uint value)`
- `line_converting_writer& write_uint16(uint16 value)`
- `line_converting_writer& write_uint64(uint64 value)`
- `line_converting_writer& write_uint8(uint8 value)`
- `string read(uint count = 0)`
- `string read_line()`
- `string read_string()`
- `string read_until(const string&in text, bool require_full)`
- `uint read_uint()`
- `uint write(const string&in data)`
- `uint16 read_uint16()`
- `uint64 get_available() const property`
- `uint64 read_7bit_encoded()`
- `uint64 read_uint64()`
- `uint8 read_uint8()`
- `void flush()`
- `void read_7bit_encoded(uint64&out integer)`
- `void write_7bit_encoded(uint64 integer)`

### Class `mail_message`
##### Behaviours / Constructors
- `mail_message@ f()`
- `mail_message@ mail_message()`
##### Methods
- `array<mail_recipient@>@ get_recipients() const`
- `bool add_attachment_file(const string &in name, const string &in path)`
- `bool add_attachment_file(const string&in name, const string&in path)`
- `bool add_attachment_string(const string &in name, const string &in content, const string &in media_type = "application/octet-stream")`
- `bool add_attachment_string(const string&in name, const string&in content, const string&in media_type = "application/octet-stream")`
- `int get_priority() const property`
- `string add_inline_attachment_file(const string &in path, const string &in content_id = "")`
- `string add_inline_attachment_file(const string&in path, const string&in content_id = "")`
- `string add_inline_attachment_string(const string &in content, const string &in media_type, const string &in content_id)`
- `string add_inline_attachment_string(const string&in content, const string&in media_type, const string&in content_id)`
- `string get_content() const property`
- `string get_disposition_notification_to() const property`
- `string get_header(const string &in name) const`
- `string get_header(const string&in name) const`
- `string get_in_reply_to() const property`
- `string get_last_error() const property`
- `string get_message_id() const property`
- `string get_references() const property`
- `string get_reply_to() const property`
- `string get_return_receipt_to() const property`
- `string get_sender() const property`
- `string get_subject() const property`
- `void add_header(const string &in name, const string &in value)`
- `void add_header(const string&in name, const string&in value)`
- `void add_recipient(const mail_recipient &in recipient)`
- `void add_recipient(const mail_recipient&in recipient)`
- `void add_recipient(const string &in address, mail_recipient_type type = RECIPIENT_TO)`
- `void add_recipient(const string&in address, mail_recipient_type type = RECIPIENT_TO)`
- `void set_content(const string &in content, const string &in content_type = "text/plain")`
- `void set_content(const string&in content, const string&in content_type = "text/plain")`
- `void set_disposition_notification_to(const string &in address) property`
- `void set_disposition_notification_to(const string&in address) property`
- `void set_html_content(const string &in html, const string &in plain_alternative = "")`
- `void set_html_content(const string&in html, const string&in plain_alternative = "")`
- `void set_in_reply_to(const string &in message_id) property`
- `void set_in_reply_to(const string&in message_id) property`
- `void set_message_id(const string &in message_id) property`
- `void set_message_id(const string&in message_id) property`
- `void set_priority(mail_priority priority)`
- `void set_read_receipt(const string &in address)`
- `void set_read_receipt(const string&in address)`
- `void set_references(const string &in references) property`
- `void set_references(const string&in references) property`
- `void set_reply_to(const string &in address) property`
- `void set_reply_to(const string&in address) property`
- `void set_return_receipt_to(const string &in address) property`
- `void set_return_receipt_to(const string&in address) property`
- `void set_sender(const string &in address)`
- `void set_sender(const string&in address)`
- `void set_subject(const string &in subject)`
- `void set_subject(const string&in subject)`

### Class `mail_recipient`
##### Behaviours / Constructors
- `mail_recipient@ f()`
- `mail_recipient@ f(mail_recipient_type type, const string &in address, const string &in real_name = "")`
- `mail_recipient@ mail_recipient()`
- `mail_recipient@ mail_recipient(mail_recipient_type type, const string&in address, const string&in real_name = "")`
##### Properties
- `mail_recipient_type type`
- `string address`
- `string real_name`

### Class `matrix3x3`
##### Behaviours / Constructors
- `void f()`
- `void f(float a1, float a2, float a3, float b1, float b2, float b3, float c1, float c2, float c3)`
- `void f(float value)`
- `void matrix3x3()`
- `void matrix3x3(float a1, float a2, float a3, float b1, float b2, float b3, float c1, float c2, float c3)`
- `void matrix3x3(float value)`
##### Methods
- `bool opEquals(const matrix3x3&in)`
- `const vector& opIndex(int row) const`
- `float get_determinant() const property`
- `float get_trace() const property`
- `matrix3x3 get_absolute() const property`
- `matrix3x3 get_inverse() const property`
- `matrix3x3 get_inverse(float determinant) const`
- `matrix3x3 get_transpose() const property`
- `matrix3x3 opAdd(const matrix3x3&in matrix) const`
- `matrix3x3 opMul(const matrix3x3&in matrix) const`
- `matrix3x3 opMul(float value) const`
- `matrix3x3 opMulR(float value) const`
- `matrix3x3 opNeg() const`
- `matrix3x3 opSub(const matrix3x3&in matrix) const`
- `matrix3x3& opAddAssign(const matrix3x3&in matrix)`
- `matrix3x3& opMulAssign(float value)`
- `matrix3x3& opSubAssign(const matrix3x3&in matrix)`
- `string opImplConv()`
- `vector get_column(int i) const`
- `vector get_row(int i) const`
- `vector opMul(const vector&in value) const`
- `vector& opIndex(int row)`
- `void set(float a1, float a2, float a3, float b1, float b2, float b3, float c1, float c2, float c3)`
- `void set_to_identity()`
- `void set_to_zero()`

### Class `memory_buffer<class T>`

### Class `memory_buffer<T>`
##### Behaviours / Constructors
- `bool f(int&in subtype, bool&out no_gc)`
- `void f(int&in subtype, const memory_buffer<T>&in other)`
- `void f(int&in subtype, uint64 ptr, uint64 size)`
- `void memory_buffer()`
- `void memory_buffer(int&in subtype, const memory_buffer<T>&in other)`
- `void memory_buffer(int&in subtype, uint64 ptr, uint64 size)`
##### Properties
- `uint64 address`
- `uint64 size`
##### Methods
- `array<T>@ opImplConv() const`
- `const T& opIndex(uint64 index) const`
- `int get_element_size() const property`
- `memory_buffer<T>& opAssign(array<T>@+ array)`
- `T& opIndex(uint64 index)`

### Class `memory_reader`
##### Behaviours / Constructors
- `memory_reader@ d(uint64 address, uint64 size, const string&in encoding = "", int byteorder = 1)`
- `memory_reader@ memory_reader()`
- `memory_reader@ memory_reader(uint64 address, uint64 size, const string&in encoding = "", int byteorder = 1)`
##### Properties
- `bool autoflush`
- `bool binary`
- `bool skip_eof`
- `bool sync_rw_cursors`
##### Methods
- `bool close(bool close_all = false)`
- `bool close_all()`
- `bool get_active() const property`
- `bool get_bad() const property`
- `bool get_eof() const property`
- `bool get_fail() const property`
- `bool get_good() const property`
- `bool open(uint64 address, uint64 size, const string&in encoding = "", int byteorder = 1)`
- `bool rseek(uint64 offset)`
- `bool rseek_end(uint64 offset = 0)`
- `bool rseek_relative(int64 offset)`
- `bool seek(uint64 offset)`
- `bool seek_end(uint64 offset = 0)`
- `bool seek_relative(int64 offset)`
- `bool wseek(uint64 offset)`
- `bool wseek_end(uint64 offset = 0)`
- `bool wseek_relative(int64 offset)`
- `datastream@ opImplCast()`
- `double read_double()`
- `float read_float()`
- `int read_int()`
- `int16 read_int16()`
- `int64 get_pos() const property`
- `int64 get_rpos() const property`
- `int64 get_wpos() const property`
- `int64 read_int64()`
- `int8 read_int8()`
- `memory_reader& opShl(double value)`
- `memory_reader& opShl(float value)`
- `memory_reader& opShl(int value)`
- `memory_reader& opShl(int16 value)`
- `memory_reader& opShl(int64 value)`
- `memory_reader& opShl(int8 value)`
- `memory_reader& opShl(string value)`
- `memory_reader& opShl(uint value)`
- `memory_reader& opShl(uint16 value)`
- `memory_reader& opShl(uint64 value)`
- `memory_reader& opShl(uint8 value)`
- `memory_reader& opShr(double&out value)`
- `memory_reader& opShr(float&out value)`
- `memory_reader& opShr(int&out value)`
- `memory_reader& opShr(int16&out value)`
- `memory_reader& opShr(int64&out value)`
- `memory_reader& opShr(int8&out value)`
- `memory_reader& opShr(string&out value)`
- `memory_reader& opShr(uint&out value)`
- `memory_reader& opShr(uint16&out value)`
- `memory_reader& opShr(uint64&out value)`
- `memory_reader& opShr(uint8&out value)`
- `memory_reader& write_double(double value)`
- `memory_reader& write_float(float value)`
- `memory_reader& write_int(int value)`
- `memory_reader& write_int16(int16 value)`
- `memory_reader& write_int64(int64 value)`
- `memory_reader& write_int8(int8 value)`
- `memory_reader& write_string(string value)`
- `memory_reader& write_uint(uint value)`
- `memory_reader& write_uint16(uint16 value)`
- `memory_reader& write_uint64(uint64 value)`
- `memory_reader& write_uint8(uint8 value)`
- `string read(uint count = 0)`
- `string read_line()`
- `string read_string()`
- `string read_until(const string&in text, bool require_full)`
- `uint read_uint()`
- `uint write(const string&in data)`
- `uint16 read_uint16()`
- `uint64 get_available() const property`
- `uint64 read_7bit_encoded()`
- `uint64 read_uint64()`
- `uint8 read_uint8()`
- `void flush()`
- `void read_7bit_encoded(uint64&out integer)`
- `void write_7bit_encoded(uint64 integer)`

### Class `memory_writer`
##### Behaviours / Constructors
- `memory_writer@ d(uint64 address, uint64 size, const string&in encoding = "", int byteorder = 1)`
- `memory_writer@ memory_writer()`
- `memory_writer@ memory_writer(uint64 address, uint64 size, const string&in encoding = "", int byteorder = 1)`
##### Properties
- `bool autoflush`
- `bool binary`
- `bool skip_eof`
- `bool sync_rw_cursors`
##### Methods
- `bool close(bool close_all = false)`
- `bool close_all()`
- `bool get_active() const property`
- `bool get_bad() const property`
- `bool get_eof() const property`
- `bool get_fail() const property`
- `bool get_good() const property`
- `bool open(uint64 address, uint64 size, const string&in encoding = "", int byteorder = 1)`
- `bool rseek(uint64 offset)`
- `bool rseek_end(uint64 offset = 0)`
- `bool rseek_relative(int64 offset)`
- `bool seek(uint64 offset)`
- `bool seek_end(uint64 offset = 0)`
- `bool seek_relative(int64 offset)`
- `bool wseek(uint64 offset)`
- `bool wseek_end(uint64 offset = 0)`
- `bool wseek_relative(int64 offset)`
- `datastream@ opImplCast()`
- `double read_double()`
- `float read_float()`
- `int read_int()`
- `int16 read_int16()`
- `int64 get_pos() const property`
- `int64 get_rpos() const property`
- `int64 get_wpos() const property`
- `int64 read_int64()`
- `int8 read_int8()`
- `memory_writer& opShl(double value)`
- `memory_writer& opShl(float value)`
- `memory_writer& opShl(int value)`
- `memory_writer& opShl(int16 value)`
- `memory_writer& opShl(int64 value)`
- `memory_writer& opShl(int8 value)`
- `memory_writer& opShl(string value)`
- `memory_writer& opShl(uint value)`
- `memory_writer& opShl(uint16 value)`
- `memory_writer& opShl(uint64 value)`
- `memory_writer& opShl(uint8 value)`
- `memory_writer& opShr(double&out value)`
- `memory_writer& opShr(float&out value)`
- `memory_writer& opShr(int&out value)`
- `memory_writer& opShr(int16&out value)`
- `memory_writer& opShr(int64&out value)`
- `memory_writer& opShr(int8&out value)`
- `memory_writer& opShr(string&out value)`
- `memory_writer& opShr(uint&out value)`
- `memory_writer& opShr(uint16&out value)`
- `memory_writer& opShr(uint64&out value)`
- `memory_writer& opShr(uint8&out value)`
- `memory_writer& write_double(double value)`
- `memory_writer& write_float(float value)`
- `memory_writer& write_int(int value)`
- `memory_writer& write_int16(int16 value)`
- `memory_writer& write_int64(int64 value)`
- `memory_writer& write_int8(int8 value)`
- `memory_writer& write_string(string value)`
- `memory_writer& write_uint(uint value)`
- `memory_writer& write_uint16(uint16 value)`
- `memory_writer& write_uint64(uint64 value)`
- `memory_writer& write_uint8(uint8 value)`
- `string read(uint count = 0)`
- `string read_line()`
- `string read_string()`
- `string read_until(const string&in text, bool require_full)`
- `uint read_uint()`
- `uint write(const string&in data)`
- `uint16 read_uint16()`
- `uint64 get_available() const property`
- `uint64 read_7bit_encoded()`
- `uint64 read_uint64()`
- `uint8 read_uint8()`
- `void flush()`
- `void read_7bit_encoded(uint64&out integer)`
- `void write_7bit_encoded(uint64 integer)`

### Class `microphone`
##### Behaviours / Constructors
- `microphone@ m(int device = -1, audio_engine@+ engine = sound_default_engine)`
- `microphone@ microphone(int device = -1, audio_engine@ engine = sound_default_engine)`
##### Methods
- `array<float>@ read(uint64 frame_count = 0)`
- `audio_data_source@ get_current() const property`
- `audio_data_source@ get_next() const property`
- `audio_data_source@ opImplCast()`
- `audio_node@ opImplCast()`
- `audio_node_state get_state()`
- `audio_node_state get_state_by_time(uint64 global_time)`
- `audio_node_state get_state_by_time_range(uint64 global_time_begin, uint64 global_time_end)`
- `audio_ring_buffer@ opImplCast()`
- `bool attach_output_bus(uint output_bus, audio_node@ destination, uint destination_input_bus)`
- `bool detach_all_output_buses()`
- `bool detach_output_bus(uint bus)`
- `bool get_active() const property`
- `bool get_looping() const property`
- `bool seek_frames(uint64 frame_index)`
- `bool seek_milliseconds(float ms)`
- `bool set_current(audio_data_source@ new_current)`
- `bool set_device(int device)`
- `bool set_loop_point(uint64 start_frame, uint64 end_frame)`
- `bool set_looping(bool looping)`
- `bool set_next(audio_data_source@ new_next)`
- `bool set_output_bus_volume(uint bus, float volume)`
- `bool set_range(uint64 start_frame, uint64 end_frame)`
- `bool set_state(audio_node_state state)`
- `bool set_state_time(audio_node_state state, uint64 time)`
- `bool set_time(uint64 local_time)`
- `float get_cursor_milliseconds() const property`
- `float get_length_milliseconds() const property`
- `float get_output_bus_volume(uint bus)`
- `float get_volume() const property`
- `float skip_milliseconds(float ms)`
- `int get_device() const property`
- `uint get_advised_read_frame_count() const property`
- `uint get_available_read() const property`
- `uint get_available_write() const property`
- `uint get_channels() const property`
- `uint get_input_bus_count() const property`
- `uint get_input_channels(uint bus) const`
- `uint get_output_bus_count() const property`
- `uint get_output_channels(uint bus) const`
- `uint get_sample_rate() const property`
- `uint write(const array<float>@ frames)`
- `uint write(const memory_buffer<float>&inout frames)`
- `uint64 get_cursor_frames() const property`
- `uint64 get_length_frames() const property`
- `uint64 get_state_time(audio_node_state state)`
- `uint64 get_time() const`
- `uint64 skip_frames(uint64 frame_count)`
- `void get_loop_point(uint64&out start_frame, uint64&out end_frame) const`
- `void get_range(uint64&out start_frame, uint64&out end_frame) const`
- `void reset()`
- `void set_volume(float volume)`

### Class `mixer`
##### Behaviours / Constructors
- `mixer@ m()`
- `mixer@ mixer()`
##### Methods
- `audio_engine@ get_engine() const property`
- `audio_node@ opImplCast()`
- `audio_node_chain@ get_effects_chain() property`
- `audio_node_chain@ get_internal_node_chain() property`
- `audio_node_state get_state()`
- `audio_node_state get_state_by_time(uint64 global_time)`
- `audio_node_state get_state_by_time_range(uint64 global_time_begin, uint64 global_time_end)`
- `audio_pan_mode get_pan_mode() const property`
- `audio_positioning_mode get_positioning() const property`
- `audio_splitter_node@ get_reverb3d_attachment() const property`
- `bool attach_output_bus(uint output_bus, audio_node@ destination, uint destination_input_bus)`
- `bool detach_all_output_buses()`
- `bool detach_output_bus(uint bus)`
- `bool get_hrtf() const property`
- `bool get_playing() const property`
- `bool get_spatialization_enabled() const property`
- `bool play(bool reset_loop_state = true)`
- `bool play_looped()`
- `bool set_mixer(mixer@ parent_mixer)`
- `bool set_output_bus_volume(uint bus, float volume)`
- `bool set_shape(ref shape)`
- `bool set_state(audio_node_state state)`
- `bool set_state_time(audio_node_state state, uint64 time)`
- `bool set_time(uint64 local_time)`
- `bool stop()`
- `float get_current_fade_volume() const property`
- `float get_directional_attenuation_factor() const property`
- `float get_distance_to_listener() const`
- `float get_doppler_factor() const property`
- `float get_max_distance() const property`
- `float get_max_gain() const property`
- `float get_min_distance() const property`
- `float get_min_gain() const property`
- `float get_output_bus_volume(uint bus)`
- `float get_pan() const property`
- `float get_pitch() const property`
- `float get_rolloff() const property`
- `float get_volume() const property`
- `int get_3d_attenuator() const property`
- `int get_3d_panner() const property`
- `int get_preferred_3d_attenuator() const property`
- `int get_preferred_3d_panner() const property`
- `mixer@ get_mixer() const`
- `ref get_shape() const property`
- `reverb3d@ get_reverb3d() const property`
- `reverb3d_placement get_reverb3d_placement() const property`
- `uint get_input_bus_count() const property`
- `uint get_input_channels(uint bus) const`
- `uint get_listener() const property`
- `uint get_output_bus_count() const property`
- `uint get_output_channels(uint bus) const`
- `uint get_pinned_listener() const property`
- `uint64 get_state_time(audio_node_state state)`
- `uint64 get_time() const`
- `vector get_direction() const`
- `vector get_direction_to_listener() const`
- `vector get_position_3d() const`
- `vector get_velocity() const`
- `void get_cone(float&out inner_radians, float&out outer_radians, float&out outer_gain)`
- `void set_3d_attenuator(int attenuator_id)`
- `void set_3d_panner(int panner_id)`
- `void set_cone(float inner_radians, float outer_radians, float outer_gain)`
- `void set_direction(const vector&in direction)`
- `void set_direction(float x, float y, float z)`
- `void set_directional_attenuation_factor(float factor) property`
- `void set_doppler_factor(float factor) property`
- `void set_fade(float start_volume, float end_volume, uint64 length)`
- `void set_fade_in_frames(float start_volume, float end_volume, uint64 length_frames)`
- `void set_fade_in_milliseconds(float start_volume, float end_volume, uint64 length_ms)`
- `void set_hrtf(bool enabled) property`
- `void set_max_distance(float distance) property`
- `void set_max_gain(float gain) property`
- `void set_min_distance(float distance) property`
- `void set_min_gain(float gain) property`
- `void set_pan(float pan) property`
- `void set_pan_mode(audio_pan_mode mode) property`
- `void set_pinned_listener(uint index) property`
- `void set_pitch(float pitch) property`
- `void set_position_3d(const vector&in position)`
- `void set_position_3d(float x, float y, float z)`
- `void set_positioning(audio_positioning_mode mode) property`
- `void set_reverb3d(reverb3d@ reverb) property`
- `void set_reverb3d_at(reverb3d@ reverb, reverb3d_placement placement)`
- `void set_rolloff(float rolloff) property`
- `void set_spatialization_enabled(bool enabled) property`
- `void set_start_time(uint64 absolute_time) property`
- `void set_stop_time(uint64 absolute_time)`
- `void set_velocity(const vector&in velocity)`
- `void set_velocity(float x, float y, float z)`
- `void set_volume(float volume) property`

### Class `mutex`
##### Behaviours / Constructors
- `mutex@ mutex()`
##### Methods
- `bool try_lock()`
- `bool try_lock(uint milliseconds)`
- `void lock()`
- `void lock(uint milliseconds)`
- `void unlock()`

### Class `mutex_lock`
##### Behaviours / Constructors
- `void mutex_lock()`
- `void mutex_lock(mutex@ target)`
- `void mutex_lock(mutex@ target, uint milliseconds)`
##### Methods
- `void unlock()`

### Class `name_value_collection`
##### Behaviours / Constructors
- `name_value_collection@ $list(int&in) { repeat { string, string } }`
- `name_value_collection@ name_value_collection()`
- `name_value_collection@ name_value_collection(const name_value_collection&in other)`
##### Methods
- `bool empty() const`
- `bool exists(const string&in name) const`
- `const string& get(const string&in name, const string&in default_value = "") const`
- `const string& get_opIndex(const string&in name) const property`
- `const string& name_at(uint index) const`
- `const string& value_at(uint index) const`
- `internet_message_header@ opCast()`
- `name_value_collection& opAssign(const name_value_collection&in other)`
- `uint64 size() const`
- `void add(const string&in name, const string&in value)`
- `void clear()`
- `void erase(const string&in name)`
- `void secure_erase(const string&in name)`
- `void set(const string&in name, const string&in value)`
- `void set_opIndex(const string&in name, const string&in value) property`

### Class `named_mutex`
##### Behaviours / Constructors
- `named_mutex@ named_mutex(const string&in name)`
##### Methods
- `bool try_lock()`
- `void lock()`
- `void unlock()`

### Class `named_mutex_lock`
##### Behaviours / Constructors
- `void named_mutex_lock()`
- `void named_mutex_lock(named_mutex@ target)`
##### Methods
- `void unlock()`

### Class `network`
##### Behaviours / Constructors
- `network @n()`
- `network@ network()`
##### Properties
- `bool IPV6enabled`
- `bool receive_timeout_event`
- `bool send_immediately`
##### Methods
- `bool disconnect_peer(uint64 peer_id)`
- `bool disconnect_peer_forcefully(uint64 peer_id)`
- `bool disconnect_peer_softly(uint64 peer_id)`
- `bool flush()`
- `bool get_active() const property`
- `bool get_packet_compression() const property`
- `bool send(uint64 peer_id, const string& in message, uint8 channel, bool reliable = true)`
- `bool send_peer(uint64 peer_pointer, const string& in message, uint8 channel, bool reliable = true)`
- `bool send_reliable(uint64 peer_id, const string& in message, uint8 channel)`
- `bool send_reliable_peer(uint64 peer_pointer, const string& in message, uint8 channel)`
- `bool send_unreliable(uint64 peer_id, const string& in message, uint8 channel)`
- `bool send_unreliable_peer(uint64 peer_pointer, const string& in message, uint8 channel)`
- `bool setup_client(uint8 max_channels, uint16 max_peers)`
- `bool setup_local_server(uint16 port, uint8 max_channels, uint16 max_peers)`
- `bool setup_server(uint16 port, uint8 max_channels, uint16 max_peers)`
- `const network_event@ request(uint timeout = 0)`
- `string get_peer_address(uint64 peer_id) const`
- `uint get_bytes_received() const property`
- `uint get_bytes_sent() const property`
- `uint get_duplicate_peers() const property`
- `uint get_packets_received() const property`
- `uint get_packets_sent() const property`
- `uint get_peer_average_round_trip_time(uint64 peer_id) const`
- `uint64 connect(const string& in host, uint16 port)`
- `uint64 get_connected_peers() const property`
- `uint64[]@ get_peer_list() const`
- `void destroy(bool flush = true)`
- `void set_bandwidth_limits(uint max_incoming_bytes_per_second, uint max_outgoing_bytes_per_second)`
- `void set_duplicate_peers(uint max_duplicates) property`
- `void set_packet_compression(bool compressed) property`

### Class `network_event`
##### Behaviours / Constructors
- `network_event @e()`
- `network_event@ network_event()`
##### Properties
- `const network_event_type type`
- `const string message`
- `const uint channel`
- `const uint64 peer_id`
##### Methods
- `network_event& opAssign(const network_event &in other)`
- `network_event& opAssign(const network_event&in other)`

### Class `pack_file`
##### Behaviours / Constructors
- `pack_file@ a()`
- `pack_file@ pack_file()`
##### Methods
- `bool add_file(const string &in filename, const string &in internal_name)`
- `bool add_file(const string&in filename, const string&in internal_name)`
- `bool add_memory(const string &in internal_name, const string&in data)`
- `bool add_memory(const string&in internal_name, const string&in data)`
- `bool add_stream(const string &in internal_name, datastream@+ ds)`
- `bool add_stream(const string&in internal_name, datastream@ ds)`
- `bool close()`
- `bool create(const string &in filename, const string&in key = "")`
- `bool create(const string&in filename, const string&in key = "")`
- `bool extract_file(const string &in internal_name, const string &in file_on_disk)`
- `bool extract_file(const string&in internal_name, const string&in file_on_disk)`
- `bool file_exists(const string &in filename)`
- `bool file_exists(const string&in filename)`
- `bool get_active() const property`
- `bool open(const string &in filename, const string &in key = "", uint64 pack_offset = 0, uint64 pack_size = 0)`
- `bool open(const string&in filename, const string&in key = "", uint64 pack_offset = 0, uint64 pack_size = 0)`
- `datastream @get_file(const string &in filename, const string &in encoding = "", int byteorder = STREAM_BYTE_ORDER_NATIVE)`
- `datastream@ get_file(const string&in filename, const string&in encoding = "", int byteorder = STREAM_BYTE_ORDER_NATIVE)`
- `int64 get_file_count() const property`
- `int64 get_file_size(const string &in filename)`
- `int64 get_file_size(const string&in filename)`
- `pack_interface@ opImplCast()`
- `string get_pack_name() const property`
- `string[]@ list_files() const`

### Class `pack_interface`
##### Methods
- `pack_file@ opCast()`

### Class `path`
##### Behaviours / Constructors
- `void f()`
- `void f(bool absolute)`
- `void f(const path&in other)`
- `void f(const path&in parent, const path&in relative)`
- `void f(const path&in parent, const string&in filename)`
- `void f(const string&in path)`
- `void f(const string&in path, path_style style)`
- `void path()`
- `void path(bool absolute)`
- `void path(const spec::path&in other)`
- `void path(const spec::path&in parent, const spec::path&in relative)`
- `void path(const spec::path&in parent, const string&in filename)`
- `void path(const string&in path)`
- `void path(const string&in path, spec::path_style style)`
##### Methods
- `bool get_is_absolute() const property`
- `bool get_is_directory() const property`
- `bool get_is_file() const property`
- `bool get_is_relative() const property`
- `bool parse(const string&in path)`
- `bool parse(const string&in path, path_style style)`
- `bool parse(const string&in path, spec::path_style style)`
- `const string& get_device() const property`
- `const string& get_filename() const property`
- `const string& get_node() const property`
- `const string& get_opIndex(int directory_level) const property`
- `const string& get_vms_version() const property`
- `int get_depth() const property`
- `path absolute() const`
- `path absolute(const path&in base) const`
- `path get_parent() const property`
- `path opDiv(const path&in append) const`
- `path opDiv(const string&in append) const`
- `path& append(const path&in path)`
- `path& assign(const path&in other)`
- `path& assign(const string&in path)`
- `path& assign(const string&in path, path_style style)`
- `path& assign_directory(const string&in directory)`
- `path& assign_directory(const string&in directory, path_style style)`
- `path& clear()`
- `path& make_absolute()`
- `path& make_absolute(const path&in base)`
- `path& make_directory()`
- `path& make_file()`
- `path& make_parent()`
- `path& opAssign(const path&in other)`
- `path& opAssign(const string&in path)`
- `path& pop_directory()`
- `path& pop_front_directory()`
- `path& push_directory(const string&in directory_name)`
- `path& resolve(const path&in path)`
- `path& set_basename(const string&in basename)`
- `path& set_device(const string&in device)`
- `path& set_extension(const string&in extension)`
- `path& set_filename(const string&in filename)`
- `path& set_node(const string&in node)`
- `spec::path absolute() const`
- `spec::path absolute(const spec::path&in base) const`
- `spec::path get_parent() const property`
- `spec::path opDiv(const spec::path&in append) const`
- `spec::path opDiv(const string&in append) const`
- `spec::path& append(const spec::path&in path)`
- `spec::path& assign(const spec::path&in other)`
- `spec::path& assign(const string&in path)`
- `spec::path& assign(const string&in path, spec::path_style style)`
- `spec::path& assign_directory(const string&in directory)`
- `spec::path& assign_directory(const string&in directory, spec::path_style style)`
- `spec::path& clear()`
- `spec::path& make_absolute()`
- `spec::path& make_absolute(const spec::path&in base)`
- `spec::path& make_directory()`
- `spec::path& make_file()`
- `spec::path& make_parent()`
- `spec::path& opAssign(const spec::path&in other)`
- `spec::path& opAssign(const string&in path)`
- `spec::path& pop_directory()`
- `spec::path& pop_front_directory()`
- `spec::path& push_directory(const string&in directory_name)`
- `spec::path& resolve(const spec::path&in path)`
- `spec::path& set_basename(const string&in basename)`
- `spec::path& set_device(const string&in device)`
- `spec::path& set_extension(const string&in extension)`
- `spec::path& set_filename(const string&in filename)`
- `spec::path& set_node(const string&in node)`
- `string get_basename() const property`
- `string get_extension() const property`
- `string opImplConv() const`
- `string to_string(path_style style = spec::PATH_STYLE_NATIVE) const`
- `string to_string(spec::path_style style = spec::PATH_STYLE_NATIVE) const`

### Class `pathfinder`
##### Behaviours / Constructors
- `bool f()`
- `int f()`
- `pathfinder @p(int size = 1024, bool cache = true)`
- `pathfinder@ pathfinder(int size = 1024, bool cache = true)`
- `void f()`
- `void f(int&in)`
##### Properties
- `bool allow_diagonals`
- `bool automatic_reset`
- `const bool solving`
- `const float total_cost`
- `int search_range`
##### Methods
- `int get_desperation_factor() const property`
- `vector[]@ find(int start_x, int start_y, int end_x, int end_y, string user_data = "")`
- `vector[]@ find(int start_x, int start_y, int start_z, int end_x, int end_y, int end_z, any@+ callback_data = null)`
- `void cancel()`
- `void reset()`
- `void set_callback_function(pathfinder_callback@ callback)`
- `void set_callback_function(pathfinder_callback_ex@ callback)`
- `void set_callback_function(pathfinder_callback_legacy@ callback)`
- `void set_desperation_factor(int factor) property`

### Class `phonon_binaural_node`
##### Behaviours / Constructors
- `phonon_binaural_node@ n(audio_engine@+ engine, int channels, int sample_rate, int frame_size = 0)`
- `phonon_binaural_node@ phonon_binaural_node(audio_engine@ engine, int channels, int sample_rate, int frame_size = 0)`
##### Methods
- `audio_node@ opImplCast()`
- `audio_node_state get_state()`
- `audio_node_state get_state_by_time(uint64 global_time)`
- `audio_node_state get_state_by_time_range(uint64 global_time_begin, uint64 global_time_end)`
- `bool attach_output_bus(uint output_bus, audio_node@ destination, uint destination_input_bus)`
- `bool detach_all_output_buses()`
- `bool detach_output_bus(uint bus)`
- `bool set_output_bus_volume(uint bus, float volume)`
- `bool set_state(audio_node_state state)`
- `bool set_state_time(audio_node_state state, uint64 time)`
- `bool set_time(uint64 local_time)`
- `float get_output_bus_volume(uint bus)`
- `uint get_input_bus_count() const property`
- `uint get_input_channels(uint bus) const`
- `uint get_output_bus_count() const property`
- `uint get_output_channels(uint bus) const`
- `uint64 get_state_time(audio_node_state state)`
- `uint64 get_time() const`
- `void set_direction(const vector&in direction, float distance)`
- `void set_direction(float x, float y, float z, float distance)`
- `void set_spatial_blend_max_distance(float max_distance)`

### Class `physics_body`
##### Methods
- `aabb get_aabb() const property`
- `any@ get_user_data() const`
- `bool get_is_active() const property`
- `bool get_is_debug_enabled() const property`
- `bool raycast(const ray&inout point, raycast_info&inout raycast_info) const`
- `bool test_aabb_overlap(const aabb&in world_aabb) const`
- `bool test_point_inside(const vector&in point) const`
- `const physics_collider& get_collider(uint index) const`
- `const physics_transform& get_transform() const property`
- `physics_collider& get_collider(uint index)`
- `physics_collider@ add_collider(physics_collision_shape@ shape, const physics_transform&in transform)`
- `physics_entity get_entity() const property`
- `uint get_nb_colliders() const property`
- `vector get_local_point(const vector&in world_point) const`
- `vector get_local_vector(const vector&in world_vector) const`
- `vector get_world_point(const vector&in local_point) const`
- `vector get_world_vector(const vector&in local_vector) const`
- `void remove_collider(physics_collider&in collider)`
- `void set_debug_enabled(bool enabled) property`
- `void set_is_active(bool is_active) property`
- `void set_transform(const physics_transform&in transform) property`
- `void set_user_data(any@ userData)`

### Class `physics_box_shape`
##### Behaviours / Constructors
- `physics_box_shape@ f(const vector&in half_extents)`
- `physics_box_shape@ physics_box_shape(const vector&in half_extents)`
##### Methods
- `aabb compute_transformed_aabb(const physics_transform&in transform) const`
- `aabb get_local_bounds() const`
- `bool get_is_convex() const property`
- `bool get_is_polyhedron() const property`
- `const physics_collision_shape@ opImplCast() const`
- `const physics_half_edge_structure_edge& get_half_edge(uint edge_index) const`
- `const physics_half_edge_structure_face& get_face(uint face_index)`
- `const physics_half_edge_structure_vertex& get_vertex(uint vertex_index)`
- `const vector get_face_normal(uint vertex_index)`
- `const vector get_vertex_position(uint vertex_index)`
- `float get_margin() const property`
- `float get_volume() const property`
- `int get_id() const property`
- `physics_collision_shape@ opImplCast()`
- `physics_shape_name get_name() const property`
- `physics_shape_type get_type() const property`
- `string opImplConv() const`
- `uint find_most_anti_parallel_face(const vector&in direction) const`
- `uint get_nb_faces() const property`
- `uint get_nb_half_edges() const property`
- `uint get_nb_vertices() const property`
- `vector get_centroid() const property`
- `vector get_local_inertia_tensor(float mass) const`
- `vector& get_half_extents() const property`
- `void set_half_extents(const vector&in half_extents) property`

### Class `physics_capsule_shape`
##### Behaviours / Constructors
- `physics_capsule_shape@ f(float radius, float height)`
- `physics_capsule_shape@ physics_capsule_shape(float radius, float height)`
##### Methods
- `aabb compute_transformed_aabb(const physics_transform&in transform) const`
- `aabb get_local_bounds() const`
- `bool get_is_convex() const property`
- `bool get_is_polyhedron() const property`
- `const physics_collision_shape@ opImplCast() const`
- `float get_height() const property`
- `float get_margin() const property`
- `float get_radius() const property`
- `float get_volume() const property`
- `int get_id() const property`
- `physics_collision_shape@ opImplCast()`
- `physics_shape_name get_name() const property`
- `physics_shape_type get_type() const property`
- `string opImplConv()`
- `string opImplConv() const`
- `vector get_local_inertia_tensor(float mass) const`
- `void set_height(float height) property`
- `void set_radius(float radius) property`

### Class `physics_collider`
##### Methods
- `bool get_is_simulation_collider() const property`
- `bool get_is_trigger() const property`
- `bool get_is_world_query_collider() const property`
- `bool raycast(const ray&in ray, raycast_info& raycast_info)`
- `bool raycast(const ray&in ray, raycast_info&inout raycast_info)`
- `bool test_aabb_overlap(const aabb&in world_aabb) const`
- `bool test_point_inside(const vector&in world_point)`
- `const aabb get_world_aabb() const property`
- `const physics_collision_shape@ get_collision_shape() const property`
- `const physics_transform get_local_to_world_transform() const`
- `const physics_transform& get_local_to_body_transform() const property`
- `physics_body@ get_body() const property`
- `physics_collision_shape@ get_collision_shape() property`
- `physics_entity get_entity() const property`
- `physics_material& get_material() property`
- `uint16 get_broad_phase_id() const property`
- `uint16 get_collide_with_mask() const property`
- `uint16 get_collision_category() const property`
- `void set_collide_with_mask(uint16 bits) property`
- `void set_collision_category(uint16 bits) property`
- `void set_is_simulation_collider(bool is_simulation_collider) property`
- `void set_is_trigger(bool is_trigger) property`
- `void set_is_world_query_collider(bool is_world_query_collider) property`
- `void set_local_to_body_transform(const physics_transform&in transform) property`
- `void set_material(const physics_material&in material) property`

### Class `physics_collision_callback_data`
##### Methods
- `physics_contact_pair get_contact_pair(uint64 index) const`
- `uint get_nb_contact_pairs() const property`

### Class `physics_collision_shape`
##### Methods
- `aabb compute_transformed_aabb(const physics_transform&in transform) const`
- `aabb get_local_bounds() const`
- `bool get_is_convex() const property`
- `bool get_is_polyhedron() const property`
- `float get_volume() const property`
- `int get_id() const property`
- `physics_shape_name get_name() const property`
- `physics_shape_type get_type() const property`
- `string opImplConv() const`
- `vector get_local_inertia_tensor(float mass) const`

### Class `physics_concave_mesh_shape`
##### Behaviours / Constructors
- `physics_concave_mesh_shape@ f(physics_triangle_mesh@ triangle_mesh, const vector&in scaling = vector(1,1,1))`
- `physics_concave_mesh_shape@ physics_concave_mesh_shape(physics_triangle_mesh@ triangle_mesh, const vector&in scaling = vector(1,1,1))`
##### Methods
- `aabb compute_transformed_aabb(const physics_transform&in transform) const`
- `aabb get_local_bounds() const`
- `bool get_is_convex() const property`
- `bool get_is_polyhedron() const property`
- `const physics_collision_shape@ opImplCast() const`
- `const vector& get_vertex_normal(uint vertex_index) const`
- `float get_volume() const property`
- `int get_id() const property`
- `physics_collision_shape@ opImplCast()`
- `physics_shape_name get_name() const property`
- `physics_shape_type get_type() const property`
- `physics_triangle_raycast_side get_raycast_test_type() const property`
- `string opImplConv() const`
- `uint get_nb_triangles() const property`
- `uint get_nb_vertices() const property`
- `vector get_local_inertia_tensor(float mass) const`
- `vector get_scale() const property`
- `vector get_vertex(uint vertex_index) const`
- `void get_triangle_vertices(uint triangle_index, vector&out v1, vector&out v2, vector&out v3) const`
- `void get_triangle_vertices_indices(uint triangle_index, uint&out v1_index, uint&out v2_index, uint&out v3_index) const`
- `void get_triangle_vertices_normals(uint triangle_index, vector&out n1, vector&out n2, vector&out n3) const`
- `void set_raycast_test_type(physics_triangle_raycast_side side) property`
- `void set_scale(const vector&in scale) property`

### Class `physics_contact_pair`
##### Behaviours / Constructors
- `void f(const physics_contact_pair&in pair)`
- `void physics_contact_pair()`
- `void physics_contact_pair(const physics_contact_pair&in pair)`
##### Methods
- `physics_body@ get_body1() const property`
- `physics_body@ get_body2() const property`
- `physics_collider@ get_collider1() const property`
- `physics_collider@ get_collider2() const property`
- `physics_contact_event_type get_event_type() const property`
- `physics_contact_point@ get_contact_point(uint index) const`
- `uint get_nb_contact_points() const property`

### Class `physics_contact_point`
##### Methods
- `const vector& get_local_point_on_collider1() const property`
- `const vector& get_local_point_on_collider2() const property`
- `const vector& get_world_normal() const property`

### Class `physics_convex_mesh`
##### Methods
- `const aabb& get_bounds() const property`
- `const physics_half_edge_structure& get_half_edge_structure() const property`
- `const vector& get_centroid() const property`
- `const vector& get_face_normal(uint index) const`
- `const vector& get_vertex(uint index) const`
- `float get_volume() const property`
- `uint get_nb_faces() const property`
- `uint get_nb_vertices() const property`
- `vector get_local_inertia_tensor(float mass, vector scale) const`

### Class `physics_convex_mesh_shape`
##### Behaviours / Constructors
- `physics_convex_mesh_shape@ f(physics_convex_mesh@ convex_mesh, const vector&in scaling = vector(1,1,1))`
- `physics_convex_mesh_shape@ physics_convex_mesh_shape(physics_convex_mesh@ convex_mesh, const vector&in scaling = vector(1,1,1))`
##### Methods
- `aabb compute_transformed_aabb(const physics_transform&in transform) const`
- `aabb get_local_bounds() const`
- `bool get_is_convex() const property`
- `bool get_is_polyhedron() const property`
- `const physics_collision_shape@ opImplCast() const`
- `const physics_half_edge_structure_edge& get_half_edge(uint edge_index) const`
- `const physics_half_edge_structure_face& get_face(uint face_index)`
- `const physics_half_edge_structure_vertex& get_vertex(uint vertex_index)`
- `const vector get_face_normal(uint vertex_index)`
- `const vector get_vertex_position(uint vertex_index)`
- `float get_margin() const property`
- `float get_volume() const property`
- `int get_id() const property`
- `physics_collision_shape@ opImplCast()`
- `physics_shape_name get_name() const property`
- `physics_shape_type get_type() const property`
- `string opImplConv() const`
- `uint find_most_anti_parallel_face(const vector&in direction) const`
- `uint get_nb_faces() const property`
- `uint get_nb_half_edges() const property`
- `uint get_nb_vertices() const property`
- `vector get_centroid() const property`
- `vector get_local_inertia_tensor(float mass) const`
- `vector& get_scale() const property`
- `void set_scale(vector& scale) const property`
- `void set_scale(vector&inout scale) const property`

### Class `physics_default_logger`
##### Methods
- `const physics_logger@ opImplCast() const`
- `physics_logger@ opImplCast()`
- `void add_file_destination(const string&in filePath, uint logLevelFlag, physics_logger_format format)`
- `void remove_all_destinations()`

### Class `physics_entity`
##### Behaviours / Constructors
- `void f(uint index, uint generation)`
- `void physics_entity()`
- `void physics_entity(uint index, uint generation)`
##### Properties
- `uint id`
##### Methods
- `bool opEquals(const physics_entity&in entity) const`
- `uint get_generation() const property`
- `uint get_index() const property`

### Class `physics_half_edge_structure`
##### Methods
- `const physics_half_edge_structure_face& get_face(uint index) const property`
- `uint add_vertex(uint vertex_point_index)`
- `uint get_nb_faces() const property`
- `uint get_nb_half_edges() const property`
- `uint get_nb_vertices() const property`
- `void compute_half_edges()`

### Class `physics_half_edge_structure_edge`
##### Behaviours / Constructors
- `void f()`
- `void physics_half_edge_structure_edge()`
##### Properties
- `uint face_index`
- `uint next_edge_index`
- `uint twin_edge_index`
- `uint vertex_index`

### Class `physics_half_edge_structure_face`
##### Methods
- `uint[]@ get_face_vertices() const`
- `void set_face_vertices(uint[]@ face_vertices)`

### Class `physics_half_edge_structure_vertex`
##### Behaviours / Constructors
- `void f(uint vertex_coords_index)`
- `void physics_half_edge_structure_vertex()`
- `void physics_half_edge_structure_vertex(uint vertex_coords_index)`
##### Properties
- `uint vertex_edge_index`
- `uint vertex_point_index`

### Class `physics_height_field`
##### Methods
- `aabb& get_bounds() const property`
- `float get_height_at(uint x, uint y) const`
- `float get_integer_height_scale() const property`
- `float get_max_height() const property`
- `float get_min_height() const property`
- `physics_height_data_type get_height_data_type() const property`
- `string opImplConv() const`
- `uint get_nb_columns() const property`
- `uint get_nb_rows() const property`
- `vector get_vertex_at(uint x, uint y) const`

### Class `physics_height_field_shape`
##### Behaviours / Constructors
- `physics_height_field_shape@ f(physics_height_field@ height_field, const vector&in scaling = vector(1,1,1))`
- `physics_height_field_shape@ physics_height_field_shape(physics_height_field@ height_field, const vector&in scaling = vector(1,1,1))`
##### Methods
- `aabb compute_transformed_aabb(const physics_transform&in transform) const`
- `aabb get_local_bounds() const`
- `bool get_is_convex() const property`
- `bool get_is_polyhedron() const property`
- `const physics_collision_shape@ opImplCast() const`
- `float get_volume() const property`
- `int get_id() const property`
- `physics_collision_shape@ opImplCast()`
- `physics_height_field@ get_height_field() const property`
- `physics_shape_name get_name() const property`
- `physics_shape_type get_type() const property`
- `physics_triangle_raycast_side get_raycast_test_type() const property`
- `string opImplConv() const`
- `vector get_local_inertia_tensor(float mass) const`
- `vector get_scale() const property`
- `vector get_vertex_at(uint x, uint y) const`
- `void set_raycast_test_type(physics_triangle_raycast_side side) property`
- `void set_scale(const vector&in scale) property`

### Class `physics_joint`
##### Methods
- `bool get_is_collision_enabled() const property`
- `physics_entity get_entity() const property`
- `physics_joint_type get_type() const property`
- `physics_rigid_body@ get_body1() const property`
- `physics_rigid_body@ get_body2() const property`
- `string opImplConv()`
- `vector get_reaction_force(float time_step) const`
- `vector get_reaction_torque(float time_step) const`

### Class `physics_joint_info`
##### Behaviours / Constructors
- `void f(physics_rigid_body@ body1, physics_rigid_body@ body2, physics_joint_type constraint_type)`
- `void physics_joint_info()`
- `void physics_joint_info(physics_rigid_body@ body1, physics_rigid_body@ body2, physics_joint_type constraint_type)`
##### Properties
- `bool isCollisionEnabled`
- `physics_joint_type type`
- `physics_joints_position_correction_technique position_correction_technique`
- `physics_rigid_body@ body1`
- `physics_rigid_body@ body2`

### Class `physics_logger`
##### Methods
- `void log(physics_logger_level level, const string&in worldName, physics_logger_category category, const string&in message)`

### Class `physics_material`
##### Methods
- `float get_bounciness() const property`
- `float get_friction_coefficient() const property`
- `float get_friction_coefficient_sqrt() const property`
- `float get_mass_density() const property`
- `string opImplConv()`
- `void set_bounciness(float bounciness) property`
- `void set_friction_coefficient(float friction_coefficient) property`
- `void set_mass_density(float mass_density) property`

### Class `physics_message`
##### Behaviours / Constructors
- `void f(string text, physics_message_type type = PHYSICS_MESSAGE_ERROR)`
- `void physics_message()`
- `void physics_message(string text, physics_message_type type = PHYSICS_MESSAGE_ERROR)`
##### Properties
- `physics_message_type type`
- `string text`

### Class `physics_overlap_callback_data`
##### Methods
- `physics_overlap_pair get_overlapping_pair(uint index) const`
- `uint get_nb_overlap_pairs() const property`

### Class `physics_overlap_pair`
##### Behaviours / Constructors
- `void f(const physics_overlap_pair&in pair)`
- `void physics_overlap_pair()`
- `void physics_overlap_pair(const physics_overlap_pair&in pair)`
##### Methods
- `physics_body& get_body1() const property`
- `physics_body& get_body2() const property`
- `physics_collider& get_collider1() const property`
- `physics_collider& get_collider2() const property`
- `physics_overlap_event_type get_event_type() const property`

### Class `physics_polygon_data`
##### Behaviours / Constructors
- `physics_polygon_data@ f(float[]@ vertices, array<array<uint>>@ faces)`
- `physics_polygon_data@ physics_polygon_data(array<float>@ vertices, array<array<uint>>@ faces)`

### Class `physics_polygon_face`
##### Properties
- `uint index_base`
- `uint nb_vertices`

### Class `physics_polygon_vertex_array`
##### Methods
- `physics_polygon_face@ get_polygon_face(uint face_index) const`
- `physics_polygon_index_data_type get_index_data_type() const property`
- `physics_polygon_vertex_data_type get_vertex_data_type() const property`
- `uint get_indices_stride() const property`
- `uint get_nb_faces() const property`
- `uint get_nb_vertices() const property`
- `uint get_vertex_index_in_face(uint face_index, uint vertex_in_face) const`
- `uint get_vertices_stride() const property`
- `vector get_vertex(uint vertex_index) const`

### Class `physics_rigid_body`
##### Methods
- `aabb get_aabb() const property`
- `any@ get_user_data() const`
- `bool get_is_active() const property`
- `bool get_is_debug_enabled() const property`
- `bool get_is_gravity_enabled() const property`
- `bool raycast(const ray&inout point, raycast_info&inout raycast_info) const`
- `bool test_aabb_overlap(const aabb&in world_aabb) const`
- `bool test_point_inside(const vector&in point) const`
- `const physics_body@ opImplCast() const`
- `const physics_collider& get_collider(uint index) const`
- `const physics_transform& get_transform() const property`
- `const vector& get_angular_lock_axis_factor() const property`
- `const vector& get_linear_lock_axis_factor() const property`
- `const vector& get_local_center_of_mass() const property`
- `const vector& get_local_inertia_tensor() const property`
- `float get_angular_damping() const property`
- `float get_linear_damping() const property`
- `float get_mass() const property`
- `physics_body@ opImplCast()`
- `physics_body_type get_type() const property`
- `physics_collider& get_collider(uint index)`
- `physics_collider@ add_collider(physics_collision_shape@ shape, const physics_transform&in transform)`
- `physics_entity get_entity() const property`
- `uint get_nb_colliders() const property`
- `vector get_angular_velocity() const property`
- `vector get_linear_velocity() const property`
- `vector get_local_point(const vector&in world_point) const`
- `vector get_local_vector(const vector&in world_vector) const`
- `vector get_world_point(const vector&in local_point) const`
- `vector get_world_vector(const vector&in local_vector) const`
- `void remove_collider(physics_collider&in collider)`
- `void set_angular_damping(float angular_damping) property`
- `void set_angular_lock_axis_factor(const vector&in angular_lock_axis_factor) property`
- `void set_angular_velocity(const vector&in angular_velocity) property`
- `void set_debug_enabled(bool enabled) property`
- `void set_is_active(bool is_active) property`
- `void set_is_gravity_enabled(bool enabled) property`
- `void set_is_sleeping(bool enabled)`
- `void set_linear_damping(float linear_damping) property`
- `void set_linear_lock_axis_factor(const vector&in linear_lock_axis_factor) property`
- `void set_linear_velocity(const vector&in linear_velocity) property`
- `void set_local_center_of_mass(const vector&in local_center_of_mass) property`
- `void set_local_inertia_tensor(const vector&in local_inertia_tensor) property`
- `void set_mass(float mass) property`
- `void set_transform(const physics_transform&in transform) property`
- `void set_type(physics_body_type type) property`
- `void set_user_data(any@ userData)`
- `void update_local_center_of_mass_from_colliders()`
- `void update_local_inertia_tensor_from_colliders()`
- `void update_mass_from_colliders()`
- `void update_mass_properties_from_colliders()`

### Class `physics_sphere_shape`
##### Behaviours / Constructors
- `physics_sphere_shape@ f(float radius)`
- `physics_sphere_shape@ physics_sphere_shape(float radius)`
##### Methods
- `aabb compute_transformed_aabb(const physics_transform&in transform) const`
- `aabb get_local_bounds() const`
- `bool get_is_convex() const property`
- `bool get_is_polyhedron() const property`
- `const physics_collision_shape@ opImplCast() const`
- `float get_margin() const property`
- `float get_radius() const property`
- `float get_volume() const property`
- `int get_id() const property`
- `physics_collision_shape@ opImplCast()`
- `physics_shape_name get_name() const property`
- `physics_shape_type get_type() const property`
- `string opImplConv()`
- `string opImplConv() const`
- `vector get_local_inertia_tensor(float mass) const`
- `void set_radius(float radius) property`

### Class `physics_transform`
##### Behaviours / Constructors
- `void f()`
- `void f(const vector&in position, const matrix3x3&in orientation)`
- `void f(const vector&in position, const quaternion&in orientation)`
- `void physics_transform()`
- `void physics_transform(const vector&in position, const matrix3x3&in orientation)`
- `void physics_transform(const vector&in position, const quaternion&in orientation)`
##### Methods
- `bool get_is_valid() const property`
- `bool opEquals(const physics_transform&in) const`
- `const quaternion& get_orientation() const property`
- `const vector& get_position() const property`
- `float[]@ get_opengl_matrix() const`
- `physics_transform get_inverse() const property`
- `physics_transform opMul(const physics_transform&in) const`
- `string opImplConv()`
- `vector opMul(const vector&in) const`
- `void set_from_opengl_matrix(float[]@ matrix)`
- `void set_orientation(const quaternion&in orientation) property`
- `void set_position(const vector&in position) property`
- `void set_to_identity()`

### Class `physics_triangle_data`
##### Behaviours / Constructors
- `physics_triangle_data@ f(float[]@ vertices, float[]@ normals, uint[]@ indices)`
- `physics_triangle_data@ f(float[]@ vertices, uint[]@ indices)`
- `physics_triangle_data@ physics_triangle_data(array<float>@ vertices, array<float>@ normals, array<uint>@ indices)`
- `physics_triangle_data@ physics_triangle_data(array<float>@ vertices, array<uint>@ indices)`

### Class `physics_triangle_mesh`
##### Methods
- `const aabb& get_bounds() const property`
- `const vector& get_vertex(uint vertex_index) const`
- `const vector& get_vertex_normal(uint vertex_index) const`
- `uint get_nb_triangles() const property`
- `uint get_nb_vertices() const property`
- `void get_triangle_vertices(uint triangle_index, vector&out v1, vector&out v2, vector&out v3) const`
- `void get_triangle_vertices_indices(uint triangle_index, uint&out v1_index, uint&out v2_index, uint&out v3_index) const`
- `void get_triangle_vertices_normals(uint triangle_index, vector&out n1, vector&out n2, vector&out n3) const`

### Class `physics_triangle_shape`
##### Methods
- `aabb compute_transformed_aabb(const physics_transform&in transform) const`
- `aabb get_local_bounds() const`
- `bool get_is_convex() const property`
- `bool get_is_polyhedron() const property`
- `const physics_collision_shape@ opImplCast() const`
- `const physics_half_edge_structure_edge& get_half_edge(uint edge_index) const`
- `const physics_half_edge_structure_face& get_face(uint face_index)`
- `const physics_half_edge_structure_vertex& get_vertex(uint vertex_index)`
- `const vector get_face_normal(uint vertex_index)`
- `const vector get_vertex_position(uint vertex_index)`
- `float get_margin() const property`
- `float get_volume() const property`
- `int get_id() const property`
- `physics_collision_shape@ opImplCast()`
- `physics_shape_name get_name() const property`
- `physics_shape_type get_type() const property`
- `physics_triangle_raycast_side get_raycast_test_type() const property`
- `string opImplConv() const`
- `uint find_most_anti_parallel_face(const vector&in direction) const`
- `uint get_nb_faces() const property`
- `uint get_nb_half_edges() const property`
- `uint get_nb_vertices() const property`
- `vector get_centroid() const property`
- `vector get_local_inertia_tensor(float mass) const`
- `void set_raycast_test_type(physics_triangle_raycast_side test_type) property`

### Class `physics_triangle_vertex_array`
##### Methods
- `bool get_has_normals() const property`
- `physics_triangle_index_data_type get_index_data_type() const property`
- `physics_triangle_normal_data_type get_vertex_normal_data_type() const property`
- `physics_triangle_vertex_data_type get_vertex_data_type() const property`
- `uint get_indices_stride() const property`
- `uint get_nb_triangles() const property`
- `uint get_nb_vertices() const property`
- `uint get_vertices_normals_stride() const property`
- `uint get_vertices_stride() const property`
- `vector get_vertex(uint vertex_index) const`
- `vector get_vertex_normal(uint vertex_index) const`
- `void get_triangle_vertices_indices(uint triangle_index, uint&out v1_index, uint&out v2_index, uint&out v3_index) const`

### Class `physics_vertex_array`
##### Methods
- `physics_vertex_data_type get_data_type() const property`
- `uint get_nb_vertices() const property`
- `uint get_stride() const property`
- `vector get_vertex(uint index) const`

### Class `physics_vertex_data`
##### Behaviours / Constructors
- `physics_vertex_data@ f(float[]@ vertices)`
- `physics_vertex_data@ physics_vertex_data(array<float>@ vertices)`

### Class `physics_world`
##### Behaviours / Constructors
- `physics_world@ physics_world(const physics_world_settings&in world_settings)`
- `physics_world@ w(const physics_world_settings&in world_settings)`
##### Methods
- `aabb get_world_aabb(const physics_collider@ collider) const`
- `bool get_is_gravity_enabled() const property`
- `bool get_is_sleeping_enabled() const property`
- `bool test_overlap(physics_body@ body1, physics_body@ body2)`
- `const physics_rigid_body& get_rigid_body(uint index) const`
- `const string& get_name() const property`
- `float get_sleep_angular_velocity() const property`
- `float get_sleep_linear_velocity() const property`
- `float get_time_before_sleep() const property`
- `physics_joint@ create_joint(const physics_joint_info&in joint_info)`
- `physics_rigid_body& get_rigid_body(uint index)`
- `physics_rigid_body@ create_rigid_body(const physics_transform&in transform)`
- `uint get_nb_rigid_bodies() const property`
- `uint16 get_nb_iterations_position_solver() const property`
- `uint16 get_nb_iterations_velocity_solver() const property`
- `vector get_gravity() const property`
- `void destroy_joint(physics_joint& joint)`
- `void destroy_joint(physics_joint&inout joint)`
- `void destroy_rigid_body(physics_rigid_body& body)`
- `void destroy_rigid_body(physics_rigid_body&inout body)`
- `void raycast(const ray&in ray, physics_raycast_callback@ callback, uint16 category_mask = 0xffff)`
- `void set_callbacks(physics_collision_callback@ collision_callback, physics_overlap_callback@ trigger_callback)`
- `void set_contacts_position_correction_technique(physics_contact_position_correction_technique technique) property`
- `void set_gravity(const vector&in gravity) property`
- `void set_is_gravity_enabled(bool enabled) property`
- `void set_is_sleeping_enabled(bool enabled) property`
- `void set_nb_iterations_position_solver(uint16 iterations) property`
- `void set_nb_iterations_velocity_solver(uint16 iterations) property`
- `void set_sleep_angular_velocity(float sleep_angular_velocity) property`
- `void set_sleep_linear_velocity(float sleep_linear_velocity) property`
- `void set_time_before_sleep(float time_before_sleep) property`
- `void test_collision(physics_body@ body, physics_collision_callback@ callback)`
- `void test_collision(physics_body@ body1, physics_body@ body2, physics_collision_callback@ callback)`
- `void test_collision(physics_collision_callback@ callback)`
- `void test_overlap(physics_body@ body, physics_overlap_callback@ callback)`
- `void test_overlap(physics_overlap_callback@ callback)`
- `void update(float time_step)`

### Class `physics_world_settings`
##### Behaviours / Constructors
- `void f()`
- `void f(const physics_world_settings &in)`
- `void physics_world_settings()`
- `void physics_world_settings(const physics_world_settings&in)`
##### Properties
- `bool is_sleeping_enabled`
- `float cos_angle_similar_contact_manifold`
- `float default_bounciness`
- `float default_friction_coefficient`
- `float default_sleep_angular_velocity`
- `float default_sleep_linear_velocity`
- `float default_time_before_sleep`
- `float persistent_contact_distance_threshold`
- `float restitution_velocity_threshold`
- `string world_name`
- `uint16 default_position_solver_iterations_count`
- `uint16 default_velocity_solver_iterations_count`
- `vector gravity`
##### Methods
- `physics_world_settings &opAssign(const physics_world_settings &in)`
- `physics_world_settings& opAssign(const physics_world_settings&in)`
- `string opImplConv()`

### Class `process`
##### Methods
- `bool get_running() const property`
- `bool get_valid() const property`
- `bool kill(bool force = true)`
- `datastream@+ get_stderr() property`
- `datastream@+ get_stdin() property`
- `datastream@+ get_stdout() property`
- `int wait()`
- `int64 get_pid() const property`
- `string read()`

### Class `quaternion`
##### Behaviours / Constructors
- `void f()`
- `void f(float x, float y, float  z, float w)`
- `void quaternion()`
- `void quaternion(float x, float y, float z, float w)`
##### Properties
- `float w`
- `float x`
- `float y`
- `float z`
##### Methods
- `bool get_is_finite() const property`
- `bool get_is_unit() const property`
- `bool get_is_valid() const property`
- `bool opEquals(const quaternion &in) const`
- `bool opEquals(const quaternion&in) const`
- `float dot(const quaternion&in) const`
- `float length() const`
- `float length_square() const`
- `matrix3x3 get_matrix() const property`
- `quaternion &opAddAssign(const quaternion &in)`
- `quaternion &opSubAssign(const quaternion &in)`
- `quaternion get_conjugate() const property`
- `quaternion get_inversed() const property`
- `quaternion get_unit() const property`
- `quaternion opAdd(const quaternion &in)`
- `quaternion opAdd(const quaternion&in)`
- `quaternion opMul(const quaternion&in)`
- `quaternion opMul(float) const`
- `quaternion opSub(const quaternion &in)`
- `quaternion opSub(const quaternion&in)`
- `quaternion& opAddAssign(const quaternion&in)`
- `quaternion& opSubAssign(const quaternion&in)`
- `string opImplConv() const`
- `vector get_v() const property`
- `void get_rotation_angle_axis(float&out angle, vector&out axis) const`
- `void inverse()`
- `void normalize()`
- `void set(float x, float y, float z, float w)`
- `void set_to_identity()`
- `void set_to_zero()`

### Class `random_gamerand`
##### Behaviours / Constructors
- `random_gamerand@ f()`
- `random_gamerand@ f(uint seed)`
- `random_gamerand@ random_gamerand()`
- `random_gamerand@ random_gamerand(uint seed)`
##### Methods
- `bool next_bool(int percent = 50)`
- `bool set_state(const string &in state)`
- `bool set_state(const string&in state)`
- `float nextf()`
- `int range(int min, int max)`
- `random_interface@ opImplCast()`
- `string get_state() const`
- `string next_character(const string &in min, const string &in max)`
- `string next_character(const string&in min, const string&in max)`
- `uint next()`
- `void seed(uint s)`

### Class `random_generator`
##### Methods
- `bool next_bool(int percent = 50)`
- `float nextf()`
- `int range(int min, int max)`
- `string next_character(const string &in min, const string &in max)`
- `uint next()`

### Class `random_interface`
##### Methods
- `bool next_bool(int percent = 50)`
- `bool set_state(const string &in state)`
- `bool set_state(const string&in state)`
- `float nextf()`
- `int range(int min, int max)`
- `string get_state() const`
- `string next_character(const string &in min, const string &in max)`
- `string next_character(const string&in min, const string&in max)`
- `uint next()`
- `void seed(uint s)`
- `void seed64(uint64 s)`

### Class `random_pcg`
##### Behaviours / Constructors
- `random_pcg@ f()`
- `random_pcg@ f(uint seed)`
- `random_pcg@ random_pcg()`
- `random_pcg@ random_pcg(uint seed)`
##### Methods
- `bool next_bool(int percent = 50)`
- `bool set_state(const string &in state)`
- `bool set_state(const string&in state)`
- `float nextf()`
- `int range(int min, int max)`
- `random_interface@ opImplCast()`
- `string get_state() const`
- `string next_character(const string &in min, const string &in max)`
- `string next_character(const string&in min, const string&in max)`
- `uint next()`
- `void seed(uint s)`

### Class `random_reader`
##### Behaviours / Constructors
- `random_reader@ random_reader(const string&in encoding = "", int byteorder = 1)`
##### Properties
- `bool autoflush`
- `bool binary`
- `bool skip_eof`
- `bool sync_rw_cursors`
##### Methods
- `bool close(bool close_all = false)`
- `bool close_all()`
- `bool get_active() const property`
- `bool get_bad() const property`
- `bool get_eof() const property`
- `bool get_fail() const property`
- `bool get_good() const property`
- `bool open(const string&in encoding = "", int byteorder = 1)`
- `bool rseek(uint64 offset)`
- `bool rseek_end(uint64 offset = 0)`
- `bool rseek_relative(int64 offset)`
- `bool seek(uint64 offset)`
- `bool seek_end(uint64 offset = 0)`
- `bool seek_relative(int64 offset)`
- `bool wseek(uint64 offset)`
- `bool wseek_end(uint64 offset = 0)`
- `bool wseek_relative(int64 offset)`
- `datastream@ opImplCast()`
- `double read_double()`
- `float read_float()`
- `int read_int()`
- `int16 read_int16()`
- `int64 get_pos() const property`
- `int64 get_rpos() const property`
- `int64 get_wpos() const property`
- `int64 read_int64()`
- `int8 read_int8()`
- `random_reader& opShl(double value)`
- `random_reader& opShl(float value)`
- `random_reader& opShl(int value)`
- `random_reader& opShl(int16 value)`
- `random_reader& opShl(int64 value)`
- `random_reader& opShl(int8 value)`
- `random_reader& opShl(string value)`
- `random_reader& opShl(uint value)`
- `random_reader& opShl(uint16 value)`
- `random_reader& opShl(uint64 value)`
- `random_reader& opShl(uint8 value)`
- `random_reader& opShr(double&out value)`
- `random_reader& opShr(float&out value)`
- `random_reader& opShr(int&out value)`
- `random_reader& opShr(int16&out value)`
- `random_reader& opShr(int64&out value)`
- `random_reader& opShr(int8&out value)`
- `random_reader& opShr(string&out value)`
- `random_reader& opShr(uint&out value)`
- `random_reader& opShr(uint16&out value)`
- `random_reader& opShr(uint64&out value)`
- `random_reader& opShr(uint8&out value)`
- `random_reader& write_double(double value)`
- `random_reader& write_float(float value)`
- `random_reader& write_int(int value)`
- `random_reader& write_int16(int16 value)`
- `random_reader& write_int64(int64 value)`
- `random_reader& write_int8(int8 value)`
- `random_reader& write_string(string value)`
- `random_reader& write_uint(uint value)`
- `random_reader& write_uint16(uint16 value)`
- `random_reader& write_uint64(uint64 value)`
- `random_reader& write_uint8(uint8 value)`
- `string read(uint count = 0)`
- `string read_line()`
- `string read_string()`
- `string read_until(const string&in text, bool require_full)`
- `uint read_uint()`
- `uint write(const string&in data)`
- `uint16 read_uint16()`
- `uint64 get_available() const property`
- `uint64 read_7bit_encoded()`
- `uint64 read_uint64()`
- `uint8 read_uint8()`
- `void flush()`
- `void read_7bit_encoded(uint64&out integer)`
- `void write_7bit_encoded(uint64 integer)`

### Class `random_well`
##### Behaviours / Constructors
- `random_well@ f()`
- `random_well@ f(uint seed)`
- `random_well@ random_well()`
- `random_well@ random_well(uint seed)`
##### Methods
- `bool next_bool(int percent = 50)`
- `bool set_state(const string &in state)`
- `bool set_state(const string&in state)`
- `float nextf()`
- `int range(int min, int max)`
- `random_interface@ opImplCast()`
- `string get_state() const`
- `string next_character(const string &in min, const string &in max)`
- `string next_character(const string&in min, const string&in max)`
- `uint next()`
- `void seed(uint s)`

### Class `random_xorshift`
##### Behaviours / Constructors
- `random_xorshift@ f()`
- `random_xorshift@ f(uint seed)`
- `random_xorshift@ f(uint64 seed)`
- `random_xorshift@ random_xorshift()`
- `random_xorshift@ random_xorshift(uint seed)`
- `random_xorshift@ random_xorshift(uint64 seed)`
##### Methods
- `bool next_bool(int percent = 50)`
- `bool set_state(const string &in state)`
- `bool set_state(const string&in state)`
- `float nextf()`
- `int range(int min, int max)`
- `int64 next64()`
- `random_interface@ opImplCast()`
- `string get_state() const`
- `string next_character(const string &in min, const string &in max)`
- `string next_character(const string&in min, const string&in max)`
- `uint next()`
- `void seed(uint s)`
- `void seed64(uint64 s)`

### Class `ray`
##### Behaviours / Constructors
- `void f(const vector&in p1, const vector&in p2, float max_frac = 1.0f)`
- `void ray()`
- `void ray(const vector&in p1, const vector&in p2, float max_frac = 1.0f)`
##### Properties
- `float max_fraction`
- `vector point1`
- `vector point2`

### Class `raycast_info`
##### Behaviours / Constructors
- `void f()`
- `void raycast_info()`
##### Properties
- `float hit_fraction`
- `int triangle_index`
- `physics_body@ body`
- `physics_collider@ collider`
- `vector world_normal`
- `vector world_point`

### Class `ref`
##### Behaviours / Constructors
- `void f()`
- `void f(const ?&in value)`
- `void f(const ref &in other)`
- `void f(int&in)`
- `void ref()`
- `void ref(const ?&in value)`
- `void ref(const ref&in other)`
##### Methods
- `bool opEquals(const ?&in value) const`
- `bool opEquals(const ref &in other) const`
- `bool opEquals(const ref&in other) const`
- `ref &opHndlAssign(const ?&in value)`
- `ref &opHndlAssign(const ref &in other)`
- `ref& opHndlAssign(const ?&in value)`
- `ref& opHndlAssign(const ref&in other)`
- `void opCast(?&out value)`

### Class `refstring`
##### Behaviours / Constructors
- `refstring @s()`
- `refstring@ refstring()`
##### Properties
- `string str`

### Class `regexp`
##### Behaviours / Constructors
- `void f(const string&in pattern, regexp_options options = RE_UTF8)`
- `void regexp()`
- `void regexp(const string&in pattern, regexp_options options = RE_UTF8)`
##### Methods
- `bool match(const string&in text, uint64 offset = 0) const`
- `bool match(const string&in text, uint64 offset, int options) const`
- `bool opEquals(const string&in text) const`
- `int subst(string& text, const string&in replacement, int options = RE_UTF8) const`
- `int subst(string& text, uint64 offset, const string&in replacement, int options = RE_UTF8) const`
- `int subst(string&inout text, const string&in replacement, int options = RE_UTF8) const`
- `int subst(string&inout text, uint64 offset, const string&in replacement, int options = RE_UTF8) const`
- `string extract(const string&in text, uint64 offset = 0) const`
- `string extract(const string&in text, uint64 offset, int options) const`
- `string[]@ split(const string&in text, uint64 offset = 0) const`
- `string[]@ split(const string&in text, uint64 offset, int options) const`

### Class `reverb3d`
##### Behaviours / Constructors
- `reverb3d@ n(audio_node@+ reverb, mixer@+ destination = mixer(), audio_engine@+ engine = sound_default_engine)`
- `reverb3d@ reverb3d(audio_node@ reverb, mixer@ destination = mixer(), audio_engine@ engine = sound_default_engine)`
##### Methods
- `audio_node@ opImplCast()`
- `audio_node@+ get_reverb() const property`
- `audio_node_state get_state()`
- `audio_node_state get_state_by_time(uint64 global_time)`
- `audio_node_state get_state_by_time_range(uint64 global_time_begin, uint64 global_time_end)`
- `audio_splitter_node@ create_attachment(audio_node@+ dry_input = null, audio_node@+ dry_output = null)`
- `bool attach_output_bus(uint output_bus, audio_node@ destination, uint destination_input_bus)`
- `bool detach_all_output_buses()`
- `bool detach_output_bus(uint bus)`
- `bool set_output_bus_volume(uint bus, float volume)`
- `bool set_state(audio_node_state state)`
- `bool set_state_time(audio_node_state state, uint64 time)`
- `bool set_time(uint64 local_time)`
- `float get_max_audible_distance() const property`
- `float get_max_volume() const property`
- `float get_max_volume_distance() const property`
- `float get_min_volume() const property`
- `float get_output_bus_volume(uint bus)`
- `float get_volume_at(float distance) const`
- `float get_volume_curve() const property`
- `mixer@+ get_mixer() const property`
- `uint get_input_bus_count() const property`
- `uint get_input_channels(uint bus) const`
- `uint get_output_bus_count() const property`
- `uint get_output_channels(uint bus) const`
- `uint64 get_state_time(audio_node_state state)`
- `uint64 get_time() const`
- `void set_max_audible_distance(float distance) property`
- `void set_max_volume(float max_volume) property`
- `void set_max_volume_distance(float distance) property`
- `void set_min_volume(float min_volume) property`
- `void set_mixer(mixer@+ mix) property`
- `void set_reverb(audio_node@+ reverb) property`
- `void set_volume_curve(float volume_curve) property`

### Class `rw_lock`
##### Behaviours / Constructors
- `rw_lock@ l()`
- `rw_lock@ rw_lock()`
##### Methods
- `bool try_read_lock()`
- `bool try_write_lock()`
- `void read_lock()`
- `void unlock()`
- `void write_lock()`

### Class `rw_read_lock`
##### Behaviours / Constructors
- `void f(rw_lock@ target)`
- `void rw_read_lock()`
- `void rw_read_lock(rw_lock@ target)`

### Class `rw_scoped_lock`
##### Behaviours / Constructors
- `void f(rw_lock@ lock, bool write)`
- `void rw_scoped_lock()`
- `void rw_scoped_lock(rw_lock@ lock, bool write)`

### Class `rw_write_lock`
##### Behaviours / Constructors
- `void f(rw_lock@ target)`
- `void rw_write_lock()`
- `void rw_write_lock(rw_lock@ target)`

### Class `script_function`
##### Methods
- `bool get_is_explicit() property`
- `bool get_is_final() property`
- `bool get_is_override() property`
- `bool get_is_private() property`
- `bool get_is_property() property`
- `bool get_is_protected() property`
- `bool get_is_read_only() property`
- `bool get_is_shared() property`
- `bool retrieve(?&out)`
- `dictionary@ call(dictionary@ args, string[]@ errors = null, int max_statement_count = 0)`
- `dictionary@ opCall(dictionary@ args, string[]@ errors = null, int max_statement_count = 0)`
- `int get_line() property`
- `string get_decl() property`
- `string get_decl(bool include_object_name, bool include_namespace = true, bool include_param_names = true)`
- `string get_declared_at(int& row, int& column)`
- `string get_declared_at(int&inout row, int&inout column)`
- `string get_name() property`
- `string get_namespace() property`
- `string get_script() property`

### Class `script_module`
##### Properties
- `uint max_statement_count`
##### Methods
- `any@ get_global(uint index)`
- `const string get_global_decl(uint index)`
- `const string get_global_name(uint index)`
- `const string get_imported_function_decl(uint index)`
- `const string get_imported_function_module(uint index)`
- `int add_section(const string&in name, const string&in code, uint line_offset = 0)`
- `int bind_all_imported_functions()`
- `int bind_imported_function(uint index, script_function@+ func)`
- `int build(string[]@ errors=null)`
- `int compile_global(const string&in section_name, const string&in code, uint line_offset = 0)`
- `int get_global_index_by_decl(const string&in decl)`
- `int get_global_index_by_name(const string&in name)`
- `int get_imported_function_index(const string&in decl)`
- `int reset_globals(string[]@ errors=null)`
- `int set_bytecode(const string&in code, bool&out debug_info_was_stripped, string[]@ errors=null)`
- `script_function@ compile_function(const string&in section_name, const string&in code, array<string>@ errors = null, bool add_to_module = false, uint line_offset = 0)`
- `script_function@+ get_function_by_decl(const string&in decl)`
- `script_function@+ get_function_by_index(uint index)`
- `script_function@+ get_function_by_name(const string&in name)`
- `string get_bytecode(bool strip_debug_info)`
- `string get_name() property`
- `uint get_function_count()`
- `uint get_global_count()`
- `uint get_imported_function_count()`
- `uint set_access_mask(uint mask)`
- `void discard()`
- `void set_name(const string&in name) property`

### Class `smtp_client`
##### Behaviours / Constructors
- `smtp_client@ f()`
- `smtp_client@ smtp_client()`
##### Methods
- `bool connect()`
- `bool get_is_authenticated() const property`
- `bool get_is_connected() const property`
- `bool get_use_ssl() const property`
- `bool login(const string &in username, const string &in password, smtp_auth_method method = SMTP_AUTH_LOGIN)`
- `bool login(const string&in username, const string&in password, smtp_auth_method method = SMTP_AUTH_LOGIN)`
- `bool login_oauth2(const string &in username, const string &in access_token)`
- `bool login_oauth2(const string&in username, const string&in access_token)`
- `bool send_message(mail_message@+ message)`
- `bool send_messages(array<mail_message@>@+ messages)`
- `int get_port() const property`
- `int get_timeout() const property`
- `string get_host() const property`
- `string get_last_error() const property`
- `string get_server_capabilities() const property`
- `string query_server_capabilities()`
- `void close()`
- `void set_host(const string &in host) property`
- `void set_host(const string&in host) property`
- `void set_port(int port) property`
- `void set_timeout(int timeout) property`
- `void set_use_ssl(bool enabled) property`

### Class `socket`
##### Behaviours / Constructors
- `socket@ socket()`
- `socket@ socket(const socket&in sock)`
##### Methods
- `bool get_blocking() const property`
- `bool get_is_datagram() const property`
- `bool get_is_null() const property`
- `bool get_is_raw() const property`
- `bool get_is_stream() const property`
- `bool get_keep_alive() const property`
- `bool get_no_delay() const property`
- `bool get_oob_inline() const property`
- `bool get_reuse_address() const property`
- `bool get_reuse_port() const property`
- `bool get_secure() const property`
- `bool poll(const timespan&inout timeout, int mode) const`
- `int get_available() const property`
- `int get_error() const property`
- `int get_receive_buffer_size() const property`
- `int get_send_buffer_size() const property`
- `int opCmp(const socket&in other)`
- `socket& opAssign(const socket&in socket)`
- `socket_address get_address() const property`
- `socket_address get_peer_address() const property`
- `socket_type get_type() const property`
- `timespan get_receive_timeout() const property`
- `timespan get_send_timeout() const property`
- `void close()`
- `void get_linger(bool&out on, int&out seconds)`
- `void get_option(int level, int option, int&out value) const`
- `void get_option(int level, int option, spec::ip_address&out value)`
- `void get_option(int level, int option, timespan&out value) const`
- `void get_option(int level, int option, uint&out value) const`
- `void get_option(int level, int option, uint8&out value) const`
- `void init(int af)`
- `void set_blocking(bool flag) property`
- `void set_keep_alive(bool flag) property`
- `void set_linger(bool on, int seconds)`
- `void set_no_delay(bool flag) property`
- `void set_oob_inline(bool flag) property`
- `void set_option(int level, int option, const spec::ip_address&in value)`
- `void set_option(int level, int option, const timespan&in value)`
- `void set_option(int level, int option, int value)`
- `void set_option(int level, int option, uint value)`
- `void set_option(int level, int option, uint8 value)`
- `void set_receive_buffer_size(int size) property`
- `void set_receive_timeout(const timespan&in timeout) property`
- `void set_reuse_address(bool flag) property`
- `void set_reuse_port(bool flag) property`
- `void set_send_buffer_size(int size) property`
- `void set_send_timeout(const timespan&in timeout) property`

### Class `socket_address`
##### Behaviours / Constructors
- `void f()`
- `void f(const socket_address&in other)`
- `void f(const spec::ip_address&in addr, uint16 port)`
- `void f(const string&in host, uint16 port)`
- `void f(const string&in host_and_port)`
- `void f(spec::ip_address_family family) explicit`
- `void f(spec::ip_address_family family, const string&in addr)`
- `void f(spec::ip_address_family family, const string&in host, const string&in port)`
- `void f(spec::ip_address_family family, const string&in host, uint16 port)`
- `void f(spec::ip_address_family family, uint16 port)`
- `void f(uint16 port) explicit`
- `void socket_address()`
- `void socket_address(const socket_address&in other)`
- `void socket_address(const spec::ip_address&in addr, uint16 port)`
- `void socket_address(const string&in host, uint16 port)`
- `void socket_address(const string&in host_and_port)`
- `void socket_address(spec::ip_address_family family)`
- `void socket_address(spec::ip_address_family family, const string&in addr)`
- `void socket_address(spec::ip_address_family family, const string&in host, const string&in port)`
- `void socket_address(spec::ip_address_family family, const string&in host, uint16 port)`
- `void socket_address(spec::ip_address_family family, uint16 port)`
- `void socket_address(uint16 port)`
##### Methods
- `int opCmp(const socket_address&in other)`
- `socket_address& opAssign(const socket_address&in addr)`
- `spec::ip_address get_host() const property`
- `spec::ip_address_family get_family() const property`
- `string opImplConv() const`
- `uint16 get_port() const property`

### Class `sound`
##### Behaviours / Constructors
- `sound@ s()`
- `sound@ sound()`
##### Methods
- `audio_data_source@+ get_datasource() const property`
- `audio_engine@ get_engine() const property`
- `audio_node@ opImplCast()`
- `audio_node_chain@ get_effects_chain() property`
- `audio_node_chain@ get_internal_node_chain() property`
- `audio_node_state get_state()`
- `audio_node_state get_state_by_time(uint64 global_time)`
- `audio_node_state get_state_by_time_range(uint64 global_time_begin, uint64 global_time_end)`
- `audio_pan_mode get_pan_mode() const property`
- `audio_positioning_mode get_positioning() const property`
- `audio_splitter_node@ get_reverb3d_attachment() const property`
- `bool attach_output_bus(uint output_bus, audio_node@ destination, uint destination_input_bus)`
- `bool close()`
- `bool detach_all_output_buses()`
- `bool detach_output_bus(uint bus)`
- `bool get_active() const property`
- `bool get_at_end() const property`
- `bool get_autoclose() const property`
- `bool get_data_format(audio_format&out format, uint&out channels, uint&out sample_rate)`
- `bool get_data_format(audio_format&out format, uint32&out channels, uint32&out sample_rate)`
- `bool get_hrtf() const property`
- `bool get_load_complete() const property`
- `bool get_looping() const property`
- `bool get_paused() const property`
- `bool get_playing() const property`
- `bool get_spatialization_enabled() const property`
- `bool load(const string&in filename, const pack_interface@+ pack = sound_default_pack)`
- `bool load_memory(const string&in data)`
- `bool load_pcm(const float[]@+ data, int samplerate, int channels)`
- `bool load_pcm(const int16[]@+ data, int samplerate, int channels)`
- `bool load_pcm(const int[]@+ data, int samplerate, int channels)`
- `bool load_pcm(const memory_buffer<float>&in data, int samplerate, int channels)`
- `bool load_pcm(const memory_buffer<int16>&in data, int samplerate, int channels)`
- `bool load_pcm(const memory_buffer<int>&in data, int samplerate, int channels)`
- `bool load_pcm(const memory_buffer<uint8>&in data, int samplerate, int channels)`
- `bool load_pcm(const uint8[]@+ data, int samplerate, int channels)`
- `bool open(audio_data_source@ datasource)`
- `bool pause()`
- `bool pause_fade(const uint64 length)`
- `bool pause_fade_in_frames(const uint64 length_in_frames)`
- `bool pause_fade_in_milliseconds(const uint64 length_in_milliseconds)`
- `bool play(bool reset_loop_state = true)`
- `bool play_looped()`
- `bool play_wait()`
- `bool seek(const uint64 position)`
- `bool seek_in_frames(const uint64 position)`
- `bool seek_in_milliseconds(const uint64 position)`
- `bool set_mixer(mixer@ parent_mixer)`
- `bool set_output_bus_volume(uint bus, float volume)`
- `bool set_shape(ref shape)`
- `bool set_state(audio_node_state state)`
- `bool set_state_time(audio_node_state state, uint64 time)`
- `bool set_time(uint64 local_time)`
- `bool stop()`
- `bool stream(const string&in filename, const pack_interface@+ pack = sound_default_pack)`
- `bool stream_pcm(const float[]@+ data, uint sample_rate = 0, uint channels = 0, uint buffer_size = 0)`
- `bool stream_pcm(const int16[]@+ data, uint sample_rate = 0, uint channels = 0, uint buffer_size = 0)`
- `bool stream_pcm(const int[]@+ data, uint sample_rate = 0, uint channels = 0, uint buffer_size = 0)`
- `bool stream_pcm(const memory_buffer<float>&in data, uint sample_rate = 0, uint channels = 0, uint buffer_size = 0)`
- `bool stream_pcm(const memory_buffer<int16>&in data, uint sample_rate = 0, uint channels = 0, uint buffer_size = 0)`
- `bool stream_pcm(const memory_buffer<int>&in data, uint sample_rate = 0, uint channels = 0, uint buffer_size = 0)`
- `bool stream_pcm(const memory_buffer<uint8>&in data, uint sample_rate = 0, uint channels = 0, uint buffer_size = 0)`
- `bool stream_pcm(const uint8[]@+ data, uint sample_rate = 0, uint channels = 0, uint buffer_size = 0)`
- `bool stream_url(const string&in url)`
- `const string& get_loaded_filename() const property`
- `double get_pitch_lower_limit() const property`
- `float get_current_fade_volume() const property`
- `float get_directional_attenuation_factor() const property`
- `float get_distance_to_listener() const`
- `float get_doppler_factor() const property`
- `float get_max_distance() const property`
- `float get_max_gain() const property`
- `float get_min_distance() const property`
- `float get_min_gain() const property`
- `float get_output_bus_volume(uint bus)`
- `float get_pan() const property`
- `float get_pitch() const property`
- `float get_rolloff() const property`
- `float get_volume() const property`
- `int get_3d_attenuator() const property`
- `int get_3d_panner() const property`
- `int get_preferred_3d_attenuator() const property`
- `int get_preferred_3d_panner() const property`
- `mixer@ get_mixer() const`
- `ref get_shape() const property`
- `reverb3d@ get_reverb3d() const property`
- `reverb3d_placement get_reverb3d_placement() const property`
- `uint get_input_bus_count() const property`
- `uint get_input_channels(uint bus) const`
- `uint get_listener() const property`
- `uint get_output_bus_count() const property`
- `uint get_output_channels(uint bus) const`
- `uint get_pinned_listener() const property`
- `uint64 get_length() property`
- `uint64 get_length_in_frames( ) const property`
- `uint64 get_length_in_milliseconds() const property`
- `uint64 get_length_in_ms() const property`
- `uint64 get_position() property`
- `uint64 get_position_in_frames() const property`
- `uint64 get_position_in_milliseconds() const property`
- `uint64 get_state_time(audio_node_state state)`
- `uint64 get_time() const`
- `vector get_direction() const`
- `vector get_direction_to_listener() const`
- `vector get_position_3d() const`
- `vector get_velocity() const`
- `void get_cone(float&out inner_radians, float&out outer_radians, float&out outer_gain)`
- `void set_3d_attenuator(int attenuator_id)`
- `void set_3d_panner(int panner_id)`
- `void set_autoclose(bool enabled = true) property`
- `void set_cone(float inner_radians, float outer_radians, float outer_gain)`
- `void set_direction(const vector&in direction)`
- `void set_direction(float x, float y, float z)`
- `void set_directional_attenuation_factor(float factor) property`
- `void set_doppler_factor(float factor) property`
- `void set_fade(float start_volume, float end_volume, uint64 length)`
- `void set_fade_in_frames(float start_volume, float end_volume, uint64 length_frames)`
- `void set_fade_in_milliseconds(float start_volume, float end_volume, uint64 length_ms)`
- `void set_hrtf(bool enabled) property`
- `void set_looping(bool looping) property`
- `void set_max_distance(float distance) property`
- `void set_max_gain(float gain) property`
- `void set_min_distance(float distance) property`
- `void set_min_gain(float gain) property`
- `void set_pan(float pan) property`
- `void set_pan_mode(audio_pan_mode mode) property`
- `void set_pinned_listener(uint index) property`
- `void set_pitch(float pitch) property`
- `void set_position_3d(const vector&in position)`
- `void set_position_3d(float x, float y, float z)`
- `void set_positioning(audio_positioning_mode mode) property`
- `void set_reverb3d(reverb3d@ reverb) property`
- `void set_reverb3d_at(reverb3d@ reverb, reverb3d_placement placement)`
- `void set_rolloff(float rolloff) property`
- `void set_spatialization_enabled(bool enabled) property`
- `void set_start_time(uint64 absolute_time) property`
- `void set_stop_time(uint64 absolute_time)`
- `void set_stop_time_with_fade(uint64 absolute_time, uint64 fade_length)`
- `void set_stop_time_with_fade_in_frames(uint64 absolute_time, uint64 fade_length)`
- `void set_stop_time_with_fade_in_milliseconds(uint64 absolute_time, uint64 fade_length)`
- `void set_timed_fade(float start_volume, float end_volume, uint64 length, uint64 absolute_time)`
- `void set_timed_fade_in_frames(float start_volume, float end_volume, uint64 length, uint64 absolute_time)`
- `void set_timed_fade_in_milliseconds(float start_volume, float end_volume, uint64 length, uint64 absolute_time)`
- `void set_velocity(const vector&in velocity)`
- `void set_velocity(float x, float y, float z)`
- `void set_volume(float volume) property`

### Class `sound_aabb_shape`
##### Behaviours / Constructors
- `sound_aabb_shape@ s(int left_range, int right_range, int backward_range, int forward_range, int lower_range, int upper_range)`
- `sound_aabb_shape@ sound_aabb_shape(int left_range, int right_range, int backward_range, int forward_range, int lower_range, int upper_range)`
##### Properties
- `int backward_range`
- `int forward_range`
- `int left_range`
- `int lower_range`
- `int right_range`
- `int upper_range`

### Class `spinlock_mutex`
##### Behaviours / Constructors
- `spinlock_mutex@ spinlock_mutex()`
##### Methods
- `bool try_lock()`
- `bool try_lock(uint milliseconds)`
- `void lock()`
- `void lock(uint milliseconds)`
- `void unlock()`

### Class `spinlock_mutex_lock`
##### Behaviours / Constructors
- `void spinlock_mutex_lock()`
- `void spinlock_mutex_lock(spinlock_mutex@ target)`
- `void spinlock_mutex_lock(spinlock_mutex@ target, uint milliseconds)`
##### Methods
- `void unlock()`

### Class `stream_socket`
##### Behaviours / Constructors
- `stream_socket@ stream_socket()`
- `stream_socket@ stream_socket(const socket&in sock)`
- `stream_socket@ stream_socket(const socket_address&in address)`
- `stream_socket@ stream_socket(const spec::ip_address_family family)`
- `stream_socket@ stream_socket(const stream_socket&in sock)`
##### Methods
- `bool bind(const socket_address&in address, bool reuse_address = false, bool IPv6_only = false)`
- `bool get_blocking() const property`
- `bool get_is_datagram() const property`
- `bool get_is_null() const property`
- `bool get_is_raw() const property`
- `bool get_is_stream() const property`
- `bool get_keep_alive() const property`
- `bool get_no_delay() const property`
- `bool get_oob_inline() const property`
- `bool get_reuse_address() const property`
- `bool get_reuse_port() const property`
- `bool get_secure() const property`
- `bool poll(const timespan&inout timeout, int mode) const`
- `int get_available() const property`
- `int get_error() const property`
- `int get_receive_buffer_size() const property`
- `int get_send_buffer_size() const property`
- `int opCmp(const stream_socket&in other)`
- `int send_bytes(const string&in data, int flags = 0)`
- `int shutdown()`
- `int shutdown_send()`
- `socket_address get_address() const property`
- `socket_address get_peer_address() const property`
- `socket_type get_type() const property`
- `stream_socket& opAssign(const socket&in sock)`
- `stream_socket& opAssign(const stream_socket&in socket)`
- `string receive_bytes(int flags = 0, const timespan&in timeout = 100000)`
- `string receive_bytes(int length, int flags = 0)`
- `timespan get_receive_timeout() const property`
- `timespan get_send_timeout() const property`
- `void close()`
- `void connect(const socket_address&in address)`
- `void connect(const socket_address&in address, const timespan&in timeout)`
- `void connect_nonblocking(const socket_address&in address)`
- `void get_linger(bool&out on, int&out seconds)`
- `void get_option(int level, int option, int&out value) const`
- `void get_option(int level, int option, spec::ip_address&out value)`
- `void get_option(int level, int option, timespan&out value) const`
- `void get_option(int level, int option, uint&out value) const`
- `void get_option(int level, int option, uint8&out value) const`
- `void init(int af)`
- `void set_blocking(bool flag) property`
- `void set_keep_alive(bool flag) property`
- `void set_linger(bool on, int seconds)`
- `void set_no_delay(bool flag) property`
- `void set_oob_inline(bool flag) property`
- `void set_option(int level, int option, const spec::ip_address&in value)`
- `void set_option(int level, int option, const timespan&in value)`
- `void set_option(int level, int option, int value)`
- `void set_option(int level, int option, uint value)`
- `void set_option(int level, int option, uint8 value)`
- `void set_receive_buffer_size(int size) property`
- `void set_receive_timeout(const timespan&in timeout) property`
- `void set_reuse_address(bool flag) property`
- `void set_reuse_port(bool flag) property`
- `void set_send_buffer_size(int size) property`
- `void set_send_timeout(const timespan&in timeout) property`
- `void shutdown_receive()`

### Class `string`
##### Behaviours / Constructors
- `void f()`
- `void f(bool value)`
- `void f(const ?&in,`
- `void f(const string &in other)`
- `void f(double value)`
- `void f(float value)`
- `void f(int value)`
- `void f(int64 value)`
- `void f(uint value)`
- `void f(uint64 value)`
- `void string()`
- `void string(bool value)`
- `void string(const ?&in, const ?&in = null, const ?&in = null, const ?&in = null, const ?&in = null, const ?&in = null, const ?&in = null, const ?&in = null, const ?&in = null, const ?&in = null, const ?&in = null, const ?&in = null, const ?&in = null, const ?&in = null, const ?&in = null, const ?&in = null)`
- `void string(const string&in other)`
- `void string(double value)`
- `void string(float value)`
- `void string(int value)`
- `void string(int64 value)`
- `void string(uint value)`
- `void string(uint64 value)`
##### Methods
- `array<string>@ split(const string &in delimiter, bool full = true, bool allow_blanks = false) const`
- `array<string>@ split(const string&in delimiter, bool full = true, bool allow_blanks = false) const`
- `bool empty() const`
- `bool ends_with(const string&in text) const`
- `bool is_alphabetic(const string&in encoding = "") const`
- `bool is_alphanumeric(const string&in encoding = "") const`
- `bool is_digits(const string&in encoding = "") const`
- `bool is_empty() const`
- `bool is_lower(const string&in encoding = "") const`
- `bool is_punctuation(const string&in encoding = "") const`
- `bool is_upper(const string&in encoding = "") const`
- `bool is_whitespace(const string&in encoding = "") const`
- `bool opEquals(const string &in other) const`
- `bool opEquals(const string&in other) const`
- `bool starts_with(const string&in text) const`
- `const string get_opIndex(uint index) const property`
- `const uint8 &opIndex(uint index) const`
- `int find(const string &in search, uint start = 0) const`
- `int find(const string&in search, uint start = 0) const`
- `int find_first(const string &in search, uint start = 0) const`
- `int find_first(const string&in search, uint start = 0) const`
- `int find_first_not_of(const string &in search, uint start = 0) const`
- `int find_first_not_of(const string&in search, uint start = 0) const`
- `int find_first_of(const string &in search, uint start = 0) const`
- `int find_first_of(const string&in search, uint start = 0) const`
- `int find_firstNotOf(const string &in search, uint start = 0) const`
- `int find_firstOf(const string &in search, uint start = 0) const`
- `int find_last(const string &in search, int start = -1) const`
- `int find_last(const string&in search, int start = -1) const`
- `int find_last_not_of(const string &in search, int start = -1) const`
- `int find_last_not_of(const string&in search, int start = -1) const`
- `int find_last_of(const string &in search, int start = -1) const`
- `int find_last_of(const string&in search, int start = -1) const`
- `int find_lastNotOf(const string &in search, int start = -1) const`
- `int find_lastOf(const string &in search, int start = -1) const`
- `int opCmp(const string &in other) const`
- `int opCmp(const string&in other) const`
- `int rfind(const string &in search, int start = -1) const`
- `int rfind(const string&in search, int start = -1) const`
- `string &opAddAssign(bool value)`
- `string &opAddAssign(const string &in other)`
- `string &opAddAssign(double value)`
- `string &opAddAssign(float value)`
- `string &opAddAssign(int64 value)`
- `string &opAddAssign(uint64 value)`
- `string &opAssign(bool value)`
- `string &opAssign(const string &in other)`
- `string &opAssign(double value)`
- `string &opAssign(float value)`
- `string &opAssign(int64 value)`
- `string &opAssign(uint64 value)`
- `string escape(bool strict_json = false) const`
- `string format(`
- `string format(const ?&in = null, const ?&in = null, const ?&in = null, const ?&in = null, const ?&in = null, const ?&in = null, const ?&in = null, const ?&in = null, const ?&in = null, const ?&in = null, const ?&in = null, const ?&in = null, const ?&in = null, const ?&in = null, const ?&in = null, const ?&in = null) const`
- `string format(string[]@+ elements) const`
- `string lower() const`
- `string opAdd(bool value) const`
- `string opAdd(const string &in other) const`
- `string opAdd(const string&in other) const`
- `string opAdd(const var&in value) const`
- `string opAdd(double value) const`
- `string opAdd(float value) const`
- `string opAdd(int64 value) const`
- `string opAdd(uint64 value) const`
- `string opAdd_r(bool value) const`
- `string opAdd_r(double value) const`
- `string opAdd_r(float value) const`
- `string opAdd_r(int64 value) const`
- `string opAdd_r(uint64 value) const`
- `string opMul(uint count) const`
- `string replace(const string& in search, const string& in replacement, bool replace_all = true, uint offset = 0) const`
- `string replace_characters(const string&in characters, const string&in replace_with) const`
- `string replace_range(uint start, int count, const string& in replacement) const`
- `string reverse(const string&in encoding = "") const`
- `string reverse_bytes() const`
- `string slice(int start = 0, int end = 0) const`
- `string substr(int start, int count = -1) const`
- `string substr(uint start = 0, int count = -1) const`
- `string trim_whitespace() const`
- `string trim_whitespace_left() const`
- `string trim_whitespace_right() const`
- `string unescape() const`
- `string upper() const`
- `string& lower_this()`
- `string& opAddAssign(bool value)`
- `string& opAddAssign(const string&in other)`
- `string& opAddAssign(const var&in value)`
- `string& opAddAssign(double value)`
- `string& opAddAssign(float value)`
- `string& opAddAssign(int64 value)`
- `string& opAddAssign(uint64 value)`
- `string& opAssign(bool value)`
- `string& opAssign(const string&in other)`
- `string& opAssign(const var&in value)`
- `string& opAssign(double value)`
- `string& opAssign(float value)`
- `string& opAssign(int64 value)`
- `string& opAssign(uint64 value)`
- `string& opMulAssign(uint count)`
- `string& replace_characters_this(const string&in characters, const string&in replace_with)`
- `string& replace_range_this(uint start, int count, const string& in replacement)`
- `string& replace_this(const string& in search, const string& in replacement, bool replace_all = true, uint offset = 0)`
- `string& trim_whitespace_left_this()`
- `string& trim_whitespace_right_this()`
- `string& trim_whitespace_this()`
- `string& upper_this()`
- `uint get_length() const property`
- `uint length() const`
- `uint size() const`
- `uint64 count(const string&in search, uint64 start = 0) const`
- `uint64 get_address() const property`
- `uint8 &opIndex(uint index)`
- `void erase(uint pos, int count = -1)`
- `void insert(uint pos, const string &in other)`
- `void insert(uint pos, const string&in other)`
- `void remove_UTF8_BOM()`
- `void reserve(uint length)`
- `void resize(uint length)`
- `void set_length(uint length) property`
- `void set_opIndex(uint index, const string&in value) property`

### Class `system_tray`
##### Behaviours / Constructors
- `system_tray@ f(const string&in tooltip, graphic@+ icon = null)`
- `system_tray@ system_tray(const string&in tooltip, graphic@ icon = null)`
##### Methods
- `bool get_valid() const property`
- `system_tray_menu@+ get_menu() property`
- `void set_icon(graphic@+ icon)`
- `void set_tooltip(const string&in tooltip)`

### Class `system_tray_menu`
##### Methods
- `array<system_tray_menu_item@>@ get_entries() const property`
- `int get_entry_count() const property`
- `system_tray_menu_item@+ insert_checkbox(const string&in label, bool checked = false, system_tray_callback@+ callback = null, bool disabled = false, int pos = -1)`
- `system_tray_menu_item@+ insert_item(const string&in label, system_tray_callback@+ callback = null, bool disabled = false, int pos = -1)`
- `system_tray_menu_item@+ insert_separator(int pos = -1)`
- `system_tray_menu_item@+ insert_submenu(const string&in label, bool disabled = false, int pos = -1)`
- `void remove_entry(system_tray_menu_item@+ item)`

### Class `system_tray_menu_item`
##### Methods
- `bool get_checked() const property`
- `bool get_enabled() const property`
- `bool get_valid() const property`
- `string get_label() const property`
- `system_tray_menu@+ get_submenu() property`
- `system_tray_menu_item_type get_type() const property`
- `void click()`
- `void set_callback(system_tray_callback@+ func)`
- `void set_checked(bool checked) property`
- `void set_enabled(bool enabled) property`
- `void set_label(const string&in label) property`

### Class `text_font`
##### Behaviours / Constructors
- `text_font@ f(const string&in name, float size, uint style = FONT_STYLE_NORMAL)`
- `text_font@ text_font(const string&in name, float size, uint style = FONT_STYLE_NORMAL)`
##### Methods
- `bool add_fallback_font(text_font@+ font)`
- `bool get_dpi(int&out hdpi, int&out vdpi) const`
- `bool get_glyph_metrics(uint ch, int&out minx, int&out maxx, int&out miny, int&out maxy, int&out advance) const`
- `bool get_is_fixed_width() const property`
- `bool get_is_scalable() const property`
- `bool get_kerning() const property`
- `bool get_kerning_size(uint prev_ch, uint ch, int&out kerning) const`
- `bool get_sdf() const property`
- `bool get_string_size(const string&in text, int&out w, int&out h) const`
- `bool get_string_size_wrapped(const string&in text, int wrap_width, int&out w, int&out h) const`
- `bool has_glyph(uint codepoint)`
- `bool measure_string(const string&in text, int max_width, int&out measured_width, int&out measured_length) const`
- `bool remove_fallback_font(text_font@+ font)`
- `bool set_direction(font_direction dir)`
- `bool set_language(const string&in language_bcp47)`
- `bool set_outline(int outline)`
- `bool set_script(uint script)`
- `bool set_sdf(bool enabled)`
- `bool set_size(float ptsize)`
- `bool set_size_dpi(float ptsize, int hdpi, int vdpi)`
- `float get_size() const property`
- `font_align get_wrap_alignment() const property`
- `font_direction get_direction() const property`
- `graphic@ get_glyph_image(uint ch) const`
- `graphic@ render_glyph_blended(uint ch, uint r, uint g, uint b)`
- `graphic@ render_glyph_lcd(uint ch, uint fg_r, uint fg_g, uint fg_b, uint bg_r, uint bg_g, uint bg_b)`
- `graphic@ render_glyph_shaded(uint ch, uint fg_r, uint fg_g, uint fg_b, uint bg_r, uint bg_g, uint bg_b)`
- `graphic@ render_glyph_solid(uint ch, uint r, uint g, uint b)`
- `graphic@ render_text_blended(const string&in text, uint r, uint g, uint b)`
- `graphic@ render_text_blended_wrapped(const string&in text, int wrap_width, uint r, uint g, uint b)`
- `graphic@ render_text_lcd(const string&in text, uint fg_r, uint fg_g, uint fg_b, uint bg_r, uint bg_g, uint bg_b)`
- `graphic@ render_text_lcd_wrapped(const string&in text, int wrap_width, uint fg_r, uint fg_g, uint fg_b, uint bg_r, uint bg_g, uint bg_b)`
- `graphic@ render_text_shaded(const string&in text, uint fg_r, uint fg_g, uint fg_b, uint bg_r, uint bg_g, uint bg_b)`
- `graphic@ render_text_shaded_wrapped(const string&in text, int wrap_width, uint fg_r, uint fg_g, uint fg_b, uint bg_r, uint bg_g, uint bg_b)`
- `graphic@ render_text_solid(const string&in text, uint r, uint g, uint b)`
- `graphic@ render_text_solid_wrapped(const string&in text, int wrap_width, uint r, uint g, uint b)`
- `int get_ascent() const property`
- `int get_descent() const property`
- `int get_faces_count() const property`
- `int get_height() const property`
- `int get_line_skip() const property`
- `int get_outline() const property`
- `int get_weight() const property`
- `string get_family_name() const property`
- `string get_style_name() const property`
- `uint get_generation() const property`
- `uint get_script() const property`
- `uint get_style() const property`
- `void clear_fallback_fonts()`
- `void set_kerning(bool enabled) property`
- `void set_line_skip(int skip) property`
- `void set_style(uint style) property`
- `void set_wrap_alignment(font_align alignment) property`

### Class `thread`
##### Behaviours / Constructors
- `thread@ t()`
- `thread@ t(const string&in name)`
- `thread@ thread()`
- `thread@ thread(const string&in name)`
##### Methods
- `bool get_running() const property`
- `bool join(uint ms)`
- `int get_id() const property`
- `string get_name() const property`
- `thread_priority get_priority() const property`
- `void join()`
- `void set_name(const string&in name) property`
- `void set_priority(thread_priority priority) property`
- `void start(thread_callback@ routine, dictionary@ args = null)`
- `void wake_up()`

### Class `thread_event`
##### Behaviours / Constructors
- `thread_event@ e(thread_event_type type = THREAD_EVENT_AUTO_RESET)`
- `thread_event@ thread_event(thread_event_type type = THREAD_EVENT_AUTO_RESET)`
##### Methods
- `bool try_wait(uint ms)`
- `void reset()`
- `void set()`
- `void wait()`
- `void wait(uint ms)`

### Class `thread_pool`
##### Behaviours / Constructors
- `thread_pool@ thread_pool(int min_capacity = 2, int max_capacity = 16, int idle_time = 60, int stack_size = 0)`
##### Methods
- `const string& get_name() const property`
- `int get_allocated() const property`
- `int get_available() const property`
- `int get_capacity() const property`
- `int get_stack_size() const property`
- `int get_used() const property`
- `void add_capacity(int modifier)`
- `void collect()`
- `void join_all()`
- `void set_stack_size(int size) property`
- `void start(thread_callback@ routine, dictionary@ args = null)`
- `void start(thread_callback@ routine, dictionary@ args, const string&in name)`
- `void start(thread_callback@ routine, dictionary@ args, const string&in name, thread_priority priority)`
- `void start(thread_callback@ routine, dictionary@ args, thread_priority priority)`
- `void stop_all()`

### Class `timer`
##### Behaviours / Constructors
- `timer@ t()`
- `timer@ t(bool speedhack_protection)`
- `timer@ t(int64 initial_elapsed, bool speedhack_protection = speedhack_protection)`
- `timer@ t(int64 initial_elapsed, uint64 accuracy, bool speedhack_protection = speedhack_protection)`
- `timer@ timer()`
- `timer@ timer(bool speedhack_protection)`
- `timer@ timer(int64 initial_elapsed, bool speedhack_protection = speedhack_protection)`
- `timer@ timer(int64 initial_elapsed, uint64 accuracy, bool speedhack_protection = speedhack_protection)`
##### Properties
- `uint64 accuracy`
##### Methods
- `bool get_paused() const property`
- `bool get_running() const property`
- `bool get_secure() const property`
- `bool has_elapsed(int64 time_units) const`
- `bool pause()`
- `bool resume()`
- `bool set_paused(bool paused)`
- `bool tick(int64 time_units)`
- `int64 get_elapsed() const property`
- `void adjust(int64 mod_elapsed)`
- `void force(int64 elapsed)`
- `void restart()`
- `void set_elapsed(int64 time_units) property`
- `void set_secure(bool secure) property`
- `void toggle_pause()`

### Class `timer_queue`
##### Behaviours / Constructors
- `timer_queue @q()`
- `timer_queue@ timer_queue()`
##### Properties
- `const string failures`
##### Methods
- `bool delete(const string&in timer_id)`
- `bool exists(const string&in timer_id) const`
- `bool is_repeating(const string&in timer_id) const`
- `bool loop(int max_timers = 0, int max_catchup_milliseconds = 100)`
- `bool restart(const string&in timer_id)`
- `bool set_timeout(const string&in timer_id, uint64 milliseconds, bool repeating = false)`
- `string[]@ list_timers()`
- `uint size() const`
- `uint64 elapsed(const string&in timer_id) const`
- `uint64 ticks_to_next_event(uint64 max = 100) const`
- `uint64 timeout(const string&in timer_id) const`
- `void flush()`
- `void reset()`
- `void set(const string&in timer_id, timer_callback@ callback, const string&in callback_data, uint64 milliseconds, bool repeating = false)`
- `void set(const string&in timer_id, timer_callback@ callback, uint64 milliseconds, bool repeating = false)`

### Class `timespan`
##### Behaviours / Constructors
- `void f()`
- `void f(const timespan&in other)`
- `void f(int days, int hours, int minutes, int seconds, int microseconds)`
- `void f(int seconds, int microseconds)`
- `void f(int64 microseconds)`
- `void timespan()`
- `void timespan(const timespan&in other)`
- `void timespan(int days, int hours, int minutes, int seconds, int microseconds)`
- `void timespan(int seconds, int microseconds)`
- `void timespan(int64 microseconds)`
##### Methods
- `bool opEquals(const timespan&in other) const`
- `bool opEquals(int64 microseconds) const`
- `int get_days() const property`
- `int get_hours() const property`
- `int get_microseconds() const property`
- `int get_milliseconds() const property`
- `int get_minutes() const property`
- `int get_seconds() const property`
- `int get_total_hours() const property`
- `int get_total_microseconds() const property`
- `int get_total_milliseconds() const property`
- `int get_total_minutes() const property`
- `int get_total_seconds() const property`
- `int get_useconds() const property`
- `int opCmp(const timespan&in other) const`
- `int opCmp(int64 microseconds) const`
- `string format(const string&in fmt = "%dd %H:%M:%S.%i")`
- `timespan opAdd(const timespan&in other) const`
- `timespan opAdd(int64 microseconds) const`
- `timespan opSub(const timespan&in other) const`
- `timespan opSub(int64 microseconds) const`
- `timespan& opAddAssign(const timespan&in other)`
- `timespan& opAddAssign(int64 microseconds)`
- `timespan& opAssign(const timespan&in other)`
- `timespan& opAssign(int64 microseconds)`
- `timespan& opSubAssign(const timespan&in other)`
- `timespan& opSubAssign(int64 microseconds)`

### Class `timestamp`
##### Behaviours / Constructors
- `void f()`
- `void f(const timestamp&in other)`
- `void f(int64 microseconds)`
- `void timestamp()`
- `void timestamp(const timestamp&in other)`
- `void timestamp(int64 microseconds)`
##### Methods
- `bool has_elapsed(int64 microseconds) const`
- `bool opEquals(const timestamp&in other) const`
- `int opCmp(const timestamp&in other) const`
- `int64 get_elapsed() const property`
- `int64 get_UTC_time() const property`
- `int64 opImplConv() const`
- `int64 opSub(const timestamp&in other) const`
- `string format(const string&in fmt, int tzd = 0xffff)`
- `timestamp opAdd(const timespan&in value) const`
- `timestamp opAdd(int64 microseconds) const`
- `timestamp opSub(const timespan&in value) const`
- `timestamp opSub(int64 microseconds) const`
- `timestamp& opAddAssign(const timespan&in value)`
- `timestamp& opAddAssign(int64 microseconds)`
- `timestamp& opAssign(const timestamp&in other)`
- `timestamp& opAssign(int64 microseconds)`
- `timestamp& opSubAssign(const timespan&in value)`
- `timestamp& opSubAssign(int64 microseconds)`
- `void update()`

### Class `tone_synth`
##### Behaviours / Constructors
- `tone_synth@ f()`
- `tone_synth@ tone_synth()`
##### Methods
- `bool freq(double freq, double length)`
- `bool freq_bend(double freq, int bend_amount, double length, double bend_start, double bend_length)`
- `bool freq_bend_ms(double freq, int bend_amount, int length, int bend_start, int bend_length)`
- `bool freq_ms(double freq, int ms)`
- `bool get_allow_silent_output() const property`
- `bool note(string note, double length)`
- `bool note_bend(string note, int bend_amount, double length, double bend_start, double bend_length)`
- `bool note_bend_ms(string note, int bend_amount, int length, int bend_start, int bend_length)`
- `bool note_ms(string note, int ms)`
- `bool rest(double length)`
- `bool rest_ms(int ms)`
- `bool rewind(double amount)`
- `bool rewind_ms(int amount)`
- `bool seek(double position)`
- `bool seek_ms(int position)`
- `bool set_edge_fades(int start, int end)`
- `bool write_wave_file(const string &in filename)`
- `bool write_wave_file(const string&in filename)`
- `double get_freq_transpose() const property`
- `double get_length() const property`
- `double get_note_transpose() const property`
- `double get_pan() const property`
- `double get_position() const property`
- `double get_tempo() const property`
- `double get_volume() const property`
- `int get_channels() property`
- `int get_length_ms() const property`
- `int get_position_ms() const property`
- `int get_sample_rate() property`
- `int get_waveform_type() const property`
- `int16[]@ write_samples()`
- `sound@ write_wave_sound()`
- `void reset()`
- `void set_allow_silent_output(bool silence) property`
- `void set_freq_transpose(double value) property`
- `void set_note_transpose(double value) property`
- `void set_pan(double value) property`
- `void set_tempo(double value) property`
- `void set_volume(double value) property`
- `void set_waveform_type(int type) property`

### Class `touch_finger`
##### Properties
- `const float pressure`
- `const float x`
- `const float y`
- `const uint64 id`

### Class `tts_voice`
##### Behaviours / Constructors
- `tts_voice @t(const string&in engines = "")`
- `tts_voice@ tts_voice(const string&in engines = "")`
##### Methods
- `array<string>@ get_voice_names() const`
- `array<string>@ list_voices() const`
- `bool get_speaking() const property`
- `bool refresh()`
- `bool set_current_voice(int index)`
- `bool set_language(const string& in language)`
- `bool set_voice(int index)`
- `bool speak(const string &in text, bool interrupt = false)`
- `bool speak(const string&in text, bool interrupt = false)`
- `bool speak_interrupt(const string &in text)`
- `bool speak_interrupt(const string&in text)`
- `bool speak_interrupt_wait(const string &in text)`
- `bool speak_interrupt_wait(const string&in text)`
- `bool speak_to_file(const string& in filename, const string &in text)`
- `bool speak_to_file(const string&in filename, const string&in text)`
- `bool speak_wait(const string &in text, bool interrupt = false)`
- `bool speak_wait(const string&in text, bool interrupt = false)`
- `bool stop()`
- `float get_pitch() const property`
- `float get_rate() const property`
- `float get_volume() const property`
- `int get_voice() const property`
- `int get_voice_count() const property`
- `sound@ speak_to_sound(const string&in text)`
- `string get_language() const property`
- `string get_voice_language(int index) const`
- `string get_voice_name(int index) const`
- `string speak_to_memory(const string &in text)`
- `string speak_to_memory(const string&in text)`
- `void set_pitch(float pitch) property`
- `void set_rate(float rate) property`
- `void set_volume(float volume) property`

### Class `uri`
##### Behaviours / Constructors
- `void f()`
- `void f(const path&in path)`
- `void f(const string&in scheme, const string&in authority, const string&in path, const string&in query)`
- `void f(const string&in scheme, const string&in authority, const string&in path, const string&in query, const string&in fragment)`
- `void f(const string&in scheme, const string&in authority, const string&in path_etc)`
- `void f(const string&in scheme, const string&in path_etc)`
- `void f(const string&in uri)`
- `void f(const uri&in base_uri, const string&in relative_uri)`
- `void f(const uri&in other)`
- `void uri()`
- `void uri(const spec::path&in path)`
- `void uri(const spec::uri&in base_uri, const string&in relative_uri)`
- `void uri(const spec::uri&in other)`
- `void uri(const string&in scheme, const string&in authority, const string&in path, const string&in query)`
- `void uri(const string&in scheme, const string&in authority, const string&in path, const string&in query, const string&in fragment)`
- `void uri(const string&in scheme, const string&in authority, const string&in path_etc)`
- `void uri(const string&in scheme, const string&in path_etc)`
- `void uri(const string&in uri)`
##### Methods
- `array<array<string>>@ get_query_parameters(bool plus_as_space = true) const`
- `bool get_is_empty() const property`
- `bool get_is_relative() const property`
- `bool normalize()`
- `bool opEquals(const spec::uri&in other)`
- `bool opEquals(const string&in uri)`
- `bool opEquals(const uri&in other)`
- `const string& get_host() const property`
- `const string& get_path() const property`
- `const string& get_raw_query() const property`
- `const string& get_scheme() const property`
- `const string& get_user_info() const property`
- `spec::uri& opAssign(const spec::uri&in other)`
- `spec::uri& opAssign(const string&in uri)`
- `string get_authority() const property`
- `string get_fragment() const property`
- `string get_path_and_query() const property`
- `string get_path_etc() const property`
- `string get_query() const property`
- `string get_raw_fragment() const property`
- `string opImplConv() const`
- `string[]@ get_path_segments() const`
- `string[][]@ get_query_parameters(bool plus_as_space = true) const`
- `uint16 get_port() const property`
- `uint16 get_specified_port() const property`
- `uri& opAssign(const string&in uri)`
- `uri& opAssign(const uri&in other)`
- `void add_query_parameter(const string&in param, const string&in value = "")`
- `void clear()`
- `void resolve(const spec::uri&in relative_uri)`
- `void resolve(const string&in relative_uri)`
- `void resolve(const uri&in relative_uri)`
- `void set_authority(const string&in authority) property`
- `void set_fragment(const string&in fragment) property`
- `void set_host(const string&in host) property`
- `void set_path(const string&in path) property`
- `void set_path_etc(const string&in path_etc) property`
- `void set_port(uint16 port) property`
- `void set_query(const string&in query) property`
- `void set_raw_fragment(const string&in fragment) property`
- `void set_raw_query(const string&in query) property`
- `void set_scheme(const string&in scheme) property`
- `void set_user_info(const string&in user_info) property`

### Class `uuid`
##### Behaviours / Constructors
- `void f()`
- `void f(const string&in str)`
- `void f(const uuid&in other)`
- `void uuid()`
- `void uuid(const string&in str)`
- `void uuid(const uuid&in other)`
##### Methods
- `bool get_is_null() const property`
- `bool opEquals(const uuid&in other) const`
- `bool try_parse(const string&in str)`
- `int get_variant() const property`
- `int get_version() const property`
- `int opCmp(const uuid&in other)`
- `string get_bytes() const`
- `string get_str() const property`
- `string opConv() const`
- `string opImplConv() const`
- `string to_string() const`
- `uuid& opAssign(const uuid&in other)`
- `void parse(const string&in str)`
- `void set_bytes(const string&in bytes)`

### Class `var`
##### Behaviours / Constructors
- `var @v()`
- `var @v(const json_array&in value)`
- `var @v(const json_object&in value)`
- `var@ var()`
- `var@ var(const bool&in value)`
- `var@ var(const double&in value)`
- `var@ var(const float&in value)`
- `var@ var(const int&in value)`
- `var@ var(const int16&in value)`
- `var@ var(const int64&in value)`
- `var@ var(const json_array&in value)`
- `var@ var(const json_object&in value)`
- `var@ var(const string&in value)`
- `var@ var(const uint&in value)`
- `var@ var(const uint16&in value)`
- `var@ var(const uint64&in value)`
##### Methods
- `bool get_empty() const property`
- `bool get_is_boolean() const property`
- `bool get_is_integer() const property`
- `bool get_is_numeric() const property`
- `bool get_is_signed() const property`
- `bool get_is_string() const property`
- `bool opAdd(const bool&in value) const`
- `bool opAddAssign(const bool&in value)`
- `bool opImplConv() const`
- `double opAdd(const double&in value) const`
- `double opAddAssign(const double&in value)`
- `double opDiv(const double&in value) const`
- `double opDivAssign(const double&in value)`
- `double opImplConv() const`
- `double opMul(const double&in value) const`
- `double opMulAssign(const double&in value)`
- `double opSub(const double&in value) const`
- `double opSubAssign(const double&in value)`
- `float opAdd(const float&in value) const`
- `float opAddAssign(const float&in value)`
- `float opDiv(const float&in value) const`
- `float opDivAssign(const float&in value)`
- `float opImplConv() const`
- `float opMul(const float&in value) const`
- `float opMulAssign(const float&in value)`
- `float opSub(const float&in value) const`
- `float opSubAssign(const float&in value)`
- `int opAdd(const int&in value) const`
- `int opAddAssign(const int&in value)`
- `int opCmp(const var&in other) const`
- `int opDiv(const int&in value) const`
- `int opDivAssign(const int&in value)`
- `int opImplConv() const`
- `int opMod(const int&in value) const`
- `int opModAssign(const int&in value)`
- `int opMul(const int&in value) const`
- `int opMulAssign(const int&in value)`
- `int opSub(const int&in value) const`
- `int opSubAssign(const int&in value)`
- `int16 opAdd(const int16&in value) const`
- `int16 opAddAssign(const int16&in value)`
- `int16 opDiv(const int16&in value) const`
- `int16 opDivAssign(const int16&in value)`
- `int16 opImplConv() const`
- `int16 opMod(const int16&in value) const`
- `int16 opModAssign(const int16&in value)`
- `int16 opMul(const int16&in value) const`
- `int16 opMulAssign(const int16&in value)`
- `int16 opSub(const int16&in value) const`
- `int16 opSubAssign(const int16&in value)`
- `int64 opAdd(const int64&in value) const`
- `int64 opAddAssign(const int64&in value)`
- `int64 opDiv(const int64&in value) const`
- `int64 opDivAssign(const int64&in value)`
- `int64 opImplConv() const`
- `int64 opMod(const int64&in value) const`
- `int64 opModAssign(const int64&in value)`
- `int64 opMul(const int64&in value) const`
- `int64 opMulAssign(const int64&in value)`
- `int64 opSub(const int64&in value) const`
- `int64 opSubAssign(const int64&in value)`
- `json_array@ opImplCast() const`
- `json_object@ opImplCast() const`
- `string opAdd(const string&in value) const`
- `string opAddAssign(const string&in value)`
- `string opImplConv() const`
- `uint opAdd(const uint&in value) const`
- `uint opAddAssign(const uint&in value)`
- `uint opDiv(const uint&in value) const`
- `uint opDivAssign(const uint&in value)`
- `uint opImplConv() const`
- `uint opMod(const uint&in value) const`
- `uint opModAssign(const uint&in value)`
- `uint opMul(const uint&in value) const`
- `uint opMulAssign(const uint&in value)`
- `uint opSub(const uint&in value) const`
- `uint opSubAssign(const uint&in value)`
- `uint16 opAdd(const uint16&in value) const`
- `uint16 opAddAssign(const uint16&in value)`
- `uint16 opDiv(const uint16&in value) const`
- `uint16 opDivAssign(const uint16&in value)`
- `uint16 opImplConv() const`
- `uint16 opMod(const uint16&in value) const`
- `uint16 opModAssign(const uint16&in value)`
- `uint16 opMul(const uint16&in value) const`
- `uint16 opMulAssign(const uint16&in value)`
- `uint16 opSub(const uint16&in value) const`
- `uint16 opSubAssign(const uint16&in value)`
- `uint64 opAdd(const uint64&in value) const`
- `uint64 opAddAssign(const uint64&in value)`
- `uint64 opDiv(const uint64&in value) const`
- `uint64 opDivAssign(const uint64&in value)`
- `uint64 opImplConv() const`
- `uint64 opMod(const uint64&in value) const`
- `uint64 opModAssign(const uint64&in value)`
- `uint64 opMul(const uint64&in value) const`
- `uint64 opMulAssign(const uint64&in value)`
- `uint64 opSub(const uint64&in value) const`
- `uint64 opSubAssign(const uint64&in value)`
- `var& opAssign(const bool&in value)`
- `var& opAssign(const double&in value)`
- `var& opAssign(const float&in value)`
- `var& opAssign(const int&in value)`
- `var& opAssign(const int16&in value)`
- `var& opAssign(const int64&in value)`
- `var& opAssign(const json_array&in value) const`
- `var& opAssign(const json_object&in value) const`
- `var& opAssign(const string&in value)`
- `var& opAssign(const uint&in value)`
- `var& opAssign(const uint16&in value)`
- `var& opAssign(const uint64&in value)`
- `var& opAssign(const var&in other)`
- `var& opPostDec()`
- `var& opPostInc()`
- `void clear()`

### Class `vector`
##### Behaviours / Constructors
- `void f()`
- `void f(float x, float y, float z = 0.0f)`
- `void vector()`
- `void vector(float x, float y, float z = 0.0f)`
##### Properties
- `float x`
- `float y`
- `float z`
##### Methods
- `bool get_is_finite() const property`
- `bool get_is_unit() const property`
- `bool get_is_zero() const property`
- `bool opEquals(const vector &in) const`
- `bool opEquals(const vector&in) const`
- `const float& opIndex(int index) const`
- `float dot(const vector&in) const`
- `float get_max_value() const property`
- `float get_min_value() const property`
- `float length() const`
- `float length_square() const`
- `float& opIndex(int index)`
- `int get_max_axis() const property`
- `int get_min_axis() const property`
- `string opImplConv() const`
- `vector &opAddAssign(const vector &in)`
- `vector &opDivAssign(float)`
- `vector &opMulAssign(float)`
- `vector &opSubAssign(const vector &in)`
- `vector cross(const vector&in) const`
- `vector get_absolute() const property`
- `vector opAdd(const vector &in) const`
- `vector opAdd(const vector&in) const`
- `vector opDiv(const vector &in) const`
- `vector opDiv(const vector&in) const`
- `vector opDiv(float) const`
- `vector opMul(const vector &in) const`
- `vector opMul(const vector&in) const`
- `vector opMul(float) const`
- `vector opSub(const vector &in) const`
- `vector opSub(const vector&in) const`
- `vector& opAddAssign(const vector&in)`
- `vector& opDivAssign(float)`
- `vector& opMulAssign(float)`
- `vector& opSubAssign(const vector&in)`
- `void normalize()`
- `void set(float x, float y, float z)`
- `void setToZero()`

### Class `weakref<class T>`

### Class `weakref<T>`
##### Behaviours / Constructors
- `bool f(int&in, bool&out)`
- `void f(int&in)`
- `void f(int&in, T@+ object) explicit`
- `void weakref()`
- `void weakref(int&in)`
- `void weakref(int&in, T@ object)`
##### Methods
- `bool opEquals(const T@+ object) const`
- `bool opEquals(const weakref<T> &in other) const`
- `bool opEquals(const weakref<T>&in other) const`
- `T@ get() const`
- `T@ opImplCast()`
- `weakref<T> &opAssign(const weakref<T> &in other)`
- `weakref<T> &opHndlAssign(const weakref<T> &in other)`
- `weakref<T> &opHndlAssign(T@ object)`
- `weakref<T>& opAssign(const weakref<T>&in other)`
- `weakref<T>& opHndlAssign(const weakref<T>&in other)`
- `weakref<T>& opHndlAssign(T@ object)`

### Class `web_socket`
##### Behaviours / Constructors
- `web_socket@ s(http_client& cs, http_request& request, http_response& response)`
- `web_socket@ s(http_client& cs, http_request& request, http_response& response, http_credentials& credentials)`
- `web_socket@ web_socket(const socket&in sock)`
- `web_socket@ web_socket(const web_socket&in sock)`
- `web_socket@ web_socket(http_client&inout cs, http_request&inout request, http_response&inout response)`
- `web_socket@ web_socket(http_client&inout cs, http_request&inout request, http_response&inout response, http_credentials&inout credentials)`
##### Methods
- `bool get_blocking() const property`
- `bool get_is_datagram() const property`
- `bool get_is_null() const property`
- `bool get_is_raw() const property`
- `bool get_is_stream() const property`
- `bool get_keep_alive() const property`
- `bool get_no_delay() const property`
- `bool get_oob_inline() const property`
- `bool get_reuse_address() const property`
- `bool get_reuse_port() const property`
- `bool get_secure() const property`
- `bool poll(const timespan&inout timeout, int mode) const`
- `int get_available() const property`
- `int get_error() const property`
- `int get_max_payload_size() const property`
- `int get_receive_buffer_size() const property`
- `int get_send_buffer_size() const property`
- `int opCmp(const web_socket&in other)`
- `int send_bytes(const string&in data, int flags = 0)`
- `int send_frame(const string&in data, int flags = WS_FRAME_TEXT)`
- `int shutdown()`
- `int shutdown(uint16 status_code, const string&in status_message = "")`
- `int shutdown_send()`
- `socket_address get_address() const property`
- `socket_address get_peer_address() const property`
- `socket_type get_type() const property`
- `string receive_bytes(int flags = 0, const timespan&in timeout = 100000)`
- `string receive_bytes(int length, int flags = 0)`
- `string receive_frame(int&out flags)`
- `timespan get_receive_timeout() const property`
- `timespan get_send_timeout() const property`
- `void close()`
- `void get_linger(bool&out on, int&out seconds)`
- `void get_option(int level, int option, int&out value) const`
- `void get_option(int level, int option, spec::ip_address&out value)`
- `void get_option(int level, int option, timespan&out value) const`
- `void get_option(int level, int option, uint&out value) const`
- `void get_option(int level, int option, uint8&out value) const`
- `void init(int af)`
- `void set_blocking(bool flag) property`
- `void set_keep_alive(bool flag) property`
- `void set_linger(bool on, int seconds)`
- `void set_max_payload_size(int size) property`
- `void set_no_delay(bool flag) property`
- `void set_oob_inline(bool flag) property`
- `void set_option(int level, int option, const spec::ip_address&in value)`
- `void set_option(int level, int option, const timespan&in value)`
- `void set_option(int level, int option, int value)`
- `void set_option(int level, int option, uint value)`
- `void set_option(int level, int option, uint8 value)`
- `void set_receive_buffer_size(int size) property`
- `void set_receive_timeout(const timespan&in timeout) property`
- `void set_reuse_address(bool flag) property`
- `void set_reuse_port(bool flag) property`
- `void set_send_buffer_size(int size) property`
- `void set_send_timeout(const timespan&in timeout) property`
- `void shutdown_receive()`
- `web_socket& opAssign(const socket&in sock)`
- `web_socket& opAssign(const web_socket&in socket)`
- `web_socket_mode get_mode() const property`

## Enums
### Enum `ARCHITECTURE`
- `ARCH_AARCH64`
- `ARCH_ALPHA`
- `ARCH_AMD64`
- `ARCH_ARM`
- `ARCH_ARM64`
- `ARCH_HPPA`
- `ARCH_IA32`
- `ARCH_IA64`
- `ARCH_LOONGARCH64`
- `ARCH_M68K`
- `ARCH_MIPS`
- `ARCH_NIOS2`
- `ARCH_POWER`
- `ARCH_PPC`
- `ARCH_RISCV32`
- `ARCH_RISCV64`
- `ARCH_S390`
- `ARCH_SH`
- `ARCH_SPARC`

### Enum `audio_attenuator`
- `audio_attenuator_basic`
- `audio_attenuator_phonon`

### Enum `audio_encoder_flags`
- `AUDIO_ENCODER_DEFAULTS`
- `AUDIO_ENCODER_OVERWRITE`

### Enum `audio_engine_flags`
- `AUDIO_ENGINE_DURATIONS_IN_FRAMES`
- `AUDIO_ENGINE_NO_AUTO_START`
- `AUDIO_ENGINE_NO_CLIP`
- `AUDIO_ENGINE_NO_DEVICE`
- `AUDIO_ENGINE_PERCENTAGE_ATTRIBUTES`

### Enum `audio_error_state`
- `AUDIO_ERROR_STATE_ACCESS_DENIED`
- `AUDIO_ERROR_STATE_ADDRESS_FAMILY_NOT_SUPPORTED`
- `AUDIO_ERROR_STATE_ALREADY_CONNECTED`
- `AUDIO_ERROR_STATE_ALREADY_EXISTS`
- `AUDIO_ERROR_STATE_ALREADY_IN_USE`
- `AUDIO_ERROR_STATE_API_NOT_FOUND`
- `AUDIO_ERROR_STATE_AT_END`
- `AUDIO_ERROR_STATE_BACKEND_NOT_ENABLED`
- `AUDIO_ERROR_STATE_BAD_ADDRESS`
- `AUDIO_ERROR_STATE_BAD_MESSAGE`
- `AUDIO_ERROR_STATE_BAD_PIPE`
- `AUDIO_ERROR_STATE_BAD_PROTOCOL`
- `AUDIO_ERROR_STATE_BAD_SEEK`
- `AUDIO_ERROR_STATE_BUSY`
- `AUDIO_ERROR_STATE_CANCELLED`
- `AUDIO_ERROR_STATE_CONNECTION_REFUSED`
- `AUDIO_ERROR_STATE_CONNECTION_RESET`
- `AUDIO_ERROR_STATE_CRC_MISMATCH`
- `AUDIO_ERROR_STATE_DEADLOCK`
- `AUDIO_ERROR_STATE_DEVICE_ALREADY_INITIALIZED`
- `AUDIO_ERROR_STATE_DEVICE_NOT_INITIALIZED`
- `AUDIO_ERROR_STATE_DEVICE_NOT_STARTED`
- `AUDIO_ERROR_STATE_DEVICE_NOT_STOPPED`
- `AUDIO_ERROR_STATE_DEVICE_TYPE_NOT_SUPPORTED`
- `AUDIO_ERROR_STATE_DIRECTORY_NOT_EMPTY`
- `AUDIO_ERROR_STATE_DOES_NOT_EXIST`
- `AUDIO_ERROR_STATE_ERROR`
- `AUDIO_ERROR_STATE_FAILED_TO_INIT_BACKEND`
- `AUDIO_ERROR_STATE_FAILED_TO_OPEN_BACKEND_DEVICE`
- `AUDIO_ERROR_STATE_FAILED_TO_START_BACKEND_DEVICE`
- `AUDIO_ERROR_STATE_FAILED_TO_STOP_BACKEND_DEVICE`
- `AUDIO_ERROR_STATE_FORMAT_NOT_SUPPORTED`
- `AUDIO_ERROR_STATE_IN_PROGRESS`
- `AUDIO_ERROR_STATE_INTERRUPT`
- `AUDIO_ERROR_STATE_INVALID_ARGS`
- `AUDIO_ERROR_STATE_INVALID_DATA`
- `AUDIO_ERROR_STATE_INVALID_DEVICE_CONFIG`
- `AUDIO_ERROR_STATE_INVALID_FILE`
- `AUDIO_ERROR_STATE_INVALID_OPERATION`
- `AUDIO_ERROR_STATE_IO_ERROR`
- `AUDIO_ERROR_STATE_IS_DIRECTORY`
- `AUDIO_ERROR_STATE_LOOP`
- `AUDIO_ERROR_STATE_MEMORY_ALREADY_MAPPED`
- `AUDIO_ERROR_STATE_NAME_TOO_LONG`
- `AUDIO_ERROR_STATE_NO_ADDRESS`
- `AUDIO_ERROR_STATE_NO_BACKEND`
- `AUDIO_ERROR_STATE_NO_DATA_AVAILABLE`
- `AUDIO_ERROR_STATE_NO_DEVICE`
- `AUDIO_ERROR_STATE_NO_HOST`
- `AUDIO_ERROR_STATE_NO_MESSAGE`
- `AUDIO_ERROR_STATE_NO_NETWORK`
- `AUDIO_ERROR_STATE_NO_SPACE`
- `AUDIO_ERROR_STATE_NOT_CONNECTED`
- `AUDIO_ERROR_STATE_NOT_DIRECTORY`
- `AUDIO_ERROR_STATE_NOT_IMPLEMENTED`
- `AUDIO_ERROR_STATE_NOT_SOCKET`
- `AUDIO_ERROR_STATE_NOT_UNIQUE`
- `AUDIO_ERROR_STATE_OUT_OF_MEMORY`
- `AUDIO_ERROR_STATE_OUT_OF_RANGE`
- `AUDIO_ERROR_STATE_PATH_TOO_LONG`
- `AUDIO_ERROR_STATE_PROTOCOL_FAMILY_NOT_SUPPORTED`
- `AUDIO_ERROR_STATE_PROTOCOL_NOT_SUPPORTED`
- `AUDIO_ERROR_STATE_PROTOCOL_UNAVAILABLE`
- `AUDIO_ERROR_STATE_SHARE_MODE_NOT_SUPPORTED`
- `AUDIO_ERROR_STATE_SOCKET_NOT_SUPPORTED`
- `AUDIO_ERROR_STATE_SUCCESS`
- `AUDIO_ERROR_STATE_TIMEOUT`
- `AUDIO_ERROR_STATE_TOO_BIG`
- `AUDIO_ERROR_STATE_TOO_MANY_LINKS`
- `AUDIO_ERROR_STATE_TOO_MANY_OPEN_FILES`
- `AUDIO_ERROR_STATE_UNAVAILABLE`

### Enum `audio_format`
- `AUDIO_FORMAT_F32`
- `AUDIO_FORMAT_S16`
- `AUDIO_FORMAT_S24`
- `AUDIO_FORMAT_S32`
- `AUDIO_FORMAT_U8`
- `AUDIO_FORMAT_UNKNOWN`

### Enum `audio_node_state`
- `AUDIO_NODE_STATE_STARTED`
- `AUDIO_NODE_STATE_STOPPED`

### Enum `audio_pan_mode`
- `AUDIO_PAN_MODE_BALANCE`
- `AUDIO_PAN_MODE_PAN`

### Enum `audio_panner`
- `audio_panner_basic`
- `audio_panner_phonon_hrtf`

### Enum `audio_positioning_mode`
- `AUDIO_POSITIONING_ABSOLUTE`
- `AUDIO_POSITIONING_RELATIVE`

### Enum `audio_wav_encoder_flags`
- `AUDIO_ENCODER_WAV_F32`
- `AUDIO_ENCODER_WAV_S16`
- `AUDIO_ENCODER_WAV_S24`
- `AUDIO_ENCODER_WAV_S32`
- `AUDIO_ENCODER_WAV_U8`

### Enum `blend_mode`
- `BLEND_MODE_ADD`
- `BLEND_MODE_ADD_PREMULTIPLIED`
- `BLEND_MODE_BLEND`
- `BLEND_MODE_BLEND_PREMULTIPLIED`
- `BLEND_MODE_MOD`
- `BLEND_MODE_MUL`
- `BLEND_MODE_NONE`

### Enum `compression_method`
- `COMPRESSION_METHOD_GZIP`
- `COMPRESSION_METHOD_ZLIB`

### Enum `datastream_byte_order`
- `STREAM_BYTE_ORDER_BIG_ENDIAN`
- `STREAM_BYTE_ORDER_LITTLE_ENDIAN`
- `STREAM_BYTE_ORDER_NATIVE`
- `STREAM_BYTE_ORDER_NETWORK`

### Enum `flip_mode`
- `FLIP_HORIZONTAL`
- `FLIP_NONE`
- `FLIP_VERTICAL`

### Enum `floating_point_classification`
- `FP_INFINITE`
- `FP_NAN`
- `FP_NORMAL`
- `FP_SUBNORMAL`
- `FP_ZERO`

### Enum `font_align`
- `FONT_ALIGN_CENTER`
- `FONT_ALIGN_LEFT`
- `FONT_ALIGN_RIGHT`

### Enum `font_direction`
- `FONT_DIRECTION_BTT`
- `FONT_DIRECTION_LTR`
- `FONT_DIRECTION_RTL`
- `FONT_DIRECTION_TTB`

### Enum `font_hinting`
- `FONT_HINTING_LIGHT`
- `FONT_HINTING_LIGHT_SUBPIXEL`
- `FONT_HINTING_MONO`
- `FONT_HINTING_NONE`
- `FONT_HINTING_NORMAL`

### Enum `font_style`
- `FONT_STYLE_BOLD`
- `FONT_STYLE_ITALIC`
- `FONT_STYLE_NORMAL`
- `FONT_STYLE_STRIKETHROUGH`
- `FONT_STYLE_UNDERLINE`

### Enum `ftp_file_type`
- `FTP_FILE_TYPE_BINARY`
- `FTP_FILE_TYPE_TEXT`

### Enum `glob_options`
- `GLOB_CASELESS`
- `GLOB_DEFAULT`
- `GLOB_FOLLOW_SYMLINKS`
- `GLOB_IGNORE_HIDDEN`

### Enum `http_status`
- `HTTP_ACCEPTED`
- `HTTP_ALREADY_REPORTED`
- `HTTP_BAD_GATEWAY`
- `HTTP_BAD_REQUEST`
- `HTTP_CONFLICT`
- `HTTP_CONTINUE`
- `HTTP_CREATED`
- `HTTP_ENCHANCE_YOUR_CALM`
- `HTTP_EXPECTATION_FAILED`
- `HTTP_FAILED_DEPENDENCY`
- `HTTP_FORBIDDEN`
- `HTTP_FOUND`
- `HTTP_GATEWAY_TIMEOUT`
- `HTTP_GONE`
- `HTTP_IM_A_TEAPOT`
- `HTTP_IM_USED`
- `HTTP_INSUFFICIENT_STORAGE`
- `HTTP_INTERNAL_SERVER_ERROR`
- `HTTP_LENGTH_REQUIRED`
- `HTTP_LOCKED`
- `HTTP_LOOP_DETECTED`
- `HTTP_METHOD_NOT_ALLOWED`
- `HTTP_MISDIRECTED_REQUEST`
- `HTTP_MOVED_PERMANENTLY`
- `HTTP_MULTI_STATUS`
- `HTTP_MULTIPLE_CHOICES`
- `HTTP_NETWORK_AUTHENTICATION_REQUIRED`
- `HTTP_NO_CONTENT`
- `HTTP_NONAUTHORITATIVE`
- `HTTP_NOT_ACCEPTABLE`
- `HTTP_NOT_EXTENDED`
- `HTTP_NOT_FOUND`
- `HTTP_NOT_IMPLEMENTED`
- `HTTP_NOT_MODIFIED`
- `HTTP_OK`
- `HTTP_PARTIAL_CONTENT`
- `HTTP_PAYMENT_REQUIRED`
- `HTTP_PERMANENT_REDIRECT`
- `HTTP_PRECONDITION_FAILED`
- `HTTP_PRECONDITION_REQUIRED`
- `HTTP_PROCESSING`
- `HTTP_PROXY_AUTHENTICATION_REQUIRED`
- `HTTP_REQUEST_ENTITY_TOO_LARGE`
- `HTTP_REQUEST_HEADER_FIELDS_TOO_LARGE`
- `HTTP_REQUEST_TIMEOUT`
- `HTTP_REQUEST_URI_TOO_LONG`
- `HTTP_REQUESTED_RANGE_NOT_SATISFIABLE`
- `HTTP_RESET_CONTENT`
- `HTTP_SEE_OTHER`
- `HTTP_SERVICE_UNAVAILABLE`
- `HTTP_SWITCHING_PROTOCOLS`
- `HTTP_TEMPORARY_REDIRECT`
- `HTTP_TOO_EARLY`
- `HTTP_TOO_MANY_REQUESTS`
- `HTTP_UNAUTHORIZED`
- `HTTP_UNAVAILABLE_FOR_LEGAL_REASONS`
- `HTTP_UNPROCESSABLE_ENTITY`
- `HTTP_UNSUPPORTED_MEDIA_TYPE`
- `HTTP_UPGRADE_REQUIRED`
- `HTTP_USE_PROXY`
- `HTTP_VARIANT_ALSO_NEGOTIATES`
- `HTTP_VERSION_NOT_SUPPORTED`

### Enum `ip_address_family`
- `IP_FAMILY_IPV4`
- `IP_FAMILY_IPV6`
- `IP_FAMILY_unix_local`
- `IP_FAMILY_UNKNOWN`

### Enum `joystick_bind_type`
- `JOYSTICK_BIND_TYPE_AXIS`
- `JOYSTICK_BIND_TYPE_BUTTON`
- `JOYSTICK_BIND_TYPE_HAT`
- `JOYSTICK_BIND_TYPE_NONE`

### Enum `joystick_control_type`
- `JOYSTICK_BUTTON_A`
- `JOYSTICK_BUTTON_B`
- `JOYSTICK_BUTTON_BACK`
- `JOYSTICK_BUTTON_GUIDE`
- `JOYSTICK_BUTTON_INVALID`
- `JOYSTICK_BUTTON_MISC`
- `JOYSTICK_BUTTON_START`
- `JOYSTICK_BUTTON_X`
- `JOYSTICK_BUTTON_Y`
- `JOYSTICK_CONTROL_DPAD_DOWN`
- `JOYSTICK_CONTROL_DPAD_LEFT`
- `JOYSTICK_CONTROL_DPAD_RIGHT`
- `JOYSTICK_CONTROL_DPAD_UP`
- `JOYSTICK_CONTROL_LEFT_SHOULDER`
- `JOYSTICK_CONTROL_LEFT_STICK`
- `JOYSTICK_CONTROL_PADDLE1`
- `JOYSTICK_CONTROL_PADDLE2`
- `JOYSTICK_CONTROL_PADDLE3`
- `JOYSTICK_CONTROL_PADDLE4`
- `JOYSTICK_CONTROL_RIGHT_SHOULDER`
- `JOYSTICK_CONTROL_RIGHT_STICK`
- `JOYSTICK_CONTROL_TOUCHPAD`

### Enum `joystick_power_state`
- `JOYSTICK_POWER_CHARGED`
- `JOYSTICK_POWER_CHARGING`
- `JOYSTICK_POWER_ERROR`
- `JOYSTICK_POWER_NO_BATTERY`
- `JOYSTICK_POWER_ON_BATTERY`
- `JOYSTICK_POWER_UNKNOWN`

### Enum `joystick_type`
- `JOYSTICK_TYPE_NINTENDO_SWITCH_JOYCON_LEFT`
- `JOYSTICK_TYPE_NINTENDO_SWITCH_JOYCON_PAIR`
- `JOYSTICK_TYPE_NINTENDO_SWITCH_JOYCON_RIGHT`
- `JOYSTICK_TYPE_NINTENDO_SWITCH_PRO`
- `JOYSTICK_TYPE_PS3`
- `JOYSTICK_TYPE_PS4`
- `JOYSTICK_TYPE_PS5`
- `JOYSTICK_TYPE_STANDARD`
- `JOYSTICK_TYPE_UNKNOWN`
- `JOYSTICK_TYPE_XBOX1`
- `JOYSTICK_TYPE_XBOX360`

### Enum `key_code`
- `KEY_0`
- `KEY_1`
- `KEY_2`
- `KEY_3`
- `KEY_4`
- `KEY_5`
- `KEY_6`
- `KEY_7`
- `KEY_8`
- `KEY_9`
- `KEY_A`
- `KEY_AC_BACK`
- `KEY_AC_BOOKMARKS`
- `KEY_AC_FORWARD`
- `KEY_AC_HOME`
- `KEY_AC_REFRESH`
- `KEY_AC_SEARCH`
- `KEY_AC_STOP`
- `KEY_AGAIN`
- `KEY_ALTERASE`
- `KEY_APOSTROPHE`
- `KEY_APPLICATION`
- `KEY_B`
- `KEY_BACK`
- `KEY_BACKSLASH`
- `KEY_C`
- `KEY_CALL`
- `KEY_CANCEL`
- `KEY_CAPSLOCK`
- `KEY_CLEAR`
- `KEY_CLEARAGAIN`
- `KEY_COMMA`
- `KEY_COPY`
- `KEY_CRSEL`
- `KEY_CURRENCYSUBUNIT`
- `KEY_CURRENCYUNIT`
- `KEY_CUT`
- `KEY_D`
- `KEY_DECIMALSEPARATOR`
- `KEY_DELETE`
- `KEY_DOWN`
- `KEY_E`
- `KEY_END`
- `KEY_ENDCALL`
- `KEY_EQUALS`
- `KEY_ESCAPE`
- `KEY_EXECUTE`
- `KEY_EXSEL`
- `KEY_F`
- `KEY_F1`
- `KEY_F10`
- `KEY_F11`
- `KEY_F12`
- `KEY_F13`
- `KEY_F14`
- `KEY_F15`
- `KEY_F16`
- `KEY_F17`
- `KEY_F18`
- `KEY_F19`
- `KEY_F2`
- `KEY_F20`
- `KEY_F21`
- `KEY_F22`
- `KEY_F23`
- `KEY_F24`
- `KEY_F3`
- `KEY_F4`
- `KEY_F5`
- `KEY_F6`
- `KEY_F7`
- `KEY_F8`
- `KEY_F9`
- `KEY_FIND`
- `KEY_G`
- `KEY_GRAVE`
- `KEY_H`
- `KEY_HELP`
- `KEY_HOME`
- `KEY_I`
- `KEY_INSERT`
- `KEY_INTERNATIONAL1`
- `KEY_INTERNATIONAL2`
- `KEY_INTERNATIONAL3`
- `KEY_INTERNATIONAL4`
- `KEY_INTERNATIONAL5`
- `KEY_INTERNATIONAL6`
- `KEY_INTERNATIONAL7`
- `KEY_INTERNATIONAL8`
- `KEY_INTERNATIONAL9`
- `KEY_J`
- `KEY_K`
- `KEY_L`
- `KEY_LALT`
- `KEY_LANG1`
- `KEY_LANG2`
- `KEY_LANG3`
- `KEY_LANG4`
- `KEY_LANG5`
- `KEY_LANG6`
- `KEY_LANG7`
- `KEY_LANG8`
- `KEY_LANG9`
- `KEY_LCTRL`
- `KEY_LEFT`
- `KEY_LEFTBRACKET`
- `KEY_LGUI`
- `KEY_LSHIFT`
- `KEY_M`
- `KEY_MEDIA_EJECT`
- `KEY_MEDIA_FAST_FORWARD`
- `KEY_MEDIA_NEXT_TRACK`
- `KEY_MEDIA_PLAY`
- `KEY_MEDIA_PREVIOUS_TRACK`
- `KEY_MEDIA_REWIND`
- `KEY_MEDIA_SELECT`
- `KEY_MEDIA_STOP`
- `KEY_MENU`
- `KEY_MINUS`
- `KEY_MODE`
- `KEY_MUTE`
- `KEY_N`
- `KEY_NONUSBACKSLASH`
- `KEY_NONUSHASH`
- `KEY_NUMLOCKCLEAR`
- `KEY_NUMPAD_0`
- `KEY_NUMPAD_00`
- `KEY_NUMPAD_000`
- `KEY_NUMPAD_1`
- `KEY_NUMPAD_2`
- `KEY_NUMPAD_3`
- `KEY_NUMPAD_4`
- `KEY_NUMPAD_5`
- `KEY_NUMPAD_6`
- `KEY_NUMPAD_7`
- `KEY_NUMPAD_8`
- `KEY_NUMPAD_9`
- `KEY_NUMPAD_A`
- `KEY_NUMPAD_AMPERSAND`
- `KEY_NUMPAD_AT`
- `KEY_NUMPAD_B`
- `KEY_NUMPAD_BACKSPACE`
- `KEY_NUMPAD_BINARY`
- `KEY_NUMPAD_C`
- `KEY_NUMPAD_CLEAR`
- `KEY_NUMPAD_CLEARENTRY`
- `KEY_NUMPAD_COLON`
- `KEY_NUMPAD_COMMA`
- `KEY_NUMPAD_D`
- `KEY_NUMPAD_DBLAMPERSAND`
- `KEY_NUMPAD_DBLVERTICALBAR`
- `KEY_NUMPAD_DECIMAL`
- `KEY_NUMPAD_DIVIDE`
- `KEY_NUMPAD_E`
- `KEY_NUMPAD_ENTER`
- `KEY_NUMPAD_EQUALS`
- `KEY_NUMPAD_EQUALSAS400`
- `KEY_NUMPAD_EXCLAM`
- `KEY_NUMPAD_F`
- `KEY_NUMPAD_GREATER`
- `KEY_NUMPAD_HASH`
- `KEY_NUMPAD_HEXADECIMAL`
- `KEY_NUMPAD_LEFTBRACE`
- `KEY_NUMPAD_LEFTPAREN`
- `KEY_NUMPAD_LESS`
- `KEY_NUMPAD_MEMADD`
- `KEY_NUMPAD_MEMCLEAR`
- `KEY_NUMPAD_MEMDIVIDE`
- `KEY_NUMPAD_MEMMULTIPLY`
- `KEY_NUMPAD_MEMRECALL`
- `KEY_NUMPAD_MEMSTORE`
- `KEY_NUMPAD_MEMSUBTRACT`
- `KEY_NUMPAD_MINUS`
- `KEY_NUMPAD_MULTIPLY`
- `KEY_NUMPAD_OCTAL`
- `KEY_NUMPAD_PERCENT`
- `KEY_NUMPAD_PERIOD`
- `KEY_NUMPAD_PLUS`
- `KEY_NUMPAD_PLUSMINUS`
- `KEY_NUMPAD_POWER`
- `KEY_NUMPAD_RIGHTBRACE`
- `KEY_NUMPAD_RIGHTPAREN`
- `KEY_NUMPAD_SPACE`
- `KEY_NUMPAD_TAB`
- `KEY_NUMPAD_VERTICALBAR`
- `KEY_NUMPAD_XOR`
- `KEY_O`
- `KEY_OPER`
- `KEY_OUT`
- `KEY_P`
- `KEY_PAGEDOWN`
- `KEY_PAGEUP`
- `KEY_PASTE`
- `KEY_PAUSE`
- `KEY_PERIOD`
- `KEY_POWER`
- `KEY_PRINTSCREEN`
- `KEY_Q`
- `KEY_R`
- `KEY_RALT`
- `KEY_RCTRL`
- `KEY_RETURN`
- `KEY_RETURN2`
- `KEY_RGUI`
- `KEY_RIGHT`
- `KEY_RIGHTBRACKET`
- `KEY_RSHIFT`
- `KEY_S`
- `KEY_SCROLLLOCK`
- `KEY_SDL_PRIOR`
- `KEY_SELECT`
- `KEY_SEMICOLON`
- `KEY_SEPARATOR`
- `KEY_SLASH`
- `KEY_SLEEP`
- `KEY_SOFTLEFT`
- `KEY_SOFTRIGHT`
- `KEY_SPACE`
- `KEY_STOP`
- `KEY_SYSREQ`
- `KEY_T`
- `KEY_TAB`
- `KEY_THOUSANDSSEPARATOR`
- `KEY_U`
- `KEY_UNDO`
- `KEY_UNKNOWN`
- `KEY_UP`
- `KEY_V`
- `KEY_VOLUMEDOWN`
- `KEY_VOLUMEUP`
- `KEY_W`
- `KEY_X`
- `KEY_Y`
- `KEY_Z`

### Enum `key_modifier`
- `KEYMOD_ALT`
- `KEYMOD_CAPS`
- `KEYMOD_CTRL`
- `KEYMOD_GUI`
- `KEYMOD_LALT`
- `KEYMOD_LCTRL`
- `KEYMOD_LGUI`
- `KEYMOD_LSHIFT`
- `KEYMOD_MODE`
- `KEYMOD_NONE`
- `KEYMOD_NUM`
- `KEYMOD_RALT`
- `KEYMOD_RCTRL`
- `KEYMOD_RGUI`
- `KEYMOD_RSHIFT`
- `KEYMOD_SCROLL`
- `KEYMOD_SHIFT`

### Enum `mail_priority`
- `MAIL_PRIORITY_HIGH`
- `MAIL_PRIORITY_HIGHEST`
- `MAIL_PRIORITY_LOW`
- `MAIL_PRIORITY_LOWEST`
- `MAIL_PRIORITY_NORMAL`

### Enum `mail_recipient_type`
- `RECIPIENT_BCC`
- `RECIPIENT_CC`
- `RECIPIENT_TO`

### Enum `memory_order`
- `MEMORY_ORDER_ACQ_REL`
- `MEMORY_ORDER_ACQUIRE`
- `MEMORY_ORDER_RELAXED`
- `MEMORY_ORDER_RELEASE`
- `MEMORY_ORDER_SEQ_CST`

### Enum `message_box_flags`
- `MESSAGE_BOX_BUTTONS_LEFT_TO_RIGHT`
- `MESSAGE_BOX_BUTTONS_RIGHT_TO_LEFT`
- `MESSAGE_BOX_ERROR`
- `MESSAGE_BOX_INFORMATION`
- `MESSAGE_BOX_WARNING`

### Enum `network_event_type`
- `event_connect`
- `event_disconnect`
- `event_disconnect_timeout`
- `event_none`
- `event_receive`

### Enum `OPERATING_SYSTEM`
- `OS_AIX`
- `OS_ANDROID`
- `OS_CYGWIN`
- `OS_DARWIN`
- `OS_FREE_BSD`
- `OS_HPUX`
- `OS_IRIX`
- `OS_LINUX`
- `OS_NACL`
- `OS_NET_BSD`
- `OS_OPEN_BSD`
- `OS_QNX`
- `OS_SOLARIS`
- `OS_TRU64`
- `OS_UNKNOWN_UNIX`
- `OS_VMS`
- `OS_VXWORKS`
- `OS_WINDOWS_NT`

### Enum `opus_application_type`
- `OPUS_APPLICATION_AUDIO`
- `OPUS_APPLICATION_RESTRICTED_LOWDELAY`
- `OPUS_APPLICATION_VOIP`

### Enum `opus_signal_type`
- `OPUS_AUTO`
- `OPUS_SIGNAL_MUSIC`
- `OPUS_SIGNAL_VOICE`

### Enum `path_style`
- `PATH_STYLE_AUTO`
- `PATH_STYLE_NATIVE`
- `PATH_STYLE_UNIX`
- `PATH_STYLE_URI`
- `PATH_STYLE_VMS`
- `PATH_STYLE_WINDOWS`

### Enum `physics_body_type`
- `PHYSICS_BODY_DYNAMIC`
- `PHYSICS_BODY_KINEMATIC`
- `PHYSICS_BODY_STATIC`

### Enum `physics_contact_event_type`
- `PHYSICS_CONTACT_EXIT`
- `PHYSICS_CONTACT_START`
- `PHYSICS_CONTACT_STAY`

### Enum `physics_contact_position_correction_technique`
- `POSITION_CORRECTION_TECHNIQUE_BAUMGARTE_CONTACTS`
- `POSITION_CORRECTION_TECHNIQUE_SPLIT_IMPULSES`

### Enum `physics_height_data_type`
- `PHYSICS_HEIGHT_DOUBLE_TYPE`
- `PHYSICS_HEIGHT_FLOAT_TYPE`
- `PHYSICS_HEIGHT_INT_TYPE`

### Enum `physics_joint_type`
- `BALL_SOCKET_JOINT`
- `FIXED_JOINT`
- `HINGE_JOINT`
- `SLIDER_JOINT`

### Enum `physics_joints_position_correction_technique`
- `JOINTS_CORRECTION_TECHNIQUE_BAUMGARTE_JOINTS`
- `JOINTS_CORRECTION_TECHNIQUE_NON_LINEAR_GAUSS_SEIDEL`

### Enum `physics_logger_category`
- `LOGGER_CATEGORY_BODY`
- `LOGGER_CATEGORY_COLLIDER`
- `LOGGER_CATEGORY_JOINT`
- `LOGGER_CATEGORY_PHYSICS_COMMON`
- `LOGGER_CATEGORY_WORLD`

### Enum `physics_logger_format`
- `LOGGER_FORMAT_HTML`
- `LOGGER_FORMAT_TEXT`

### Enum `physics_logger_level`
- `LOGGER_LEVEL_ERROR`
- `LOGGER_LEVEL_INFORMATION`
- `LOGGER_LEVEL_WARNING`

### Enum `physics_message_type`
- `PHYSICS_MESSAGE_ERROR`
- `PHYSICS_MESSAGE_INFORMATION`
- `PHYSICS_MESSAGE_WARNING`

### Enum `physics_overlap_event_type`
- `PHYSICS_OVERLAP_EXIT`
- `PHYSICS_OVERLAP_START`
- `PHYSICS_OVERLAP_STAY`

### Enum `physics_polygon_index_data_type`
- `POLYGON_INDEX_INTEGER_TYPE`
- `POLYGON_INDEX_SHORT_TYPE`

### Enum `physics_polygon_vertex_data_type`
- `POLYGON_VERTEX_DOUBLE_TYPE`
- `POLYGON_VERTEX_FLOAT_TYPE`

### Enum `physics_shape_name`
- `SHAPE_BOX`
- `SHAPE_CAPSULE`
- `SHAPE_CONVEX_MESH`
- `SHAPE_HEIGHTFIELD`
- `SHAPE_SPHERE`
- `SHAPE_TRIANGLE`
- `SHAPE_TRIANGLE_MESH`

### Enum `physics_shape_type`
- `SHAPE_TYPE_CAPSULE`
- `SHAPE_TYPE_CONCAVE`
- `SHAPE_TYPE_CONVEX_POLYHEDRON`
- `SHAPE_TYPE_SPHERE`

### Enum `physics_triangle_index_data_type`
- `TRIANGLE_INDEX_INTEGER_TYPE`
- `TRIANGLE_INDEX_SHORT_TYPE`

### Enum `physics_triangle_normal_data_type`
- `TRIANGLE_NORMAL_DOUBLE_TYPE`
- `TRIANGLE_NORMAL_FLOAT_TYPE`

### Enum `physics_triangle_raycast_side`
- `TRIANGLE_RAYCAST_SIDE_BACK`
- `TRIANGLE_RAYCAST_SIDE_FRONT`
- `TRIANGLE_RAYCAST_SIDE_FRONT_AND_BACK`

### Enum `physics_triangle_vertex_data_type`
- `TRIANGLE_VERTEX_DOUBLE_TYPE`
- `TRIANGLE_VERTEX_FLOAT_TYPE`

### Enum `physics_vertex_data_type`
- `VERTEX_DOUBLE_TYPE`
- `VERTEX_FLOAT_TYPE`

### Enum `pixel_format`
- `PIXELFORMAT_ABGR32`
- `PIXELFORMAT_ABGR8888`
- `PIXELFORMAT_ARGB32`
- `PIXELFORMAT_ARGB8888`
- `PIXELFORMAT_BGR24`
- `PIXELFORMAT_BGRA32`
- `PIXELFORMAT_BGRA8888`
- `PIXELFORMAT_INDEX8`
- `PIXELFORMAT_RGB24`
- `PIXELFORMAT_RGBA32`
- `PIXELFORMAT_RGBA8888`
- `PIXELFORMAT_UNKNOWN`
- `PIXELFORMAT_XBGR8888`
- `PIXELFORMAT_XRGB8888`

### Enum `process_flags`
- `PROCESS_BACKGROUND`
- `PROCESS_CAPTURE`
- `PROCESS_FAIL_EXCEPTION`
- `PROCESS_PIPE_STDERR`
- `PROCESS_PIPE_STDIN`
- `PROCESS_PIPE_STDOUT`
- `PROCESS_STDERR_TO_STDOUT`
- `PROCESS_WAIT`

### Enum `regexp_options`
- `RE_ANCHORED`
- `RE_CASELESS`
- `RE_DOLLAR_END_ONLY`
- `RE_DOTALL`
- `RE_DUPNAMES`
- `RE_EXTENDED`
- `RE_EXTRA`
- `RE_FIRSTLINE`
- `RE_GLOBAL`
- `RE_MULTILINE`
- `RE_NEWLINE_ANY`
- `RE_NEWLINE_ANY_CRLF`
- `RE_NEWLINE_CR`
- `RE_NEWLINE_CRLF`
- `RE_NEWLINE_LF`
- `RE_NO_AUTO_CAPTURE`
- `RE_NO_UTF8_CHECK`
- `RE_NO_VARS`
- `RE_NOT_BOL`
- `RE_NOT_EMPTY`
- `RE_NOT_EOL`
- `RE_UNGREEDY`
- `RE_UTF8`

### Enum `renderer_logical_presentation`
- `LOGICAL_PRESENTATION_DISABLED`
- `LOGICAL_PRESENTATION_INTEGER_SCALE`
- `LOGICAL_PRESENTATION_LETTERBOX`
- `LOGICAL_PRESENTATION_OVERSCAN`
- `LOGICAL_PRESENTATION_STRETCH`

### Enum `reverb3d_placement`
- `reverb3d_postattenuate`
- `reverb3d_postpan`
- `reverb3d_prepan`

### Enum `sdl_hint_priority`
- `SDL_HINT_DEFAULT`
- `SDL_HINT_NORMAL`
- `SDL_HINT_OVERRIDE`

### Enum `smtp_auth_method`
- `SMTP_AUTH_CRAM_MD5`
- `SMTP_AUTH_CRAM_SHA1`
- `SMTP_AUTH_LOGIN`
- `SMTP_AUTH_NONE`
- `SMTP_AUTH_NTLM`
- `SMTP_AUTH_PLAIN`
- `SMTP_AUTH_XOAUTH2`

### Enum `socket_select_mode`
- `SOCKET_SELECT_ERROR`
- `SOCKET_SELECT_READ`
- `SOCKET_SELECT_WRITE`

### Enum `socket_type`
- `SOCKET_TYPE_DATAGRAM`
- `SOCKET_TYPE_RAW`
- `SOCKET_TYPE_STREAM`

### Enum `string_base64_options`
- `STRING_BASE64_DEFAULT`
- `STRING_BASE64_PADLESS`
- `STRING_BASE64_URL`
- `STRING_BASE64_URL_PADLESS`

### Enum `system_power_state`
- `POWER_STATE_CHARGED`
- `POWER_STATE_CHARGING`
- `POWER_STATE_ERROR`
- `POWER_STATE_NO_BATTERY`
- `POWER_STATE_ON_BATTERY`
- `POWER_STATE_UNKNOWN`

### Enum `system_tray_menu_item_type`
- `SYSTEM_TRAY_CHECKBOX`
- `SYSTEM_TRAY_ITEM`
- `SYSTEM_TRAY_SEPARATOR`
- `SYSTEM_TRAY_SUBMENU`

### Enum `thread_event_type`
- `THREAD_EVENT_AUTO_RESET`
- `THREAD_EVENT_MANUAL_RESET`

### Enum `thread_priority`
- `THREAD_PRIORITY_HIGH`
- `THREAD_PRIORITY_HIGHEST`
- `THREAD_PRIORITY_LOW`
- `THREAD_PRIORITY_LOWEST`
- `THREAD_PRIORITY_NORMAL`

### Enum `touch_device_type`
- `TOUCH_DEVICE_DIRECT`
- `TOUCH_DEVICE_INDIRECT_ABSOLUTE`
- `TOUCH_DEVICE_INDIRECT_RELATIVE`
- `TOUCH_DEVICE_TYPE_INVALID`

### Enum `web_socket_error_codes`
- `WS_ERR_HANDSHAKE_ACCEPT`
- `WS_ERR_HANDSHAKE_NO_KEY`
- `WS_ERR_HANDSHAKE_NO_VERSION`
- `WS_ERR_HANDSHAKE_UNSUPPORTED_VERSION`
- `WS_ERR_INCOMPLETE_FRAME`
- `WS_ERR_NO_HANDSHAKE`
- `WS_ERR_PAYLOAD_TOO_BIG`
- `WS_ERR_UNAUTHORIZED`

### Enum `web_socket_frame_flags`
- `WS_FRAME_FLAG_FIN`

### Enum `web_socket_frame_opcodes`
- `WS_FRAME_OP_BINARY`
- `WS_FRAME_OP_BITMASK`
- `WS_FRAME_OP_CLOSE`
- `WS_FRAME_OP_CONT`
- `WS_FRAME_OP_PING`
- `WS_FRAME_OP_PONG`
- `WS_FRAME_OP_SETRAW`
- `WS_FRAME_OP_TEXT`

### Enum `web_socket_mode`
- `WS_CLIENT`
- `WS_SERVER`

### Enum `web_socket_send_flags`
- `WS_FRAME_BINARY`
- `WS_FRAME_TEXT`

### Enum `web_socket_status_codes`
- `WS_ENDPOINT_GOING_AWAY`
- `WS_EXTENSION_REQUIRED`
- `WS_MALFORMED_PAYLOAD`
- `WS_NORMAL_CLOSE`
- `WS_PAYLOAD_NOT_ACCEPTABLE`
- `WS_PAYLOAD_TOO_BIG`
- `WS_POLICY_VIOLATION`
- `WS_PROTOCOL_ERROR`
- `WS_RESERVED`
- `WS_RESERVED_ABNORMAL_CLOSE`
- `WS_RESERVED_NO_STATUS_CODE`
- `WS_RESERVED_TLS_FAILURE`
- `WS_UNEXPECTED_CONDITION`

### Enum `window_flags`
- `WINDOW_FLAG_ALWAYS_ON_TOP`
- `WINDOW_FLAG_BORDERLESS`
- `WINDOW_FLAG_FULLSCREEN`
- `WINDOW_FLAG_HIDDEN`
- `WINDOW_FLAG_MAXIMIZED`
- `WINDOW_FLAG_MINIMIZED`
- `WINDOW_FLAG_RESIZABLE`

### Enum `window_flash_operation`
- `FLASH_BRIEFLY`
- `FLASH_CANCEL`
- `FLASH_UNTIL_FOCUSED`

### Enum `window_progress_state`
- `PROGRESS_STATE_ERROR`
- `PROGRESS_STATE_INDETERMINATE`
- `PROGRESS_STATE_INVALID`
- `PROGRESS_STATE_NONE`
- `PROGRESS_STATE_NORMAL`
- `PROGRESS_STATE_PAUSED`
