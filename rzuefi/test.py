import ctypes
from ctypes import *
from ctypes.util import find_library

lib_name = find_library("rz_core")
if not lib_name:
    raise ImportError("No native rz_core library")

try:
    from ctypes import CDLL
    lib = CDLL(lib_name)
except ImportError:
    pass

try:
    from ctypes import WinDLL
    lib = WinDLL(lib_name)
except ImportError:
    pass

class struct_rz_list_iter_t(Structure):
    pass

class struct_rz_analysis_t(Structure):
    pass

class struct_rz_list_t(Structure):
    pass

class struct_rz_list_iter_t:
    _pack = 1
    _fields_ = [
    ('data', ctypes.POINTER(None)),
    ('n', (struct_rz_list_iter_t)),
    ('p', (struct_rz_list_iter_t)),
    ]

class struct_rz_list_t:
    _fields_ = [
    ('head', (struct_rz_list_iter_t)),
    ('tail', (struct_rz_list_iter_t)),
    ('free', ctypes.CFUNCTYPE(None, ctypes.POINTER(None))),
    ('length', ctypes.c_int32),
    ('sorted', ctypes.c_bool),
    ]

class struct_rz_config_t:
    _fields_ = [
        ('lock', ctypes.c_int),
        ('user', ctypes.c_void_p),
        ('c_printf', ctypes.c_void_p),
        ('nodes', ctypes.POINTER(struct_rz_list_t)),
        ('ht', ctypes.c_void_p),
    ]

struct_rz_analysis_t._fields_ = [
    ('cpu', ctypes.POINTER(ctypes.c_char)),
    ('os', ctypes.POINTER(ctypes.c_char)),
    ('bits', ctypes.c_int32),
    ('lineswidth', ctypes.c_int32),
    ('big_endian', ctypes.c_int32),
    ('sleep', ctypes.c_int32),
    ('cpp_abi', ctypes.c_void_p),
    ('plugin_data', ctypes.POINTER(None)),
    ('user', ctypes.POINTER(None)),
    ('gp', ctypes.c_uint64),
    ('bb_tree', ctypes.c_void_p),
    ('fcns', ctypes.c_void_p),
    ('ht_addr_fun', ctypes.c_void_p),
    ('ht_name_fun', ctypes.c_void_p),
    ('reg', ctypes.c_void_p),
    ('last_disasm_reg', ctypes.POINTER(ctypes.c_ubyte)),
    ('syscall', ctypes.c_void_p),
    ('diff_ops', ctypes.c_int32),
    ('diff_thbb', ctypes.c_double),
    ('diff_thfcn', ctypes.c_double),
    ('iob', ctypes.c_void_p),
    ('flb', ctypes.c_void_p),
    ('flg_class_set', ctypes.c_void_p),
    ('flg_class_get', ctypes.c_void_p),
    ('flg_fcn_set', ctypes.c_void_p),
    ('binb', ctypes.c_void_p),
    ('coreb', ctypes.c_void_p),
    ('maxreflines', ctypes.c_int32),
    ('esil_goto_limit', ctypes.c_int32),
    ('pcalign', ctypes.c_int32),
    ('esil', ctypes.c_void_p),
    ('cur', ctypes.c_void_p),
    ('limit', ctypes.c_void_p),
    ('plugins', ctypes.c_void_p),
    ('sdb_noret', ctypes.c_void_p),
    ('sdb_fmts', ctypes.c_void_p),
    ('sdb_zigns', ctypes.c_void_p),
    ('ht_xrefs_from',ctypes.c_void_p),
    ('ht_xrefs_to', ctypes.c_void_p),
    ('recursive_noreturn', ctypes.c_bool),
    ('zign_spaces', ctypes.c_void_p),
    ('zign_path', ctypes.POINTER(ctypes.c_char)),
    ('sdb', ctypes.c_void_p),
    ('sdb_pins', ctypes.c_void_p),
    ('addr_hints', ctypes.c_void_p),
    ('arch_hints', ctypes.c_void_p),
    ('bits_hints', ctypes.c_void_p),
    ('hint_cbs', ctypes.c_void_p),
    ('meta', ctypes.c_void_p),
    ('meta_spaces', ctypes.c_void_p),
    ('type_db', ctypes.c_void_p),
    ('sdb_cc', ctypes.c_void_p),
    ('sdb_classes', ctypes.c_void_p),
    ('sdb_classes_attrs', ctypes.c_void_p),
    ('cb', ctypes.c_void_p),
    ('opt', ctypes.c_void_p),
    ('reflines', ctypes.c_void_p),
    ('columnSort', ctypes.c_void_p),
    ('stackptr', ctypes.c_int32),
    ('log', ctypes.c_void_p),
    ('read_at', ctypes.c_void_p),
    ('verbose', ctypes.c_bool),
    ('flag_get', ctypes.c_void_p),
    ('ev', ctypes.c_void_p),
    ('imports', ctypes.c_void_p),
    ('visited', ctypes.c_void_p),
    ('constpool', ctypes.c_void_p),
    ('leaddrs', ctypes.c_void_p),
    ('arch_target', ctypes.c_void_p),
    ('arch_profile', ctypes.c_void_p),
    ]

