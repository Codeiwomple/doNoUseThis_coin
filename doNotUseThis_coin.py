import json
import logging

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization

from setup_logger import logger
from blockchain import Blockchain
from block import Block
from transaction import Transaction

"""
File to test and use the blockchain functionality
"""


# Set logger to name of class
logger = logging.getLogger('DoNotUseThis_coin')


def Main():

    # Create a user
    # (addr, private_key)
    bobAddr, bobKey = createUser()
    aliceAddr, aliceKey = createUser()

    # Create new blockchain
    print('\n' + "**CREATE BLOCKCHAIN**")
    myCoin = Blockchain()

    # Create a transaction
    # From bob to alice 100
    createTransaction(myCoin, bobAddr, aliceAddr, 100, bobKey)

    # Mine the block
    print('\n' + "**MINE THE BLOCK**")
    # Bob will mine, reward is 100
    myCoin.minePendingTransactions(bobAddr)

    # Retrieve balances
    print('\n' + "**GET BALANCES**")
    print("Bob's balance: " + str(myCoin.getBalance(bobAddr)))
    print("Alice's balance: " + str(myCoin.getBalance(aliceAddr)))

    # Check blockchain is valid
    print('\n' + "**CHECK CHAIN IS VALID**")
    print(f"The chain is {myCoin.isValid()}")

    # Create some more transactions
    # Bob should be on 0 (inc mining reward), Alice +100
    createTransaction(myCoin,  aliceAddr, bobAddr, 50, aliceKey)
    createTransaction(myCoin, bobAddr, aliceAddr, 5, bobKey)
    createTransaction(myCoin, bobAddr, aliceAddr, 5, bobKey)
    # Now Bob should have +40, Alice +60... Mining rewards not yet included

    # Mine the block
    print('\n' + "**MINE THE BLOCK**")
    # Bob will mine, +100 in pending
    myCoin.minePendingTransactions(bobAddr)

    # Retrieve balances
    print('\n' + "**GET BALANCES**")
    print("Bob's balance: " + str(myCoin.getBalance(bobAddr)))
    print("Alice's balance: " + str(myCoin.getBalance(aliceAddr)))

    # Check blockchain is valid
    print('\n' + "**CHECK CHAIN IS VALID**")
    print(f"The chain is {myCoin.isValid()}")

    """
    ################### TAMPER TEST CHANGE HASH ####################
    # Tamper with chain
    print('\n' + "**TAMPER WITH CHAIN**")
    print("**CHANGE A HASH**")
    print("**BEFORE**")
    print(str(myCoin))

    # Change a hash in second block
    myCoin.blockchain[1].hash = "CHANGED"

    print("**AFTER**")
    print(str(myCoin))

    # Check blockchain is valid
    print('\n' + "**CHECK CHAIN IS VALID**")
    print(f"The chain is {myCoin.isValid()}")
    """

    """
    ################### TAMPER TEST CHANGE PREVIOUS HASH ####################
    # Tamper with chain
    print('\n' + "**TAMPER WITH CHAIN**")
    print("**CHANGE A PREV HASH**")
    print("**BEFORE**")
    print(str(myCoin))

    # Change previoushash in second block
    myCoin.blockchain[1].previousHash = "CHANGED"

    print("**AFTER**")
    print(str(myCoin))

    # Check blockchain is valid
    print('\n' + "**CHECK CHAIN IS VALID**")
    print(f"The chain is {myCoin.isValid()}")
    """

    """
    ################### TAMPER TEST CHANGE A TRANSACTION VALUE ####################
    # Tamper with chain
    print('\n' + "**TAMPER WITH CHAIN**")
    print("**CHANGE A TRANSACTION VALUE**")
    print("**BEFORE**")
    print(str(myCoin.blockchain[2].transactions[1]))

    # Change a transaction value in third block
    myCoin.blockchain[2].transactions[1].ammount = 100
    print("**AFTER**")
    print(str(myCoin.blockchain[2].transactions[1]))

    # Check blockchain is valid
    print('\n' + "**CHECK CHAIN IS VALID**")
    print(f"The chain is {myCoin.isValid()}")
    """

    """
    ################### TEST SIGN WITH WRONG KEY ####################
    # Sign transaction from alice with bobs key
    createTransaction(myCoin,  aliceAddr, bobAddr, 50, bobKey)
    """


def createTransaction(blockchain, fromAddr, toAddr, ammount, signingKey):
    """
    Function to create a transaction and add it to the chains 
    pending Tx to be mined
    """

    # Declare a transaction
    print('\n' + "**DECLARE TRANSACTION**")
    tx = Transaction(fromAddr, toAddr, ammount)

    # Sign transaction
    print('\n' + "**SIGN TRANSACTION**")
    tx.signTransaction(signingKey)

    # Add the trasaction to pending
    print('\n' + "**ADD TRANSACTION**")
    blockchain.addTransaction(tx)


def createUser():
    """
    Function to generate an address and private key to create transactions 
    and test blockchain functionality
    """
    # Create keys
    print("**CREATE CRYPTO KEYS**")
    private_key = ec.generate_private_key(ec.SECP256K1(), default_backend())
    public_key = private_key.public_key()

    # Create address from keys
    print('\n' + "**CREATE WALLET ADDRESS**")
    addr = public_key.public_bytes(
        encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo)

    return (addr, private_key)


if __name__ == "__main__":
    Main()
