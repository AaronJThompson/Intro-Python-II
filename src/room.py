# Implement a class to hold room information. This should have name and
# description attributes.
import textwrap

class Room:
  def __init__(self, name, description):
    self.name = name
    self.description = description
    self.n_to = None
    self.e_to = None
    self.s_to = None
    self.w_to = None

  def __str__(self):
    return f"{self.name}\n{self.description}"

  def print(self):
    text = self.__str__()
    for line in textwrap.wrap(text, width=50):
      print(line.center(80))