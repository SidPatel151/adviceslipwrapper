import requests
from functers.url import * 
from functers.search import * 


class AdviceslipC(Url, Search):

  def __init__(self, session: requests.Session() = None):
    self.session = session or requests.Session()

    