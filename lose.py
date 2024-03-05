class Lose:
    def __init__(self, nb_warriors, nb_hunters, nb_wizards):
        self.nb_warriors = nb_warriors
        self.nb_hunters = nb_hunters
        self.nb_wizards = nb_wizards

    def __repr__(self):
        return f"Loses(nb_warriors={self.nb_warriors}, nb_hunters={self.nb_hunters}, nb_wizards={self.nb_wizards})"
