from ScopeMyError import *

def pop():
    try:
      raise ScopeMyError("Bad hostname")

    except ScopeMyError as e:
      print(e.abc())

pop()