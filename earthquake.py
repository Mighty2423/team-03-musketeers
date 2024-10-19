earthquake = {
  'Name': 'earthquake',
  'At home': {'message': 'Sirens and phone alerts: \n\"Take cover under a table, desk, or other sturdy bolted furniture!\"'},
  'Take cover under bolted furniture': {'message': 'Stay inside until the shaking stops and it is clear to exit'},
  
  'Take cover under a table, desk': {'message': 'You survive. You are safe.'},
  'Take cover clinging to the toilet': {'message': 'You survive the earthquake. You are safe.'},

  'Run outside': {'message': 'You run outside and hug a tree. You die.'},

  'Drive away': {'message': 'You try to drive away while the earth is rumbling. Your car crashes. You die.'},
}


#1
earthquake['At home']['Take cover under bolted furniture'] = earthquake['Take cover under bolted furniture']
  #2
earthquake['Take cover under bolted furniture']['Take cover under a table, desk'] = earthquake['Take cover under a table, desk']
  #2
earthquake['Take cover under bolted furniture']['Take cover clinging to the toilet'] = earthquake['Take cover clinging to the toilet']

#1
earthquake['At home']['Run outside'] = earthquake['Run outside']

#1
earthquake['At home']['Drive away'] = earthquake['Drive away']

def get():
  return earthquake

