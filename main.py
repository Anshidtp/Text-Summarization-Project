from textsummarizer.pipeline.stage01_data_ingestion import DataIngestionTrainPipeline
from textsummarizer.pipeline.stage02_data_evaluation import DataValidationTrainPipeline
from textsummarizer.pipeline.stage03_data_transformation import DataTransformationTrainPipeline
from textsummarizer.logging import logger

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f"{STAGE_NAME} started")
    data_ingestion = DataIngestionTrainPipeline()
    data_ingestion.main()
    logger.info(f"{STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f"{STAGE_NAME} started")
    data_validation = DataValidationTrainPipeline()
    data_validation.main()
    logger.info(f"{STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f"{STAGE_NAME} started")
    data_transformation = DataTransformationTrainPipeline()
    data_transformation.main()
    logger.info(f"{STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e