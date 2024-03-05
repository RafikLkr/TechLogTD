class Game : 
    def __init__(self):
        self.nb_warriors = 0
        self.nb_hunters = 0
        self.nb_wizards = 0
        self.player_name = ""
        
    def config(self):
        self.player_name = input("Entrez votre nom de joueur : ")