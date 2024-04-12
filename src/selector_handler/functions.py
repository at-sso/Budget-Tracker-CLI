__all__ = [
    "register",
    "search",
    "edit",
    "delete",
    "item_exists",
]

import json as _json
from typing import List, Dict, Union

_DataList = List[Dict[str, Union[str, float]]]

import src.const as const
from src.var import var
from src.logger import logger as logger


def __load_data() -> _DataList:
    """
    The function __load_data loads data from a JSON file, handling file not found or JSON decoding
    errors by logging an exception and creating an empty JSON file if necessary before attempting to
    load data again.

    @return The function __load_data returns a list containing the data loaded from the JSON file,
    or an empty list if the file does not exist or is not in JSON format.
    """
    logger.was_called(__load_data)

    data: _DataList = []

    try:
        with open(const.JSON_FILE, "r") as f:
            data = _json.load(f)
    except (FileNotFoundError, _json.JSONDecodeError):
        logger.exc(c=__load_data, default=True)
        with open(const.JSON_FILE, "w") as f:
            f.write("[]")
        data = __load_data()

    return data


def __save_data(data: _DataList) -> None:
    """
    The function __save_data saves data to a JSON file.

    @param data The data parameter is a list containing the data to be saved to the JSON file.
    """
    logger.was_called(__save_data)
    with open(const.JSON_FILE, "w") as f:
        _json.dump(data, f, separators=(",", ":"))


__data: _DataList = __load_data()


def item_exists(name: str) -> bool:
    """
    The function `item_exists` checks if an item with the given name exists in the data. If found,
    it returns True; otherwise, it returns False and sets an extra message accordingly.

    @param name The `name` parameter is a string representing the name of the item being searched for
    in the data.

    @return The function returns a boolean value indicating whether the item exists in the data or not.
    """
    logger.was_called(item_exists, name)
    for item in __data:
        if item["name"] == name:
            var.extra_message = f"Item '{name}' already exists."
            return True
    var.extra_message = f"Item '{name}' not found."
    return False


def register(name: str, amount: float) -> None:
    """
    The function register adds a new item to the data list and saves it to the JSON file.

    @param name The name parameter is a string representing the name of the item to be registered.
    @param amount The amount parameter is a float representing the amount of the item to be registered.
    """
    logger.was_called(register, name, amount)
    __data.append({"name": name, "amount": amount})
    __save_data(__data)
    var.extra_message = f"Item '{name}' registered successfully."


def search(name: str) -> None:
    """
    The function search searches for an item by name in the data list.

    @param name The name parameter is a string representing the name of the item to search for.
    """
    logger.was_called(search, name)
    for item in __data:
        var.extra_message = (
            f"Found item:\nName: '{item['name']}', Amount: '{item['amount']}'."
        )
        return


def edit(name: str, new_amount: float) -> None:
    """
    The function edit modifies the amount of an item in the data list and saves the changes
    to the JSON file.

    @param name The name parameter is a string representing the name of the item to be edited.
    @param new_amount The new_amount parameter is a float representing the new amount of the item.
    """
    logger.was_called(edit, name, new_amount)
    for item in __data:
        item["amount"] = new_amount
        __save_data(__data)
        var.extra_message = f"Item '{name}' edited successfully."


def delete(name: str) -> None:
    """
    The function delete removes item or items (if any) from the data list and saves the changes
    to the JSON file.

    @param name The name parameter is a string representing the name of the item to be deleted.
    """
    logger.was_called(delete)
    __data[:] = [item for item in __data if item["name"] != name]
    __save_data(__data)
    var.extra_message = f"Item(s) '{name}' deleted successfully."
