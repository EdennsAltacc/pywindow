import ctypes
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
lib_path = os.path.join(BASE_DIR, "so", "main.so")
lib = ctypes.CDLL(lib_path)

class Pywindow_Color(ctypes.Structure):
    _fields_ = [
        ("r", ctypes.c_ubyte),
        ("g", ctypes.c_ubyte),
        ("b", ctypes.c_ubyte),
        ("a", ctypes.c_ubyte)
    ]

LOOP_CALLBACK = ctypes.CFUNCTYPE(None)

lib.test.argtypes = [ctypes.c_char_p, ctypes.c_int, ctypes.c_int, LOOP_CALLBACK]
lib.test.restype = ctypes.c_int

lib.begin_drawing.argtypes = []
lib.begin_drawing.restype = None

lib.end_drawing.argtypes = []
lib.end_drawing.restype = None

lib.clear_background.argtypes = [Pywindow_Color]
lib.clear_background.restype = None

_active_callback_holder = None

def begin_drawing():
    lib.begin_drawing()

def end_drawing():
    lib.end_drawing()

def clear_background(color: Pywindow_Color):
    lib.clear_background(color)

def init(title: str, width: int, height: int, loop_function):
    global _active_callback_holder
    _active_callback_holder = LOOP_CALLBACK(loop_function)
    lib.test(title.encode("utf-8"), width, height, _active_callback_holder)