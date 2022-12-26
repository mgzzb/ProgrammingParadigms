import sys


class move_robot:

  def __init__(self, steps):
    self.i = 0
    self.max = int(steps)
    self.grid = [0, 0]
    self.position = 'north'

  def __next__(self):
    # check if it is less than max
    while self.i <= self.max:
      # check if it is first time moving
      if self.i == 0:
        self.i += 1
        return tuple(self.grid)

      elif self.grid[0] == 0 and self.grid[1] == 0:
        self.grid[1] = self.i
        self.position = 'east'

      elif self.grid[0] == 0 and self.grid[1] == 1:
        self.grid[0] = self.i
        self.position = 'south'

      # move robot depending on conditions
      elif self.position == 'south':
        self.grid[1] = self.grid[1] - self.i
        self.position = 'west'

      elif self.position == 'west':
        self.grid[0] = self.grid[0] - self.i
        self.position = 'north'

      elif self.position == 'north':
        self.grid[1] = self.grid[1] + self.i
        self.position = 'east'

      elif self.position == 'east':
        self.grid[0] = self.grid[0] + self.i
        self.position = 'south'

      # increament and return result of grid
      self.i += 1
      return tuple(self.grid)

    raise StopIteration()

  def __iter__(self):
    return self


def main():

  #store first argument in n
  n = int(sys.argv[1])

  #iterate through move_robot
  for v in move_robot(n):
    print(v)


if __name__ == '__main__':
  main()
