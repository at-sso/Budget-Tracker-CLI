from typing import Set as _Set

from .func import *
from .handler import selector
from .logger import logger
from .var import var


def main() -> int:
    "Main function"
    logger.info(f"Main function started.")
    logger.was_called(main)
    _one_to_five: _Set[str] = {"1", "2", "3", "4", "5"}

    while True:
        extras.clear_terminal()
        prt(
            "Budget Tracking System\n"
            "1. Register Item\n"
            "2. Search Item\n"
            "3. Edit Item\n"
            "4. Delete Item\n"
            "5. Exit\n",
            i=f"{var.extra_message}\n",
        )

        selection: str = inp("Enter your choice.")
        name: str = ""
        if selection == "5":  # Exit main loop
            prt("\nExiting...")
            break
        if selection not in _one_to_five:  # Invalid choice
            var.extra_message = "Invalid choice. Please try again."
            continue
        else:  # Selection is either 1-4 (str)
            try:
                selector.get(selection)(name)  # type: ignore
            except TypeError:
                var.extra_message = "An error occured."
                logger.exc(f"The returned type of 'selector' ({selection}) is None.")
    return 0
