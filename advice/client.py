import requests
from functers.url import * 
from functers.search import * 


class AdviceslipC(Url, Search):
  '''
  Where all the function will go, you will have to use this..
  '''

  def __init__(self, session: requests.Session() = None):
    self.session = session or requests.Session()

    