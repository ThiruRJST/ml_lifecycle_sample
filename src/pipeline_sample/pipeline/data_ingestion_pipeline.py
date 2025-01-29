from src.pipeline_sample.components.data_ingestion import DataIngestion
from src.pipeline_sample.config.configuration import ConfigurationManager
from src.pipeline_sample import logger


STAGE_NAME = "Data Ingestion"

class DataIngestionTrainPipeline:
    def __init__(self):
        pass
    
    def run_ingestion_pipeline(self):
        config_manager = ConfigurationManager()
        data_ingestion_config = config_manager.get_data_ingestion_config()
        data_ingestion_component = DataIngestion(config=data_ingestion_config)
        data_ingestion_component.download_file()