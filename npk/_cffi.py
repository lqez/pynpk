import os, sys
from cffi import FFI

if sys.platform == 'linux2':
    dllname = 'libnpk.so'
elif sys.platform == 'win32' or sys.platform == 'cygwin':
    dllname = 'libnpk.dll'
else:
    dllname = 'libnpk.dylib'


ffi = FFI()
ffi.cdef(open(os.path.join(os.path.dirname(__file__),'npk.h')).read())
c = ffi.dlopen(dllname)
