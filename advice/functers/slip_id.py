from requests import Session
from advice.errors import * 
from .base import *
from advice.constants import BASE_URL


class Slip_id(Base):
  def get_id(self, slip_id: int=1):
    '''
    slip_id: int , set to 1 because slip_id start from 1, you can input any number from 1-224. If you do put 0 for an arg, it will default to 1'''
    Sessione = Session()
    # get = self.gete(BASE_URL)
    q = {
      slip_id: slip_id
    }
    self.slip_id = slip_id if slip_id else 1 
    print(self.slip_id)
    if self.slip_id < 1 or self.slip_id > 224:
      print('e')
      raise NotRecognizable("Slip_id doesn\'t exist")
    s = []
    # res = Sessione.get(f"{BASE_URL}/{self.slip_id}").json()
    res = Sessione.get(f"https://api.adviceslip.com/advice/{slip_id}", params=q)
    for i in res:
      s.append(i)

    for v in s:
      v = str(v).replace('b', ' ').replace("'", '')
      return print(v)
    
# t = Slip_id()

# t.get_id(0)