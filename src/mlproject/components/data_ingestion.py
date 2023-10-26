import os
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging

from sklearn.model_selection import train_test_split

import pandas as pd
from dataclasses import dataclass
from src.mlproject.utils import read_sql_data

@dataclass
class Dataingestionconfig:
    train_data_Path:str=os.path.join('artifact','train.csv')
    test_data_Path:str=os.path.join('artifact','test.csv')
    raw_data_Path:str=os.path.join('artifact','raw.csv')

class Dataingestion:
    def __init__(self):
        self.ingestion_config=Dataingestionconfig()

    
    def initiate_data_ingestion(self):
        try:
            ##reading codd
            df=read_sql_data()
            logging.info("reading from mysql databse")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_Path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_Path,index=False,header=True)

            train_set,test_set=train_test_split(df,test_size=0.2,random_state=43)

            train_set.to_csv(self.ingestion_config.train_data_Path,index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_Path,index=False,header=True)

            logging.info("data ingestion completed")

            return(
                self.ingestion_config.train_data_Path,
                self.ingestion_config.test_data_Path
            )

        except Exception as e:
            raise CustomException(e,sys)
