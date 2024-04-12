## Budget Tracker CLI

This project is a simple budget tracking system implemented in Python. It allows users to register, search, edit, and delete items from their budget.

### Dependencies

This project relies on two external components:

- **Python:** The core functionality is written in Python. Ensure you have Python 3.10 or later installed on your system. ([https://www.python.org/downloads/](https://www.python.org/downloads/))
- **C Compiler (Optional):** The `random64.c` file generates random numbers using a shared library. You'll need a C compiler like GCC to build it.

**Important Note:** The provided build commands for the shared library are specific to Windows 10 and Ubuntu 22.04 on WSL. The build process might differ slightly depending on your operating system and compiler.

### Getting Started

To use this system, follow these steps:

1. **Clone the Repository:** Clone this repository to your local machine using Git.
2. **Install Dependencies:** Make sure you have Python 3.10+ and a C compiler installed.
3. **Build the C Extension (Optional):**
   - If you want to use the custom random number generation, follow the build instructions for your specific operating system:
     - **Windows 10:** Open a command prompt and navigate to the project directory. Run the following command:
       ```bash
       gcc -shared -o random64.dll -std=c99 -Wall -Werror -fpic random64.c
       ```
     - **WSL (Ubuntu 22.04):** Open a terminal and navigate to the project directory. Run the following command:
       ```bash
       gcc -shared -o random64.so -std=c99 -Wall -Werror -fPIC random64.c
       ```
   - If either you don't build the extension or the ctypes package fails to load the binaries, the code will use Python's built-in modules.
4. **Run the System:** Open a terminal or command prompt, navigate to the project directory, and run the following command:
   ```bash
   python main.py
   ```

### Usage

Once the system is running, you will be presented with a menu with the following options:

```
1. Register Item
2. Search Item
3. Edit Item
4. Delete Item
5. Exit
```

Choose the appropriate option by entering the corresponding number. You can register a new item, search for an existing item, edit an item, or delete an item from your budget.

### Configuration

This project utilizes mypy: [https://mypy.readthedocs.io/en/stable/](https://mypy.readthedocs.io/en/stable/) for static type checking. The configuration for mypy is as follows:

```ini
[mypy]
python_version = 3.10
pretty = True
ignore_missing_imports = True
```

These settings ensure compatibility with Python version 3.10, enable pretty printing of mypy errors, and ignore missing imports during type checking.

### License

This project is licensed under the MIT License - see the '[license](license)' for details.
