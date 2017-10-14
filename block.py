import hashlib
import time
from typing import Dict, Tuple, List

# Block keeps block headers
class Block(object):
    def __init__(self,data:bytes,prevBlockHash:bytes):
        self.Timestamp = int(time.time())
        self.Data = data
        self.PrevBlockHash = prevBlockHash
        self.SetHash()

# SetHash calculates and sets block hash
    def SetHash(self):
        timestamp = int.to_bytes(self.Timestamp,8,'little')
        headers = b''.join([self.PrevBlockHash,self.Data,timestamp])
        self.Hash = hashlib.sha256(headers).digest()

# NewGenesisBlock creates and returns genesis Block
    def NewGenesisBlock():
        return Block(b"Genesis Block", b'')

