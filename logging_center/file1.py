# file1.py

import logging
from logging_config import *

logger = logging.getLogger(__name__)

def some_function():
    logger.debug("Debug message from file1")

if __name__ == "__main__":
    some_function()