class struct_rz_core_t:
    _fields_ = [
    ('bin', ctypes.c_void_p),
    ('plugins', ctypes.c_void_p),
    ('config', ctypes.c_void_p),
    ('offset', ctypes.c_uint64),
    ('prompt_offset', ctypes.c_uint64),
    ('blocksize', ctypes.c_uint32),
    ('blocksize_max', ctypes.c_uint32),
    ('block', ctypes.c_void_p),
    ('yank_buf', ctypes.c_void_p),
    ('yank_addr', ctypes.c_uint64),
    ('tmpseek', ctypes.c_bool),
    ('vmode', ctypes.c_bool),

    ('cons', ctypes.c_void_p),
    ('io', ctypes.POINTER(struct_rz_io_t)),
    ('file', ctypes.c_void_p),
    ('files', ctypes.c_void_p),
    ('num', ctypes.c_void_p),
    ('rc', ctypes.c_uint64),
    ('lib', ctypes.c_void_p),
    ('rcmd', ctypes.c_void_p),
    ('root_cmd_descriptor', ctypes.c_void_p),
    ('cmd_descriptors', ctypes.c_void_p),
    ('analysis', ctypes.POINTER(struct_rz_analysis_t)),
    ('rasm', ctypes.c_void_p),
    ('times', ctypes.c_void_p),
    ('parser', ctypes.c_void_p),
    ('print', c_void_p),
    ('lang', c_void_p),
    ('dbg', c_void_p),
    ('flags', c_void_p),
    ('search', c_void_p),
    ('egg', c_void_p),
    ('graph', c_void_p),
    ('panels_root', c_void_p),
    ('panels', c_void_p),
    ('cmdqueue', c_void_p),
    ('lastcmd', ctypes.POINTER(ctypes.c_char)),
    ('cmdlog', ctypes.POINTER(ctypes.c_char)),
    ('cfglog', ctypes.c_bool),
    ('cmdrepeat', ctypes.c_int32),
    ('cmdtimes', ctypes.POINTER(ctypes.c_char)),
    ('cmd_in_backticks', ctypes.c_bool),
    ('rtr_n', ctypes.c_int32),
    ('rtr_host', ctypes.c_void_p),
    ('asmqjmps', ctypes.POINTER(ctypes.c_uint64)),
    ('asmqjmps_count', ctypes.c_int32),
    ('asmqjmps_size', ctypes.c_int32),
    ('is_asmqjmps_letter', ctypes.c_bool),
    ('keep_asmqjmps', ctypes.c_bool),
    ('visual', ctypes.c_void_p),
    ('http_up', ctypes.c_int32),
    ('gdbserver_up', ctypes.c_int32),
    ('printidx',  ctypes.c_void_p),
    ('stkcmd', ctypes.POINTER(ctypes.c_char)),
    ('in_search', ctypes.c_bool),
    ('watchers', c_void_p),
    ('scriptstack', c_void_p),
    ('tasks',  ctypes.c_void_p),
    ('max_cmd_depth', ctypes.c_int32),
    ('switch_file_view', ctypes.c_ubyte),
    ('sdb', c_void_p),
    ('incomment', ctypes.c_int32),
    ('curtab', ctypes.c_int32),
    ('seltab', ctypes.c_int32),
    ('cmdremote', c_void_p),
    ('lastsearch', c_void_p),
    ('cmdfilter', c_void_p),
    ('break_loop', ctypes.c_bool),
    ('binat', ctypes.c_bool),
    ('fixedbits', ctypes.c_bool),
    ('fixedarch', ctypes.c_bool),
    ('fixedblock', ctypes.c_bool),
    ('table_query', ctypes.POINTER(ctypes.c_char)),
    ('c2', c_void_p),
    ('autocomplete', c_void_p),
    ('autocomplete_type', ctypes.c_int32),
    ('maxtab', ctypes.c_int32),
    ('ev', c_void_p),
    ('gadgets', c_void_p),
    ('scr_gadgets', ctypes.c_bool),
    ('log_events', ctypes.c_bool),
    ('ropchain', c_void_p),
    ('use_tree_sitter_r2cmd', ctypes.c_bool),
    ('use_rzshell_autocompletion', ctypes.c_bool),
    ('seek_history', c_void_p),
    ('marks', c_void_p),
    ('marks_init', c_void_p),
    ('rz_main_rz_find', c_void_p),
    ('rz_main_rz_diff', c_void_p),
    ('rz_main_rz_bin', c_void_p),
    ('rz_main_rz_run', c_void_p),
    ('rz_main_rz_gg', c_void_p),
    ('rz_main_rz_asm', c_void_p),
    ('rz_main_rz_ax', c_void_p)
    ]

core = lib.rz_core_new()
lib.rz_core_file_open(core, ctypes.create_string_buffer(b"/bin/ls"), 4, 0) 
print("Success")
