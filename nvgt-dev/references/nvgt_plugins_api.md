# NVGT Plugins API Reference

> **IMPORTANT NOTE:** These syntaxes belong to NVGT plugins written in C++. To use them, you MUST include the pragma directive at the top of your script. Example:
> `#pragma plugin("plugin_name")`

---
## Plugin: `curl`
**Syntax to use:** `#pragma plugin("curl")`

### Global Functions
- `string curl_url_decode(const string& in)`
- `string curl_url_encode(const string& in)`

### Classes
#### Class `internet_request`
##### Behaviours / Constructors
- `internet_request @i()`
- `internet_request @i(const string &in, bool = true)`
- `internet_request @i(const string &in, const string &in, bool = true)`
- `internet_request @i(const string &in, const string &in, const string &in, bool = true)`
##### Properties
- `bool follow_redirects`
- `const bool complete`
- `const bool in_progress`
- `const bool no_curl`
- `const double bytes_downloaded`
- `const double bytes_uploaded`
- `const double download_percent`
- `const double download_size`
- `const double total_time`
- `const double upload_percent`
- `const double upload_size`
- `const int status_code`
- `const string auth_password`
- `const string auth_username`
- `const string final_url`
- `const string path`
- `const string response_body`
- `const string response_headers`
- `const string url`
- `int max_redirects`
- `string debug_file`
- `string user_agent`
##### Methods
- `bool mail(const string &in, const string &in, const string &in, const string &in) const`
- `bool perform()`
- `bool perform(const string &in)`
- `bool post(const string &in, const string &in, const string &in = '')`
- `void reset() const`
- `void set_authentication(string, string)`
- `void set_header(const string &in, const string& in) const`
- `void set_mail(const string &in, const string &in) const`
- `void set_path(const string &in) const`
- `void set_payload(const string &in) const`
- `void set_url(const string &in) const`

---
## Plugin: `fast`
**Syntax to use:** `#pragma plugin("fast")`

### Global Functions
- `double abs(double x)`
- `double acos(double x)`
- `double acosh(double x)`
- `double asin(double x)`
- `double asinh(double x)`
- `double atan(double x)`
- `double atan2(double y, double x)`
- `double atan2_approx(double y, double x)`
- `double atan_approx(double x)`
- `double atanh(double x)`
- `double blend(double a, double b, double x, double y)`
- `double cbrt(double x)`
- `double ceil(double x)`
- `double copysign(double x, double y)`
- `double cos(double x)`
- `double cos_approx(double x)`
- `double cosh(double x)`
- `double cospi(double x)`
- `double erf(double x)`
- `double erfc(double x)`
- `double exp(double x)`
- `double exp10(double x)`
- `double exp2(double x)`
- `double expm1(double x)`
- `double fdim(double x, double y)`
- `double floor(double x)`
- `double fma(double x, double y, double z)`
- `double fmod(double x, double y)`
- `double frfrexp(double x)`
- `double hypot(double x, double y)`
- `double hypot(double x, double y, double z)`
- `double ldexp(double n, int x)`
- `double lgamma(double x)`
- `double log(double x)`
- `double log10(double x)`
- `double log1p(double x)`
- `double log2(double x)`
- `double max(double x, double y)`
- `double min(double x, double y)`
- `double nextafter(double x, double y)`
- `double pow(double x, double y)`
- `double remainder(double x, double y)`
- `double rint(double x)`
- `double round(double x)`
- `double sin(double x)`
- `double sin_approx(double x)`
- `double sinh(double x)`
- `double sinpi(double a)`
- `double sqrt(double x)`
- `double tan(double x)`
- `double tanh(double x)`
- `double tgamma(double x)`
- `double trunc(double x)`
- `int expfrexp(double x)`
- `int ilogb(double x, int n)`
- `int16 parse_int16(const string&)`
- `int16 parse_int16(const string&, const int)`
- `int32 parse_int32(const string&)`
- `int32 parse_int32(const string&, const int)`
- `int64 parse_int64(const string&)`
- `int64 parse_int64(const string&, const int)`
- `int8 parse_int8(const string&)`
- `int8 parse_int8(const string&, const int)`
- `string read_file(const string &in, mode = mode_read, creation = creation_open_existing, caching = caching_all, flag = flag_multiplexable)`
- `uint16 parse_uint16(const string&)`
- `uint16 parse_uint16(const string&, const int)`
- `uint32 parse_uint32(const string&)`
- `uint32 parse_uint32(const string&, const int)`
- `uint64 parse_uint64(const string&)`
- `uint64 parse_uint64(const string&, const int)`
- `uint8 parse_uint8(const string&)`
- `uint8 parse_uint8(const string&, const int)`
- `void write_file(const string &in, const string &in, mode = mode_write, creation = creation_if_needed, caching = caching_all, flag = flag_multiplexable)`

