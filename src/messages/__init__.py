__all__ = [
    "PRT_MAIN_MENU",
    "PRT_OPERATION_CANCELED",
    "PRT_ERROR",
    "PRT_INVALID_CHOICE",
    "PRT_INIT_ITEM_ALREADY_EXISTS",
    "PRT_INIT_ITEM_NOT_FOUND",
    "PRT_INIT_REGISTER_REGISTERED_SUCCESSFULLY",
    "PRT_INIT_SEARCH_ITEM_FOUND",
    "PRT_INIT_EDIT_ITEM_EDITED_SUCCESSFULLY",
    "PRT_INIT_DELETED_ITEM_DELETED_SUCCESSFULLY",
    "INP_ENTER_MAIN_MENU_CHOICE",
    "INP_INIT_REGISTER_HANDLER_ITEM_NAME",
    "INP_INIT_REGISTER_HANDLER_ITEM_AMOUNT",
    "INP_INIT_SEARCH_HANDLER_ITEM_TO_SEARCH",
    "INP_INIT_EDIT_HANDLER_ITEM_TO_EDIT",
    "INP_INIT_EDIT_HANDLER_NEW_ITEM_AMOUNT",
    "INP_INIT_DELETED_HANDLER_ITEM_TO_DELETE",
]

# Prefixes:
# PRT = PRINT MESSAGES, RETURNS: print(*s, ...)
# INP = INPUT MESSAGES, RETURNS: input(f"{s}\n> ")
# INIT = String that is within ('init'ialized) in a function.

from typing import Callable, Tuple, Any

_single_injector = Callable[[Any], str]
_double_injector = Callable[[Tuple[Any, Any]], str]

PRT_MAIN_MENU: str = (
    "Budget Tracking System\n"
    "1. Add Item\n"
    "2. Find Item\n"
    "3. Update Item\n"
    "4. Remove Item\n"
    "5. Exit\n"
)
PRT_OPERATION_CANCELED: str = "Action canceled."
PRT_ERROR: str = "Oops! Something went wrong. Please try again."
PRT_INVALID_CHOICE: _single_injector = (
    lambda s: f"Invalid option '{s}'. Please choose a valid option."
)
PRT_INIT_ITEM_ALREADY_EXISTS: _single_injector = (
    lambda s: f"An item named '{s}' already exists. Please try a different name."
)
PRT_INIT_ITEM_NOT_FOUND: _single_injector = (
    lambda s: f"We couldn't find an item named '{s}'."
)
PRT_INIT_REGISTER_REGISTERED_SUCCESSFULLY: _single_injector = (
    lambda s: f"Item '{s}' added successfully!"
)
PRT_INIT_SEARCH_ITEM_FOUND: _double_injector = (
    lambda s: f"Found item:\nName: '{s[0]}', Amount: '{s[1]}'."
)
PRT_INIT_EDIT_ITEM_EDITED_SUCCESSFULLY: _double_injector = (
    lambda s: f"Item '{s[0]}' updated successfully. New amount: '{s[1]}'."
)
PRT_INIT_DELETED_ITEM_DELETED_SUCCESSFULLY: _single_injector = (
    lambda s: f"Item(s) '{s}' deleted successfully."
)

INP_ENTER_MAIN_MENU_CHOICE: str = "What would you like to do?"
INP_INIT_REGISTER_HANDLER_ITEM_NAME: str = "\nWhat would you like to name the item?"
INP_INIT_REGISTER_HANDLER_ITEM_AMOUNT: str = "\nEnter the item's amount."
INP_INIT_SEARCH_HANDLER_ITEM_TO_SEARCH: str = "\nWhat item are you looking for?"
INP_INIT_EDIT_HANDLER_ITEM_TO_EDIT: str = (
    "\nEnter the name of the item you want to update."
)
INP_INIT_EDIT_HANDLER_NEW_ITEM_AMOUNT: str = "\nEnter the new amount for the item."
INP_INIT_DELETED_HANDLER_ITEM_TO_DELETE: str = (
    "\nEnter the name of the item you want to remove."
)
