## ... your code here 

fibonacci = (n) ->

  first = 0;
  second = 1;
  current = 0;
  count = 1;

  while (count <= n)
    first = second
    second = current
    current = first + second
    count = count + 1

  return current

# console.log fibonacci(5)
# console.log fibonacci(12)