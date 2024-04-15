from cgi import test
import os
import sys
from src.CreditCardFraudDetection.exception import CustomException
from src.CreditCardFraudDetection.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split

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
            logging.info("Reading data from local machine")
            csv_file_path = "C:/Users/HP/Desktop/creditcard.csv"  # path of dataset in your local machine
            df = pd.read_csv(csv_file_path)
            
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            train_dataset, test_dataset = train_test_split(df, test_size=0.2)
            train_dataset.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_dataset.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
            
        except Exception as e:
            raise CustomException(e,sys)
