import logging

''''
What Is Logging in Python?

Logging means recording what your program is doing while it runs —

for example:
When it started or stopped
What actions it took (like “logged into website”, “file downloaded”)

Noted that It’s like keeping a diary of your program’s behavior so that you (or another developer) can later understand what happened — especially if something goes wrong.

Python’s built-in logging module has 5 main levels:

1. DEBUG: Detailed information, typically of interest only when diagnosing problems.
2. INFO:  General events / progress I.E login success, file saved etc.  
3. WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g., ‘disk space low’). The software is still working as expected.
4. ERROR: Due to a more serious problem, the software has not been able to perform some function.  "Page not found"
5. CRITICAL: A very serious error, indicating that the program itself may be unable to continue running.

'''

# print(logging.info("This is an info message"))  # None
# print(logging.error("This is an error message"))  # None
# print(logging.debug("This is a debug message"))  # None
# print(logging.warning("This is a warning message"))  # None
# print(logging.critical("This is a critical message"))  # None


'''
output 

PS D:\All other stuffs\100_days_of_Python_course\logging_tut> python tut1.py
None
ERROR:root:This is an error message
None
None
WARNING:root:This is a warning message
None
CRITICAL:root:This is a critical message

'''

# by default logging logs messages not store in any file i.e  No file output by default
# You don’t know which file/module generated each log message
# You can configure logging to log messages to a file, include timestamps, and more.


from custom_logging import setup_logger

logger = setup_logger(__name__)

logger.info("This is an info message")
logger.error("This is an error message")    