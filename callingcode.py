#Jake Eaton
#Call Characters and Items

from room import Room
from character import Character, Enemy
from item import Item
from death import Death
import time
import sys
import os
from pygame import mixer
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

def Call():
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        for person in inhabitant:
            person.describe()

    items = current_room.get_item()
    if items is not None:
        for item in items:
            item.describe()

    print("")

        command = input("> ")
    if command in ["Top", "Bottom", "42", "66", "Back"]:    #If the command is one of the ones in the list, the user will be moved to the room accordingly
        current_room = current_room.move(command)

    elif command == "Talk":                                 #If the user wants to talk, the indented code will run
        print("Who do you want to talk with? ")
        talker = input("> ")
        found = False                                       #True or False Boolean deciding if there is a person there
        for person in inhabitant:                           #If there is an inhabitant, the following code will run
            if person.get_name() == talker:                 #Gets the name of the Person if they are registered as a talker
                found = True                                #Changes Boolean to True
                person.talk()                               #Makes the person talk
                time.sleep(4)
        if not found:                                       #If the person is not there the indented code runs
            print("That person is not here!")

    elif command == "Fight":                                #If the user wants to fight, the indented code will run
        print("Who do you want to fight?")
        fighter = input("> ")                                   #Allows user to input who they want to fight
        there = False                                       #True or False Boolean deciding if there is a fighter there or not
        for person in inhabitant:                           #If there is a person who fights then the following code will run
            if person.get_name() == fighter:
                print("What will you fight with?")
                fight_with = input("> ")                        #Fight with variable allowing user to input what they want to fight with

                if fight_with in on_hand:                   #If what the user wants to fight with is on hand (as determined by list), the indented code will run

                    if person.fight(fight_with) == True:    #If the weapon is the enemies weakness
                        print("You destroy your enemy...\n")
                        time.sleep(3)
                        current_room.get_character().remove(person)   #Removes the person if they are defeated

                else:
                    if isinstance(person, Enemy):
                        Death()
                        mixer.music.fadeout(3000)         #Music fades away for 3 seconds
                        time.sleep(3)
                        dead = True                       #If the user loses the fight, the dead Boolean is made True

                else:
                    print("You don't have a " + fight_with + "\n")    #If the weapon is not in the list, it prints this
                there = True
        if not there:
            print("That person is not here")              #If the person the user has typed is not there, this code is run


    elif command == "Take":                               #If the user wants to take an item, the indented code is run
        if item is not None:
            print("You take the " +  item.get_name() + " along with you\n")
            on_hand.append(item.get_name())               #Adds the item to the on_hand list so that the user can use it in fights
            current_room.get_item().remove(item)          #Removes the item from the room

        else:
            print("There is nothing here to take!\n")     #If there is no item in the room, this code gets printed

    else:
        print("You can't do that!\n")                     #If the user types in something that isn't an option, this code gets printed

