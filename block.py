import hashlib
import json


class Block:
    """Class to represent a single block on the chain"""

    def __init__(self, index, timestamp, data, previousHash=''):
        """Initialise instance of block"""
        self.index = index
        self.timestamp = timestamp
        self.data = data  # List of json transactions
        self.previousHash = previousHash
        self.hash = self.calculateHash()

    def calculateHash(self):
        """Create a hash of current block instance"""
        data = f"{self.index} {self.previousHash} {self.timestamp} {json.dumps(self.data)}"

        hashGen = hashlib.sha256()
        hashGen.update(data.encode())

        return hashGen.hexdigest()

    def __str__(self):
        """Return a block in a human readable string, in this case JSON"""
        b = {
            "Index": self.index,
            "Timestamp": self.timestamp,
            "Previous hash": self.previousHash,
            "Data": self.data
        }

        return json.dumps(b, indent=4)
