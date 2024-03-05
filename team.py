import abc

class Team(abc.ABC):
  def __init__(self, members):
    self._members = []
    
  @abc.abstractmethod  
  def __len__(self):
    pass
  
  @abc.abstractmethod
  def __getitem__(self):
    pass
  
  