from dataclasses import dataclass
import os
import sys


from src.CreditCardFraudDetection.exception import CustomException
from src.CreditCardFraudDetection.logger import logging

@dataclass
class DataTransformationConfig:
    preprocessor_object_file_path = os.path.join('artifacts','preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
    
    def get_data_transformer_object(self):
        '''
        This function is responsible for data transformation
        '''
        try:
            pass
        except Exception as e:
            raise CustomException(e,sys)
               