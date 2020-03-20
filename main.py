#Jake Eaton

from room import Room
from character import Character, Enemy
from item import Item
from introduction import Intro
from callingcode import Call
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

Intro()

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
mixer.music.play()

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
    type("a: Hardware is the term used to describe the physical components of the computer whereas software are the non-physical programs that are stored on the computer's hardware\n")
    
