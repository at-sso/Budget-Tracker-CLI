__all__ = [
    "prt",
    "inp",
    "clear_terminal",
    "numeric_only",
]

import os as _os
import re as _re
from typing import Callable as _Callable, List as _List, Any as _Any

_ListAny = _List[_Any]

from src.logger import logger as _logger
from src.var import var


def prt(*s: str, i: str = "") -> None:
    """
    The function `prt` logs a function call with the provided arguments and prints the given strings
    with an optional string as a separator.

    @param *s The `*s` parameter in the `prt` function is a variable number of string arguments
    that will be printed.
    @param i The `i` parameter in the `prt` function is an optional string argument used as a separator
    in the printed output.
    """
    _logger.was_called(prt, *s, i)
    return print(*s, i)


def inp(s: str = "") -> str:
    """
    The function `inp` logs a function call with the provided argument and prompts the user for input,
    displaying the provided string as a prompt.

    @param s The `s` parameter in the `inp` function is an optional string argument used as a prompt
    for the user input.

    @return str The function `inp` returns the user input as a string.
    """
    _logger.was_called(inp, s)
    return input(f"{s}\n> ")


def clear_terminal() -> int:
    """
    The function `clear_terminal` clears the terminal screen by calling the appropriate system command
    based on the operating system. If the operating system is Windows, it executes the command "cls";
    otherwise, it executes the command "clear".

    @return The function `clear_terminal` returns an integer representing the exit status of the system
    command execution.
    """
    _logger.was_called(clear_terminal)
    return _os.system("cls" if _os.name == "nt" else "clear")


def numeric_only(
    input_string: str, instance: _Callable[[str], int | float]
) -> int | float:
    """
    The function `numeric_only` sanitizes an input string to contain only numeric characters (digits and
    decimal point), using a regular expression. If the resulting string is empty, it returns 0. Otherwise,
    it calls the provided instance function with the sanitized input string.

    @param input_string The `input_string` parameter in the `numeric_only` function is a string that
    contains alphanumeric characters. This parameter is sanitized to remove any non-numeric characters
    before processing.
    @param instance The `instance` parameter in the `numeric_only` function is a callable object that
    accepts a string argument and returns either an integer or a float value.

    @return The function `numeric_only` returns either an integer or a float value, depending on the
    result of calling the provided instance function with the sanitized input string.
    """
    _logger.was_called(numeric_only, input_string, instance)
    input_string = _re.sub(r"[^0-9.]", "", input_string)
    if input_string == "":
        return var.limit
    try:
        return instance(input_string)
    except ValueError:
        _logger.exc(c=numeric_only, default=True)
        return var.limit
