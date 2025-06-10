# Nonce Mining Simulation 

import time

class BlockWithMining(Block):
    def mine_block(self, difficulty):
        prefix = '0' * difficulty
        start = time.time()
        while not self.hash.startswith(prefix):
            self.nonce += 1
            self.hash = self.calculate_hash()
        end = time.time()
        print(f"Block mined with nonce: {self.nonce}")
        print(f"Time taken: {end - start:.4f} seconds")
        print(f"Final Hash: {self.hash}")

# Example usage
block = BlockWithMining(1, time.time(), "Mining Test", "0")
block.mine_block(4)