### Enums
#### Enum `caching`
- `caching_all`
- `caching_none`
- `caching_only_metadata`
- `caching_reads`
- `caching_reads_and_metadata`
- `caching_safety_barriers`
- `caching_temporary`
- `caching_unchanged`

#### Enum `creation`
- `creation_always_new`
- `creation_if_needed`
- `creation_only_if_not_exist`
- `creation_open_existing`
- `creation_truncate_existing`

#### Enum `flag`
- `flag_anonymous_inode`
- `flag_byte_lock_insanity`
- `flag_disable_parallelism`
- `flag_disable_prefetching`
- `flag_disable_safety_barriers`
- `flag_disable_safety_unlinks`
- `flag_maximum_prefetching`
- `flag_multiplexable`
- `flag_none`
- `flag_unlink_on_first_close`
- `flag_win_create_case_sensitive_directory`
- `flag_win_disable_sparse_file_creation`
- `flag_win_disable_unlink_emulation`

#### Enum `mode`
- `mode_append`
- `mode_attr_read`
- `mode_attr_write`
- `mode_none`
- `mode_read`
- `mode_unchanged`
- `mode_write`

---
## Plugin: `git`
**Syntax to use:** `#pragma plugin("git")`

### Global Functions
- `funcdef int git_repository_match_callback(git_repository@ repo, const string&in path, const string&in user_data)`
- `int git_last_error_class()`
- `string git_last_error_text()`

### Classes
#### Class `git_repository`
##### Behaviours / Constructors
- `git_repository@r()`
##### Methods
- `bool close()`
- `bool get_active() property`
- `git_repository_commit@ commit(const string&in author, const string&in author_email, const string&in committer, const string&in committer_email, const string&in message, const string&in ref="HEAD")`
- `git_repository_commit@ commit(const string&in author, const string&in author_email, const string&in message, const string&in ref="HEAD")`
- `git_repository_commit@ commit_lookup(const string&in oid)`
- `git_repository_commit_iterator@ commit_iterate(string[]@ path_filter={}, const string&in author_filter='', const string&in message_filter='', uint64 min_time_filter=0, uint64 max_time_filter=0, uint start=0, uint count=0)`
- `git_repository_entry@ get_entry(uint index)`
- `int add(const string&in path)`
- `int add_all(string[]@ paths, int flags = 0)`
- `int add_all(string[]@ paths, int flags, git_repository_match_callback@ callback, const string&in callback_data = "")`
- `int create(const string&in path)`
- `int get_entry_count() property`
- `int get_is_empty() property`
- `int open(const string&in path)`
- `int remove(const string&in path)`
- `int remove_all(string[]@ paths)`
- `int remove_all(string[]@ paths, git_repository_match_callback@ callback, const string&in callback_data = "")`
- `int update_all(string[]@ paths)`
- `int update_all(string[]@ paths, git_repository_match_callback@ callback, const string&in callback_data = "")`
- `string commit_diff(git_repository_commit@+ commit1, git_repository_commit@+ commit2, uint context_lines=3, uint interhunk_lines=0, uint flags=0, uint format=1, string[]@+ pathspec={}, const string&in old_prefix="a", const string&in new_prefix="b")`
- `string get_path() property`
- `string get_workdir() property`

#### Class `git_repository_commit`
##### Methods
- `const string get_author() property`
- `const string get_author_email() property`
- `const string get_body() property`
- `const string get_committer() property`
- `const string get_committer_email() property`
- `const string get_id() property`
- `const string get_message() property`
- `const string get_raw_header() property`
- `git_repository_commit@ get_parent(uint)`
- `int get_parent_count() property`
- `string get_summary() property`
- `uint get_time() property`

#### Class `git_repository_commit_iterator`
##### Methods
- `bool opPostInc()`
- `git_repository_commit@ get_commit() property`
- `git_repository_commit@ opImplCast()`

