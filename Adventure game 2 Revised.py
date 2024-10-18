#Adventure game 2 the rewrite
# Author Alton white
#testers Mathew Bruson , Tyler Aho ,

#commets


#Thank you for playing
no = "\n Thank you for playing. "
#general error message
beep = ("Invalid response. Please try again")
#reapeater
#choices opening
open =("Welcome to the adventure. \n Please chose your weapon? SWORD MACE MAGIC STAFF? ")
sword = ("With that sword You will be going to the Mt coreonet. Wish to fight a monster or go down to the Misty Forest? MONSTER or FOREST? ")
mace = ("You will be going to the black sand beach. Do you wish to go NORTH or SOUTH ")
magic_staff = ("You will go to misty forest. When you arrive theres a cave at the entrence. \n Do you enter the forest or do you enter the cave? Enter FOREST or CAVE ")
#mosnter fight or run
#fight win with might you find a house
#fight skill die                             
monster = ("You come before a monster. Do you fight with might or skill? \n Please chose how to wield your weapon? Choose SKILL or MIGHT? ")
might = ("You slay the monster but you die ")
skill = ("You have fallen.")
#forest path 
#roll a dice even or odd
#even found a way home
#odd enter a empty house
forest = ("Welcome to the Forest. \n You see two path your home and a empty house. \n Do you whish to go Home or the the House? HOME or HOUSE? ")
home = ("You found your way home congraualtions!")
house = ("You come before a monster and die  with out warning.")
#cave path
#to forest choice
#cave takes you to another world bye I am no longer your narrator. Bye system lost
cave = ("You stand out of the cave! \n Please chose to enter the Cave or go to the Forest? ENETER or FOREST ")
enter = ("The cave takes you to another world bye I am no longer your narrator. \n Good Bye may you live well and die well. \n System connection lost")
#Black sand beach
#North go to forest
#south to empty house
Black_sands =("Welcome to the Black Sands beach. \n Please chose which way NORTH or SOUTH? ")
South = ("You found a empty house. \n You die without waring a night terror left you your skull.")
North = forest
#starter
scene =input(open).lower()

#Fight monster or go to the forest
if scene == "sword":
    print()
    scene = input(sword).lower()
    #Black sand beach North or south
    #forest path 
    if scene == "forest":
        print()
        scene = input(forest).lower()
            #end found your way home 
        if(scene == "home"):
            print()
            print(home)
            #fight monster
        elif scene == "house":
            print()
            print(house)
        else:
            print(beep)
    elif scene == "monster":
        print()
        scene = input(monster).lower()
        if (scene == "skill"):
            print()
            print(skill)
        elif (scene == "might"):
            print(might)
        else:
            print(beep)
    else:
        print(beep)
elif(scene.lower() == "magic staff"):
    print(magic_staff)
    scene = input()
    if (scene.lower() == "forest"):
        print()
        scene = input(forest).lower()
                 #end found your way home 
        if(scene == "home"):
            print()
            print(home)
        elif (scene == "house"):
            print(house)
        else:
            print(beep)
    elif (scene.lower() == "cave"):
        print(cave)
        scene = input(cave).lower()
        if(scene == "enter"):
            print(enter)
            #everthing up works
            #Beach area options north and south
        elif(scene == "forest"):
            print()
            scene = input(forest).lower()
                 #end found your way home 
            if(scene == "home"):
                print()
                print(home)
            elif (scene == "house"):
                print(house)
            else:
                print(beep)
        else:
            print(beep)
    else:
        print(beep)
elif(scene.lower() == "mace"):
    print()
    scene = input(Black_sands).lower()
    print
    if(scene.lower() == "north"):
        print()
        scene = input(North).lower() # NORTH leads directly to FOREST so all you need is the last inputs
        #end found your way home 
        if(scene == "home"):
            print()
            print(home)
            #fight monster
        elif(scene == "house"):
            print()
            print(house)
        else:
            print(beep)
    elif(scene.lower() == "south"):
        print()
        print(South) # is this suppose to end?
    else:
        print(beep)                            
else:
    print(beep)
