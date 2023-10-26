from src.mlproject.logger import logging
from src.mlproject.components.data_ingestion import Dataingestion
from src.mlproject.components.data_ingestion import Dataingestionconfig
import sys
from src.mlproject.utils import read_sql_data

from src.mlproject.exception import CustomException

if __name__=="__main__":
    logging.info("The execution has started")

    try:
        #data_ingestion_config=Dataingestionconfig()
        data_ingestion=Dataingestion()
        data_ingestion.initiate_data_ingestion()
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)
     