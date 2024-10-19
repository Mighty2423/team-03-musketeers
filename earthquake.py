earthquake = {
  'Name': 'earthquake',
  'At home': {'message': 'Earthquake Warning'},
  'Earthquake Warning': {'message': 'Sirens and phone alerts'},
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



earthquake['At home']['Earthquake Warning']=earthquake['Earthquake Warning']
earthquake['Earthquake Warning']['Sirens and phone alerts']=earthquake=['Sirens and phone alerts']
earthquake['Sirens and phone alerts']['Take cover under a table ,desk, or other sturdy bolted furniture']=earthquake=['Take cover under a table ,desk, or other sturdy bolted furniture']
earthquake['Take cover under a table ,desk, or other sturdy bolted furniture']['Stay inside until the shaking stops and it is safe to exit']=earthquake=['Stay inside until the shaking stops and it is safe to exit']

earthquake['Take cover under a table ,desk']['you survive']=earthquake=['you survive']
earthquake['Take cover under a table ,desk']['house Collapse']=earthquake=['house Collapse']
earthquake['house Collapse']['you die']=earthquake=['you die']

earthquake['Take cover clinging to the toilet']['you survive']=earthquake=['you survive']
earthquake['Take cover clinging to the toilet']['house Collapse']=earthquake=['house Collapse']
earthquake['house Collapse']['you die']=earthquake=['you die']

earthquake['Act quickly']['runn outside and hug a tree']=earthquake=['runn outside and hug a tree']
earthquake['runn outside and hug a tree']['you die']=earthquake=['you die']
earthquake['runn outside and hug a tree']['you survive']=earthquake=['you survive']

earthquake['run away and drive away']['car crash']=earthquake=['car crash']
earthquake['car crash']['you die']=earthquake=['you die']

def get():
  return earthquake

