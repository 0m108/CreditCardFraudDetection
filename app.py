from src.CreditCardFraudDetection.logger import logging
from src.CreditCardFraudDetection.exception import CustomException
import sys

from src.CreditCardFraudDetection.components.data_ingestion import DataIngestionConfig,DataIngestion

from src.CreditCardFraudDetection.components.data_transformation import DataTransformationConfig,DataTransformation

if __name__ == "__main__":
    logging.info("The execution has started")
    
    try:
        data_ingestion = DataIngestion()
        train_data_path,test_data_path = data_ingestion.initiate_data_ingestion()
        
        data_transformation = DataTransformation()
        train_data,test_data,_=data_transformation.initiate_data_transformation(train_data_path,test_data_path)
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)