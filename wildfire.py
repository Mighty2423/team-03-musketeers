wildfire = {
        'Name': 'wildfire',
        'At home': {'message': "You've been notified of a wildfire approaching in your area You have 5 minutes to evacuate. What do you do?"},
        
        
        'Stay put': {'message': 'The house is burning with you in it. You die'},


        'Get close to water': {'message': 'You get close to a body of water and get on a boat to middle of a lake.'},
        'Pick people up in boat': {'message': "You pick up anyone by the beaches on your boat, and your boat gets heavy and sinks. You die."},
        'Stay in the lake': {'message': "You stay in the middle of the lake until the fire dies down. You are safe."},



        'Go into forest': {'message': "You go into the forest and get to the middle of the forest."},
        'Follow wildlife': {'message': "You follow the large wild life and get chased by a bear. You die."},
        'Climb a tree': {'message': "You climb a tree and wait for help. The fire overtakes you. You die."},
        'Look for emergency personnel': {'message': "You start walking away and look for emergency personnel. You get lost and overtaken by the fire. You die."},


        'Get in a car': {'message': "You get in a car on and start driving down the road"},
        'Follow the evacuation': {'message': "You leave and follow the evacution of the neighborhood"},
        'Drive to nearest town': {'message': "You leave and drive to the nearest town. You make it to the town and are safe."},
        'Drive to nearest body of water': {'message': "You arrive at a body of water and get on a boat to middle of a lake."},
        'Find people to pickup': {'message': "You head down to find any one needing a ride"},
        'Leave car and run away': {'message': "You leave the car and start running away from the fire, but it overtakes you. You die."},

}


#1
wildfire['At home']['Get in a car'] = wildfire['Get in a car']
  #2
wildfire['Get in a car']['Follow the evacuation'] = wildfire['Follow the evacuation']
    #3
wildfire['Follow the evacuation']['Leave car and run away'] = wildfire['Leave car and run away']
    #3
wildfire['Follow the evacuation']['Find people to pickup'] = wildfire['Find people to pickup']
  #2
wildfire['Get in a car']['Drive to nearest town'] = wildfire['Drive to nearest town']
  #2
wildfire['Get in a car']['Drive to nearest body of water'] = wildfire['Drive to nearest body of water']
    #3
wildfire['Drive to nearest body of water']['Pick people up in boat'] = wildfire['Pick people up in boat']
    #3
wildfire['Drive to nearest body of water']['Stay in the lake'] = wildfire['Stay in the lake']


#1
wildfire['At home']['Stay put'] = wildfire['Stay put']


#1
wildfire['At home']['Go into forest'] = wildfire['Go into forest']
  #2
wildfire['Go into forest']['Follow wildlife'] = wildfire['Follow wildlife']
  #2
wildfire['Go into forest']['Climb a tree'] = wildfire['Climb a tree']
  #2
wildfire['Go into forest']['Look for emergency personnel'] = wildfire['Look for emergency personnel']


#1
wildfire['At home']['Get close to water'] = wildfire['Get close to water']
  #2
wildfire['Get close to water']['Pick people up in boat'] = wildfire['Pick people up in boat']
  #2
wildfire['Get close to water']['Stay in the lake'] = wildfire['Stay in the lake']

def get():
  return wildfire