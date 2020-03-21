#Jake Eaton

from room import Room
from character import Character, Enemy
from item import Item
from introduction import Intro
from callingcode import Call
from death import Death
import time
import os
import sys
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import mixer

def type(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)
    sys.stdout.write("\n")

def type2(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.75)
    sys.stdout.write("\n")

#Intro()

first_room = Room("The old ruins of an ancient Castle")
first_room.set_description("You recognise the old castle as the place you lost your friend. She fell from the tallest tower. The castle has remained closed ever since. But wasn't it destroyed recently?")

second_room = Room("The frozen isle of a Supermarket")
second_room.set_description("It has been nearly twenty years since you were here. Last time you were here, you messed with the temperature controls and caused all the products to defrost. You were banned from entering. But why do they want to know about this?")

third_room = Room("An office filled with computers")
third_room.set_description("Your first job. After succeeding at University you quickly rose the ranks to become the leader of a tech team for the GCHQ. You recognise the motherboard on your desk. One of its logic circuits were not functioning correctly. Last time you had to test it... should you do the same?")

forth_room = Room("A riverside resturant")
forth_room.set_description("One of the darkest days of your life. It was here where you were betrayed. You were just enjoying a friendly meal until you started to lose your breath. Poisoned by your trusted ally... is he the key to all this?")

fifth_room = Room("The black abyss of space")
fifth_room.set_description("You don't remember this... is this even your memory?")

guards = Character("Guards", "The Guards of the Castle. There is no way you can defeat all of them. Don't talk to them too much otherwise they will take you down.")
guards.set_conversation("Move along unless you want us to arrest you.")
first_room.set_character(guards)

customers = Character("Customers", "Fellow customers of the supermarket. Absent minded and quite possibly stupid, they won't notice your work of art.")
customers.set_conversation("Oh excuse me!")
second_room.set_character(customers)

friend = Character("Eve","Quite literally one of the only people you can trust now. You would give your life for her.")
friend.set_conversation("Go on! Solve the puzzle! Your clever enough!")
forth_room.set_character(friend)

crew_member = Character("Crew Member from the Aorus","One of the seven crew members from your ship, the Aorus")
crew_member.set_conversation("Watch out Sir. We are picking up some strange stuff approaching our position quickly.")
fifth_room.set_character(crew_member)

mixer.init()
mixer.music.load("Battle.Of.The.Heroes.mp3")
mixer.music.play(10)

current_room = first_room
inventory = []

dead = False

while dead == False:
    type("You suddenly find youself focusing on one memory...\n")

    current_room.get_details()

    print(" ")

    type("You can't figure out why the people want to see this memory")
    time.sleep(2)
    type("Despite that, you walked forward toward the castle before being hit by one of the guards.")
    time.sleep(2)
    type("'We are embracing the future now.' they said.")
    time.sleep(2)
    type("You are confused. But before you could say anything the guard spoke again 'In order to enter, you must answer the question on the door.'")
    time.sleep(2)
    type("You were about to protest again but the guard cut you up.")
    time.sleep(2)
    type("'Answer it otherwise you will not enter!' said the Guard. You sigh and look around. There aren't many people but your friend is inside waiting for you. You walk over to the door and read the question.\n")
    time.sleep(2)
    type("What is Hardware and Software?\n")
    time.sleep(2)
    type("a: Hardware is the term used to describe the physical components of the computer whereas software is the non-physical programs that are stored on the computer's hardware\n")
    time.sleep(2)
    type("b: Hardware is the term used to describe the non-physical programs of the computer whereas software is the physical components of the computer\n")
    time.sleep(2)
    type("c: Hardware you can slap, software you can hit\n")
    time.sleep(2)
    type("d: Hardware and software doesn't exist... Duh!\n")
    answer1 = input(">> ")
    if answer1 != ("a") or ("A"):
        type("'Incorrect! The correct answer is a!'")
        time.sleep(2)
        type("The guard raises his sword and cuts you down where you stand...")
        time.sleep(2)
        Death()
        dead = True

    elif answer1 == ("a") or ("A"):
        type("'Well done.' said the guard. He pushed open the door and you enter the castle ruins")
        time.sleep(2)
        type("You look around and see your friend on the top of the ruins taking selfies")
        time.sleep(2)
        type("You sigh and turn to move towards the stairs. But when you arrive at them, you are met with another guard")
        time.sleep(2)
        type("'Come on what is the question?' you ask. The guard smiled and pointed to the sign they were holding")
        time.sleep(2)
        type("You look at the sign:\n")
        time.sleep(2)
        type("True or False? Library Files are non-compiled files which run when they are needed by a program")
        time.sleep(2)
        answer2 = input(">> ")
        if answer2 != ("true") or ("True"):
            type("'Incorrect! They are precompiled!'")
            time.sleep(2)
            type("The guard spins their spear and impales you...")
            time.sleep(2)
            Death()
            dead = True

        elif answer2 == ("false") or ("False"):
            type("'Correct. You may pass.' said the guard moving aside")
            time.sleep(2)
            type("You quickly move up the stairs only to met with yet another guard. Rolling your eyes, you read the question on their sign\n")
            time.sleep(2)
            type("What are the three different translators which can be run by a computer?\n")
            time.sleep(2)
            type("a: Compilers, Programmers and Translators\n")
            time.sleep(2)
            type("b: Translators, Assembler and Interpreters\n")
            time.sleep(2)
            type("c: Compilers, Interpreters and Assemblers\n")
            time.sleep(2)
            type("d: Compilers, Interpreters and Translators\n")
            time.sleep(2)
            answer3 = input(">> ")
            if answer3 != ("c") or ("C"):
                type("'Incorrect, the answer is C!'")
                time.sleep(2)
                type("The guard grabs you by the wrist and drags you to the wall")
                time.sleep(2)
                type("The guard lifts you up and throws you over the wall...")
                time.sleep(2)
                Death()
                dead = True

            elif answer3 == ("c") or ("C"):
                type("'Well done. Go on.' said the guard moving aside")
                time.sleep(2)
                type("You walk up and look around. You see your friend and some other items. You remeber the castle rules saying whatever you find, you can take")
                Call()
                     

##while dead == True:
##    Menu()
    
