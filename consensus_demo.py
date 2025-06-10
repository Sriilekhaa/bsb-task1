#Consensus Mechanism Simulation
import random

# Simulate PoW
pow_validators = [{"name": "Miner1", "power": random.randint(100, 1000)} for _ in range(3)]
pow_winner = max(pow_validators, key=lambda x: x['power'])
print(f"[PoW] {pow_winner['name']} wins with power {pow_winner['power']}")

# Simulate PoS
pos_validators = [{"name": "Staker1", "stake": random.randint(100, 1000)} for _ in range(3)]
pos_winner = max(pos_validators, key=lambda x: x['stake'])
print(f"[PoS] {pos_winner['name']} wins with stake {pos_winner['stake']}")

# Simulate DPoS
voters = ["Alice", "Bob", "Carol"]
delegates = {"Delegate1": 0, "Delegate2": 0, "Delegate3": 0}
for _ in voters:
    vote = random.choice(list(delegates.keys()))
    delegates[vote] += 1
dpos_winner = max(delegates, key=delegates.get)
print(f"[DPoS] {dpos_winner} wins with {delegates[dpos_winner]} votes")
