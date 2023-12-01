from textsummarizer.pipeline.stage01_data_ingestion import DataIngestionTrainPipeline
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