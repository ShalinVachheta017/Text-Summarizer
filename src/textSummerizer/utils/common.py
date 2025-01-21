'''
This file contains common utility functions for the Text-Summerizer project.

The common module includes functions for handling paths, logging, and exceptions.

Functions:

'''

import os
from box.exceptions import BoxException
from textSummerizer.logging import logger
import yaml
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns it as a ConfigBox object

    Args:
        path_to_yaml (str): path like input

    Returns:
        ConfigBox: returns the yaml file as a ConfigBox object

    """

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)

    except BoxException as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=False):
    """creates directories if they do not exist

    Args:
        path_to_directories (list): list of paths to create directories
        verbose (bool, optional): prints the message if True. Defaults to False.

    """


for path in path_to_directories:

    os.makedirs(path, exist_ok=True)
    if verbose:
        logger.info(f"Directory created at {path}")


@ensure_annotations
def get_size(path: Path) -> str:
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"
