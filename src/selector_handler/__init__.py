from typing import (
    Any,
    Dict as _Dict,
    Callable as _Callable,
    Tuple as _Tuple,
)

from src.var import var

from src.functions import *
from .functions import *
from src.logger import logger

_TupleStrFloatOrNone = _Tuple[str, float] | None


def __if_empty_do_nothing(*msg: str) -> _Tuple[str, float, bool, bool]:
    """
    Check if the input string is empty, if it is, return the default value for float,
    if not, return the entered string and the float value.

    @param msg The `msg` parameter in the `__if_empty_do_nothing` method is a tuple containing
    two strings: the first string is used as a prompt to input a name, and the second string
    is used as a prompt to input a float value.

    @return The function `__if_empty_do_nothing` returns a tuple containing a string representing
    a name, a float value, and a boolean flag. If the input string is empty, it returns a default
    tuple with an empty string, 0.0, and `True`. If the input string is not empty, it returns a tuple
    with the entered string, the float value entered, and `False`.
    """
    logger.was_called(__if_empty_do_nothing, msg)
    default_values: _Tuple[str, float, bool, bool] = "", 0.0, True, True
    item_does_not_exists: _Tuple[str, float, bool, bool] = "", 0.0, True, False

    # Input string.
    name_input: str = inp(msg[0])
    if item_exists(name_input) == False:
        return item_does_not_exists

    # Check if string is empty.
    if not name_input:
        return default_values

    # Input float value.
    amount_input: float = numeric_only(inp(msg[1]), float)

    # Check if float value is empty or not a valid float.
    if amount_input == 0.0:
        return default_values
    return name_input, amount_input, False, True


def __handler(*msg: str, f: _Callable[..., Any]) -> _TupleStrFloatOrNone:
    """
    The function `__handler` logs the call to the logger with the function name and messages received.
    It then checks if the provided messages are empty; if so, it calls the `__its_empty` function to
    handle the empty case. Subsequently, it verifies if the amount matches the limit; if it does, it
    also calls the `__its_empty` function to handle this condition. Finally, it executes the provided
    callable function with the received name and amount parameters.

    @param *msg The `*msg` parameter represents a variable number of string arguments passed
    to the function.
    @param f The `f` parameter is a callable function.

    @return The function returns a tuple containing strings and floats representing the result
    of executing the provided callable function, after handling possible empty message scenarios.
    """
    logger.was_called(__handler, msg)

    name, amount, is_empty, name_exists = __if_empty_do_nothing(*msg)
    if not name_exists:
        return None
    if is_empty:
        return __its_empty()
    if amount == var.limit:
        return __its_empty()
    return f(name, amount)


def __its_empty() -> Any:
    """
    The function `__its_empty` sets an additional message in the variable `var.extra_message` indicating
    that the operation has been canceled. It then returns `None`.

    @param var.extra_message The `var.extra_message` parameter is a string that represents an
    additional message to be set in the `var.extra_message` variable, indicating the operation's
    cancellation.
    """
    var.extra_message = "Operation canceled."
    return None


def __handler_str_only(msg: str, f: _Callable[..., Any]) -> str:
    """
    The function `__handler_str_only` prompts the user for input using the `inp` function with the
    provided message. If the input is empty, it calls the `__its_empty` function to handle the empty
    case. Otherwise, it executes the provided callable function with the input string as the argument.

    @param msg The `msg` parameter is a string representing the message to prompt the user for input.
    @param f The `f` parameter is a callable function that operates on a string input.

    @return The function returns a string representing the result of executing the provided callable
    function with the user input.
    """
    name_input: str = inp(msg)
    if not name_input:
        return __its_empty()
    return f(name_input)


def __register() -> _TupleStrFloatOrNone:
    """
    The function `__register` prompts the user to enter an item name and its amount, then registers the item
    using the provided name and amount. If the amount is not numeric, it's converted to a float. Returns
    a tuple containing the item name and its amount.

    @return A tuple containing the registered item's name and its amount as a float.
    """
    logger.was_called(__register)
    return __handler(
        "\nEnter item name.",
        "\nEnter item amount.",
        f=register,
    )


def __search() -> str | None:
    """
    The function `__search` prompts the user to enter an item name to search for. It searches for the item
    with the provided name and returns the name of the item if found.

    @return The name of the item if found, otherwise an empty string.
    """
    logger.was_called(__search)
    return __handler_str_only(
        "\nEnter item name to search.",
        f=search,
    )


def __edit() -> _TupleStrFloatOrNone:
    """
    The function `__edit` prompts the user to enter an item name and its new amount. It edits the item with
    the provided name, updating its amount. If the new amount is not numeric, it's converted to a float.
    Returns a tuple containing the edited item's name and its new amount.

    @return A tuple containing the edited item's name and its new amount as a float.
    """
    logger.was_called(__edit)
    return __handler(
        "\nEnter item name to edit.",
        "\nEnter new amount.",
        f=edit,
    )


def __delete() -> str | None:
    """
    The function `__delete` prompts the user to enter an item name to delete. It deletes the item with the
    provided name. Returns the name of the deleted item.

    @return The name of the deleted item.
    """
    logger.was_called(__delete)
    return __handler_str_only(
        "\nEnter item name to delete.",
        f=delete_item,
    )


selector: _Dict[str, _Callable[[], None]] = {
    "1": lambda: logger.returned(__register),
    "2": lambda: logger.returned(__search),
    "3": lambda: logger.returned(__edit),
    "4": lambda: logger.returned(__delete),
}
"""
The function selector is a dictionary that maps strings to callable functions, each corresponding
to a specific action. Each key in the dictionary represents a choice, and its associated value is a
lambda function that takes a string s as input. The lambda functions call different logger functions
(__register, __search, __edit, __delete) passing the input string s as an argument.
"""
