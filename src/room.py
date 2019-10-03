# Implement a class to hold room information. This should have name and
# description attributes.
import textwrap

class Room:
  def __init__(self, name, description, items = []):
    self.name = name
    self.description = description
    self.items = items
    self.n_to = None
    self.e_to = None
    self.s_to = None
    self.w_to = None

  def add_items(self, items):
    self.items.extend(items)
    return self.items
  
  def add_item(self, item):
    self.items.append(item)
    return self.items

  def remove_item(self, name):
    item = None
    item_index = None
    for idx, i in enumerate(self.items):
      if i.name.lower() == name:
        item = i
        item_index = idx
        break
    if item:
      return self.items.pop(item_index)
    else:
      return False

  def __item_string__(self):
    return "\n".join(str(item) for item in self.items)

  def __str__(self):
    return f"\n{self.name}\n{self.description}\nItems\n{self.__item_string__()}"

  def __center_wrap__(self, text, cwidth=80, **kw):
    lines = textwrap.wrap(text, **kw)
    return "\n".join(line.center(cwidth) for line in lines)
  def print(self):
    lines = self.__str__().splitlines()
    for line in lines:
      print(self.__center_wrap__(line, cwidth=80, width=50))