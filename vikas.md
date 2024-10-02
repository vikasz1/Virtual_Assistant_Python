
# Main - Standalone Executable

This guide explains how to convert your Python script `main.py` into a standalone executable file (.exe) that can run on Windows systems without requiring Python to be installed.

## Prerequisites

- **Python**: Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).
- **pip**: `pip` is Python's package installer and should come with your Python installation.

## Installation Steps

### 1. Install PyInstaller

PyInstaller bundles your Python script and its dependencies into an executable file.

```bash
pip install pyinstaller
```

### 2. Install `pywin32` (if needed)

For certain Windows-specific functionalities, you might need the `pywin32` package.

```bash
pip install pywin32
```

### 3. Install/Upgrade `gtts` and `gtts-token` (if needed for text-to-speech)

Ensure you have the latest versions of the `gtts` and `gtts-token` libraries, which are used for text-to-speech functionality.

```bash
python -m pip install --upgrade gtts
python -m pip install --upgrade gtts-token
```

## Creating the Executable

**Important**: Navigate to the directory containing your `main.py` script in the terminal or command prompt before running the following commands.

### Method 1: Using `--hidden-import` and `--onefile`

```bash
pyinstaller --hidden-import=pyttsx3.drivers.sapi5 --onefile main.py
```

- `--hidden-import=pyttsx3.drivers.sapi5`: This flag explicitly includes the `sapi5` driver used by `pyttsx3` to avoid potential import errors in the executable.
- `--onefile`: This option creates a single executable file that contains all necessary dependencies.

### Method 2: Alternative `--hidden-import`

```bash
pyinstaller --hidden-import=pyttsx3.drivers --onefile main.py
```

This command is similar to Method 1 but uses `pyttsx3.drivers` instead of the specific `sapi5` driver. Use this if your project requires different `pyttsx3` drivers.

## After Execution

- **Executable Location**: After running the commands, you will find the generated executable file (`main.exe`) inside the `dist` folder in your project directory.
- **Distribution**: You can share the `dist` folder with users. They will be able to run your application without needing Python or any dependencies installed on their system.

## Troubleshooting

- **ValueError: Unable to find token seed! Did <https://translate.google.com> change?**
  - This error is related to the `gtts` library. Upgrading `gtts` and `gtts-token` as mentioned in the installation steps should resolve this issue.

- **Other Errors**
  - If you encounter other errors, carefully review the error messages. They often provide clues about missing dependencies or configuration issues. You can search for solutions online or consult the documentation for the libraries you are using.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
