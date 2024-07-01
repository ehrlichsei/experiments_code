# file2.py

import logging
from logging_config import *

logger = logging.getLogger(__name__)

def another_function():
    logger.debug("Debug message from file2")

if __name__ == "__main__":
    another_function()
