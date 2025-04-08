import os
import sys
import pickle
from sklearn.neighbors import NearestNeighbors
from skincare_recommender.logger.log import logging
from skincare_recommender.config.configuration import AppConfiguration
from skincare_recommender.exception.exception_handler import AppException


class ModelTrainer:
    def __init__(self, app_config = AppConfiguration()):
        try:
            self.model_trainer_config = app_config.get_model_trainer_config()
        except Exception as e:
            raise AppException(e, sys) from e

    
    def train(self):
        try:
            #loading pivot data
            final_features = pickle.load(open(self.model_trainer_config.transformed_data_file_path,'rb'))
            #Training model
            knn_model = NearestNeighbors(metric = 'cosine',algorithm = 'brute')
            knn_model.fit(final_features)


            #Saving model object for recommendations
            os.makedirs(self.model_trainer_config.trained_model_dir, exist_ok=True)
            knn_recommendation_model = os.path.join(self.model_trainer_config.trained_model_dir,self.model_trainer_config.trained_model_name)
            pickle.dump(knn_model,open(knn_recommendation_model,'wb'))
            logging.info(f"Saving final model to {knn_recommendation_model}")

        except Exception as e:
            raise AppException(e, sys) from e

    

    def initiate_model_trainer(self):
        try:
            logging.info(f"{'='*20}Model Trainer log started.{'='*20} ")
            self.train()
            logging.info(f"{'='*20}Model Trainer log completed.{'='*20} \n\n")
        except Exception as e:
            raise AppException(e, sys) from e
