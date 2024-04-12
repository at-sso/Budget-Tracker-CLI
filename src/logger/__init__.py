import os
from typing import Any, Callable, List
import logging
import traceback as tb

import src.const as const


class __Logger:
    "The class `__Logger` initializes a logger object, deletes old log files, and configures logging settings."

    def __init__(self) -> None:
        "Initializes a logger object, deletes old log files, and configures logging settings."
        # Delete the oldest files.
        log_path: str = const.LOGGER_PATH
        log_file: str = const.LOGGER_FILE

        # Start the logger
        self.__log: logging.Logger = logging.getLogger(__name__)
        self.__log.setLevel(logging.DEBUG)

        # Delete the oldest files.
        files: List[str] = os.listdir(log_path)
        if not len(files) < 10:
            logger_amount: int = max((len(files)) // 10, 1)
            files_to_delete: List[str] = files[: len(log_path) - logger_amount]
            for file_name in files_to_delete:
                file_path: str = os.path.join(log_path, file_name)
                os.remove(file_path)

        # Create a file handler
        logger_handler = logging.FileHandler(log_file, mode="w")
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
        )
        logger_handler.setFormatter(formatter)
        # Add the handler to the logger
        self.__log.addHandler(logger_handler)
        self.info("Logger started.")

    def __func_at(self, c: Callable[..., Any]) -> str:
        """
        The method `__func_at` returns a string representing the name and memory location of a given callable object.

        @param c The `c` parameter is a callable object.

        @return The method `__func_at` returns a string representing the name and memory location
        of the given callable object `c`.
        """
        return f"'{c.__name__}' at <{id(c)}>"

    def info(self, s: str) -> None:
        """
        Logs an informational message.

        @param s The `s` parameter is a string containing the message to be logged.
        """
        self.__log.info(s)

    def exc(
        self, s: str = "", c: Callable[..., Any] = object, default: bool = False
    ) -> None:
        """
        Logs a warning message for unhandled exceptions or a custom message followed by the exception trace.

        @param s The `s` parameter is a string containing a custom message (if any).
        @param c The `c` parameter is a callable object associated with the exception (if any).
        @param default The `default` parameter is a boolean flag indicating whether the exception is unhandled.
        """
        if default:
            self.__log.warning(
                f"Unhandled exception raised in {self.__func_at(c)}:\n{tb.format_exc()}"
            )
            return
        self.__log.warning(f"{s}\n{tb.format_exc()}")

    def was_called(self, c: Callable[..., Any], *data: Any) -> None:
        """
        Logs a message indicating that a function was called, along with any associated data.

        @param c The `c` parameter is a callable object representing the function that was called.
        @param data The `data` parameter is a variable-length list of data passed to the function.
        """
        self.info(
            f"Function {self.__func_at(c)} was called"
            + (f" with the following data:\n{data}" if data != () else ".")
        )

    def returned(self, c: Callable[..., Any], *args: Any) -> None:
        """
        Logs a message indicating that a function returned a value.

        @param c The `c` parameter is a callable object representing the function that returned a value.
        @param args The `args` parameter is a variable-length list of arguments passed to the function.
        """
        val: Any = None
        if args:
            val = c(args)
        else:
            val = c()
        self.info(
            f"Function {self.__func_at(c)} returned: {val} ({type(val).__name__})"
        )


logger = __Logger()
