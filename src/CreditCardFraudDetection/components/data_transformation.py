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
    preprocessor_file_path = os.path.join("artifacts","preprocessor.pkl")
    
class DataTransformation:
    def __init__(self):
        data_transformation_config = DataTransformationConfig()
    
    def get_preprocessor_obj(self,train_dataset_path,test_dataset_path):
        train_dataset = pd.read_csv(train_dataset_path)
        test_dataset = pd.read_csv(test_dataset_path)
        
        
    
    def initiate_data_transformation(self,train_dataset_path,test_dataset_path):
        pass