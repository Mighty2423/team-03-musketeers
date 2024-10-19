earthquake = {
  'Name': 'earthquake',
  'At home': {'message': 'Earthquake Warning'},
  'Earthquake Warning': {'message': 'Sirens and phone alerts'},
  'Sirens and phone alerts': {'message': 'Take cover under a table ,desk, or other sturdy bolted furniture'},
  'Take cover under bolted furniture': {'message': 'Stay inside until the shaking stops and it is safe to exit'},
  
  'Take cover under a table, desk':{'message': 'You survive. You are safe.'},
  'Take cover clinging to the toilet':{'message': 'you survive You are safe.'},

'Act quickly': {'message': 'runn outside and hug a tree'},
'runn outside and hug a tree': {'message': 'you die'},


'run away and drive away': {'message': 'car crash'},
'car crash': {'message': 'you die'},
}



earthquake['At home']['Earthquake Warning']=earthquake['Earthquake Warning']
earthquake['Earthquake Warning']['Sirens and phone alerts']=earthquake['Sirens and phone alerts']
earthquake['Sirens and phone alerts']['Take cover under a table, desk']=earthquake['Take cover under a table, desk']
earthquake['Take cover under a table, desk']['Stay inside until the shaking stops and it is safe to exit']=earthquake['Stay inside until the shaking stops and it is safe to exit']

earthquake['Take cover under a table ,desk']['you survive You are safe.']=earthquake['you surviveYou are safe.']
earthquake['Take cover clinging to the toilet']['you surviveYou are safe.']=earthquake['you survive You are safe.']


earthquake['Act quickly']['runn outside and hug a tree']=earthquake['runn outside and hug a tree']
earthquake['runn outside and hug a tree']['you die']=earthquake['you die']

earthquake['run away and drive away']['car crash']=earthquake['car crash']
earthquake['car crash']['you die']=earthquake['you die']

def get():
  return earthquake

