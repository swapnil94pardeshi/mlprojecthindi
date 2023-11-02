from src.mlproject.logger import logging
from src.mlproject.components.data_ingestion import Dataingestion
from src.mlproject.components.data_ingestion import Dataingestionconfig
from src.mlproject.components.data_transformation import DataTransformationConfig,DataTransformation

import sys
from src.mlproject.utils import read_sql_data,save_object


from src.mlproject.exception import CustomException

if __name__=="__main__":
    logging.info("The execution has started")

    try:
        #data_ingestion_config=Dataingestionconfig()
        data_ingestion=Dataingestion()
        train_data_Path,test_data_Path=data_ingestion.initiate_data_ingestion()

        #data_transformation_config=DataTransformationConfig()
        data_transformation=DataTransformation()
        data_transformation.initiate_data_transformation(train_data_Path,test_data_Path)

    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)
     