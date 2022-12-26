changeEnough = (changeInPocket, amount) -> 
	# Your Function implementation here

  if (changeInPocket[0] * 0.25 + changeInPocket[1] * 0.10 + changeInPocket[2] * 0.05 + changeInPocket[3] * 0.01) >= amount
    return true

  return false


# Keep the line below so we can test your code!
module.exports = { changeEnough }

# Testing 
#console.log(changeEnough([2, 100, 0, 0], 14.11));
#console.log(changeEnough([0, 0, 20, 5], 0.75));
#console.log(changeEnough([30, 40, 20, 5], 12.55));
#console.log(changeEnough([10, 0, 0, 50], 3.85));
#console.log(changeEnough([1, 0, 5, 219], 19.99));