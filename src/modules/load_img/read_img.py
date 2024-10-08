import cv2
import sys
from src.logger import logging
from src.exception import CustomException

class ReadImage:
    def __init__(self):
        logging.info('Initialize read image module ...')
    
    
    def read_image(self, img_path):
        try:
            img_data = cv2.imread(img_path)
            logging.info('Finished reading image.')
            return img_data
            
        except Exception as e:
            raise CustomException(e,sys)
    
    
    