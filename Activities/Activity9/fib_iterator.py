import sys


def fibonacci(n):

  # initialize num1, num2
  num1 = 0
  num2 = 1

  if n == 0:
    print(num1)  # if n == 0, then just print 0
  elif n < 0:  # if n is negative ask to input a positive value
    print('ERROR!\nYou need to enter a positive number')

  # else create fibonacci number
  else:
    print(num1)  # print first two values
    print(num2)
    # for loop where we calculate and print fibonacci number
    for x in range(1, n):
      temp = num1 + num2
      num1 = num2
      num2 = temp
      print(temp)


def main():
  if len(sys.argv) != 2:
    print('Error! You did not enter a value')
  else:
    input = int(sys.argv[1])
    fibonacci(input)


if __name__ == '__main__':
  main()
