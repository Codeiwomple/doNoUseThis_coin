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
        self.chain = [self._createGenesisBlock()]

    def _createGenesisBlock(self):
        """Create genesis/ first block on chain"""

        self.genBlock = Block(0, "01/01/2017", "Genesis block", "0")

        logger.info("Genisis block created")
        logger.info("An info message")

        return self.genBlock

    def getLatestBlock(self):
        """Return the latest block on the chain"""
        return self.chain[len(self.chain) - 1]

    def addBlock(self, newBlock):
        """Push a new block to the blockchain"""
        newBlock.previousHash = self.getLatestBlock().hash
        newBlock.hash = newBlock.calculateHash()

        # Debug output
        logger.info("New block created")
        logger.debug(newBlock.hash)
        logger.debug(str(newBlock))

        self.chain.append(newBlock)

    def __str__(self):
        """Return blockchain in a human readable (json) string"""
        jData = []

        for b in self.chain:
            block = {
                "Index": b.index,
                "Hash": b.hash,
                "Previous hash": b.previousHash
            }

            jData.append(block)

        return json.dumps(jData, indent=4)
