function computeEnumeration(termPositions) {
  /* your solution goes here */

  let output = []; // array for output value
  
  for(i=0; i < termPositions.length; i++){ // go through array of termPositions
    
    if(termPositions[i] < 1){ // if number is less than one, return null
      
       output[i] = null; 
      
    }else{
      
      let n = 0; // keep count of the value we are currently checking
      let state = 0; // the state we are at
      let num_values = 0; // the number of values the diagonal has
      let num = 2; //numerator value
      let den = 2; //denomenator value
      
      while(termPositions[i]>n){
          n += 1; //start at position 1
         
          if(state == 0){ // check position one value
            if(n==termPositions[i]){ // if termPosition is one assign value        
              output[i] = num + "/" + den; // store num and den in output value
            }else{
              state = 1;    // move to next state
              num_values +=1; // increment number diagonal has
            } 
            
          }else if(state == 1){
            den += 2; // increment  denomenator by 2
            
            for(j = 0; j<num_values; j++){ // go through each value in the diagonal
              if(n==termPositions[i]){ // if termPosition is equal to n (current position) assign value
                output[i] = num + "/" + den; // store num and den in output value
              }
              num += 2; // increment numerator by two
              den -= 2; // decrease denomenator by two
              n += 1; // increment position by 1
              
            }
            
            if(n==termPositions[i]){// if termPosition is equal to n (current position) assign value
                output[i] = num + "/" + den; // store num and den in output value
            }
            
            num_values +=1; // increment number diagonal has
            state = 2; // move to next state
          }else if(state == 2){
            num += 2; // increment numerator by two
            for(j = 0; j<num_values; j++){ // go through each value in the diagonal
              if(n==termPositions[i]){// if termPosition is equal to n (current position) assign value
                output[i] = num + "/" + den; // store num and den in output value
              }
              num -= 2; // decrease numerator by two
              den += 2;// increment denomenator by two
              n += 1; // increment position by 1
            }
            
            if(n==termPositions[i]){// if termPosition is equal to n (current position) assign value
                output[i] = num + "/" + den; // store num and den in output value
            }
            
            num_values +=1; // increment number diagonal has
            
            state = 1; // move to next state
        }
      }   
    }
  }
  
  return output; // return output
}