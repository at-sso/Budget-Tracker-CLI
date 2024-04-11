from typing import Dict as _Dict, Callable as _Callable, Tuple as _Tuple

from src.func import *
from src.logger import logger

_TupleStrFloat = _Tuple[str, float]


def __a(name: str) -> _TupleStrFloat:
    """
    The function `__a` prompts the user to enter an item name and its amount, then registers the item
    using the provided name and amount. If the amount is not numeric, it's converted to a float. Returns
    a tuple containing the item name and its amount.

    @param name The `name` parameter is a string representing the name of the item to be registered.
    @return A tuple containing the registered item's name and its amount as a float.
    """
    logger.was_called(__a)
    name = inp("\nEnter item name.")
    amount: float = extras.numeric_only(
        inp("\nEnter item amount."),
        float,
    )
    register_item(name, amount)
    return (name, amount)


def __b(name: str) -> str:
    """
    The function `__b` prompts the user to enter an item name to search for. It searches for the item
    with the provided name and returns the name of the item if found.

    @param name The `name` parameter is a string representing the name of the item to be searched for.
    @return The name of the item if found, otherwise an empty string.
    """
    logger.was_called(__a)
    name = inp("\nEnter item name to search.")
    search_item(name)
    return name


def __c(name: str) -> _TupleStrFloat:
    """
    The function `__c` prompts the user to enter an item name and its new amount. It edits the item with
    the provided name, updating its amount. If the new amount is not numeric, it's converted to a float.
    Returns a tuple containing the edited item's name and its new amount.

    @param name The `name` parameter is a string representing the name of the item to be edited.
    @return A tuple containing the edited item's name and its new amount as a float.
    """
    logger.was_called(__a)
    name = inp("\nEnter item name to edit.")
    amount: float = extras.numeric_only(
        inp("\nEnter new amount."),
        float,
    )
    edit_item(name, amount)
    return (name, amount)


def __d(name: str) -> str:
    """
    The function `__d` prompts the user to enter an item name to delete. It deletes the item with the
    provided name. Returns the name of the deleted item.

    @param name The `name` parameter is a string representing the name of the item to be deleted.
    @return The name of the deleted item.
    """
    logger.was_called(__a)
    name = inp("\nEnter item name to delete.")
    delete_item(name)
    return name


selector: _Dict[str, _Callable[[str], None]] = {
    "1": lambda s: logger.returned(__a, s),
    "2": lambda s: logger.returned(__b, s),
    "3": lambda s: logger.returned(__c, s),
    "4": lambda s: logger.returned(__d, s),
}
"""
The function selector is a dictionary that maps strings to callable functions, each corresponding
to a specific action. Each key in the dictionary represents a choice, and its associated value is a
lambda function that takes a string s as input. The lambda functions call different logger functions
(__a, __b, __c, __d) passing the input string s as an argument.
"""
