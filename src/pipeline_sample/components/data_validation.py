import json
import pandas as pd

from src.pipeline_sample.utils.common import create_directories
from src.pipeline_sample.entity.config_entity import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config
        create_directories([self.config.root_dir])
    
    def initiate_data_validation(self):
        
        ##Read the data file
        data = pd.read_csv(self.config.data_file)
        all_cols = data.columns.tolist()
        
        ##Get schema
        schema = self.config.all_schema
        
        for col in all_cols:
            if col not in schema:
                status = {"validation_status": "Failed", "reason": f"Column {col} not in schema"}
                with open(self.config.status_file, "w") as f:
                    json.dump(status, f)
            
            else:
                status = {"validation_status": "Success"}
                with open(self.config.status_file, "w") as f:
                    json.dump(status, f)
        
        