#### Class `git_repository_entry`
##### Methods
- `string get_oid() property`
- `string get_path() property`
- `uint get_ctime() property`
- `uint get_file_size() property`
- `uint get_mtime() property`

---
## Plugin: `legacy_sound`
**Syntax to use:** `#pragma plugin("legacy_sound")`

### Global Functions
- `array<string>@ get_sound_input_devices() property`
- `array<string>@ get_sound_output_devices() property`
- `bool get_SOUND_AVAILABLE() property`
- `bool get_sound_global_hrtf() property`
- `bool pack_set_global_identifier(const string&in)`
- `float get_sound_master_volume() property`
- `funcdef bool sound_seek_callback(uint, string)`
- `funcdef int sound_read_callback(string &out, uint, string)`
- `funcdef uint sound_length_callback(string)`
- `funcdef void sound_close_callback(string)`
- `uint get_sound_input_device() property`
- `uint get_sound_input_device_count() property`
- `uint get_sound_output_device() property`
- `uint get_sound_output_device_count() property`
- `void set_sound_global_hrtf(bool) property`
- `void set_sound_input_device(uint) property`
- `void set_sound_master_volume(float) property`
- `void set_sound_output_device(uint) property`

### Global Properties
- `const int PACK_OPEN_MODE_APPEND`
- `const int PACK_OPEN_MODE_CREATE`
- `const int PACK_OPEN_MODE_NONE`
- `const int PACK_OPEN_MODE_READ`
- `const string pack_global_identifier`
- `mixer@ sound_default_mixer`
- `pack@ sound_default_pack`

### Classes
#### Class `mixer`
##### Behaviours / Constructors
- `mixer @m()`
##### Methods
- `bool get_pan_sliding() const property`
- `bool get_pitch_sliding() const property`
- `bool get_sliding() const property`
- `bool get_volume_sliding() const property`
- `bool set_fx(const string &in, int = -1)`
- `bool set_mixer(mixer@ = null)`
- `bool set_position(float, float, float, float, float, float, float, float, float)`
- `bool slide_pan(float, uint)`
- `bool slide_pitch(float, uint)`
- `bool slide_volume(float, uint)`
- `float get_pan() const property`
- `float get_pitch() const property`
- `float get_volume() const property`
- `void set_hrtf(bool = true)`
- `void set_pan(float) property`
- `void set_pitch(float) property`
- `void set_volume(float) property`

#### Class `pack`
##### Behaviours / Constructors
- `pack @p()`
##### Methods
- `bool add_file(const string &in disc_filename, const string& in pack_filename, bool allow_replace = false)`
- `bool add_memory(const string &in pack_filename, const string& in data, bool allow_replace = false)`
- `bool close()`
- `bool delete_file(const string &in pack_filename)`
- `bool file_exists(const string &in pack_filename) const`
- `bool get_active() const property`
- `bool open(const string &in, uint = PACK_OPEN_MODE_READ, bool = false)`
- `bool raw_seek(int offset)`
- `bool set_pack_identifier(const string&in)`
- `bool stream_close(uint index)`
- `string get_file_name(int index) const`
- `string read_file(const string &in pack_filename, uint offset_in_file, uint read_byte_count) const`
- `string stream_read(uint index, uint read_byte_count) const`
- `string[]@ list_files() const`
- `uint get_file_offset(const string &in pack_filename) const`
- `uint get_file_size(const string &in pack_filename) const`
- `uint get_size() const property`
- `uint stream_open(const string &in pack_filename, uint offset_in_file) const`
- `uint stream_pos(uint index) const`
- `uint stream_seek(uint index, uint offset, int origin) const`
- `uint stream_size(uint index) const`

