import random

class Hat:
  houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

  @classmethod
  def sort(cls, name):
    print(name, "is in", random.choice(cls.houses))


for i in range(4):
  Hat.sort("Harry")
  i += 1

