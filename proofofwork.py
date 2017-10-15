import hashlib
from block import Block

maxNonce = 0xffffffffffffffff
targetBits = 24

# ProofOfWork represents a proof-of-work
class ProofOfWork(object):
	def __init__(self):
		self.block = None
		self.target = target = 1<<(256-targetBits)

	def setBlock(self,block:Block):
		self.block = block

	def prepareData(self,nonce:int) -> bytes:
		data = [self.block.PrevBlockHash,
				self.block.Data,
				self.block.Timestamp.to_bytes(8,'little'),
				targetBits.to_bytes(8,'little'),
				nonce.to_bytes(8,'little'),
			]
		data = b''.join(data)
		return data

	# Run performs a proof-of-work
	def Run(self) -> (int,bytes):
		print("Mining the block containing \"%s\"\n"%(self.block.Data,))
		for nonce in range(maxNonce):
			data = self.prepareData(nonce)
			hash = hashlib.sha256(data).digest()
			hashInt = int.from_bytes(hash,'little')
			if hashInt<self.target:
				self.block.Hash = hash
				self.block.Nonce = nonce
				return (nonce,hash)
			else:
				nonce+=1
			if nonce % 1000 == 0:
				print('\r',nonce,end='')

	# Validate validates block's PoW
	def Validate(self) -> bool:
		data = self.prepareData(self.block.Nonce)
		hash = hashlib.sha256(data).digest()
		hashInt = int.from_bytes(hash,'little')
		if hashInt<self.target:
			return True
		return False

if __name__ == '__main__':
	import hashlib
	maxNonce = 0xffffffffffffffff
	targetBits = 24
	target = 1<<(256-targetBits)
	for nonce in range(maxNonce):
		data =int.to_bytes(nonce,16,'little')
		hash = hashlib.sha256(data).digest()
		hashInt = int.from_bytes(hash,'little')
		if hashInt<target:
			break
		else:
			nonce+=1
		if nonce % 1000 == 0:
			print('\r',nonce,end='')
	print(nonce)

