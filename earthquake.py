earthquakes = {
  'Name': 'earthquakes',
  'At home': {'message': 'Earthquakes Warning'},
  'Earthquakes Warning': {'message': 'Sirens and phone alerts'},
  'Sirens and phone alerts': {'message': 'Take cover under a table ,desk, or other sturdy bolted furniture'},
  'Take cover under a table ,desk, or other sturdy bolted furniture': {'message': 'Stay inside until the shaking stops and it is safe to exit'},
  
  'Take cover under a table ,desk':{'message': 'you survive'},
  'Take cover under a table ,desk':  {'message': 'house Collapse'},
  'house Collapse': {'message': 'you die'},
  
  
'Take cover clinging to the toilet':{'message': 'you survive'},
'Take cover clinging to the toilet': {'message': 'house Collapse'},
'house Collapse': {'message': 'you die'},

'Act quickly': {'message': 'runn outside and hug a tree'},
'runn outside and hug a tree': {'message': 'you die'},
'runn outside and hug a tree': {'message': 'you survive'},

'run away and drive away': {'message': 'car crash'},
'car crash': {'message': 'you die'},
}



earthquakes['At home']['Earthquakes Warning']=earthquakes['Earthquakes Warning']
earthquakes['Earthquakes Warning']['Sirens and phone alerts']=earthquakes=['Sirens and phone alerts']
earthquakes['Sirens and phone alerts']['Take cover under a table ,desk, or other sturdy bolted furniture']=earthquakes=['Take cover under a table ,desk, or other sturdy bolted furniture']
earthquakes['Take cover under a table ,desk, or other sturdy bolted furniture']['Stay inside until the shaking stops and it is safe to exit']=earthquakes=['Stay inside until the shaking stops and it is safe to exit']

earthquakes['Take cover under a table ,desk']['you survive']=earthquakes=['you survive']
earthquakes['Take cover under a table ,desk']['house Collapse']=earthquakes=['house Collapse']
earthquakes['house Collapse']['you die']=earthquakes=['you die']

earthquakes['Take cover clinging to the toilet']['you survive']=earthquakes=['you survive']
earthquakes['Take cover clinging to the toilet']['house Collapse']=earthquakes=['house Collapse']
earthquakes['house Collapse']['you die']=earthquakes=['you die']

earthquakes['Act quickly']['runn outside and hug a tree']=earthquakes=['runn outside and hug a tree']
earthquakes['runn outside and hug a tree']['you die']=earthquakes=['you die']
earthquakes['runn outside and hug a tree']['you survive']=earthquakes=['you survive']

earthquakes['run away and drive away']['car crash']=earthquakes=['car crash']
earthquakes['car crash']['you die']=earthquakes=['you die']

def get():
  return earthquakes