#### Class `sound`
##### Behaviours / Constructors
- `sound @s()`
##### Properties
- `const string loaded_filename`
##### Methods
- `bool close()`
- `bool get_active() const property`
- `bool get_pan_sliding() const property`
- `bool get_paused() const property`
- `bool get_pitch_sliding() const property`
- `bool get_playing() const property`
- `bool get_sliding() const property`
- `bool get_volume_sliding() const property`
- `bool load(const string &in filename, pack@ packfile = @sound_default_pack, bool allow_preloads = !system_is_mobile)`
- `bool load(sound_close_callback@, sound_length_callback@, sound_read_callback@, sound_seek_callback@, const string &in, const string&in = "")`
- `bool load(string& data, uint size, const string&in preload_filename = "", bool legacy_encrypt = false)`
- `bool load_url(const string &in url)`
- `bool pause()`
- `bool play(bool reset_loop_state = true)`
- `bool play_looped()`
- `bool play_wait()`
- `bool push_memory(const string &in data, bool end_stream = false, int pcm_rate = 0, int pcm_channels = 0)`
- `bool seek(float position)`
- `bool set_fx(const string &in fx, int index = -1)`
- `bool set_mixer(mixer@ mixer = null)`
- `bool set_position(float listener_x, float listener_y, float listener_z, float sound_x, float sound_y, float sound_z, float rotation = 0.0, float pan_step = 1.0, float volume_step = 1.0)`
- `bool slide_pan(float, uint)`
- `bool slide_pitch(float, uint)`
- `bool slide_volume(float, uint)`
- `bool stop()`
- `bool stream(const string &in filename, pack@ containing_pack = sound_default_pack)`
- `double get_pitch_lower_limit() const property`
- `float get_length() const property`
- `float get_pan() const property`
- `float get_pitch() const property`
- `float get_position() const property`
- `float get_volume() const property`
- `void set_hrtf(bool enable = true)`
- `void set_length(float length = 0.0)`
- `void set_pan(float) property`
- `void set_pitch(float) property`
- `void set_volume(float) property`

#### Class `sound_environment`
##### Behaviours / Constructors
- `sound_environment @s()`
##### Methods
- `bool add_box(const string&in, float, float, float, float, float, float)`
- `bool add_material(const string&in, float, float, float, float, float, float, float, bool = false)`
- `mixer@ new_mixer()`
- `sound@ new_sound()`
- `void set_listener(float, float, float, float)`
- `void update()`

---
## Plugin: `redis`
**Syntax to use:** `#pragma plugin("redis")`

### Classes
#### Class `blocking_redis_subscriber`
##### Behaviours / Constructors
- `blocking_redis_subscriber@ f()`
##### Methods
- `array<string>@ get_messages(const string&in)`
- `bool get_is_running() const property`
- `bool has_messages(const string&in)`
- `bool subscribe(array<string>@)`
- `int get_port() const property`
- `string get_host() const property`
- `string get_last_error() const property`
- `string get_password() const property`
- `void set_host(const string&in) property`
- `void set_password(const string&in) property`
- `void set_port(int) property`
- `void stop()`

