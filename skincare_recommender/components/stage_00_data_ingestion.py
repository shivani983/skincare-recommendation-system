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
            self.data_ingestion_config = app_config.get_data_ingestion_config()
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

