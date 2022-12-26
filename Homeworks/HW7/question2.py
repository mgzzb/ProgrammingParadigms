import sys


def move_robot(steps):
  #define variables
  i = 0
  max = int(steps)
  grid = [0, 0]
  position = 'north'

  # while i is less or equal than max enter the loop
  while i <= max:

    # set conditions to move robot
    if i == 0:
      position = 'north'

    elif grid[0] == 0 and grid[1] == 0:
      grid[1] = i
      position = 'east'

    elif grid[0] == 0 and grid[1] == 1:
      grid[0] = i
      position = 'south'

    elif position == 'south':
      grid[1] = grid[1] - i
      position = 'west'

    elif position == 'west':
      grid[0] = grid[0] - i
      position = 'north'

    elif position == 'north':
      grid[1] = grid[1] + i
      position = 'east'

    elif position == 'east':
      grid[0] = grid[0] + i
      position = 'south'

    #incremeant count and yield grid points
    i += 1
    yield tuple(grid)


def main():
  #store first argument in n
  n = int(sys.argv[1])

  # go through move_robot
  for v in move_robot(n):
    print(v)


if __name__ == '__main__':
  main()
