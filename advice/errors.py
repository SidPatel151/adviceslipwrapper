import warnings



class Ratelimit(Exception):
  '''
  Ratelimiting, will input later
  '''
  pass

class keypageError(Exception):
  '''
  Error to show when going to high for total_res'
  '''
  pass

class Stringerror(Exception):
  '''
  used for the loop string error
  '''
  pass

class NotRecognizable(Exception):
  def __init__(self, error):
    '''
    If slip_id is not recognizable
    '''

    self.error = error
  def __repr__(self):
    return self.error


