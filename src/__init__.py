from .functions import *
from .selector_handler import *
from .logger import logger
from .var import var
from .messages import *


def main() -> int:
    "Main function"
    logger.info(f"Main function started.")
    logger.was_called(main)

    while True:
        clear_terminal()
        prt(PRT_MAIN_MENU, i=f"{var.extra_message}\n")

        user_selection: str = inp(INP_ENTER_MAIN_MENU_CHOICE)
        if selector(user_selection) or user_selection == "5":
            prt("\nExiting...")
            break

    return 0
