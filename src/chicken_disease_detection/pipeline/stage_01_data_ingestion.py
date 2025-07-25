from src.chicken_disease_detection.config.configuration import ConfigurationManager
from src.chicken_disease_detection.components.data_ingeshion import DataIngestion
from src.chicken_disease_detection import logger



STAGE_NAME = "Data Ingestion stage"

class DataIngestionTraningPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


if __name__ == "__main__":
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        pipeline = DataIngestionTraningPipeline()
        pipeline.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x\n\n")
    except Exception as e:
        logger.exception(e)
        raise e
       
    
    
    