import logging  # Importing the logging module

class LogGen:
    @staticmethod
    def loggen():
    
        # Static method to generate a logger instance.
       
        # Configuring the logging system
        logging.basicConfig(
            filename=".\\logs\\automation.log",  # Specifying the path for the log file
            format='%(asctime)s: %(levelname)s: %(message)s',  # Specifying the log message format
            datefmt='%m/%d/%Y %I:%M:%S %p'  # Specifying the date/time format for log messages
        )
        
        # Getting the root logger instance
        logger = logging.getLogger()
        
        # Setting the logging level to INFO
        logger.setLevel(logging.INFO)
        
        # Returning the logger instance
        return logger
