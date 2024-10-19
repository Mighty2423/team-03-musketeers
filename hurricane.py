hurricane = {
    "name": "Hurricane",
    'At home': {'message': 'Hurricane Warning'},
    'Hurricane Warning': {'message': 'Sirens and phone alerts'},
    'Sirens and phone alerts': {'message': 'Take cover under a table ,desk, that is sturdy bolted furniture'},
    'Take cover under a table ,desk, that is sturdy bolted furniture': {'message': 'Stay away from windows and doors'},
    'Stay away from windows and doors': {'message': 'Waring for looters'},
    'Waring for looters': {'message': 'stay away from damaged properties or face later consequences'},

    'stay away from damaged properties or face later consequences': {'message' : 'take cover under a table ,desk'}, 
    'Take cover under a table ,desk': {'message': 'you survive You are safe.'},
    
    'Act quickly': {'message': 'runn outside and hug a tree'},
    'runn outside and hug a tree': {'message': 'you die after being hit by flying debris'},

    'run away and drive away': {'message': 'Sucked into the hurricane'},
    'Sucked into the hurricane': {'message': 'you die by being hit by suffocation'},
    }


hurricane['At home'] = hurricane['Hurricane Warning']
hurricane['Hurricane Warning'] = hurricane['Sirens and phone alerts']
hurricane['Sirens and phone alerts'] = hurricane['Take cover under a table ,desk, that is sturdy bolted furniture']
hurricane['Take cover under a table ,desk, that is sturdy bolted furniture'] = hurricane['Stay away from windows and doors']
hurricane['Stay away from windows and doors'] = hurricane['Waring for looters'] = hurricane['stay away from damaged properties']


hurricane['stay away from damaged properties'] = hurricane['take cover under a table ,desk']
hurricane['take cover under a table ,desk'] = hurricane['you survive You are safe.']

hurricane['Act quickly'] = hurricane['runn outside and hug a tree']
hurricane['runn outside and hug a tree'] = hurricane['you die after being hit by flying debris']

hurricane['run away and drive away'] = hurricane['Sucked into the hurricane']
hurricane['Sucked into the hurricane']= hurricane['you die by being hit by suffocation']


def get():
  return hurricane