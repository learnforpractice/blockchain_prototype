import time
from block import Block

# Blockchain keeps a sequence of Blocks

class Blockchain:
    def __init__(self):
        self.blocks = [Block.NewGenesisBlock()]

    # AddBlock saves provided data as a block in the blockchain
    def AddBlock(self,data:bytes):
        prevBlock = self.blocks[len(self.blocks)-1]
        newBlock = Block(data, prevBlock.Hash)
        self.blocks.append(newBlock)
        return newBlock

    # NewBlockchain creates a new Blockchain with genesis Block
    def NewBlockchain(self):
        return Blockchain()

