import hashlib
import time
from typing import Dict, Tuple, List

# Block keeps block headers
class Block(object):
    def __init__(self,data:bytes,prevBlockHash:bytes):
        self.Timestamp = int(time.time())
        assert isinstance(data,bytes)
        self.Data = bytes(data)
        self.PrevBlockHash = prevBlockHash
        self.Nonce = 0
        self.Hash = b''

# NewGenesisBlock creates and returns genesis Block
    def NewGenesisBlock():
        return Block(b"Genesis Block", b'')

