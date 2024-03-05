from team import Team

class Enemy(Team):
  def __init__(self, unit):
    super().__init__()
    self.__unit = unit
    self.__damage = 0
    self.__loot = 0
    
  def get_name(self):
    return self.__unit
    
  def get_damage(self):
    damage = 0
    for member in self._members :
      damage = damage + member.degat
    return damage
  
  def get_loot(self):
    loot = 0
    for member in self._members :
      loot = loot + member.loot
    return loot
  
  def get_members_type(self):
    types_of_members = [type(member) for member in self._members]
    return types_of_members