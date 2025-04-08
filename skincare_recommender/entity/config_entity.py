from collections import namedtuple

DataIngestionConfig = namedtuple("DatasetConfig",["dataset_download_url",
                                                  "raw_data_dir",
                                                  "ingested_dir"])

DataValidationConfig = namedtuple("DataValidationConfig", ["clean_data_dir",
                                                           "cosmetics_csv_file",
                                                           "serialized_objects_dir"])

DataTransformationConfig = namedtuple("DataTransformationConfig", ["clean_data_file_path",
                                                                   "transformed_data_dir"]) 


ModelTrainerConfig = namedtuple("ModelTrainerConfig", ["transformed_data_file_path",
                                                      "trained_model_dir",
                                                      "trained_model_name"])

ModelRecommendationConfig = namedtuple("ModelRecommendationConfig", [
    "product_df_serialized_objects",        # DataFrame with product metadata
    "vectorizer_serialized_objects",        # Trained TF-IDF/Count Vectorizer
    "cosine_similarity_serialized_objects"  # Pre-computed similarity matrix
])
