import json
import logging
import difflib

from setup_logger import logger
from block import Block

# Set logger to name of class
logger = logging.getLogger('Blockchain')


class Blockchain:
    """Class to represent and manage the blockchain"""

    def __init__(self):
        """Create a chain containing a genesis block"""
        self.blockchain = [self._createGenesisBlock()]
        self.difficulty = 4

    def _createGenesisBlock(self):
        """Create genesis/ first block on chain"""

        self.genBlock = Block(0, "01/01/2017", "Genesis block", "0")

        logger.info("Genisis block created")

        return self.genBlock

    def getLatestBlock(self):
        """Return the latest block on the chain"""
        return self.blockchain[len(self.blockchain) - 1]

    def addBlock(self, newBlock):
        """Mine new block and push to the blockchain"""
        print("Call mine")
        newBlock.previousHash = self.getLatestBlock().hash
        newBlock.mineBlock(self.difficulty)

        # Logging
        logger.info(f"New block created: {newBlock.index} {newBlock.hash}")
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
                logger.warning(
                    f"currBlock {currBlock.index} hash's do not match!")
                logger.warning(f"Recorded hash: {currBlock.hash}")
                logger.warning(f"Actual hash: {currBlock.calculateHash()}")

                return False

            if(prevBlock.hash != prevBlock.calculateHash()):
                logger.warning(
                    f"prevBlock {prevBlock.index} hash's do not match!")
                logger.warning(f"Recorded hash: {prevBlock.hash}")
                logger.warning(f"Actual hash: {prevBlock.calculateHash()}")
                return False

        return True
