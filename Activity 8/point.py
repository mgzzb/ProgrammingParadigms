import math  #need math library for sqt


# create the class point
class Point:
  # create the constructor of x, y
  def __init__(self, x, y):
    self.x = x
    self.y = y

  # create method to print (x,y)
  def print(self):
    print(f"({self.x}, {self.y})")


#calculate the Euclidean distance with two points as parameters
def distance(p1, p2):
  first = (p2.x - p1.x) * (p2.x - p1.x)
  second = (p2.y - p1.y) * (p2.y - p1.y)
  return (math.sqrt(first + second))


# Initialize point
p1 = Point(3, 7)
p2 = Point(-1, -2)

# print points format (x, y)
p1.print()
p2.print()

#get the distance and print the distance
print(distance(p1, p2))
