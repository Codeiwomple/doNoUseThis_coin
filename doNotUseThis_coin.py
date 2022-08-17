import json
import logging

from setup_logger import logger
from blockchain import Blockchain
from block import Block

# Set logger to name of class
logger = logging.getLogger('DoNotUseThis_coin')


class DoNotUseThis_coin:
    """Class to """

    def __init__(self):
        """"""
        # Create a blockchain
        self.myBlockchain = Blockchain()

        # Add some blocks
        data = {
            "Transactions": [
                {
                    "To": "John",
                    "From": "Ben",
                    "Ammount": 100
                },
                {
                    "To": "Jodie",
                    "From": "Ben",
                    "Ammount": 20
                }
            ]
        }

        self.myBlockchain.addBlock(Block(1, "10/07/2017", data))

        data = {
            "Transactions": [
                {
                    "To": "Conor",
                    "From": "Ben",
                    "Ammount": 1000
                },
                {
                    "To": "Jodie",
                    "From": "James",
                    "Ammount": 200
                }
            ]
        }
        self.myBlockchain.addBlock(Block(2, "12/07/2017", data))

        print(str(self.myBlockchain))


if __name__ == '__main__':
    myCoin = DoNotUseThis_coin()
