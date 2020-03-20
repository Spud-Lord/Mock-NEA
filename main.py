#Jake Eaton

from room import Room
from character import Character, Enemy
from item import Item
from introduction import Intro
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

mixer.init()
mixer.music.load("Battle.Of.The.Heroes_1.mp3")
mixer.music.play()

Intro()

##first_room = Room("The old ruins of an ancient Castle")
##first_room.set_description("You recognise the old castle as the place you lost your friend. She fell from the tallest tower. The castle has remained closed ever since. But wasn't it destroyed recently?")
##
##second_room = Room("The frozen isle of a Supermarket")
##second_room.set_description("It has been nearly twenty years since you were here. Last time you were here, you messed with the temperature controls and caused all the products to defrost. You were banned from entering. But why do they want to know about this?")
##
##third_room = Room("An office filled with computers")
##third_room.set_description("Your first job. After succeeding at University you quickly rose the ranks to become the leader of a tech team for the GCHQ. You recognise the motherboard on your desk. One of its logic circuits were not functioning correctly. Last time you had to test it... should you do the same?")
##
##forth_room = Room("A riverside resturant")
##forth_room.set_description("One of the darkest days of your life. It was here where you were betrayed. You were just enjoying a friendly meal until you started to lose your breath. Poisoned by your trusted ally... is he the key to all this?")
##
##fifth_room = Room("")
##fifth_room.set_description("")
##
##sixth_room = Room("")
##sixth_room.set_description("")
##
##seventh_room = Room("")
##seventh_room.set_description("")


