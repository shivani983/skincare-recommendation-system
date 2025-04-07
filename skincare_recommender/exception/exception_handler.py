import os
import sys


class AppException(Exception):
    """Base class for exceptions in this module."""


    def __init__(self,error_message: Exception, error_detail:sys):
        """ error"""

        super.__init__(error_message)
        self.error_message = AppException.error_message_detail(error_message,error_detail = error_detail)
        

    @staticmethod
    def error_message_detail(error: Exception, error_detail:sys):
        """
        error :Exception object raise from module
        error_detail : is system module contains detail information about system execution""" 
        _, _, exc_tb = error_detail.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename   