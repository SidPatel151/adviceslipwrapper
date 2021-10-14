import warnings


  
class Ratelimit(Exception):
  pass

class keypageError(Exception):
  pass

class NotRecognizable(Exception):
  def __init__(self, error):
    self.error = error
  def __repr__(self):
    return self.error


