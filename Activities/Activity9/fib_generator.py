import sys


def fibonacci(n):

  num1 = 0
  num2 = 1

  for x in range(n + 1):
    yield num1
    num1, num2 = num2, num1 + num2


def main():

  if len(sys.argv) != 2:
    print('Error! You did not enter a value.')

  else:

    input = int(sys.argv[1])
    print(list(fibonacci(input)))


if __name__ == '__main__':
  main()
