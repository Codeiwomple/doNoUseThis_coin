import hashlib
import json
import logging
import time

# Set logger to name of class
logger = logging.getLogger('Block')


class Block:
    """Class to represent a single block on the chain"""

    def __init__(self, index, timestamp, data, previousHash=''):
        """Initialise instance of block"""
        self.index = index
        self.timestamp = timestamp
        self.data = data  # List of json transactions
        self.previousHash = previousHash
        self.nonce = 0

        self.hash = self.calculateHash()

    def calculateHash(self):
        """Create a hash of current block instance"""
        data = f"{self.index} {self.previousHash} {self.timestamp} {json.dumps(self.data)} {self.nonce}"

        hashGen = hashlib.sha256()
        hashGen.update(data.encode())

        return hashGen.hexdigest()

    def mineBlock(self, difficulty):
        """Function to mine a block using proof of work"""
        while(self.hash[0:difficulty] != '0' * difficulty):
            self.nonce += 1
            self.hash = self.calculateHash()
            # print(self.hash)
            # time.sleep(0.5)

        logger.info("New block mined")
        logger.debug(f"Nonce: {self.nonce}")

    def __str__(self):
        """Return a block in a human readable string, in this case JSON"""
        b = {
            "Index": self.index,
            "Timestamp": self.timestamp,
            "Previous hash": self.previousHash,
            "Data": self.data
        }

        return json.dumps(b, indent=4)