#### Class `redis_client`
##### Behaviours / Constructors
- `redis_client@ f()`
##### Methods
- `array<array<double>@>@ geopos(const string&in, array<string>@)`
- `array<redis_value@>@ pipeline_execute()`
- `array<string>@ acl_getuser(const string&in)`
- `array<string>@ acl_list()`
- `array<string>@ client_list()`
- `array<string>@ georadius(const string&in, double, double, double, const string&in, bool = false, bool = false, bool = false, int64 = -1)`
- `array<string>@ georadiusbymember(const string&in, const string&in, double, const string&in, bool = false, bool = false, bool = false, int64 = -1)`
- `array<string>@ hkeys(const string&in)`
- `array<string>@ hvals(const string&in)`
- `array<string>@ keys(const string&in)`
- `array<string>@ lrange(const string&in, int64, int64)`
- `array<string>@ mget(array<string>@)`
- `array<string>@ scan(int64, const string&in = "", int64 = -1)`
- `array<string>@ sdiff(array<string>@)`
- `array<string>@ sinter(array<string>@)`
- `array<string>@ smembers(const string&in)`
- `array<string>@ srandmember_count(const string&in, int64)`
- `array<string>@ sunion(array<string>@)`
- `array<string>@ zrange(const string&in, int64, int64, bool = false)`
- `array<string>@ zrangebyscore(const string&in, double, double, bool = false, int64 = -1, int64 = -1)`
- `array<string>@ zrevrange(const string&in, int64, int64, bool = false)`
- `bool acl_deluser(const string&in)`
- `bool acl_setuser(const string&in, const string&in)`
- `bool bgrewriteaof()`
- `bool bgsave()`
- `bool client_pause(int64)`
- `bool client_setname(const string&in)`
- `bool config_resetstat()`
- `bool config_rewrite()`
- `bool config_set(const string&in, const string&in)`
- `bool connect()`
- `bool connect(const string&in, int, const string&in = "", int = 0)`
- `bool del(const string&in)`
- `bool discard()`
- `bool exists(const string&in)`
- `bool expire(const string&in, int64)`
- `bool flushall()`
- `bool flushdb()`
- `bool get_is_connected() const property`
- `bool getbit(const string&in, int64)`
- `bool hexists(const string&in, const string&in)`
- `bool hset(const string&in, const string&in, const string&in)`
- `bool hsetnx(const string&in, const string&in, const string&in)`
- `bool lset(const string&in, int64, const string&in)`
- `bool ltrim(const string&in, int64, int64)`
- `bool migrate(const string&in, int, const string&in, int, int, bool = false, bool = false)`
- `bool mset(array<string>@)`
- `bool mset(dictionary@)`
- `bool multi()`
- `bool pfadd(const string&in, array<string>@)`
- `bool pfadd(const string&in, const string&in)`
- `bool pfmerge(const string&in, array<string>@)`
- `bool pipeline_add(array<string>@)`
- `bool pipeline_begin()`
- `bool psetex(const string&in, int64, const string&in)`
- `bool restore(const string&in, int64, const string&in, bool = false)`
- `bool save()`
- `bool script_exists(const string&in)`
- `bool script_flush()`
- `bool select(int64)`
- `bool set(const string&in, const string&in, int64 = 0)`
- `bool setbit(const string&in, int64, bool)`
- `bool setex(const string&in, int64, const string&in)`
- `bool setnx(const string&in, const string&in)`
- `bool sismember(const string&in, const string&in)`
- `bool smove(const string&in, const string&in, const string&in)`
- `bool unwatch()`
- `bool watch(array<string>@)`
- `bool watch(const string&in)`
- `dictionary@ config_get(const string&in)`
- `dictionary@ hgetall(const string&in)`
- `dictionary@ memory_stats()`
- `dictionary@ object(const string&in, const string&in)`
- `double geodist(const string&in, const string&in, const string&in, const string&in = "m")`
- `double hincrbyfloat(const string&in, const string&in, double)`
- `double zincrby(const string&in, double, const string&in)`
- `double zscore(const string&in, const string&in)`
- `int get_database() const property`
- `int get_port() const property`
- `int get_timeout() const property`
- `int64 append(const string&in, const string&in)`
- `int64 bitcount(const string&in, int64 = -1, int64 = -1)`
- `int64 bitop(const string&in, const string&in, array<string>@)`
- `int64 bitpos(const string&in, bool, int64 = -1, int64 = -1)`
- `int64 client_id()`
- `int64 dbsize()`
- `int64 decr(const string&in)`
- `int64 decrby(const string&in, int64)`
- `int64 geoadd(const string&in, double, double, const string&in)`
- `int64 hdel(const string&in, const string&in)`
- `int64 hincrby(const string&in, const string&in, int64)`
- `int64 hlen(const string&in)`
- `int64 incr(const string&in)`
- `int64 incrby(const string&in, int64)`
- `int64 lastsave()`
- `int64 linsert(const string&in, const string&in, const string&in, const string&in)`
- `int64 llen(const string&in)`
- `int64 lpush(const string&in, const string&in)`
- `int64 lrem(const string&in, int64, const string&in)`
- `int64 memory_usage(const string&in, int = -1)`
- `int64 pfcount(array<string>@)`
- `int64 pfcount(const string&in)`
- `int64 publish(const string&in, const string&in)`
- `int64 rpush(const string&in, const string&in)`
- `int64 sadd(const string&in, array<string>@)`
- `int64 sadd(const string&in, const string&in)`
- `int64 scard(const string&in)`
- `int64 setrange(const string&in, int64, const string&in)`
- `int64 srem(const string&in, const string&in)`
- `int64 strlen(const string&in)`
- `int64 ttl(const string&in)`
- `int64 zadd(const string&in, double, const string&in)`
- `int64 zcard(const string&in)`
- `int64 zcount(const string&in, double, double)`
- `int64 zrank(const string&in, const string&in)`
- `int64 zrem(const string&in, const string&in)`
- `int64 zremrangebyrank(const string&in, int64, int64)`
- `int64 zremrangebyscore(const string&in, double, double)`
- `int64 zrevrank(const string&in, const string&in)`
- `redis_value@ eval(const string&in, array<string>@ = null, array<string>@ = null)`
- `redis_value@ evalsha(const string&in, array<string>@ = null, array<string>@ = null)`
- `redis_value@ exec()`
- `redis_value@ execute(array<string>@)`
- `string acl_whoami()`
- `string client_getname()`
- `string dump(const string&in)`
- `string geohash(const string&in, const string&in)`
- `string get(const string&in)`
- `string get_host() const property`
- `string get_last_error() const property`
- `string get_password() const property`
- `string getrange(const string&in, int64, int64)`
- `string hget(const string&in, const string&in)`
- `string info(const string&in = "")`
- `string lindex(const string&in, int64)`
- `string lpop(const string&in)`
- `string memory_doctor()`
- `string ping(const string&in = "")`
- `string rpop(const string&in)`
- `string script_load(const string&in)`
- `string spop(const string&in)`
- `string srandmember(const string&in)`
- `string type(const string&in)`
- `void disconnect()`
- `void set_database(int) property`
- `void set_host(const string&in) property`
- `void set_password(const string&in) property`
- `void set_port(int) property`
- `void set_timeout(int) property`

