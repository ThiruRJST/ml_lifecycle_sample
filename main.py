from src.pipeline_sample import logger
from src.pipeline_sample.pipeline.data_ingestion_pipeline import DataIngestionTrainPipeline
from src.pipeline_sample.pipeline.data_validation_pipeline import DataValidationTrainPipeline

STAGE_NAME = "Data Ingestion"
logger.info (f">>>>>>>>>>>>>>>>> {STAGE_NAME} Started <<<<<<<<<<<<<<<<")
try:
    pipeline = DataIngestionTrainPipeline()
    pipeline.run_ingestion_pipeline()
    logger.info (f">>>>>>>>>>>>>>>>> {STAGE_NAME} Finished <<<<<<<<<<<<<<<<")

except Exception as e:
    logger.error(f"Failed to run the {STAGE_NAME} pipeline with exception: {e}")
    raise e


STAGE_NAME = "Data Validation"
logger.info (f">>>>>>>>>>>>>>>>> {STAGE_NAME} Started <<<<<<<<<<<<<<<<")
try:
    pipeline = DataValidationTrainPipeline()
    pipeline.validate_data()
    logger.info (f">>>>>>>>>>>>>>>>> {STAGE_NAME} Finished <<<<<<<<<<<<<<<<")

except Exception as e:
    logger.error(f"Failed to run the {STAGE_NAME} pipeline with exception: {e}")
    raise e