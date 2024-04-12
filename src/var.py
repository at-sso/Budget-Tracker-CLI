import ctypes

from src.const import DLL_FILE


def _random64() -> float:
    # Load the shared library.
    random64_lib = ctypes.CDLL(DLL_FILE)
    # Define the return type to float.
    random64_lib.random64.restype = ctypes.c_float
    return random64_lib.random64()


class __Var:
    extra_message: str = "Good looking!"
    limit: float = _random64()


var = __Var
