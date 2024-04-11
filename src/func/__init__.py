import json as _json
from typing import Callable, List as _List, Any as _Any

_ListAny = _List[_Any]

import src.const as _const
import src.func.extras as extras
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


__all__ = [
    "extras",
    "register_item",
    "search_item",
    "edit_item",
    "delete_item",
    "prt",
    "inp",
]


# Function to load data from file
def __load_data() -> _ListAny:
    """
    The function __load_data loads data from a JSON file, handling file not found or JSON decoding
    errors by logging an exception and creating an empty JSON file if necessary before attempting to
    load data again.

    @return The function __load_data returns a list containing the data loaded from the JSON file,
    or an empty list if the file does not exist or is not in JSON format.
    """
    _logger.was_called(__load_data)

    data: _ListAny = []

    try:
        with open(_const.JSON_FILE, "r") as f:
            data = _json.load(f)
    except (FileNotFoundError, _json.JSONDecodeError):
        _logger.exc(c=__load_data, default=True)
        with open(_const.JSON_FILE, "w") as f:
            f.write("[]")
        data = __load_data()

    return data


# Function to save data to file
def __save_data(data: _ListAny) -> None:
    """
    The function __save_data saves data to a JSON file.

    @param data The data parameter is a list containing the data to be saved to the JSON file.
    """
    _logger.was_called(__save_data)
    with open(_const.JSON_FILE, "w") as f:
        _json.dump(data, f)


__not_found: Callable[[str], str] = lambda s: f"Item '{s}' not found."
"""
The callable __not_found is a lambda function that generates a string indicating that an item
with a given name was not found.

@param name The name parameter is a string representing the name of the item that was not found.
"""


# Function to register a new item
def register_item(name: str, amount: float) -> None:
    """
    The function register_item adds a new item to the data list and saves it to the JSON file.

    @param name The name parameter is a string representing the name of the item to be registered.
    @param amount The amount parameter is a float representing the amount of the item to be registered.
    """
    data: _ListAny = __load_data()
    data.append({"name": name, "amount": amount})
    __save_data(data)
    var.extra_message = f"Item {name} registered successfully."


# Function to search for an item
def search_item(name: str) -> None:
    """
    The function search_item searches for an item by name in the data list.

    @param name The name parameter is a string representing the name of the item to search for.
    """
    data: _ListAny = __load_data()
    for item in data:
        if item["name"] == name:
            var.extra_message = (
                f"Found item:\nName: {item['name']}, Amount: {item['amount']}"
            )
            return
    var.extra_message = __not_found(name)


# Function to edit an item
def edit_item(name: str, new_amount: float) -> None:
    """
    The function edit_item modifies the amount of an item in the data list and saves the changes
    to the JSON file.

    @param name The name parameter is a string representing the name of the item to be edited.
    @param new_amount The new_amount parameter is a float representing the new amount of the item.
    """
    data: _ListAny = __load_data()
    for item in data:
        if item["name"] == name:
            item["amount"] = new_amount
            __save_data(data)
            var.extra_message = f"Item {name} edited successfully."
            return
    var.extra_message = __not_found(name)


# Function to delete an item
def delete_item(name: str) -> None:
    """
    The function delete_item removes an item from the data list and saves the changes to the JSON file.

    @param name The name parameter is a string representing the name of the item to be deleted.
    """
    data: _ListAny = __load_data()
    for item in data:
        if item["name"] == name:
            data.remove(item)
            __save_data(data)
            var.extra_message = f"Item {name} deleted successfully."
            return
    var.extra_message = __not_found(name)
