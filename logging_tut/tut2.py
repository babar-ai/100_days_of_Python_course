'''
# Difference b/w logging.info and logging.debug

1. Visibility Difference

Python logging shows messages based on the configured level.

Example configuration:
logging.basicConfig(level=logging.INFO)

-> this configuration will hide debug() messages
-> info() is used only when we want to print general message on consule not in file


but if we configure like 
Example configuration:
logging.basicConfig(level=logging.DEBUG)

Simple Rule to Remember

Use INFO when the message is important for users.

Use DEBUG when the message is useful only for debugging.

one key difference if we configure logging as info then debug messages will be not ignored.
But if we configure with DEBUG the logging.info message will automatically enable .

'''

""
""" Very Useful Trick (Recommended)

Sometimes you want:

DEBUG saved in file

INFO printed on screen

You can do this with different handler levels:"""

import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler(sys.stdout)
    ]
)

logging.getLogger().handlers[0].setLevel(logging.DEBUG)   # file
logging.getLogger().handlers[1].setLevel(logging.INFO)    # console