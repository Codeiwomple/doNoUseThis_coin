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

        # print(data)
        # print(json.dumps(data, indent=4))

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

        print()
        print(str(self.myBlockchain))


if __name__ == '__main__':
    myCoin = DoNotUseThis_coin()
