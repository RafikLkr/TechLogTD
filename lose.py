class Lose:
    def __init__(self, nb_warriors, nb_hunters, nb_wizards):
        self.nb_warriors = 0
        self.nb_hunters = 0
        self.nb_wizards = 0

    def __repr__(self):
        return f"Loses(nb_warriors={self.nb_warriors}, nb_hunters={self.nb_hunters}, nb_wizards={self.nb_wizards})"
