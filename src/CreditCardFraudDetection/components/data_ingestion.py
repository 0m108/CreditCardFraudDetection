import os
import sys
from src.CreditCardFraudDetection.exception import CustomException
from src.CreditCardFraudDetection.logger import logging

from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    raw_data_path:str = os.path.join('artifacts','raw.csv')
    train_data_path:str = os.path.join('artifacts','train.csv')
    test_data_path:str = os.path.join('artifacts','test.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
        
    def initiate_data_ingestion(self):
        try:
            ##reading the data from local storage
            logging.info("Reading data from local storage")
            
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            
        except Exception as e:
            raise CustomException(e,sys)
