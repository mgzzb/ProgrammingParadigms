function fibonacci(n) {

  let first = 0;
  let second = 1;
  let current = 0;
  let count = 1;

  while (count < n) {

    first = second;
    second = current;
    current = first + second;
    count = count + 1;

  }

  return current;

}
