hurricane = {
    "name": "Hurricane",
    'At home': {'message': 'Hurricane Warning'},
    'Hurricane Warning': {'message': 'Sirens and phone alerts'},
    'Sirens and phone alerts': {'message': 'Take cover under a table ,desk, that is sturdy bolted furniture'},
    'Take cover under a table ,desk, that is sturdy bolted furniture': {'message': 'Stay away from windows and doors'},
    'Stay away from windows and doors': {'message': 'Stay in the shelter until the warning is over'},
    'Stay in the shelter until the warning is over Stay away from flood waters Stay away from downed power lines Stay away from debris Stay away from damaged buildings Stay away from damaged roads Stay away from damaged bridges Stay away from damaged trees Stay away from large groups of people': {'message': 'Waring for looters'},
    'Waring for looters': {'message': 'stay away from damaged properties or face later consequences'},

    'stay away from damaged properties or face later consequences': {'message' : 'take cover under a table ,desk'}, 
    'Take cover under a table ,desk': {'message': 'you survive'},
    'Take cover under a table ,desk':  {'message': 'house ripped off foundation'},
    'house ripped off foundation': {'message': 'you die'},

    'Act quickly': {'message': 'runn outside and hug a tree'},
    'runn outside and hug a tree': {'message': 'you die after being hit by flying debris'},



    'run away and drive away': {'message': 'Sucked into the hurricane'},
    'Sucked into the hurricane': {'message': 'you die by flying debris'},
    'Sucked into the hurricane': {'message': 'you die by being hit by suffocation'},
    }



hurricane['Hurricane Warning']['next'] = hurricane['Sirens and phone alerts']
hurricane['Sirens and phone alerts']['next'] = hurricane['Take cover under a table ,desk, that is sturdy bolted furniture']
hurricane['Take cover under a table ,desk, that is sturdy bolted furniture']['next'] = hurricane['Stay away from windows and doors']
hurricane['Stay away from windows and doors']['next'] = hurricane['Stay in the shelter until the warning is over Stay away from flood waters Stay away from downed power lines Stay away from debris Stay away from damaged buildings Stay away from damaged roads Stay away from damaged bridges Stay away from damaged trees Stay away from large groups of people']
hurricane['Stay in the shelter until the warning is over Stay away from flood waters Stay away from downed power lines Stay away from debris Stay away from damaged buildings Stay away from damaged roads Stay away from damaged bridges Stay away from damaged trees Stay away from large groups of people']['next'] = hurricane['Waring for looters']
hurricane['Waring for looters']['next'] = hurricane['stay away from damaged properties']
hurricane['stay away from damaged properties']['next'] = hurricane['take cover under a table ,desk']
hurricane['take cover under a table ,desk']['next'] = hurricane['you survive']
hurricane['take cover under a table ,desk']['next'] = hurricane['house ripped off foundation']
hurricane['house ripped off foundation']['next'] = hurricane['you die']

hurricane['Act quickly']['next'] = hurricane['runn outside and hug a tree']
hurricane['runn outside and hug a tree']['next'] = hurricane['you die after being hit by flying debris']

hurricane['run away and drive away']['next'] = hurricane['Sucked into the hurricane']
hurricane['Sucked into the hurricane']['next'] = hurricane['you die by flying debris']
hurricane['Sucked into the hurricane']['next'] = hurricane['you die by being hit by suffocation']


def get():
  return hurricane