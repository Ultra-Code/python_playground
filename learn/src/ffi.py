import ctypes as c
import platform
import sys


def get_libc() -> c.CDLL:
    match platform.system():
        case "Linux":
            return c.cdll.LoadLibrary("libc.so.6")
        case "Windows":
            return c.cdll.LoadLibrary("libc.dll")
        case "Darwin":
            return c.cdll.LoadLibrary("liblibc.dylib")
        case _:
            sys.exit(1)


libc = get_libc()
msg = c.c_wchar_p("hello world")
libc.printf(msg)
