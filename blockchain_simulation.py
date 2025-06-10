#Block Simulation in Code 
import hashlib, time

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        value = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(value.encode()).hexdigest()

# Create genesis block
genesis_block = Block(0, time.time(), "Genesis Block", "0")

# Create next blocks
block1 = Block(1, time.time(), "Transaction 1", genesis_block.hash)
block2 = Block(2, time.time(), "Transaction 2", block1.hash)

# Print blocks
for block in [genesis_block, block1, block2]:
    print(f"Block {block.index} Hash: {block.hash}")

# Tampering demo
block1.data = "Hacked Transaction"
block1.hash = block1.calculate_hash()
print(f"\nAfter tampering Block 1:\nBlock 1 New Hash: {block1.hash}")
print(f"Block 2 Previous Hash Still: {block2.previous_hash}")
