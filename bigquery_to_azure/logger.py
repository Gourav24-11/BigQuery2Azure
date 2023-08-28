"""
logger.py
This module contains the Logger class for logging transfer status.
"""

class Logger:
    def __init__(self, log_file: str):
        self.log_file = log_file

    def log(self, message: str) -> None:
        """
        Log a message to the log file.
        """
        with open(self.log_file, "a") as file:
            file.write(message + "\n")
