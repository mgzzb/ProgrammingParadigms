function reverseNum(num){
  let numReverse = []; // store reverse numbers
  let k = 0; //count of where we are storing values of numReverse 
  for(i=(num.length-1); i>=0; i--){ // loop
    numReverse[k] = num[i]; // store in reverse order
    k++; // incremeant count of storing 
  }
  
  return numReverse.join('');
}

function reversedSum(num1, num2) {
  /* your solution goes here */
  num1 = reverseNum( num1.toString() ); // num 1 reversed
  num2 = reverseNum( num2.toString() ); // num2 reversed

  let sum = parseInt(num1, 10) + parseInt(num2, 10); // add two reversed values

  sum = reverseNum( sum.toString() ); //reverse sum

  return parseInt(sum, 10); //return value without leading zeros
}