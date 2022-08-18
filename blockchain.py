import json
import logging
import datetime

from setup_logger import logger
from block import Block
from transaction import Transaction

# Set logger to name of class
logger = logging.getLogger('Blockchain')


class Blockchain:
    """Class to represent and manage the blockchain"""

    def __init__(self):
        """Create a chain containing a genesis block"""
        self.blockchain = [self._createGenesisBlock()]
        self.pendingTransactions = []
        self.difficulty = 2
        self.miningReward = 100

    def __str__(self):
        """Return blockchain in a human readable (json) string"""
        jData = []

        for b in self.blockchain:
            block = {
                "Timestamp": b.timestamp,
                "Hash": b.hash,
                "Previous hash": b.previousHash
            }

            jData.append(block)

        return json.dumps(jData, indent=4)

    def _createGenesisBlock(self):
        """Create genesis/ first block on chain"""

        self.genBlock = Block(str(datetime.datetime.now()), [], None)

        logger.info("Genisis block created")

        return self.genBlock

    def getLatestBlock(self):
        """Return the latest block on the chain"""
        return self.blockchain[len(self.blockchain) - 1]

    def minePendingTransactions(self, miningRewardAddr):
        """Mine a block with the list of pending transactions"""
        # Note this block will include timestamp at start of mining
        # Not block creation
        newBlock = Block(str(datetime.datetime.now()),
                         self.pendingTransactions)
        newBlock.mineBlock(self.difficulty)

        self.blockchain.append(newBlock)

        logger.info("Block added to blockchain")

        # Send mining reward and empty pending transaction list
        self.pendingTransactions = [Transaction(
            None, miningRewardAddr, self.miningReward)]

        logger.debug(f"Pending TX cleared")
        logger.debug(f"Mining reward added for {miningRewardAddr}")

    def createTransaction(self, transaction):
        """Add a transaction to the pending transaction list"""
        self.pendingTransactions.append(transaction)
        logger.debug(f"Trasaction created {str(transaction)}")

    def getBalance(self, addr):
        """Calculates and returns balance of given address"""
        balance = 0

        logger.debug(f"Calculating balance for {addr}")

        # Loop all transactions in entire chain

        for block in self.blockchain:
            for transaction in block.transactions:
                if(transaction.fromAddr == addr):
                    # addr has sent money so deduct
                    balance -= transaction.ammount

                    logger.debug(
                        f"{transaction.ammount} sent to {transaction.toAddr}")
                    logger.debug(f"Balance {balance}")
                if(transaction.toAddr == addr):
                    # addr has recieved money so increase
                    balance += transaction.ammount

                    logger.debug(
                        f"{transaction.ammount} recieved from {transaction.fromAddr}")
                    logger.debug(f"Balance {balance}")

        return balance

    def isValid(self):
        """Function to check all block in the chain for validity"""

        for i in range(1, len(self.blockchain)):
            currBlock = self.blockchain[i]
            prevBlock = self.blockchain[i-1]

            # Check block hashs match recorded values
            if(currBlock.hash != currBlock.calculateHash()):
                logger.warning(
                    f"Block {currBlock.index} hash's do not match!")
                logger.warning(f"Recorded hash: {currBlock.hash}")
                logger.warning(f"Actual hash: {currBlock.calculateHash()}")

                return False

            if(prevBlock.hash != prevBlock.calculateHash()):
                logger.warning(
                    f"Previous block {prevBlock.index} hash's do not match!")
                logger.warning(f"Recorded hash: {prevBlock.hash}")
                logger.warning(f"Actual hash: {prevBlock.calculateHash()}")
                return False

        return True

    def printPendingTransactions(self):

        for transaction in self.pendingTransactions:
            print(str(transaction))
