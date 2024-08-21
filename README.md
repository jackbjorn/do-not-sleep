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

## Troubleshooting

- **Notepad Not Found:**
  - Ensure Notepad is not manually closed or interfered with while the script is running.
  
- **Hotkey Not Working:**
  - Verify that no other applications are intercepting the hotkey combination.
  
- **Dependencies Issues:**
  - Ensure all required libraries are installed correctly. Use the `pip` commands provided to manage dependencies.

## License
This script is provided as-is without any warranty. Use it at your own risk.

## Contact
For any questions or issues, please contact the author.