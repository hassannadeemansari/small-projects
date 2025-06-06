#🟢Q3 – Simple Voting System
# Create a class Candidate with attributes name and votes.
# Create a method add_vote() to increase votes.
# Allow 3 candidates and find the one with the highest votes.

class Candidate:
    def __init__(self, name):
        self.name = name
        self.votes = 0

    def add_votes(self):
        self.votes += 1


candidates = [
    Candidate("Hassan"),
    Candidate("Nadeem"),
    Candidate("Ahmed")
]

candidates[0].add_votes()
candidates[0].add_votes()
candidates[0].add_votes()
candidates[0].add_votes()
candidates[1].add_votes()
candidates[1].add_votes()
candidates[0].add_votes()
candidates[2].add_votes()
candidates[2].add_votes()

for candidate in candidates:
    print(candidates)

def find_winner(candidates):
    winner = max(candidates, key=lambda c: c.votes)
    return winner

winner = find_winner(candidates)
print(f"\n🏆 Winner is: {winner.name} with {winner.votes} votes")