import platform
import sys

if hasattr(platform, "python_implementation"):
    use_cpython = platform.python_implementation() == "CPython"

if not use_cpython:
    sys.path.insert(1, "/usr/lib/python3.11/site-packages/")