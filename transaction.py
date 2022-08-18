import json
import logging

from setup_logger import logger
from block import Block

# Set logger to name of class
logger = logging.getLogger('Transaction')


class Transaction:
    """Class to represent a transaction"""

    def __init__(self, fromAddr, toAddr, ammount):
        """"""
        self.fromAddr = fromAddr
        self.toAddr = toAddr
        self.ammount = ammount

    def __str__(self):
        """Output transaction in human readable format"""
        tx = {
            "From": self.fromAddr,
            "To": self.toAddr,
            "Ammount": self.ammount
        }

        return json.dumps(tx, indent=4)
