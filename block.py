import hashlib
import json
import logging
import time

# Set logger to name of class
logger = logging.getLogger('Block')


class Block:
    """Class to represent a single block on the chain"""

    def __init__(self, timestamp, transactions, previousHash=''):
        """Initialise instance of block"""
        self.timestamp = timestamp
        self.transactions = transactions
        self.previousHash = previousHash
        self.nonce = 0

        self.hash = self.calculateHash()

    def __str__(self):
        """Return a block in a human readable string, in this case JSON"""
        block = {
            "Timestamp": self.timestamp,
            "Hash": self.hash,
            "Previous hash": self.previousHash,
            "Nonce": self.nonce,
            "Transactions": [str(tx) for tx in self.transactions]
        }

        return json.dumps(block, indent=4)

    def calculateHash(self):
        """Create a hash of current block instance"""

        hashData = f"{self.timestamp}{self.transactions}{self.previousHash}{self.nonce}"

        hashGen = hashlib.sha256()
        hashGen.update(hashData.encode())

        return hashGen.hexdigest()

    def mineBlock(self, difficulty):
        """Function to mine a block using proof of work"""
        logger.debug(f"Mining... difficulty {difficulty}")

        while(self.hash[0:difficulty] != '0' * difficulty):
            self.nonce += 1
            self.hash = self.calculateHash()
            # print(self.hash, self.nonce)
            # time.sleep(0.5)

        logger.info(f"New block mined {self.timestamp} {self.hash}")
        logger.debug(str(self))

    def transactionsAreValid(self):
        """Check all transactions in block and validate"""

        for tx in self.transactions:
            if not tx.isValid():
                return False
        return True
