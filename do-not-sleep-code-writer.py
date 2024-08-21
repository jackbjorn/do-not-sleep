import time
import pyautogui
import subprocess
import psutil
import win32gui
import win32con
import random
import ctypes
import signal
import sys
import keyboard

# Constants for preventing sleep
ES_CONTINUOUS = 0x80000000
ES_SYSTEM_REQUIRED = 0x00000001

# Sample keywords, operators, and Python elements
keywords = ['if', 'else', 'elif', 'for', 'while', 'try', 'except', 'finally', 'with', 'def', 'class', 'import', 'from', 'as', 'return', 'yield', 'break', 'continue', 'pass', 'raise']
data_types = ['int', 'float', 'str', 'list', 'dict', 'set', 'tuple', 'bool', 'None']
operators = ['+', '-', '*', '/', '%', '**', '//', '==', '!=', '>', '<', '>=', '<=', 'and', 'or', 'not', 'is', 'in']
exceptions = ['ValueError', 'TypeError', 'IndexError', 'KeyError', 'AttributeError', 'ZeroDivisionError', 'ImportError']
libraries = ['random', 'os', 'sys', 'math', 'datetime', 'itertools', 'collections', 'functools']

# Example of variable names, functions, and classes
var_names = ['var1', 'value', 'my_list', 'result', 'index', 'counter', 'flag', 'total', 'item', 'data']
func_names = ['process_data', 'calculate', 'check_value', 'handle_error', 'get_item', 'sort_list']
class_names = ['MyClass', 'DataProcessor', 'Calculator', 'ErrorHandler', 'ItemManager']

# Virtual key codes for each character
VK_CODES = {
    'a': 0x41, 'b': 0x42, 'c': 0x43, 'd': 0x44, 'e': 0x45, 'f': 0x46, 'g': 0x47, 'h': 0x48, 'i': 0x49, 'j': 0x4A,
    'k': 0x4B, 'l': 0x4C, 'm': 0x4D, 'n': 0x4E, 'o': 0x4F, 'p': 0x50, 'q': 0x51, 'r': 0x52, 's': 0x53, 't': 0x54,
    'u': 0x55, 'v': 0x56, 'w': 0x57, 'x': 0x58, 'y': 0x59, 'z': 0x5A, 'A': 0x41, 'B': 0x42, 'C': 0x43, 'D': 0x44,
    'E': 0x45, 'F': 0x46, 'G': 0x47, 'H': 0x48, 'I': 0x49, 'J': 0x4A, 'K': 0x4B, 'L': 0x4C, 'M': 0x4D, 'N': 0x4E,
    'O': 0x4F, 'P': 0x50, 'Q': 0x51, 'R': 0x52, 'S': 0x53, 'T': 0x54, 'U': 0x55, 'V': 0x56, 'W': 0x57, 'X': 0x58,
    'Y': 0x59, 'Z': 0x5A, '0': 0x30, '1': 0x31, '2': 0x32, '3': 0x33, '4': 0x34, '5': 0x35, '6': 0x36, '7': 0x37,
    '8': 0x38, '9': 0x39, ' ': 0x20, '\n': 0x0D, '\t': 0x09, '!': 0x31, '@': 0x32, '#': 0x33, '$': 0x34, '%': 0x35,
    '^': 0x36, '&': 0x37, '*': 0x38, '(': 0x39, ')': 0x30, '_': 0xBD, '+': 0xBB, '-': 0xBD, '=': 0xBB, '{': 0xDB,
    '}': 0xDD, '[': 0xDB, ']': 0xDD, '|': 0xDC, '\\': 0xDC, ':': 0xBA, ';': 0xBA, '"': 0xDE, "'": 0xDE, '<': 0xBC,
    '>': 0xBE, '?': 0xBF, ',': 0xBC, '.': 0xBE, '/': 0xBF, '~': 0xC0, '`': 0xC0
}

def send_key(key_code):
    # Simulate a physical key press and release
    ctypes.windll.user32.keybd_event(key_code, 0, 0, 0) # Key down
    ctypes.windll.user32.keybd_event(key_code, 0, 2, 0) # Key up

def prevent_sleep():
    ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS | ES_SYSTEM_REQUIRED)

def allow_sleep():
    ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS)

def signal_handler(sig, frame):
    # Cleanly exit the script
    print("\nInterrupt received. Exiting script.")
    allow_sleep() # revert the sleep prevention
    sys.exit(0)

def hotkey_handler():
    global exit_flag
    print("Hotkey pressed. Exiting script.")
    exit_flag = True

# def handle_hotkey():
#     print("Hotkey pressed. Exiting script.")
#     allow_sleep()
#     sys.exit(0)

def setup_hotkeys():
    keyboard.add_hotkey('shift+alt+ctrl+c', handle_hotkey)

def generate_import():
    """Generates random import statements."""
    if random.choice([True, False]):
        return f"import {random.choice(libraries)}"
    else:
        return f"from {random.choice(libraries)} import {random.choice(['*', 'path', 'exit', 'sqrt', 'datetime'])}"

