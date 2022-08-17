import json

from blockchain import Blockchain
from block import Block


class DoNotUseThis_coin:
    """Class to """

    def __init__(self):
        """"""
        # Create a blockchain
        self.myBlockchain = Blockchain()

        # Add some blocks
        self.myBlockchain.addBlock(Block(1, "10/07/2017", {'ammount': 4}))
        self.myBlockchain.addBlock(Block(2, "12/07/2017", {'ammount': 10}))

        print(self.myBlockchain.chain)


if __name__ == '__main__':
    myCoin = DoNotUseThis_coin()
