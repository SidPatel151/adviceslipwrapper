import requests

class Base:
  session = requests.Session
  base_url: str = 'https://api.adviceslip.com/advice/'


class Caller:
    def callback(self, funct, callback,  url) -> str:
      with requests.Session():
        res = url.json()
        return [funct(**data) for data in res]

