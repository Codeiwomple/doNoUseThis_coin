import json
import logging

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization

from setup_logger import logger
from blockchain import Blockchain
from block import Block
from transaction import Transaction


# Set logger to name of class
logger = logging.getLogger('DoNotUseThis_coin')


def Main():
    # Create keys
    print("**CREATE CRYPTO KEYS**")
    private_key = ec.generate_private_key(ec.SECP256K1(), default_backend())
    public_key = private_key.public_key()

    # Create address from keys
    print("**CREATE WALLET ADDRESS**")
    myAddr = public_key.public_bytes(
        encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo)

    # Create new blockchain
    print("**CREATE BLOCKCHAIN**")
    myCoin = Blockchain()

    # Create some transactions
    print("**CREATE TRANSACTION**")
    tx1 = Transaction(myAddr, "Someone", 100)

    # Sign transaction
    print("**SIGN TRANSACTION**")
    tx1.signTransaction(private_key)

    # Add the trasaction
    print("**ADD TRANSACTION**")
    myCoin.addTransaction(tx1)

    # Mine the block
    print("**MINE THE BLOCK**")
    myCoin.minePendingTransactions(myAddr)

    # Retrieve balance
    print("**GET MY BALANCE**")
    print(myCoin.getBalance(myAddr))


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
