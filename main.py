from src.chicken_disease_detection import logger
from src.chicken_disease_detection.pipeline.stage_01_data_ingestion import DataIngestionTraningPipeline
from src.chicken_disease_detection.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    pipeline = DataIngestionTraningPipeline()
    pipeline.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x\n\n")
except Exception as e:
        logger.exception(e)
        raise e



SATGE_NAME = "Prepare Base Model stage"
try:
    logger.info(f"*******************")
    logger.info(f">>>>> stage {SATGE_NAME} started <<<<<")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f">>>>> stage {SATGE_NAME} completed <<<<<\n\nx==========x\n\n")
except Exception as e:
        logger.exception(e)
        raise e




    