def generate_variable_declaration():
    """Generates random variable declarations."""
    var_name = random.choice(var_names)
    data_type = random.choice(data_types)
    if data_type == 'int':
        value = random.randint(0, 100)
    elif data_type == 'float':
        value = round(random.uniform(0, 100), 2)
    elif data_type == 'str':
        value = f'"{random.choice(var_names)}"'
    elif data_type == 'list':
        value = [random.randint(0, 10) for _ in range(random.randint(2, 5))]
    elif data_type == 'dict':
        value = {random.choice(var_names): random.randint(0, 10) for _ in range(random.randint(2, 5))}
    elif data_type == 'set':
        value = set([random.randint(0, 10) for _ in range(random.randint(2, 5))])
    elif data_type == 'tuple':
        value = tuple([random.randint(0, 10) for _ in range(random.randint(2, 5))])
    elif data_type == 'bool':
        value = random.choice([True, False])
    else:
        value = 'None'
    return f"{var_name} = {value}"

def generate_function_definition():
    """Generates random function definitions."""
    func_name = random.choice(func_names)
    var_name = random.choice(var_names)
    return f"def {func_name}({var_name}):\n    return {var_name} * 2"

def generate_class_definition():
    """Generates random class definitions."""
    class_name = random.choice(class_names)
    func_name = random.choice(func_names)
    var_name = random.choice(var_names)
    return (f"class {class_name}:\n"
            f"    def __init__(self, {var_name}):\n"
            f"        self.{var_name} = {var_name}\n\n"
            f"    def {func_name}(self):\n"
            f"        return self.{var_name} * 2")

def generate_conditional():
    """Generates random if-else blocks."""
    var_name = random.choice(var_names)
    return (f"if {var_name} {random.choice(operators[7:])} {random.randint(0, 10)}:\n"
            f"    print('Condition met')\n"
            f"else:\n"
            f"    print('Condition not met')")

def generate_loop():
    """Generates random loops."""
    return (f"for i in range({random.randint(1, 10)}):\n"
            f"    print(i)")

def generate_try_except():
    """Generates random try-except blocks."""
    exception = random.choice(exceptions)
    return (f"try:\n"
            f"    {random.choice(var_names)} / 0\n"
            f"except {exception} as e:\n"
            f"    print('Handled {exception}:', e)")

def generate_random_code():
    """Generates a random line of Python code."""
    generators = [generate_import, generate_variable_declaration, generate_function_definition, generate_class_definition, generate_conditional, generate_loop, generate_try_except]
    return random.choice(generators)()

def find_notepad_window():
    def callback(hwnd, windows):
        if win32gui.IsWindowVisible(hwnd):
            if 'notepad' in win32gui.GetWindowText(hwnd).lower():
                windows.append(hwnd)
    windows = []
    win32gui.EnumWindows(callback, windows)
    return windows[0] if windows else None

def is_notepad_running():
    for proc in psutil.process_iter(['name']):
        if proc.info['name'].lower() == "notepad.exe":
            return True
    return False

def type_into_notepad(content):
    # Start Notepad and wait for it to be ready
    subprocess.Popen(['notepad.exe'])
    time.sleep(2)
    
    hwnd = find_notepad_window()
    if hwnd is None:
        print("Notepad window is not found")
        return

    win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
    win32gui.SetForegroundWindow(hwnd)
    
    # Typing simulation
    type_char = 0
    for char in content:
        if not is_notepad_running():
            print("Notepad has been closed. Exiting.")
            break
        type_char += 1
        prevent_sleep()
        if type_char >= random.uniform(10, 50):
            pyautogui.moveRel(random.randint(-10, 10), random.randint(-10, 10), duration=0.01)
            type_char = 0
        if char in VK_CODES:
            vk_code = VK_CODES[char]
            send_key(vk_code)
            time.sleep(random.uniform(0.05, 0.15))
        time.sleep(random.uniform(0.01, 0.05))

def main_loop():
    global exit_flag
    while not exit_flag:
        # Your main loop code here
        # Example:
        # Generate and print 4000 lines of random Python code
        num_lines = 4000
        python_code = ""
        for _ in range(num_lines):
            python_code = python_code + str(generate_random_code()) + "\n"
        # Run the typing function
        type_into_notepad(python_code)
        # Exit if the flag is set
        if exit_flag:
            break

if __name__ == '__main__':
    # Set up signal handler for Ctrl+C
    signal.signal(signal.SIGINT, signal_handler)
    
    # Set up hotkey monitoring
    keyboard.add_hotkey('shift+alt+ctrl+c', hotkey_handler)

    # Run the main loop
    main_loop()
    # # Set up signal handler for Ctrl+C
    # signal.signal(signal.SIGINT, signal_handler)
    
    # # Set up hotkey monitoring
    # keyboard.add_hotkey('shift+alt+ctrl+c', hotkey_handler)
    
    # # Generate and print 4000 lines of random Python code 
    # num_lines = 4000
    # python_code = "\n".join(str(generate_random_code()) for _ in range(num_lines))
    
    # # Run the typing function
    # type_into_notepad(python_code)




