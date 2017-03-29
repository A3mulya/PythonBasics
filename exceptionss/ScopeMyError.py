class ScopeMyError(Exception):
   args=0
   def __init__(self, arg):
      self.args = arg

   def abc(self):
     return self.args