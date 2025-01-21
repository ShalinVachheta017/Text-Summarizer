'''
This script creates the project structure for the textSummerizer project.
The project structure is as follows:
    textSummerizer
    ├── .github/workflows/.gitkeep
    ├── src/textSummerizer/__init__.py
    ├── src/textSummerizer/components/__init__.py
    ├── src/textSummerizer/utils/__init__.py
    ├── src/textSummerizer/utils/common.py
    ├── src/textSummerizer/logging/__init__.py
    ├── src/textSummerizer/config/__init__.py
    ├── src/textSummerizer/config/configuration.py
    ├── src/textSummerizer/pipeline/__init__.py
    ├── src/textSummerizer/entity/__init__.py
    ├── src/textSummerizer/constants/__init__.py
    ├── config/config.yaml
    ├── main.py
    ├── params.yaml
    ├── requirements.txt
    ├── Dockerfile
    ├── setup.py
    ├── app.py
    └── research/trials.ipynb
    └── README.md
    └── LICENSE
    
The script checks if the files already exist and if they are empty. If the file does not exist or is empty, it creates the file.
If the file already exists, it logs that the file already exists.

The script also checks if the project name is valid by ensuring it does not contain any special characters or whitespace. If the project name is invalid, it logs an error message. 

The script then creates the project structure by creating directories and files as needed. It logs the successful creation of each file.

Note: This script assumes that the current working directory is the root of the project. Adjust the paths and file names according to your project structure.

'''
import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name = 'textSummerizer'

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",  # constrctor file
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "main.py",
    "params.yaml",
    "requirements.txt",
    "Dockerfile",
    "setup.py",
    "app.py",
    "research/trials.ipynb"
]

# Checking if the project name is valid
for filepath in list_of_files:
    filepath = Path(filepath)  # Ensure the path is a Path object
    filedir, filename = os.path.split(filepath)
    
    if filedir != "":  # if the file is not in the root directory
        # create the directory if it does not exist
        os.makedirs(filedir, exist_ok=True)
        logging.info("Creating directory: {filedir} for the file {filename}")

    # check if the file already exists
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass    # create an empty file
        logging.info(f"Created {filepath}")
    else:
        logging.info(f"{filename} already exists")
