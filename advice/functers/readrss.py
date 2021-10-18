import feedparser 
import datetime 
import functools 
from advice.errors import * 


def call(func):
    @functools.wraps(func)
    def timer_wrapper(*args, **kwargs):
      function_called = True
      if function_called:
        mins = 1 
        end = datetime.datetime.utcnow() + datetime.timedelta(seconds = mins*5) 
        while True:
          difference = end - datetime.datetime.now()
          count_hours, rem = divmod(difference.seconds, 3600)
          count_minutes, count_seconds = divmod(rem, 60)
          if difference.days == 0 and count_hours == 0 and count_minutes == 0 and count_seconds == 0:
            return func(*args, **kwargs)

    function_called = False
    return timer_wrapper


class Parser:
  def __init__(self):
    self.base_Url = feedparser.parse('https://api.adviceslip.com/daily_adviceslip.rss')
    self.entry = self.base_Url.entries
  
  # for i in range(2):
  @call
  def parsersfact(self):

      if self.entry:
          l = self.entry[0]
          values = l.values()
          list_vals = list(values)

          a_value = list_vals[0]

          print(a_value)



  def parsefacts(self, loop = 'off'):
    '''
    Loop: bool = off or on, you can turn this on and it will loop the fact every 24 hours, but if off it will only call once.
    '''
    self.loop = loop
    if self.loop.lower() == 'on':
      while True:
        self.parsersfact()
    elif self.loop.lower() == 'off':
      return self.parsersfact()
    else:
      raise Stringerror
    


t = Parser()

t.parsefacts()

