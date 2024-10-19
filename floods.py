floods = {
  'Name': 'floods',
  'At home': {'message': 'A Flash Flood Warning is issued when a flash flood is imminent or occurring. \nIf you are in a flood-prone area, move immediately to high ground.'},
  'Get to high ground': {'message': 'You get to the roof. You wait for first responders to rescue you. You get away safely.'},
  'Stay put': {'message': 'You stay at home and the flood overtakes you. You die.'},

  'Head for your boat':{'message': 'You get to your boat.'},
  'Row to safety area': {'message': 'You head for the cleared saftey area. You are safe.'},
  'Start looting': {'message': 'You get caught by the cops. You try to get away, but drown. You die.'},
   

}
#1
floods['At home']['Get to high ground'] = floods['Get to high ground']

#1
floods['At home']['Stay put'] = floods['Stay put']

#1
floods['At home']['Head for your boat'] = floods['Head for your boat']
  #2
floods['Head for your boat']['Row to safety area'] = floods['Row to safety area']
  #2
floods['Head for your boat']['Start looting'] = floods['Start looting']





def get():
  return floods