from src.CreditCardFraudDetection.logger import logging
from src.CreditCardFraudDetection.exception import CustomException
import sys

from src.CreditCardFraudDetection.components.data_ingestion import DataIngestionConfig,DataIngestion

if __name__ == "__main__":
    logging.info("The execution has started")
    
    try:
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()
        
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)