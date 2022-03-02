import ctypes
import time

st = time.time()
so = ctypes.cdll.LoadLibrary('./_checksig.so')
verify = so.verify
verify.argtypes = [ctypes.c_char_p]
verify.resttype = ctypes.c_void_p
free = so.free
free.argtypes = [ctypes.c_void_p]

ptr = verify('testdata/logs'.encode('utf-8'))
out = ctypes.string_at(ptr)
free(ptr)


print(out.decode('utf-8'))

et = time.time()

print(et - st)
