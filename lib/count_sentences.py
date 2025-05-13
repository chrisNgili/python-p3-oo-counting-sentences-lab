#!/usr/bin/env python3
import re
class MyString:
  def __init__( self, value=""):
    self.value = value

  @property
  def value(self):
    return self._value 

  @value.setter
  def value(self, new_value):
    if type(new_value) != str:
      print("The value must be a string.")

    else:
      self._value = new_value    
  def is_sentence(self):
    if self.value[-1] != ".":
      return False
    else:
      return True

  def is_question(self):
    if self.value[-1] != "?":
      return False
    else:
      return True    

  def is_exclamation(self):
    if self.value[-1] != "!":
      return False
    else:
      return True    
    
  def count_sentences(self):
      return len([s for s in re.split(r'[.!?]', self._value) if s.strip()])
  pass
print(MyString("Hello.").is_sentence())