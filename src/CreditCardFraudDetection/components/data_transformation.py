import os
import sys
import pandas as pd
from dataclasses import dataclass
from sklearn import preprocessing
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

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
            numerical_columns = []
            
            '''
            # If categorical features are present
            categorical_columns = []
            '''
            numerical_pipeline = Pipeline(steps=[
                ("imputer", SimpleImputer(strategy='median'))
            ])
            '''
            categorical_pipeline = Pipeline(steps=[
                ("imputer", SimpleImputer(strategy = "most_frequent")),
                ("one_hot_encoder", OneHotEncoder()),
            ])
            
            logging.info(f"Categorical Columns:{categorical_columns}")
            
            '''
            logging.info(f"Numerical Columns:{numerical_columns}")
            
            preprocessor = ColumnTransformer(
                [
                    ("numerical_pipeline",numerical_pipeline,numerical_columns),
                    '''
                    ("categorical_pipeline",categorical_pipeline,categorical_columns)
                    '''
                ]
            )
            
            return preprocessor
            
        except Exception as e:
            raise CustomException(e,sys)
    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info("Reading the train and test file")
            
            preprocessing_object = self.get_data_transformer_object()
            
            
        except Exception as e:
            raise CustomException(sys,e)
               