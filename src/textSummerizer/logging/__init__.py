'''
 This file is an overview of logging
 This general idea is to log important information about the running of the text summarizer.
 The logging level determines the severity of the log entries.
 In this case, we'll use INFO level to log everything that's useful for debugging and understanding the progress of the summarization process.
 The log messages will be written to a file named "running_logs.log" in the "logs" directory.
 The logger object will be used to log messages using the defined log level and format.
 
 '''
# Import necessary libraries for file and logging management
import os
import sys
import logging

# Define the logging format string
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Define the directory and filepath for log files
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")

# Create the logs directory if it does not exist
os.makedirs(log_dir, exist_ok=True)

# Configure the logging settings
logging.basicConfig(
    level=logging.INFO,  # Set the logging level to INFO
    format=logging_str,  # Use the defined logging format
    handlers=[
        logging.FileHandler(log_filepath),  # Log to the specified file
        # Also log to the standard output (console)
        logging.StreamHandler(sys.stdout)
    ]
)

# Create a logger object with a specific name
logger = logging.getLogger("textSummarizerLogger")
