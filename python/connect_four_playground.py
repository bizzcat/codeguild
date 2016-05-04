class Board1:
  def __init__(self):
    self.rows = []

  def add(self, color, col):
    self.rows[self.get_bottom(col)] = color

class Board2:
  def __init__(self):
    self.d = {}

  def add(self, color, col):
    self.d[col] = color

b = Board2()
print(b.d)
b.add('r', 3)
print(b.d)
b.add('y', 4)
print(b.d)
