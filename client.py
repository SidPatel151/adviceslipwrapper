import requests
from advice.functers.url import Url
from advice.constants import BASE_URL
from advice.functers.search import Search
from advice.functers.slip_id import Slip_id
from advice.functers.readrss import Parser


class Client(Url,Search, Slip_id, Parser):

  Base = BASE_URL
#   '''
#   Where all the function will go, you will have to use this..
#   '''

  def __init__(self, session: requests.Session() = None):
    self.session = session or requests.Session()

    