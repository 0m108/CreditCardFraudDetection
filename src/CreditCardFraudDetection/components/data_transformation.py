import os
import sys
import numpy as np
import pandas as pd
from src.CreditCardFraudDetection.utils import save_object
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
    
    def get_preprocessor_obj(self, train_or_test_dataset_path):
        
        try:
            dataset = pd.read_csv(train_or_test_dataset_path)
            numerical_columns = list(dataset.columns)
        
            numerical_pipeline = Pipeline(steps=[
                ("imputer",SimpleImputer(strategy='median')),
                ("scalar",StandardScaler())
            ])
        
            logging.info(f"Numerical Columns:{numerical_columns}")
        
            preprocessor=ColumnTransformer(
                    [
                        ("num_pipeline",numerical_pipeline,numerical_columns)
                    ]

            )
            return preprocessor
        except Exception as e:
            raise CustomException(e,sys)
    
    def initiate_data_transformation(self,train_dataset_path,test_dataset_path):
        try:
            train_dataset = pd.read_csv(train_dataset_path)
            test_dataset = pd.read_csv(test_dataset_path)
            logging.info("Reading the train and test file")
            
            preprocessing_obj = self.get_preprocessor_obj(train_dataset_path)
            
            target_column_name = "Class"
            ## divide the train dataset to independent and dependent feature

            input_features_train_df=train_dataset.drop(columns=[target_column_name], axis=1)
            target_feature_train_df=train_dataset[target_column_name]

            ## divide the test dataset to independent and dependent feature
            

            input_feature_test_df=test_dataset.drop(columns=[target_column_name], axis=1)
            target_feature_test_df=test_dataset[target_column_name]
            
            logging.info("Applying Preprocessing on training and test dataframe")
            
            input_feature_train_arr=preprocessing_obj.fit_transform(input_features_train_df)
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)
            
            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            save_object(

                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )
            logging.info(f"Saved preprocessing object")
            
            return(
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_file_path
            )
            
        except Exception as e:
            raise CustomException(e,sys)