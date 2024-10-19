flooding = {
  'Name': 'floods',
  'At home': {'message': 'Flood Warnings'},
  
  'Flash Flood Warning': {'message': 'A Flash Flood Warning is issued when a flash flood is imminent or occurring. If you are in a flood-prone area, move immediately to high ground. A flash flood is a sudden violent flood that can take from minutes to hours to develop. It is even possible to experience a flash flood in areas not immediately receiving rain.'},
  'Flood Watch': {'message': 'A Flood Watch is issued when conditions are favorable for flooding. Be prepared to move to higher ground and stay informed.'},
  'Stay put': {'message': 'Stay put. Do not attempt to drive or walk through flooded areas. If you are trapped by moving water, move to the highest possible point and call 911 for help.'},



  'Head for your boat':{'message': 'Get to your boat.'},
  'Get to your boat': {'message': 'head for cleared saftey area.'},
  'head for cleared saftey area': {'message': 'pickup people on the way.'},
  'pickup people on the way': {'message': 'head for cleared saftey area.'},

  'head for cleared saftey area': {'message': 'You got away safely and are safe'},


  'Get to high ground': {'message': 'get to the roof'},
  'Get to the roof': {'message': 'Wait for help'},
  'Wait for help': {'message': 'national guard and other emergency personnel are on their way to help you.'},
  'national guard and other emergency personnel are on their way to help you.':{'message':'You got away safely and are safe '},
  'You got away safely and are safe': {'message': ''},

}
#1
flooding ['At home']['Head for your boat'] = flooding ['Head for your boat']
#2
flooding ['Head for your boat']['Get to your boat']=flooding ['Get to your boat']
flooding ['Get to your boat']['head for cleared saftey area']=flooding['head for cleared saftey area']
flooding ['head for cleared saftey area']['pickup people on the way']=flooding['pickup people on the way']
flooding ['pickup people on the way']['head for cleared saftey area.']=flooding['head for cleared saftey area.']
flooding ['head for cleared saftey area.']['You got away safely and are safe']=flooding['You got away safely and are safe']




#1
flooding ['At home']['Get to high ground'] = flooding ['Get to high ground']
#
flooding ['Get to high ground']['get to the roof']=flooding['get to the roof']
#
flooding ['get to the roof']['Wait for help']=flooding['Wait for help']
#
flooding ['Wait for help']['national guard and other emergency personnel are on their way to help you.']=flooding['national guard and other emergency personnel are on their way to help you.']
#
flooding ['national guard and other emergency personnel are on their way to help you.']['You got away safely and are safe']=flooding['You got away safely and are safe']
#
flooding ['You got away safely and are safe']
flooding ['no help comes. You die']=flooding['no help comes. You die']

def get():
  return flooding