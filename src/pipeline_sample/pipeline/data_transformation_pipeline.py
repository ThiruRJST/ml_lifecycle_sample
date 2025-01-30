import os

from src.pipeline_sample import logger
from src.pipeline_sample.components.data_transformation import DataTransformation
from src.pipeline_sample.utils.common import create_directories
from src.pipeline_sample.config.configuration import ConfigurationManager



# First component
class DataTransformationTrainPipeline:
    def __init__(self):
        
        self.data_transformation_config = ConfigurationManager().get_data_transformation_config()
        create_directories([self.data_transformation_config.root_dir])
        
    def transform_data(self):
        data_transformation = DataTransformation(self.data_transformation_config)
        data_transformation.initiate_data_transformation()
        
        logger.info(f"Data transformation completed successfully")