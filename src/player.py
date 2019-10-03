# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
  def __init__(self, name, current_room, inventory = []):
    self.current_room = current_room
    self.name = name
    self.inventory = inventory

  def __add_item__(self, item):
    self.inventory.append(item)
    item.on_take()
    return self.inventory

  def __remove_item__(self, idx):
    item = self.inventory.pop(idx)
    item.on_drop()
    return self.inventory

  def pickup_item(self, name):
    item = current_room.pop_item(name)
    if item:
      self.__add_item__(item)
      return item
    else:
      return False