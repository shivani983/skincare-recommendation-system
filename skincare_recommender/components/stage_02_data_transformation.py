import os
import sys
import pickle
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from scipy.sparse import csr_matrix, hstack
from sklearn.feature_extraction.text import TfidfVectorizer

from skincare_recommender.logger.log import logging
from skincare_recommender.config.configuration import AppConfiguration
from skincare_recommender.exception.exception_handler import AppException


class DataTransformation:
    def __init__(self, app_config=AppConfiguration()):
        try:
            self.data_transformation_config = app_config.get_data_transformation_config()
            self.data_validation_config = app_config.get_data_validation_config()
        except Exception as e:
            raise AppException(e, sys) from e

    def get_data_transformer(self):
        try:
            # Load cleaned dataframe
            df= pd.read_csv(self.data_transformation_config.clean_data_file_path)
            df['combined_text'] = df['Label'] + " " + df['Brand'] + " " + df['Name'] + " " + df['Ingredients']

            # Process textual data (TF-IDF on Ingredients column as an example)
            tfidf = TfidfVectorizer(stop_words='english')
            tfidf_matrix = tfidf.fit_transform(df['combined_text'])

            numeric_cols = ['Price', 'Rank','Combination','Dry','Normal', 'Oily', 'Sensitive']
            numeric_data = df[numeric_cols]
            logging.info("TF-IDF transformation completed on 'Ingredients' column")

            # Process numeric features

            scaler = MinMaxScaler()
            numeric_matrix = scaler.fit_transform(numeric_data)
            logging.info("Scaled numeric data using MinMaxScaler")

            # csr_matrix
            numcsr_matrix = csr_matrix(numeric_matrix)


            # Combine numeric and textual data
            final_features = hstack([tfidf_matrix, numcsr_matrix]).tocsr()
            logging.info("Combined TF-IDF and scaled numeric matrix")

            # Create index mappings for later use
            indices_name = pd.Series(df.index, index=df['Name']).drop_duplicates()
            indices_label = pd.Series(df.index, index=df['Label']).drop_duplicates()
            indices_ingredients = pd.Series(df.index, index=df['Ingredients']).drop_duplicates()
            indices_brand = pd.Series(df.index, index=df['Brand']).drop_duplicates()

            # Save transformed sparse matrix
            os.makedirs(self.data_transformation_config.transformed_data_dir, exist_ok=True)
            pickle.dump(final_features, open(os.path.join(
                self.data_transformation_config.transformed_data_dir, "transformed_cosmetics.pkl"), 'wb'))
            logging.info(f"Saved csr_matrix to {self.data_transformation_config.transformed_data_dir}")

            # Save indices for later lookup
            os.makedirs(self.data_validation_config.serialized_objects_dir, exist_ok=True)
            pickle.dump({
                "indices_name": indices_name,
                "indices_label": indices_label,
                "indices_ingredients": indices_ingredients,
                "indices_brand": indices_brand
            }, open(os.path.join(self.data_validation_config.serialized_objects_dir, "indices.pkl"), 'wb'))
            logging.info(f"Saved index mappings to {self.data_validation_config.serialized_objects_dir}")

        except Exception as e:
            raise AppException(e, sys) from e

    def initiate_data_transformation(self):
        try:
            logging.info(f"{'=' * 20} Data Transformation log started. {'=' * 20}")
            self.get_data_transformer()
            logging.info(f"{'=' * 20} Data Transformation log completed. {'=' * 20}\n\n")
        except Exception as e:
            raise AppException(e, sys) from e
