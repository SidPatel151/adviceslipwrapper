import feedparser 
import datetime 
from .constants import * 
import functools 


def call(func):
    @functools.wraps(func)
    def timer_wrapper(*args, **kwargs):
      function_called = True
      if function_called:
        print('e')
        mins = 1 
        end = datetime.datetime.utcnow() + datetime.timedelta(seconds = mins*5) 
        while True:
          difference = end - datetime.datetime.now()
          count_hours, rem = divmod(difference.seconds, 3600)
          count_minutes, count_seconds = divmod(rem, 60)
          if difference.days == 0 and count_hours == 0 and count_minutes == 0 and count_seconds == 0:
            return func(*args, **kwargs)

    function_called = False
    print('(((')
    return timer_wrapper


class Parser:
  def __init__(self):
    self.base_Url = feedparser.parse('https://api.adviceslip.com/daily_adviceslip.rss')
    self.entry = self.base_Url.entries
  
  # for i in range(2):
  @call
  def parsersfact(self, loop = 'on'):
      self.loop = loop
      print(self.loop)

      if self.entry:
          l = self.entry[0]
          values = l.values()
          list_vals = list(values)

          a_value = list_vals[0]

          print(a_value)



  def loop(self):
    loops = self.loop
    print(loops)
    if self.loop == 'on':
      print('ssss')
      while True:
        print('dnib')
        self.parsersfact()
    else:
      print('sus')
      return self.parsersfact()
    


t = Parser()

t.loop()

