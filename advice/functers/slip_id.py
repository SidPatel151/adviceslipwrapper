from requests import Session
from advice.errors import * 
from .base import *
from advice.constants import BASE_URL
from .url import *
import json


class Slip_id(Base):
  def get_id(self, slip_id: int=1):
    Sessione = Session()
    # get = self.gete(BASE_URL)
    q = {
      slip_id: slip_id
    }
    self.slip_id = slip_id if slip_id else 1 
    s = []
    # res = Sessione.get(f"{BASE_URL}/{self.slip_id}").json()
    res = Sessione.get(f"https://api.adviceslip.com/advice/{slip_id}", params=q)
    for i in res:
      s.append(i)

    for v in s:
      v = str(v).replace('b', ' ').replace("'", '')
      print(v)
    
t = Slip_id()

t.get_id(5)