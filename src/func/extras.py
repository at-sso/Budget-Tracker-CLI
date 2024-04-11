import os as _os
import re as _re
from typing import Callable as _Callable

from src.logger import logger

__all__ = [
    "clear_terminal",
    "numeric_only",
]


def clear_terminal() -> int:
    """
    The function `clear_terminal` clears the terminal screen by calling the appropriate system command
    based on the operating system. If the operating system is Windows, it executes the command "cls";
    otherwise, it executes the command "clear".

    @return The function `clear_terminal` returns an integer representing the exit status of the system
    command execution.
    """
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
    logger.was_called(numeric_only)
    input_string = _re.sub(r"[^0-9.]", "", input_string)
    if input_string == "":
        return 0
    try:
        return instance(input_string)
    except ValueError:
        logger.exc(c=numeric_only, default=True)
        return 0
