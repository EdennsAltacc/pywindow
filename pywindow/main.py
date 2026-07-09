import ctypes
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

lib_path = os.path.join(BASE_DIR, "so", "main.so")
lib = ctypes.CDLL(lib_path)

lib.test.argtypes = []
lib.test.restype = ctypes.c_int

def init():
    print(str(lib.test()))
    print("Hello from Pywindow!")