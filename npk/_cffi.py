import os, sys
from cffi import FFI

if sys.platform == 'linux2':
    dllname = 'npk'
elif sys.platform == 'win32' or sys.platform == 'cygwin':
    dllname = 'libnpk.dll'
else:
    dllname = 'libnpk.dylib'

headers = """
typedef int                             NPK_RESULT;
typedef void*                           NPK_PACKAGE;
typedef void*                           NPK_ENTITY;
typedef ptrdiff_t                       NPK_HANDLE;
typedef unsigned int                    NPK_FLAG;
typedef unsigned int                    NPK_HASHKEY;
typedef int                             NPK_TEAKEY;
typedef char                            NPK_CHAR;
typedef const NPK_CHAR*                 NPK_CSTR;
typedef NPK_CHAR*                       NPK_STR;
typedef unsigned int                    NPK_SIZE;
typedef unsigned short                  NPK_NAMESIZE;
typedef char                            NPK_BYTE;
typedef unsigned long long              NPK_64BIT;
typedef int                             NPK_TIME;
typedef int                             bool;

enum { 
    NPK_ENTITY_NULL = 0,
    NPK_ENTITY_TEXTFILE = 1,
    NPK_ENTITY_ENCRYPT_XXTEA = 2,
    NPK_ENTITY_ENCRYPT_TEA = 4,
    NPK_ENTITY_COMPRESS_ZLIB = 8,
    NPK_ENTITY_COMPRESS_BZIP2 = 16,
    NPK_ENTITY_REVERSE = 32
};

NPK_PACKAGE npk_package_open            ( NPK_CSTR filename, NPK_TEAKEY teakey[4] );
bool        npk_package_close           ( NPK_PACKAGE package );
NPK_ENTITY  npk_package_get_entity      ( NPK_PACKAGE package, NPK_CSTR entityname );
NPK_ENTITY  npk_package_get_first_entity( NPK_PACKAGE package );
NPK_CSTR    npk_entity_get_name         ( NPK_ENTITY entity );
NPK_SIZE    npk_entity_get_size         ( NPK_ENTITY entity );
NPK_SIZE    npk_entity_get_packed_size  ( NPK_ENTITY entity );
NPK_SIZE    npk_entity_get_offset       ( NPK_ENTITY entity );
bool        npk_entity_is_ready         ( NPK_ENTITY entity );
NPK_ENTITY  npk_entity_next             ( NPK_ENTITY entity );
bool        npk_entity_read             ( NPK_ENTITY entity, void* buf );
bool        npk_entity_read_partial     ( NPK_ENTITY entity, void* buf, NPK_SIZE offset, NPK_SIZE size );
NPK_STR     npk_error_to_str            ( NPK_RESULT res );

NPK_RESULT  npk_entity_alloc( NPK_ENTITY* lpEntity );
NPK_RESULT  npk_entity_init( NPK_ENTITY entity );
NPK_RESULT  npk_entity_get_current_flag( NPK_ENTITY entity, NPK_FLAG* flag );
NPK_RESULT  npk_entity_get_new_flag( NPK_ENTITY entity, NPK_FLAG* flag );
NPK_RESULT  npk_entity_set_flag( NPK_ENTITY entity, NPK_FLAG flag );
NPK_RESULT  npk_entity_add_flag( NPK_ENTITY entity, NPK_FLAG flag );
NPK_RESULT  npk_entity_sub_flag( NPK_ENTITY entity, NPK_FLAG flag );
NPK_RESULT  npk_entity_write( NPK_ENTITY entity, NPK_HANDLE handle, bool forceProcessing );
NPK_RESULT  npk_entity_export( NPK_ENTITY entity, NPK_CSTR filename, bool forceOverwrite );
NPK_RESULT  npk_package_alloc( NPK_PACKAGE* lpPackage, NPK_TEAKEY teakey[4] );
NPK_RESULT  npk_package_init( NPK_PACKAGE package );
NPK_RESULT  npk_package_save( NPK_PACKAGE package, NPK_CSTR filename, bool forceOverwrite );
NPK_RESULT  npk_package_clear( NPK_PACKAGE package );
NPK_RESULT  npk_package_add_file( NPK_PACKAGE package, NPK_CSTR filename, NPK_CSTR entityname, NPK_ENTITY* lpEntity );
NPK_RESULT  npk_package_add_entity( NPK_PACKAGE package, NPK_ENTITY entity );
NPK_RESULT  npk_package_remove_entity( NPK_PACKAGE package, NPK_ENTITY entity );
NPK_RESULT  npk_package_detach_entity( NPK_PACKAGE package, NPK_ENTITY entity );
NPK_RESULT  npk_package_remove_all_entity( NPK_PACKAGE package );
NPK_RESULT  npk_package_detach_all_entity( NPK_PACKAGE package );
"""

ffi = FFI()
ffi.cdef(headers)
c = ffi.dlopen(dllname)
