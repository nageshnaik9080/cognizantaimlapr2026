#configure log format
import logging

def setup_logger():
    #create logger for healthcare application
    logger = logging.getLogger('healthcare_logger')
    logger.setLevel(logging.DEBUG)
    
    #check if logger already has handlers to avoid duplicate logs
    if logger.hasHandlers():
        return logger

    #file handler
    file_handler = logging.FileHandler('healthcare.log')
    logger.setLevel(logging.DEBUG)

    #formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger
    
