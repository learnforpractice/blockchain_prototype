from blockchain import Blockchain
from proofofwork import ProofOfWork

if __name__ == '__main__':
    bc  = Blockchain()
    pow = ProofOfWork()

    print('add new block\n')
    bc.AddBlock(b"Send 1 BTC to Ivan")

    print('add new block\n')
    bc.AddBlock(b"Send 2 more BTC to Ivan")

    for block in bc.blocks:
        pow.setBlock(block)
        pow.Run()


    for block in bc.blocks:
        print("Prev. hash:", block.PrevBlockHash.hex())
        print("Data:", block.Data.hex())
        print("Hash:", block.Hash.hex())
        pow.setBlock(block)
        print("PoW: ", pow.Validate())
        print()
        

