__all__ = ["selector"]

from typing import Any, Dict, Callable, Literal, Tuple, Set

from src.var import var
from src.functions import *
from .functions import *
from src.logger import logger
from src.messages import *

_TupleStrFloatOrNone = Tuple[str, float] | None
_StrOrNone = str | None
_IfEmpty = Tuple[str, float, bool, bool]


def __empty(s: str) -> bool:
    return True if s == "" else False


def __its_empty() -> Any:
    """
    The function `__its_empty` sets an additional message in the variable `var.extra_message` indicating
    that the operation has been canceled. It then returns `None`.
    """
    var.extra_message = PRT_OPERATION_CANCELED
    return None


def __if_empty_do_nothing(*msg: str, skip: bool) -> _IfEmpty:
    """
    The function `__if_empty_do_nothing` performs a series of checks on input strings and floats,
    returning appropriate default values based on the conditions met.

    @param msg The `msg` parameter is a variable-length argument that represents the messages
    received by the function. These messages are used to prompt input from the user.
    @param skip The `skip` parameter is a boolean flag indicating whether to skip certain
    checks based on the existence of input data.

    @return The function `__if_empty_do_nothing` returns a tuple representing either default
    values or input data based on the conditions met during the checks. If the input string
    exists and the `skip` flag is `True`, it returns a predefined tuple denoting existence.
    If the input string is empty, it returns default values. If the input float value is
    either empty or not a valid float, it also returns default values.
    """
    logger.was_called(__if_empty_do_nothing, msg)
    default_values: _IfEmpty = "", 0.0, True, True
    already_exists: _IfEmpty = "", 0.0, True, False

    # Input string.
    name_input: str = inp(msg[0])
    if __empty(name_input):
        return default_values
    if item_exists(name_input) and not skip:
        return already_exists

    # Check if string is empty.
    if not name_input:
        return default_values

    # Input float value.
    amount_input: float = numeric_only(inp(msg[1]), float)

    # Check if float value is empty or not a valid float.
    if amount_input == var.limit:
        return default_values
    return name_input, amount_input, False, True


def __handler(
    *msg: str, f: Callable[..., Any], skip_existence: bool = False
) -> _TupleStrFloatOrNone:
    """
    The function `__handler` processes input messages and a callback function, performing
    checks and calling the function if conditions are met.

    @param msg The `msg` parameter represents the messages received by the function.
    @param f The `f` parameter is a callable function that the handler executes with
    appropriate input parameters.
    @param skip_existence The `skip_existence` parameter is a boolean flag indicating
    whether to skip existence checks for input data.

    @return The function `__handler` returns a tuple representing either the result of
    calling the provided function or `None` based on the conditions met during the checks.
    If the input name does not exist, it returns `None`. If the input is empty or reaches
    a certain limit, it returns a predefined tuple denoting emptiness.
    """
    logger.was_called(__handler, msg)

    name, amount, is_empty, name_exists = __if_empty_do_nothing(
        *msg, skip=skip_existence
    )
    if not name_exists:
        return None
    if is_empty:
        return __its_empty()
    if amount == var.limit:
        return __its_empty()
    return f(name, amount)


def __handler_str_only(
    msg: str, f: Callable[..., Any], check: bool = True
) -> _StrOrNone:
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
    if __empty(name_input):
        return __its_empty()
    if item_exists(name_input) == False and check:
        return None
    if not name_input:
        return __its_empty()
    return f(name_input)


def __register_handler() -> _TupleStrFloatOrNone:
    """
    The function `__register_handler` prompts the user to enter an item name and its amount, then registers the item
    using the provided name and amount. If the amount is not numeric, it's converted to a float. Returns
    a tuple containing the item name and its amount.

    @return A tuple containing the registered item's name and its amount as a float.
    """
    logger.was_called(__register_handler)
    return __handler(
        INP_INIT_REGISTER_HANDLER_ITEM_NAME,
        INP_INIT_REGISTER_HANDLER_ITEM_AMOUNT,
        f=register,
    )


def __search_handler() -> _StrOrNone:
    """
    The function `__search_handler` prompts the user to enter an item name to search for. It searches for the item
    with the provided name and returns the name of the item if found.

    @return The name of the item if found, otherwise an empty string.
    """
    logger.was_called(__search_handler)
    return __handler_str_only(
        INP_INIT_SEARCH_HANDLER_ITEM_TO_SEARCH,
        f=search,
    )


def __edit_handler() -> _TupleStrFloatOrNone:
    """
    The function `__edit_handler` prompts the user to enter an item name and its new amount. It edits the item with
    the provided name, updating its amount. If the new amount is not numeric, it's converted to a float.
    Returns a tuple containing the edited item's name and its new amount.

    @return A tuple containing the edited item's name and its new amount as a float.
    """
    logger.was_called(__edit_handler)

    return __handler(
        INP_INIT_EDIT_HANDLER_ITEM_TO_EDIT,
        INP_INIT_EDIT_HANDLER_NEW_ITEM_AMOUNT,
        f=edit,
        skip_existence=True,
    )


def __delete_handler() -> _StrOrNone:
    """
    The function `__delete_handler` prompts the user to enter an item name to delete. It deletes the item with the
    provided name. Returns the name of the deleted item.

    @return The name of the deleted item.
    """
    logger.was_called(__delete_handler)
    return __handler_str_only(
        INP_INIT_DELETED_HANDLER_ITEM_TO_DELETE,
        f=delete,
    )


__selector_values: Set[str] = {"1", "2", "3", "4"}

__selector_handler: Dict[str, Callable[[], None]] = {
    "1": lambda: logger.returned(__register_handler),
    "2": lambda: logger.returned(__search_handler),
    "3": lambda: logger.returned(__edit_handler),
    "4": lambda: logger.returned(__delete_handler),
}
"""
The function __selector_handler is a dictionary that maps strings to callable functions, each corresponding
to a specific action. Each key in the dictionary represents a choice, and its associated value is a
lambda function. The lambda functions call handler functions (__register_handler, __search_handler, 
__edit_handler, __delete_handler) passing the input string s as an argument.
"""


def selector(s: str) -> Literal[False]:
    """
    The function `selector` checks if a given string `s` is in the '__selector_values' Set.
    If it is, it attempts to call a corresponding handler function from the '__selector_handler'
    dictionary. If a `TypeError` exception occurs during this process, it logs an error message
    indicating that the returned type of the handler is None, and sets 'var.extra_message' to
    'PRT_ERROR'. If the string `s` is not found in the dictionary, it sets 'var.extra_message'
    to 'PRT_INVALID_CHOICE'.

    @param s The `s` parameter is a string that is checked against the '__selector_values' dictionary.
    @return The function returns False in all cases.
    """
    if s in __selector_values:
        try:
            __selector_handler.get(s, lambda *args: False)()
        except TypeError:
            var.extra_message = PRT_ERROR
            logger.exc(f"The returned type of '{__selector_handler}' is None.")
        finally:
            return False
    var.extra_message = PRT_INVALID_CHOICE(s)
    return False
