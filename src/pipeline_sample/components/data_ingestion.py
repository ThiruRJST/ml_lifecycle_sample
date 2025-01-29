import os
import urllib.request as request

from src.pipeline_sample import logger
from src.pipeline_sample.entity.config_entity import DataIngestionConfig
from src.pipeline_sample.utils.common import create_directories

# First component
class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
        create_directories([self.config.root_dir])
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(self.config.source_URL, self.config.local_data_file)
            logger.info(f"Downloaded file from {self.config.source_URL} with informations: {headers} to {filename}")
        else:
            logger.info(f"File already exists at {self.config.local_data_file}")
            
            