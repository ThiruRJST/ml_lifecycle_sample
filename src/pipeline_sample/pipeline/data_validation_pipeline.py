import os

from src.pipeline_sample import logger
from src.pipeline_sample.components.data_validation import DataValidation
from src.pipeline_sample.entity.config_entity import DataValidationConfig
from src.pipeline_sample.utils.common import create_directories
from src.pipeline_sample.config.configuration import ConfigurationManager



# First component
class DataValidationTrainPipeline:
    def __init__(self):
        
        self.data_validation_config = ConfigurationManager().get_data_validation_config()
        create_directories([self.data_validation_config.root_dir])
        
    def validate_data(self):
        data_validation = DataValidation(self.data_validation_config)
        data_validation.initiate_data_validation()
        logger.info(f"Data validation completed successfully")