import ctypes
import platform
import sys

libc: ctypes.CDLL | None = None
match platform.system():
    case "Linux":
        libc = ctypes.cdll.LoadLibrary("libc.so.6")
    case "Windows":
        libc = ctypes.cdll.msvcrt
    case "Darwin":
        pass
    case _:
        sys.exit(1)

libc.print(b"hello world")
