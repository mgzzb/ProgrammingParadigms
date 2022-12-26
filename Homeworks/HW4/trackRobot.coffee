trackRobot = (north=0, east=0, south=0, west=0) -> # variables=0 in order to give them each a value in case nothing is passed 

	# Your Function implementation here
    
  loc = [0,0] # the array we will return with result

  loc[0] = (east-west) # set coordinates x
  loc[1] = (north-south) # set coordinates y
  
  return loc # robot's final location


module.exports = { trackRobot }

# TEST
#console.log(trackRobot(20, 30, 10, 40))
#console.log(trackRobot())
#console.log(trackRobot(-10, 20, 10))
