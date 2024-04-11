# Budget Tracker CLI

This is a simple budget tracking system implemented in Python. It allows users to register, search, edit, and delete items from their budget.

## Getting Started

To use this system, follow these steps:

1. Clone this repository to your local machine.
2. Run the `main.py` script to start the budget tracking system.

## Usage

Once the system is running, you will be presented with a menu with the following options:

```
1. Register Item
2. Search Item
3. Edit Item
4. Delete Item
5. Exit
```

Choose the appropriate option by entering the corresponding number. You can register a new item, search for an existing item, edit an item, or delete an item from your budget.

## Configuration

This project utilizes [mypy](https://mypy.readthedocs.io/en/stable/) for static type checking. The configuration for mypy is as follows:

```ini
[mypy]
python_version = 3.10
pretty = True
ignore_missing_imports = True
```

These settings ensure compatibility with Python version 3.10, enable pretty printing of mypy errors, and ignore missing imports during type checking.

## License

This project is licensed under the MIT License - see the [LICENSE](license) file for details.
