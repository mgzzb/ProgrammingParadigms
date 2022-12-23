const assert = require('assert');
const question2 = require('./question2')


describe('findMaxConsecutiveOnes(nums)', function() {
  describe('Test cases', function() {
    it('Will return 4 with following input [0,1,1,1,1,0,1,1,0,0,0,1,1,0]', function() {
      assert.equal(question2.findMaxConsecutiveOnes([0,1,1,1,1,0,1,1,0,0,0,1,1,0]), 4);
    });
    
    it('Will return 10 with following input [1,1,1,1,1,1,1,1,1,1,0]', function() {
      assert.equal(question2.findMaxConsecutiveOnes([1,1,1,1,1,1,1,1,1,1,0]), 10);
    });
    
    it('Will return 0 with following input [0]', function() {
      assert.equal(question2.findMaxConsecutiveOnes([0]), 0);
    });
    
  });
});