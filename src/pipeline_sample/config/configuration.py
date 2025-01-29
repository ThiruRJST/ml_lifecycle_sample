from src.pipeline_sample.constants import *
from src.pipeline_sample.entity.config_entity import DataIngestionConfig
from src.pipeline_sample.utils.common import read_yaml, create_directories


class ConfigurationManager:
    def __init__(self,
                 config_filepath: Path = CONFIG_FILE_PATH,
                 schema_file_path: Path = SCHEMA_FILE_PATH,
                 params_file_path: Path = PARAMS_FILE_PATH):
        
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_file_path)
        self.schema = read_yaml(schema_file_path)
        
        if type(self.config.artifacts_root) == str:
            create_directories([self.config.artifacts_root])
        else:
            create_directories(self.config.artifacts_root)
    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        
        config = self.config.data_ingestion
        return  DataIngestionConfig(
            root_dir=Path(config.root_dir),
            source_URL=config.source_URL,
            local_data_file=Path(config.local_data_file)
        )
        