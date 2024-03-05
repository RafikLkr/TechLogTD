import abc

class Team(abc.ABC):
  def __init__(self):
    self._members = []
    
  @abc.abstractmethod  
  def __len__(self):
    return len(self._members)
  
  @abc.abstractmethod
  def __getitem__(self, i):
    return self._members[i]
  
  