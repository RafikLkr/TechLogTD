from team import Team

class Enemy(Team):
  def __init__(self, unit, damage, loot):
    super().__init__()
    self.__unit = unit
    self.__damage = damage
    self.__loot = loot
    
  def get_name(self):
    return self.__unit
    
  def get_damage(self):
    return self.__damage
  
  def get_loot(self):
    return self.__loot
  
  def get_members_type(self):
    types_of_members = [type(member) for member in self._members]
    return types_of_members