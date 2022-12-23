/* 

Q1: Write a generator function using closures that return the next number in the fibonacci sequence(starting from n = 0, i.e., it returns zero when it is first invoked).Save this function in a file named as question1.js.

*/

var k = 2;
var num1 = 0;
var num2 = 1;

const fibonacci = n => {

    if (n == 0 || n == 1) {
        return n;
    }

    function fib(){
      k = num1 + num2;
      num1 = num2;
      num2 = k;
    }

  
    for ( k = 2; k <= n; k++) {
      fib();
    }
  
    return k;
}

console.log(fibonacci(0));
console.log(fibonacci(1));
console.log(fibonacci(5));
console.log(fibonacci(6));
console.log(fibonacci(10));