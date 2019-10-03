
class Item:
  def __init__(self, name, description):
    self.name = name
    self.description = description

  def __str__(self):
    return f"\n{self.name}\n{self.description}\n "

  def on_take(self):
    print(f"You have picked up a {self.name}")

  def on_drop(self):
    print(f"You have dropped a {self.name}")