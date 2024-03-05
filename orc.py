import random 

class Orc:
  def __init__(self):
    self.degat = random.choice(range(3, 5))
    self.loot = random.choice(range(2, 2.5))