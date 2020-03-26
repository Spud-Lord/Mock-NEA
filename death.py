#Jake Eaton
#Death

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

def Death():
    mixer.init()
    mixer.music.load("imperial_alert.mp3")
    mixer.music.play(5)

    type("'Critical Failure!' you hear a voice shout")
    time.sleep(2)
    type("Your mind suddenly starts to flash with memories and your body aches in pain")
    time.sleep(2)
    type("'Memory Overload! They are resisting the implant!'")
    time.sleep(2)
    type("'Release the implant! Set him free!' a woman shouts")
    time.sleep(2)
    type("You shout in pain as the neural implant is removed from the back of your neck")
    time.sleep(2)
    type("You feel your blood flowing down your neck as you are set free")
    time.sleep(2)
    type("You collapse onto the cold solid floor beneath you and pant heavily")
    time.sleep(2)
    type("'You resisted. You changed the memory.' said a woman above you. You try to look up at the woman")
    time.sleep(2)
    type("'I am sorry. But unless you follow our orders, you can not live.' you can just make out a gun pointing at your head")
    time.sleep(2)
    type("You hold up your hand, shaking")
    time.sleep(2)
    type("'Wait a minute!' you say weakly. But it didn't stop the inevitable...")
    time.sleep(2)
    type("You don't even hear the gun fire...")
    time.sleep(2)
    type("You don't even feel yourself hit the ground...")
    time.sleep(2)
    type2("You feel nothing...")

def Death2():
    type("The woman pulls the device from behind her back and fires it four times")
    time.sleep(2)
    type("Your arms and legs begin to bleed and you yell out in pain")
    time.sleep(2)
    type("'We have no further use for you and we cannot risk you revealing this information' the woman said")
    time.sleep(2)
    type("'Don't worry. You will forget what happened to you.' the woman walked away still holding the gun and you could do nothing...")
    time.sleep(2)
    type("As you slowly bleed out, you waited for the darkness to consume you...")
    time.sleep(2)
    type("Eventually...")
    time.sleep(2)
    type2("You...")
    time.sleep(2)
    type2("Felt...")
    time.sleep(2)
    type2("Nothing...")
