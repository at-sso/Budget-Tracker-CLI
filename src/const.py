import os as _os
import sys as _sys
from typing import List as _List, Any as _Any
from pathlib import Path
from datetime import datetime as _dt


def __mkdirs(*paths: str) -> _List[_Any]:
    """
    The function `__mkdirs` creates directories specified by the given paths, ensuring they exist.
    If the directory already exists, it skips the creation process.

    @param paths The `paths` parameter in the `__mkdirs` method is a list of strings representing
    the paths to be created. Each path is resolved to its absolute form before processing.

    @return The function `__mkdirs` returns a list of absolute paths that have been created.
    If no directories were created, an empty list is returned.
    """
    absolute_paths: _List[_Any] = []
    for p in paths:
        absolute_path: str = str(Path(p).resolve())
        absolute_paths.append(absolute_path)
        if not _os.path.exists(absolute_path):
            _os.makedirs(absolute_path)
    return absolute_paths


ABSOLUTE_PATH: str = _os.path.abspath(_os.path.dirname(_sys.argv[0])).replace("\\", "/")
JSON_PATH: str = f"{ABSOLUTE_PATH}/json"
JSON_FILE: str = f"{JSON_PATH}/budget_data.json"
LOGGER_PATH: str = f"{ABSOLUTE_PATH}/log"
LOGGER_FILE: str = f"{LOGGER_PATH}/{_dt.now().strftime('%Y-%m-%d-%H-%M-%S')}.log"
DLL_FILE: str = f"{ABSOLUTE_PATH}/src/bin/random64" + (
    ".dll" if _os.name == "nt" else ".so"
)

__mkdirs(
    JSON_PATH,
    LOGGER_PATH,
)
