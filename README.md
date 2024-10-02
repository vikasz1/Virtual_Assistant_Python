
## Virtual Assistant Project

This project aims to create a simple virtual assistant using Python.

### Setup

1. **Install Python:** Ensure you have Python installed on your system. You can download it from [https://www.python.org/](https://www.python.org/).
2. **Install Required Libraries:**
   - **SpeechRecognition:** `pip install SpeechRecognition`
   - **pyttsx3:** `pip install pyttsx3`
   - **wikipedia:** `pip install wikipedia`
   - **datetime:** (Already included in Python)
   - **webbrowser:** (Already included in Python)
   - **os:** (Already included in Python)
   - **pyjokes:** `pip install pyjokes`
   - **requests:** `pip install requests`
   - **beautifulsoup4:** `pip install beautifulsoup4`
   - **wolframalpha:** `pip install wolframalpha`

### Running the Project

1. **Open the Project:** Navigate to the project directory in your terminal or command prompt.
2. **Run the Script:** Execute the `main.py` file using the command `python main.py`.

### Features

- **Greeting:** The assistant greets you when you start it.

- **Voice Recognition:** The assistant can understand your voice commands.
- **Text-to-Speech:** The assistant can speak back to you.
- **Wikipedia Search:** Get information from Wikipedia.
- **Time and Date:** Get the current time and date.
- **Open Websites:** Open websites in your default browser.
- **Jokes:** Tell you a joke.
- **Weather Information:** Get the current weather conditions.
- **Wolfram Alpha Integration:** Access Wolfram Alpha's knowledge engine for more complex queries.

### Usage

- **Start the assistant:** Say "Hey Jarvis" or "Hello Jarvis" to activate the assistant.
- **Give commands:** Speak your commands clearly and concisely.
- **End the session:** Say "Goodbye Jarvis" or "Exit" to close the assistant.

### Example Commands

- "What's the weather like today?"
- "Open YouTube"
- "Tell me a joke"
- "What is the capital of France?"
- "What is the meaning of life?"


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
