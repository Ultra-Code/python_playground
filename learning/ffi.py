import ctypes as c
import platform
import sys
from typing import Any


def get_libc() -> Any:
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
libc.print(b"hello world")
