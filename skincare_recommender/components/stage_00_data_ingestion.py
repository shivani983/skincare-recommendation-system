import os
import sys
from six.moves import urllib
import zipfile
from skincare_recommender.logger.log import logging
from skincare_recommender.exception.exception_handler import AppException
from skincare_recommender.config.configuration import AppConfiguration



class DataIngestion:
    def __init__(self, app_config = AppConfiguration):
        """
        data ingestion initialization
        data_ingestion_config: DataIngestionConfig"""
        try:
            logging.info(f"{'='*20}Data Ingestion log started.{'='*20}")
            self.app_config = AppConfiguration()
            self.data_ingestion_config = self.app_config.get_data_ingestion_config()
        except Exception as e:
            raise AppException(e,sys) from e

    def download_data(self):
        """
        fetch the data from the url"""

        try:
             dataset_url = self.data_ingestion_config.dataset_download_url
             zip_download_dir = self.data_ingestion_config.raw_data_dir
             os.makedirs(zip_download_dir, exist_ok = True)
             data_file_name = os.path.basename(dataset_url)
             zip_file_path = os.path.join(zip_download_dir, data_file_name)
             logging.info(f"downloading data from {dataset_url} into file {zip_file_path}")
             urllib.request.urlretrieve(dataset_url,zip_file_path)
             logging.info(f"downloaded data from {dataset_url} into file {zip_file_path}")
             return zip_file_path
        
        except Exception as e:
            raise AppException(e,sys) from e
        
    def extract_zip_file(self,zip_file_path: str):
        """
            zip_file_path :str
            extracts the zip file into the data direcotry
            function returns None"""

        try:
            ingested_dir = self.data_ingestion_config.ingested_dir
            os.makedirs(ingested_dir, exist_ok = True)
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(ingested_dir)
            logging.info(f"Extracting zip file: {zip_file_path} into dir: {ingested_dir}")

        except Exception as e:
            raise AppException(e,sys) from e

    def initiate_data_ingestion(self):
        try:
            zip_file_path = self.download_data()
            self.extract_zip_file(zip_file_path = zip_file_path)
            logging.info(f"{'='*20} data ingestion log completed. {'='*20} \n\n")
        except Exception as e:
            raise AppException(e,sys) from e                



