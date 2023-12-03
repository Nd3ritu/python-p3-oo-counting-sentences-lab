#!/usr/bin/env python3

class MyString:
  def __init__(self,value = None):
    self._value = value

  def get_value(self):
    return self._value

  def set_value(self, value):
    if isinstance(value, str):
      self._value = value
    else:
      print("The value must be a string.")

  value = property(get_value, set_value)

  def is_sentence(self):
      if self._value is not None and self._value.endswith("."):
        return True
      else:
        return False
      
  def is_question(self):
    if self._value is not None and self._value.endswith("?"):
       return True
    else:
      return False
    
  def is_exclamation(self):
    if self._value is not None and self._value.endswith("!"):
      return True
    else:
      return False
    
  def count_sentences(self):
    val = self.value
    if val is None:
      return 0
    
    for i in ['!', '?']:
      val = val.replace(i , '.')

    sentences = [s for s in val.split('.') if s ]

    return len(sentences)
