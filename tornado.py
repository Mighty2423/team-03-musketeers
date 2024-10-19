tornado = {
    'name': 'Tornado',
    'At home': {'message': 'Tornado Warning'},
    'Tornado Warning': {'message': 'Sirens and phone alerts'},
    'Sirens and phone alerts': {'message': 'Take cover under a table ,desk, that is sturdy bolted furniture'},
    'Take cover under a table ,desk, that is sturdy bolted furniture': {'message': 'Stay away from windows and doors'},
    'Stay away from windows and doors': {'message': 'Stay in the shelter until the warning is over'},

    'Take cover under a table ,desk': {'message': 'you survive'},
    'Take cover under a table ,desk':  {'message': 'house ripped off foundation'},
    'house ripped off foundation': {'message': 'you die'},

    'Act quickly': {'message': 'runn outside and hug a tree'},
    'runn outside and hug a tree': {'message': 'you die after being hit by flying debris'},



    'run away and drive away': {'message': 'Sucked into the tornado'},
    'Sucked into the tornado': {'message': 'you die by flying debris'},
    'Sucked into the tornado': {'message': 'you die by being hit by suffocation'},
}


tornado['At home']['yes'] = tornado['Tornado Warning']
tornado['At home']['no'] = tornado['Act quickly']
tornado['Tornado Warning']['yes'] = tornado['Sirens and phone alerts']
tornado['Tornado Warning']['no'] = tornado['Act quickly']
tornado['Sirens and phone alerts']['yes'] = tornado['Take cover under a table ,desk, that is sturdy bolted furniture']
tornado['Sirens and phone alerts']['no'] = tornado['Act quickly']
tornado['Take cover under a table ,desk, that is sturdy bolted furniture']['yes'] = tornado['Stay away from windows and doors']
tornado['Take cover under a table ,desk, that is sturdy bolted furniture']['no'] = tornado['Act quickly']
tornado['Stay away from windows and doors']['yes'] = tornado['Stay in the shelter until the warning is over']
tornado['Stay away from windows and doors']['no'] = tornado['Act quickly']

tornado['Take cover under a table ,desk']['yes'] = tornado['you survive']
tornado['Take cover under a table ,desk']['no'] = tornado['house ripped off foundation']

tornado['Act quickly']['yes'] = tornado['runn outside and hug a tree']
tornado['Act quickly']['no'] = tornado['run away and drive away']
tornado['runn outside and hug a tree']['yes'] = tornado['you die after being hit by flying debris']
tornado['run away and drive away']['yes'] = tornado['Sucked into the tornado']
tornado['Sucked into the tornado']['yes'] = tornado['you die by flying debris']
tornado['Sucked into the tornado']['no'] = tornado['you die by being hit by suffocation']

tornado['you survive']['yes'] = tornado['you survive']
tornado['house ripped off foundation']['yes'] = tornado['you die']

tornado['you die after being hit by flying debris']['yes'] = tornado['you die']
tornado['you die by flying debris']['yes'] = tornado['you die']
tornado['you die by being hit by suffocation']['yes'] = tornado['you die']

def tornado():
  return