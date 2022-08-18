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
        self.transactions = transactions  # List of json transactions
        self.previousHash = previousHash
        self.nonce = 0

        self.hash = self.calculateHash()

    def calculateHash(self):
        """Create a hash of current block instance"""

        hashData = f"{self.timestamp}{json.dumps(self.transactions)}{self.previousHash}{self.nonce}"

        hashGen = hashlib.sha256()
        hashGen.update(hashData.encode())

        return hashGen.hexdigest()

    def mineBlock(self, difficulty):
        """Function to mine a block using proof of work"""
        logger.debug(f"Mining difficulty {difficulty}")

        while(self.hash[0:difficulty] != '0' * difficulty):
            self.nonce += 1
            self.hash = self.calculateHash()
            # print(self.hash, self.nonce)
            # time.sleep(0.5)

        logger.info("New block mined")
        logger.debug(f"Nonce: {self.nonce}")

    def __str__(self):
        """Return a block in a human readable string, in this case JSON"""
        b = {
            "Timestamp": self.timestamp,
            "Hash": self.hash,
            "Previous hash": self.previousHash,
            "Nonce": self.nonce,
            "Transactions": self.transactions
        }

        return json.dumps(b, indent=4)
