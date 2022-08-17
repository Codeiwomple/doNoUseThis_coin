import hashlib
import json


class Block:
    """Class to represent a single block on the chain"""

    def __init__(self, index, timestamp, data, previousHash=''):
        """Initialise instance of block"""
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previousHash = previousHash
        self.hash = self.calculateHash

    def calculateHash(self):
        """Create a hash of current block instance"""
        # data = f"{self.index} {self.previousHash} {self.timestamp} {json.dumps(self.data)}"
        data = f"{self.index} {self.previousHash} {self.timestamp} {self.data}"

        hashGen = hashlib.sha256()
        hashGen.update(data.encode())

        return hashGen.hexdigest()
