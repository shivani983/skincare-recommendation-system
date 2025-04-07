import yaml
import sys
from skincare_recommender.exception.exception_handler import AppException


def read_yaml_file(file_path:str)->dict:
    """
    reads a yaml file and returns the contents as s dictionary.
    file_path: str
    """

    try:
        with open(file_path,'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
        
    except Exception as e:
        raise AppException(e,sys) from e    