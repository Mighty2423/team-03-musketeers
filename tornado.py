tornado = {
  'Name': 'tornado',
  'At home': {'message': 'Sirens and phone alerts: \n\"Take cover under a table, desk, or other sturdy bolted furniture!\"'},
  'Take cover under bolted furniture': {'message': 'Stay inside until the shaking stops and it is clear to exit'},
  
  'Take cover under a table, desk': {'message': 'You survive. You are safe.'},
  'Take cover clinging to the toilet': {'message': 'You survive the tornado. You are safe.'},

  'Run outside': {'message': 'You run outside and hug a tree. You die.'},

  'Drive away': {'message': 'You try to drive away while the tornado is hitting. Your car crashes. You die.'},
}


#1
tornado['At home']['Take cover under bolted furniture'] = tornado['Take cover under bolted furniture']
  #2
tornado['Take cover under bolted furniture']['Take cover under a table, desk'] = tornado['Take cover under a table, desk']
  #2
tornado['Take cover under bolted furniture']['Take cover clinging to the toilet'] = tornado['Take cover clinging to the toilet']

#1
tornado['At home']['Run outside'] = tornado['Run outside']

#1
tornado['At home']['Drive away'] = tornado['Drive away']

def get():
  return tornado