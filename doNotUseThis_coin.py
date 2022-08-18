import json
import logging

from setup_logger import logger
from blockchain import Blockchain
from block import Block
from transaction import Transaction

# Set logger to name of class
logger = logging.getLogger('DoNotUseThis_coin')


def Main():
    # Create new blockchain
    myCoin = Blockchain()

    # Create some transactions
    print("**CREATE TRANSACTIONS**")
    myCoin.createTransaction(Transaction("Ben", "John", 100))
    myCoin.createTransaction(Transaction("Jodie", "Ben", 20))

    # Mine the block
    print("**MINE THE BLOCK**")
    myCoin.minePendingTransactions("Conor")

    # Retrieve balance
    print("**GET MY BALANCE**")
    print(myCoin.getBalance("Conor"))

    # Create some more transactions
    print("**CREATE TRANSACTIONS**")
    myCoin.createTransaction(Transaction("Ben", "Conor", 1000))
    myCoin.createTransaction(Transaction("James", "Jodie", 200))

    # Mine the block
    print("**MINE THE BLOCK**")
    myCoin.minePendingTransactions("Conor")

    # Retrieve balance
    print("**GET MY BALANCE**")
    print(myCoin.getBalance("Conor"))


if __name__ == "__main__":
    Main()


"""
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

    print("Add new block 1")
    myCoin.addBlock(Block("10/07/2017", data))

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
    print("Add new block 2")
    myCoin.addBlock(Block("12/07/2017", data))

    print(str(myCoin))

    print(f"The chain is valid {myCoin.isValid()}")

    print("Change block 2 data")
    myCoin.blockchain[2].data = "Hello"

    print(f"The chain is valid {myCoin.isValid()}")
"""
