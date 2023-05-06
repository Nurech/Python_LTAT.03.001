class Candidate:
    def __init__(self, name: str):
        self.name = name
        self.votes = 0

    def add_vote(self):
        self.votes += 1


class Voter:
    def __init__(self, name: str):
        self.name = name

    def vote(self, candidate: Candidate):
        candidate.add_vote()


def main():
    kaja = Candidate("Kaja")
    juri = Candidate("Jüri")
    martin = Candidate("Martin")

    jaanus = Voter("Jaanus")
    urve = Voter("Urve")
    ain = Voter("Ain")
    maarja = Voter("Maarja")
    siim = Voter("Siim")

    jaanus.vote(kaja)
    urve.vote(juri)
    ain.vote(martin)
    maarja.vote(kaja)
    siim.vote(kaja)
    siim.vote(martin)
    maarja.vote(juri)
    jaanus.vote(juri)
    ain.vote(kaja)

    # Output results
    candidates = [kaja, juri, martin]
    winner = max(candidates, key=lambda c: c.votes)
    # print(candidates)

    for candidate in candidates:
        print(f"{candidate.name}: {candidate.votes} votes")

    print(f"Winner: {winner.name}")

main()
