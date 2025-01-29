import joblib
import json
import os
import yaml

from box import ConfigBox
from box.exceptions import BoxValueError
from ensure import ensure_annotations
from pathlib import Path
from src.pipeline_sample import logger
from typing import Any


@ensure_annotations
def read_yaml(yaml_filepath: Path) -> ConfigBox:
    """read yaml file and returns

    Args:
        yaml_filepath (Path): path to yaml file

    Raises:
        ValueError: if yaml file is empty

    Returns:
        ConfigBox: return config box type object
    """

    try:
        with open(yaml_filepath, "r") as file:
            yaml_data = yaml.safe_load(file)
            logger.info(f"YAML file laoded successfully: {yaml_filepath}")
            return ConfigBox(yaml_data)

    except BoxValueError as e:
        raise ValueError(f"YAML file is empty: {yaml_filepath}")

    except Exception as e:
        raise e


@ensure_annotations
def create_directories(paths_to_directories: list, verbose=True):
    """Create directories

    Args:
        paths_to_directories (list): list of paths to directories
        verbose (bool, optional): Whether to show a message or not
        Ignore if multiple directories are created. Defaults to True.
    """

    for directory in paths_to_directories:
        os.makedirs(directory, exist_ok=True)
        if verbose:
            logger.info(f"Directory created: {directory}")

@ensure_annotations
def save_json(save_path:Path, data: dict):
    """save to data to json file

    Args:
        save_path (Path): path to save json file
        data (dict): dict data to save
    """
    with open(save_path, "w") as file:
        json.dump(data, file, indent=4)
        
    logger.info(f"Data saved to json file: {save_path}")
    
@ensure_annotations
def load_json(path: Path):
    """load data from json file to configbox

    Args:
        path (Path): json filepath to load.
    
    Returns:
        ConfigBox: return config box type object
    """
    with open(path, "r") as file:
        data = json.load(file)
        return ConfigBox(data)
    logger.info(f"Data loaded from json file: {path}")

@ensure_annotations
def save_bin(data: Any, save_path: Path):
    """save binary file data

    Args:
        data (Any): The data to save in binary file
        save_path (Path): The path to save the binary file
    """
    with open(save_path, "wb") as file:
        joblib.dump(data, file)
    logger.info(f"Data saved to binary file: {save_path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """load data from binary file

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in file
    """
    with open(path, "rb") as file:
        data = joblib.load(file)
        logger.info(f"Data loaded from binary file: {path}")
        return data
    