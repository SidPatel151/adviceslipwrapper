import requests

class Base:
  session = requests.Session
  base_url: str = 'https://api.adviceslip.com/advice/'


class Caller:
    def callback(self, funct, callback,  url) -> str: # I was going to plan on using this, but it wasn't necessary, maybe a better api wrapper could use this 
      with requests.Session():
        res = url.json()
        return [funct(**data) for data in res]

