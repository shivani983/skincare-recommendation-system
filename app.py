from skincare_recommender.exception.exception_handler import AppException
import sys
from skincare_recommender.logger.log import logging

try:
    a = 3/0
except Exception as e:

    logging.info(e)
    raise AppException(e,sys) from e
