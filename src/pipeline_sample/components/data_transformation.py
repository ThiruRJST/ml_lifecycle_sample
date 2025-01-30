import json
import pandas as pd
import os

from sklearn.model_selection import train_test_split
from src.pipeline_sample import logger
from src.pipeline_sample.entity.config_entity import DataTransformationConfig
from src.pipeline_sample.utils.common import create_directories



class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        create_directories([self.config.root_dir])
    
    def initiate_data_transformation(self):
        
        status_check = json.load(open(self.config.status_file, 'r'))
        if status_check['validation_status'] == "Success":
            data = pd.read_csv(self.config.data_file)
            
            ##Data Transformation
            train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)
            logger.info(f"Dataset Split into Train and Test with shapes: {train_data.shape} and {test_data.shape} respectively.")
            
            train_data.to_csv(os.path.join(self.config.root_dir, "train_data.csv"), index=False)
            test_data.to_csv(os.path.join(self.config.root_dir, "test_data.csv"), index=False)
        
        else:
            logger.info(f"Data Schema is not valid.")