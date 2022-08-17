from block import Block


class Blockchain:
    """Class to represent and manage the blockchain"""

    def __init__(self):
        """Create a chain containing a genesis block"""
        self.chain = [self._createGenesisBlock()]

    def _createGenesisBlock(self):
        """Create genesis/ first block on chain"""

        self.genBlock = Block(0, "01/01/2017", "Genesis block", "0")
        print("Genisis block created")

        return self.genBlock

    def getLatestBlock(self):
        """Return the latest block on the chain"""
        return self.chain[len(self.chain) - 1]

    def addBlock(self, newBlock):
        """Push a new block to the blockchain"""
        newBlock.previousHash = self.getLatestBlock().hash
        newBlock.hash = newBlock.calculateHash()

        print(
            f"New block ({newBlock.data}) with hash: {newBlock.hash} created")

        self.chain.append(newBlock)
