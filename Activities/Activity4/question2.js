function findMaxConsecutiveOnes(nums) {
    /* your solution goes here */
  var count = 0; // cout the numbers of consecutive 1s
  var max = 0; // keep max score of consecutives 1s
  
  for(j=0; j<nums.length; j++){ // go through all the array of nums
    
    if(nums[j]==1){ // check if it is a one
      count += 1; // increment count
    }else{ // if not a 1 restart count
      count = 0; 
    }

    if(count>max){ // check if count is bigger than max valued store
        max = count; // store count in max
    }
    
  }
  
  return max; // return max
  
}

module.exports = {findMaxConsecutiveOnes}