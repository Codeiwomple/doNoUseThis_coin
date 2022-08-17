import json
import logging

from setup_logger import logger
from block import Block

# Set logger to name of class
logger = logging.getLogger('Blockchain')


class Blockchain:
    """Class to represent and manage the blockchain"""

    def __init__(self):
        """Create a chain containing a genesis block"""
        self.blockchain = [self._createGenesisBlock()]

    def _createGenesisBlock(self):
        """Create genesis/ first block on chain"""

        self.genBlock = Block(0, "01/01/2017", "Genesis block", "0")

        logger.info("Genisis block created")

        return self.genBlock

    def getLatestBlock(self):
        """Return the latest block on the chain"""
        return self.blockchain[len(self.blockchain) - 1]

    def addBlock(self, newBlock):
        """Push a new block to the blockchain"""
        newBlock.previousHash = self.getLatestBlock().hash
        newBlock.hash = newBlock.calculateHash()

        # Logging
        logger.info(f"New block created: {newBlock.hash}")
        logger.debug(str(newBlock))

        self.blockchain.append(newBlock)

    def __str__(self):
        """Return blockchain in a human readable (json) string"""
        jData = []

        for b in self.blockchain:
            block = {
                "Index": b.index,
                "Hash": b.hash,
                "Previous hash": b.previousHash
            }

            jData.append(block)

        return json.dumps(jData, indent=4)

    def isValid(self):
        """Function to check all block in the chain for validity"""

        for i in range(1, len(self.blockchain)):
            currBlock = self.blockchain[i]
            prevBlock = self.blockchain[i-1]

            # Check block hashs matche recorded values
            if(currBlock.hash != currBlock.calculateHash()):
                return False
            if(prevBlock.hash != prevBlock.calculateHash()):
                return False

        return True