#### Class `redis_value`
##### Behaviours / Constructors
- `redis_value@ f()`
##### Methods
- `array<redis_value@>@ get_array() const`
- `bool get_is_array() const property`
- `bool get_is_error() const property`
- `bool get_is_integer() const property`
- `bool get_is_nil() const property`
- `bool get_is_string() const property`
- `int64 get_integer() const`
- `string get_string() const`

### Enums
#### Enum `redis_type`
- `REDIS_TYPE_HASH`
- `REDIS_TYPE_LIST`
- `REDIS_TYPE_NONE`
- `REDIS_TYPE_SET`
- `REDIS_TYPE_STRING`
- `REDIS_TYPE_ZSET`

---
## Plugin: `sqlite`
**Syntax to use:** `#pragma plugin("sqlite")`

### Global Functions
- `funcdef int sqlite3authorizer(string, int, string, string, string, string)`

### Classes
#### Class `pack_interface`
##### Methods
- `sqlite_pack@ opCast()`

#### Class `sqlite3`
##### Behaviours / Constructors
- `sqlite3@ db()`
- `sqlite3@ db(const string&in, int=6)`
##### Methods
- `bool get_active() property`
- `int close()`
- `int execute(const string&in, string[][]@=null)`
- `int get_last_error()`
- `int limit(int id, int val)`
- `int open(const string&in, int=6)`
- `int set_authorizer(sqlite3authorizer@, const string&in="")`
- `int64 get_last_insert_rowid() property`
- `int64 get_rows_changed() property`
- `int64 get_total_rows_changed() property`
- `sqlite3statement@ prepare(const string&in, int&out=void)`
- `string get_last_error_text()`
- `void set_last_insert_rowid(int64) property`

#### Class `sqlite3statement`
##### Methods
- `double column_double(int)`
- `int bind_blob(int, const string&in, bool=true)`
- `int bind_double(int, double)`
- `int bind_int(int, int)`
- `int bind_int64(int, int64)`
- `int bind_null(int)`
- `int bind_param_index(const string&in)`
- `int bind_text(int, const string&in, bool=true)`
- `int clear_bindings()`
- `int column_bytes(int)`
- `int column_int(int)`
- `int column_type(int)`
- `int get_bind_param_count() property`
- `int get_column_count() property`
- `int reset()`
- `int step()`
- `int64 column_int64(int)`
- `string bind_param_name(int)`
- `string column_blob(int)`
- `string column_decltype(int)`
- `string column_name(int)`
- `string column_text(int)`
- `string get_expanded_sql_statement() property`
- `string get_sql_statement() property`

