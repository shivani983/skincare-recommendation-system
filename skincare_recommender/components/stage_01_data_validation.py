import os
import sys
import ast 
import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import hstack, csr_matrix

from skincare_recommender.logger.log import logging
from skincare_recommender.config.configuration import AppConfiguration
from skincare_recommender.exception.exception_handler import AppException



class DataValidation:
    def __init__(self, app_config = AppConfiguration()):
        try:
            self.data_validation_config= app_config.get_data_validation_config()
        except Exception as e:
            raise AppException(e, sys) from e


    def preprocess_data(self):
        try:
            df = pd.read_csv(self.data_validation_config.cosmetics_csv_file, encoding='utf-8', on_bad_lines='skip')
            logging.info(f"the shape of the cosmetics.csv file is {df.shape}")



            text_cols = ['Label', 'Brand', 'Name','Ingredients']
            for cols in text_cols:
               df[cols] = df[cols].fillna("")

            df['Price']= df['Price'].fillna(df['Price'].mean())
            df['Rank'] = df['Rank'].fillna(df['Rank'].mean())


            # Saving the cleaned data for transformation
            os.makedirs(self.data_validation_config.clean_data_dir, exist_ok=True)
            df.to_csv(os.path.join(self.data_validation_config.clean_data_dir,'clean_cosmetics_data.csv'), index = False)
            logging.info(f"Saved cleaned data to {self.data_validation_config.clean_data_dir}")


            #saving numeric_data objects for web app
            os.makedirs(self.data_validation_config.serialized_objects_dir, exist_ok=True)
            pickle.dump(df,open(os.path.join(self.data_validation_config.serialized_objects_dir, "final_data.pkl"),'wb'))
            logging.info(f"Saved final_rating serialization object to {self.data_validation_config.serialized_objects_dir}")


        except Exception as e:
            raise AppException(e, sys) from e


    def initiate_data_validation(self):
        try:
            logging.info(f"{'='*20}Data Validation log started.{'='*20} ")
            self.preprocess_data()
            logging.info(f"{'='*20}Data Validation log completed.{'='*20} \n\n")
        except Exception as e:
            raise AppException(e, sys) from e        
            





