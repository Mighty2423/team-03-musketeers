tornado = {
    'name': 'Tornado',
    'At home': {'message': 'Tornado Warning'},
    'Tornado Warning': {'message': 'Sirens and phone alerts'},
    'Sirens and phone alerts': {'message': 'Take cover under a table ,desk, that is sturdy bolted furniture'},
    'Take cover under a table ,desk, that is sturdy bolted furniture': {'message': 'Stay away from windows and doors'},
    'Stay away from windows and doors': {'message': 'Stay in the shelter until the warning is over'},

    'Take cover under a table ,desk': {'message': 'you survive'},

    'Act quickly': {'message': 'runn outside and hug a tree'},
    'runn outside and hug a tree': {'message': 'you die after being hit by flying debris'},

    'run away and drive away': {'message': 'Sucked into the tornado'},
    'Sucked into the tornado': {'message': 'you die by flying debris'},
}


tornado['At home'] = tornado['Tornado Warning']
tornado['Sirens and phone alerts'] = tornado['Take cover under a table ,desk, that is sturdy bolted furniture']
tornado['Take cover under a table ,desk, that is sturdy bolted furniture'] = tornado['Stay away from windows and doors']
tornado['Stay away from windows and doors'] = tornado['Act quickly']

tornado['Act quickly'] = tornado['Take cover under a table ,desk']
tornado['Take cover under a table ,desk'] = tornado['you survive and safe']


tornado['Act quickly'] = tornado['runn outside and hug a tree']
tornado['Act quickly'] = tornado['run away and drive away']
tornado['runn outside and hug a tree'] = tornado['you die after being hit by flying debris']





def tornado():
  return