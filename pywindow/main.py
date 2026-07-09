import ctypes
import os

lib_path = os.path.abspath("./so/main.so")
lib = ctypes.CDLL(lib_path)

lib.test.argtypes = [ctypes.c_void_p]
lib.test.restype = ctypes.c_int

def init():
    print(str(lib.test()))
    print("Hello from Pywindow!")