__all__ = [
    "register",
    "search",
    "edit",
    "delete_item",
    "item_exists",
]

import json as _json
from typing import Callable, List as _List, Any as _Any

_ListAny = _List[_Any]

import src.const as _const
from src.var import var
from src.logger import logger as _logger


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

__data: _ListAny = __load_data()


def item_exists(name: str) -> bool:
    _logger.was_called(item_exists, name)
    for item in __data:
        if item["name"] == name:
            return True
    var.extra_message = __not_found(name)
    return False


def register(name: str, amount: float) -> None:
    """
    The function register_item adds a new item to the data list and saves it to the JSON file.

    @param name The name parameter is a string representing the name of the item to be registered.
    @param amount The amount parameter is a float representing the amount of the item to be registered.
    """
    _logger.was_called(register, name, amount)
    __data.append({"name": name, "amount": amount})
    __save_data(__data)
    var.extra_message = f"Item '{name}' registered successfully."


def search(name: str) -> None:
    """
    The function search_item searches for an item by name in the data list.

    @param name The name parameter is a string representing the name of the item to search for.
    """
    _logger.was_called(search, name)
    for item in __data:
        if item_exists(item["name"]):
            var.extra_message = (
                f"Found item:\nName: '{item['name']}', Amount: '{item['amount']}'."
            )
            return
    var.extra_message = __not_found(name)


def edit(name: str, new_amount: float) -> None:
    """
    The function edit_item modifies the amount of an item in the data list and saves the changes
    to the JSON file.

    @param name The name parameter is a string representing the name of the item to be edited.
    @param new_amount The new_amount parameter is a float representing the new amount of the item.
    """
    _logger.was_called(edit, name, new_amount)
    for item in __data:
        if item_exists(item["name"]):
            item["amount"] = new_amount
            __save_data(__data)
            var.extra_message = f"Item '{name}' edited successfully."
            return
    var.extra_message = __not_found(name)


def delete_item(name: str) -> None:
    """
    The function delete_item removes an item from the data list and saves the changes to the JSON file.

    @param name The name parameter is a string representing the name of the item to be deleted.
    """
    _logger.was_called(delete_item)
    for item in __data:
        if item_exists(item["name"]):
            __data.remove(item)
            __save_data(__data)
            var.extra_message = f"Item '{name}' deleted successfully."
            return
    var.extra_message = __not_found(name)
