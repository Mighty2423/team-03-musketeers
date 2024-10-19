hurricane = {
  'Name': 'hurricane',
  'At home': {'message': 'Sirens and phone alerts: \n\"Take cover under a table, desk, or other sturdy bolted furniture!\"'},
  'Take cover under bolted furniture': {'message': 'Stay inside until the shaking stops and it is clear to exit'},
  
  'Take cover under a table, desk': {'message': 'You survive. You are safe.'},
  'Take cover clinging to the toilet': {'message': 'You survive the hurricane. You are safe.'},

  'Run outside': {'message': 'You run outside and hug a tree. You die.'},

  'Drive away': {'message': 'You try to drive away while the hurricane is hitting. Your car crashes. You die.'},
}


#1
hurricane['At home']['Take cover under bolted furniture'] = hurricane['Take cover under bolted furniture']
  #2
hurricane['Take cover under bolted furniture']['Take cover under a table, desk'] = hurricane['Take cover under a table, desk']
  #2
hurricane['Take cover under bolted furniture']['Take cover clinging to the toilet'] = hurricane['Take cover clinging to the toilet']

#1
hurricane['At home']['Run outside'] = hurricane['Run outside']

#1
hurricane['At home']['Drive away'] = hurricane['Drive away']

def get():
  return hurricane