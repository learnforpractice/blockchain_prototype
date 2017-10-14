from blockchain import Blockchain

if __name__ == '__main__':
    bc  = Blockchain()

    bc.AddBlock(b"Send 1 BTC to Ivan")
    bc.AddBlock(b"Send 2 more BTC to Ivan")

    for block in bc.blocks:
        print("Prev. hash:", block.PrevBlockHash.hex())
        print("Data:", block.Data.hex())
        print("Hash:", block.Hash.hex())
        print()