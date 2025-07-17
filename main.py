from src.chicken_disease_detection import logger
from src.chicken_disease_detection.pipeline.stage_01_data_ingestion import DataIngestionTraningPipeline

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    pipeline = DataIngestionTraningPipeline()
    pipeline.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x\n\n")
except Exception as e:
    logger.exception(e)
    raise e