#### Class `sqlite_pack`
##### Behaviours / Constructors
- `sqlite_pack @p()`
##### Methods
- `bool add_directory(const string &in dir, const bool allow_replace = false)`
- `bool add_file(const string &in disc_filename, const string& in pack_filename, bool allow_replace = false)`
- `bool add_memory(const string &in pack_filename, const string& in data, bool allow_replace = false)`
- `bool add_stream(const string &in internal_name, datastream@ ds, const bool allow_replace=false)`
- `bool close()`
- `bool create(const string &in filename, const string&in key = "")`
- `bool delete_file(const string &in pack_filename)`
- `bool extract_file(const string &in internal_name, const string &in file_on_disk)`
- `bool file_exists(const string &in pack_filename) const`
- `bool get_active() const property`
- `bool open(const string &in filename, const int mode = SQLITE_PACK_OPEN_MODE_READ_ONLY, const string& key = "")`
- `bool open(const string &in filename, const string &in key = "", const bool rw = false)`
- `bool rekey(const string& key)`
- `bool rename_file(const string& old, const string& new_)`
- `datastream@ get_file(const string&in file_name, const bool rw = false)`
- `dictionary@[]@ exec(const string& sql)`
- `int64 get_file_count() const property`
- `pack_interface@ opImplCast()`
- `sqlite3statement@ prepare(const string& statement, const bool persistant = false)`
- `string get_file_name(int64 index) const`
- `string read_file(const string &in pack_filename, uint offset_in_file, uint read_byte_count) const`
- `string[]@ find(const string& what, const sqlite_pack_find_mode mode = SQLITE_PACK_FIND_MODE_LIKE)`
- `string[]@ list_files() const`
- `uint get_file_size(const string &in pack_filename) const`
- `uint get_size() const property`
- `void allocate_file(const string& file_name, const int64 size, const bool allow_replace = false)`
- `void clear()`

### Enums
#### Enum `pack_open_mode`
- `SQLITE_PACK_OPEN_MODE_CREATE`
- `SQLITE_PACK_OPEN_MODE_FULL_MUTEX`
- `SQLITE_PACK_OPEN_MODE_MEMORY`
- `SQLITE_PACK_OPEN_MODE_NO_FOLLOW`
- `SQLITE_PACK_OPEN_MODE_NO_MUTEX`
- `SQLITE_PACK_OPEN_MODE_PRIVATE_CACHE`
- `SQLITE_PACK_OPEN_MODE_READ_ONLY`
- `SQLITE_PACK_OPEN_MODE_READ_WRITE`
- `SQLITE_PACK_OPEN_MODE_SHARED_CACHE`
- `SQLITE_PACK_OPEN_MODE_URI`

#### Enum `sqlite_pack_find_mode`
- `SQLITE_PACK_FIND_MODE_GLOB`
- `SQLITE_PACK_FIND_MODE_LIKE`
- `SQLITE_PACK_FIND_MODE_REGEXP`

---
## Plugin: `systemd_notify`
**Syntax to use:** `#pragma plugin("systemd_notify")`

### Global Functions
- `int systemd_notify(const string&in state)`

---
## Plugin: `test_plugin`
**Syntax to use:** `#pragma plugin("test_plugin")`

### Global Functions
- `void do_exception()`
- `void do_test()`

---
## Plugin: `unicode`
**Syntax to use:** `#pragma plugin("unicode")`

### Classes
#### Class `string`
##### Methods
- `bool has_script(const string&) const`
- `bool is_alphabetic() const`
- `bool is_alphanumeric() const`
- `bool is_control() const`
- `bool is_nfc() const`
- `bool is_nfd() const`
- `bool is_nfkc() const`
- `bool is_nfkd() const`
- `bool is_noncharacter() const`
- `bool is_numeric() const`
- `bool is_private_use() const`
- `bool is_reserved() const`
- `bool is_supplementary() const`
- `bool is_surrogate() const`
- `bool is_valid_char() const`
- `bool is_valid_scalar() const`
- `bool is_valid_unicode() const`
- `bool is_whitespace() const`
- `int collate(const string&, const bool) const`
- `int compare(const string&, const bool) const`
- `string casefold() const`
- `string get_script() const`
- `string lowercase() const`
- `string lowercase(const string&) const`
- `string titlecase() const`
- `string titlecase(const string&) const`
- `string to_nfc() const`
- `string to_nfd() const`
- `string to_nfkc() const`
- `string to_nfkd() const`
- `string to_unaccented() const`
- `string uppercase() const`
- `string uppercase(const string&) const`
- `uint64[]@ find(const string&, const bool) const`
- `unicode::general_category general_category() const`

### Enums
#### Enum `general_category`
- `CC`
- `CF`
- `CN`
- `CO`
- `CS`
- `LL`
- `LM`
- `LO`
- `LT`
- `LU`
- `MC`
- `ME`
- `MN`
- `ND`
- `NL`
- `NO`
- `PC`
- `PD`
- `PE`
- `PF`
- `PI`
- `PO`
- `PS`
- `SC`
- `SK`
- `SM`
- `SO`
- `ZL`
- `ZP`
- `ZS`
