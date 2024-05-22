import sys
from src.CreditCardFraudDetection.exception import CustomException
from src.CreditCardFraudDetection.logger import logging
import pandas as pd
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score
import os
import pickle
import numpy as np


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)