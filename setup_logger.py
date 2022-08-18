import logging
import sys

"""
A class to set up logging functionality for doNotUseThis_coin

Logging levels:
CRITICAL
ERROR
WARNING
INFO
DEBUG
NOTSET
"""

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
logger = logging.getLogger('log')
