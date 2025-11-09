"""
How Custom Logging Fixes Problems discussed in tut1.py

By creating a custom logger (like your get_logger() function):
Logs include timestamps, module names, and severity levels
Logs can be sent to files, console, or remote servers
Each module can have its own logger name and level
You can format logs consistently
Can be centralied for entire project, making debugging and monitoring much easier

"""
import logging
from logging.handlers import RotatingFileHandler



def setup_logger(name: str = None):
    if name is None:
        name = __name__  # Use caller's module name
    
    logger = logging.getLogger(name)
    

    # 1: Prevent duplicate handler
    if logger.handlers:
        return logger
    

    logger.setLevel(logging.INFO)
    
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        "%Y-%m-%d %H:%M:%S"
    )
    
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # : Add rotation (5MB max, 3 backups)
    file_handler = RotatingFileHandler(
        "automation.log",
        maxBytes=5*1024*1024,              # file size
        backupCount=3,
        encoding="utf-8"
    )
    
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    


    return logger
