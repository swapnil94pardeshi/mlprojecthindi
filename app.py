from src.mlproject.logger import logging
from src.mlproject.components.data_ingestion import Dataingestion
from src.mlproject.components.data_ingestion import Dataingestionconfig
from src.mlproject.components.data_transformation import DataTransformationConfig,DataTransformation
from src.mlproject.components.model_trainer import ModelTrainerConfig,ModelTrainer

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
        train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data_Path,test_data_Path)

        model_trainer=ModelTrainer()
        print(model_trainer.initiate_model_trainer(train_arr,test_arr))



    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)
     