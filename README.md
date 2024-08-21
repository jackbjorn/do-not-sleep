# Notepad Automation Script

## Author
Jack Bjorn

## Email

## Date
August 15, 2024

## Description
This script automates the process of typing randomly generated Python code into Notepad. It launches Notepad, simulates key presses to type the code, and allows for clean termination through a hotkey or interrupt signal. It ensures that the system does not enter sleep mode while the script is running.

## Features
- **Automated Typing:** Types randomly generated Python code into Notepad.
- **Clean Exit:** Exits gracefully when a specified hotkey is pressed or an interrupt signal (Ctrl+C) is received.
- **Sleep Prevention:** Prevents the system from sleeping while the script is active.

## Libraries Used
The script utilizes the following libraries:
- `time`: For managing delays and pauses.
- `pyautogui`: For simulating key presses and mouse movements.
- `subprocess`: For launching Notepad.
- `psutil`: For process management and termination.
- `win32gui`: For interacting with Windows GUI elements.
- `win32con`: For Windows constants.
- `random`: For generating random values.
- `ctypes`: For interacting with low-level system functions.
- `signal`: For handling interrupt signals.
- `sys`: For system-specific parameters and functions.
- `keyboard`: For monitoring hotkey presses.
- `win32api`: For interacting with the Windows API.
- `win32process`: For handling process-specific operations.
- `win32com.client`: For COM object management (if needed in future extensions).

## Installation

To install the required libraries, create a `requirements.txt` file with the following content:

```
pyautogui
psutil
pywin32
keyboard
```

Then, run the following command to install the dependencies:

```bash
pip install -r requirements.txt
```

To freeze your current environment's dependencies into a `requirements.txt` file, use:

```bash
pip freeze > requirements.txt
```

## Usage

1. **Run the Script:**
   - Execute the script using Python:
     ```bash
     python script_name.py
     ```
   - The script will launch Notepad and begin typing randomly generated Python code.

2. **Exit the Script:**
   - **Hotkey:** Press `Shift + Alt + Ctrl + C` to stop the script at any time.
   - **Interrupt Signal:** Press `Ctrl+C` in the console to terminate the script.

3. **Script Behavior:**
   - The script will continue typing code until the exit condition is met.
   - Upon termination, the script will close the Notepad window cleanly.

## Compiling and Packaging the script 
To install and use PyInstaller to package your Python script into a standalone executable, follow these steps:

1. **Install PyInstaller:**
   - You can install PyInstaller using `pip`. Open your command prompt or terminal and run:
        ```bash
        pip install pyinstaller
        ```
 
 2. **Package Your Script:**
    - Once PyInstaller is installed, you can use it to create an executable from your Python script. Navigate to the directory containing your script and run:
        ```bash
        pyinstaller --onefile your_script.py
        ```
    - `--onefile` bundles everything into a single executable file. If you omit this option, PyInstaller will create a directory with several files instead.

3. **Locate the Executable:**
    - After PyInstaller finishes building, you will find the executable in the dist directory within your project folder. The path will look something like:
        ```bash
        your_project/
        │
        ├── build/
        ├── dist/
        │   └── your_script.exe
        ├── your_script.py
        └── your_script.spec
        ```
4. **Run the Executable:**
    - You can now run the executable directly by double-clicking it or executing it from the command line:
        ```bash
        ./dist/your_script.exe
        ```
## Additional PyInstaller Options
- `--icon=icon.ico:` Use this option to add an icon to your executable.
    ```bash
    pyinstaller --onefile --icon=icon.ico your_script.py
    ```
- `--noconsole:` If you are creating a GUI application and do not want a command prompt window to appear, use this option.
    ```bash
    pyinstaller --onefile --noconsole your_script.py
    ```
- `--add-data="source_path;destination_path":` Include additional files (like configuration files) with your executable. Use a semicolon (;) on Windows and a colon (:) on macOS/Linux.
    ```bash
    pyinstaller --onefile --add-data="config.json;." your_script.py
    ```

## Troubleshooting

- **Notepad Not Found:**
  - Ensure Notepad is not manually closed or interfered with while the script is running.
  
- **Hotkey Not Working:**
  - Verify that no other applications are intercepting the hotkey combination.
  
- **Dependencies Issues:**
  - Ensure all required libraries are installed correctly. Use the `pip` commands provided to manage dependencies.

- **Missing Files or Libraries:**
    - If your executable is missing files or libraries, ensure that all dependencies are correctly installed and that PyInstaller can locate them. You may need to specify additional options or manually adjust the .spec file PyInstaller creates.

- **Antivirus Issues:** 
    - Sometimes, antivirus software may falsely flag executables created by PyInstaller. If this happens, you may need to add an exception in your antivirus settings.

## License
This script is provided as-is without any warranty. Use it at your own risk.

## Contact
For any questions or issues, please contact the author.