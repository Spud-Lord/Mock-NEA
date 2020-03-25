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

Intro()

first_room = Room("The old ruins of an ancient Castle")
first_room.set_description("You recognise the old castle as the place you lost your friend. She fell from the tallest tower. The castle has remained closed ever since. But wasn't it destroyed recently?")

second_room = Room("The frozen isle of a Supermarket")
second_room.set_description("It has been nearly twenty years since you were here. Last time you were here, you messed with the temperature controls and caused all the products to defrost. You were banned from entering. But why do they want to know about this?")

third_room = Room("An office filled with computers")
third_room.set_description("Your first job. After succeeding at University you quickly rose the ranks to become the leader of a tech team for the GCHQ. You recognise the motherboard on your desk. You also notice a test paper you were meant to fill in weeks ago. Last time you wer here, you had to test the board and complete the test... should you do the same?")

forth_room = Room("A riverside resturant")
forth_room.set_description("One of the darkest days of your life. It was here where you were betrayed. You were just enjoying a friendly meal until you started to lose your breath. Poisoned by your trusted ally... is he the key to all this?")

fifth_room = Room("The black abyss of space")
fifth_room.set_description("You don't remember this... is this even your memory?")

f_r_friend = Character("Your Friend","The puzzles have delayed you but at least you are here now.\n")
f_r_friend.set_conversation("Hey! Come here!")
first_room.set_character(f_r_friend)

guards = Enemy("Guards", "The Guards of the Castle. There is no way you can defeat all of them. Don't talk to them too much otherwise they will take you down.\n")
guards.set_conversation("Move along unless you want us to arrest you.")
first_room.set_character(guards)

customers = Character("Customers", "Fellow customers of the supermarket. Absent minded and quite possibly stupid, they won't notice your work of art.\n")
customers.set_conversation("Oh excuse me!")
second_room.set_character(customers)

friend = Character("Eve","Quite literally one of the only people you can trust now. You would give your life for her.\n")
friend.set_conversation("Go on! Solve the puzzle! Your clever enough!")
forth_room.set_character(friend)

crew_member = Character("Crew Member from the Aorus","One of the seven crew members from your ship, the Aorus\n")
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

    time.sleep(2)

    current_room.get_details()

    time.sleep(4)

    print(" ")

    type("You can't figure out why the people want to see this memory")
    time.sleep(2)
    type("Despite that, you walk forward toward the castle before being hit by one of the guards.")
    time.sleep(2)
    type("'We are embracing the future now.' they said.")
    time.sleep(2)
    type("You are confused. But before you could say anything the guard spoke again 'In order to enter, you must answer the question on the door.'")
    time.sleep(2)
    type("You were about to protest again but the guard cut you up.")
    time.sleep(2)
    type("'Answer it otherwise you will not enter!' said the Guard. You sigh and look around. There aren't many people but your friend is inside waiting for you. You walk over to the door and read the question with the guard standing right beside you.\n")
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
    answer1 = input("")
    if answer1.lower() != "a":
        type("'Incorrect! The correct answer is a!'")
        time.sleep(2)
        type("The guard raises his sword and cuts you down where you stand...\n")
        time.sleep(2)
        Death()
        dead = True

    elif answer1.lower() == "a":
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
        answer2 = input("")
        if answer2.lower() == "true":
            type("'Incorrect! They are precompiled!'")
            time.sleep(2)
            type("The guard spins their spear and impales you...\n")
            time.sleep(2)
            Death()
            dead = True

        elif answer2.lower() == "false":
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
            answer3 = input("")
            if answer3.lower() != "c":
                type("'Incorrect, the answer is C!'")
                time.sleep(2)
                type("The guard grabs you by the wrist and drags you to the wall")
                time.sleep(2)
                type("The guard lifts you up and throws you over the wall...\n")
                time.sleep(2)
                Death()
                dead = True

            elif answer3.lower() == "c":
                type("'Well done. Go on.' said the guard moving aside")
                time.sleep(2)
                type("You walk up and look around. You see your friend and begin to move towards her")
                time.sleep(2)
                type("'Hey! Come look at this picture I took!' she said happily.")
                time.sleep(2)
                type("You take the phone from her to see the picture better in the bright sun")
                time.sleep(2)
                type("Suddenly, someone turns and pushes your friend over the wall...")
                time.sleep(2)
                type("You try to catch her but it is too late...")
                time.sleep(2)
                type("She didn't even have time to scream before she hit the ground and died...")
                time.sleep(2)
                type("You did nothing but look over the edge...")
                time.sleep(2)
                type("You couldn't believe what just happened")
                time.sleep(2)
                type("You turned to face the person who did it but they had already run off")
                time.sleep(2)
                type("Lost... you stood up on the wall and prepared to jump...")
                time.sleep(2)

    current_room = second_room

    type("You suddenly find youself focusing on another memory...\n")

    current_room.get_details()

    type("You realise you have a briefcase in your hand. You notice the freezer and walk over there. Passing the two shoppers that were down the same isle. You kneel down next to the control panel and look at it")
    time.sleep(2)
    type("Unscrewing the cover revealed just what you were looking for. The connector to link up your laptop with the controls")
    time.sleep(2)
    type("You open your briefcase and turn on the laptop inside. You link up the connector to it and wait for your program to load up")
    time.sleep(2)
    type("As long as you mess up the logic gates, all will be just as you expect")
    time.sleep(2)
    type("You see your first problem appear. It is the first logic gate to answer")
    time.sleep(2)
    type("Weirdly, your program is giving it to you in equation form\n")
    time.sleep(2)
    type("Work out the output of this equation:\n")
    time.sleep(2)
    type("Output = (Not(A AND B)) OR (NAND (XOR C D)E)")
    type("""a = 1
B = 0
C = 1
D = 1
E = 0""")
    answer4 = input("")
    if answer4 != "1":
        type("Your laptop suddenly shuts down")
        time.sleep(2)
        type("'OI! WHAT DO YOU THINK YOU'RE DOING?' shouted a voice")
        time.sleep(2)
        type("Before you could even look up, you were shot in the back with a taser")
        time.sleep(2)
        Death()

    elif answer4 == "1":
        type("Your laptop accepted the answer and you waited for it to continue")
        time.sleep(2)
        type("One of the shopkeepers approached you...")
        time.sleep(2)
        type("'What ar you doing Sir?' he asked")
        time.sleep(2)
        type("'I'm one of the support teams. I got the call to say this freezer was messing up so I was sent to fix it' you reply.")
        time.sleep(2)
        type("'I had no idea it was broken. I'll leave you to it!' He left you and you went back to your laptop")
        time.sleep(2)
        type("Another question was on screen:")
        time.sleep(2)
        type("What does XOR stand for?")
        answer5 = input("")
        if answer5.lower() != "exclusive or":
            type("Your laptop suddenly shuts down")
            time.sleep(2)
            type("'OI! WHAT DO YOU THINK YOU'RE DOING?' shouted a voice")
            time.sleep(2)
            type("Before you could even look up, you were shot in the back with a taser")
            time.sleep(2)
            Death()

        elif answer5.lower() == "exclusive or":
            type("Once again, the laptop accepted and answer and you waited")
            time.sleep(2)
            type("Your laptop suddenly turned black and then lights back up")
            time.sleep(2)
            type("On screen is another question. Your code had more flaws than you thought")
            time.sleep(2)
            type("What is the order you must complete Boolean Algebraic Equations (Insert a , inbetween each one)")
            answer6 = input("")
            if answer6.lower() != "brackets, not, and, or":
                type("Your laptop suddenly shuts down")
                time.sleep(2)
                type("'OI! WHAT DO YOU THINK YOU'RE DOING?' shouted a voice")
                time.sleep(2)
                type("Before you could even look up, you were shot in the back with a taser")
                time.sleep(2)
                Death()

            elif answer6.lower() == "brackets, not, and, or":
                type("Your laptop accepted the answer")
                time.sleep(2)
                type("This seemed to be the last question as suddenly the freezer stopped making any sort of sound")
                time.sleep(2)
                type("You quickly pack up the laptop and leave...")

    current_room = third_room

    type("Yet another memory was filling your brain...\n")

    current_room.get_details()

    type("Why on earth do they want this memory?")
    time.sleep(2)
    type("Sitting at your desk, you plugged all the cables, inserted the RAM and placed the AMTel CPU in the socket")
    time.sleep(2)
    type("Upon attempting to boot it, you realise what was wrong")
    time.sleep(2)
    type("Some of its Half Adders were not functioning correctly")
    time.sleep(2)
    type("'How do people break these things?' you think to yourself")
    time.sleep(2)
    type("You try to remember what a Half Adder ...")
    time.sleep(2)
    type("You remember it has a AND Gate... but what is the other one?
    time.sleep(2)
    type("What is the other Logic Gate used to complete the Half Adder? (Just type the Logic Gate)")
    answer7 = input("")
    if answer7.lower() != "xor":
         type("You attempt to fix it but fail...")
         time.sleep(2)
         type("Suddenly your door opens. Your boss is standing there")
         time.sleep(2)
         type("'You need to leave. Now.' she says")
         time.sleep(2)
         type("Before you could say anything, she continues her sentence:")
         time.sleep(2)
         type("You have been found guilty of treason by an internal investigation and if you do not leave you will be sentenced to death")
         time.sleep(2)
         type("Seeing no hope, you stand up and leave...")
         Death()

    elif answer7.lower() == "xor":
        type("You attempt to fix it and succeed")
        time.sleep(2)
        type("Looking at the test paper, you remember why you didn't do it before")
        time.sleep(2)
        type("A paper on the Classification of Programming Languages and Translators...")
        time.sleep(2)
        type("Your least favourite section of Computer Science...")
        time.sleep(2)
        type("You realise that you need this paper finished now")
        time.sleep(2)
        type("'Its only a few questions.' you think to yourself")
        time.sleep(2)
        type("You look at the first question:")
        time.sleep(2)
        type("What is an example of a Second Generation programming Language?")
        answer8 = input("")
        if answer8.lower() != "assembly code":
            type("Suddenly your door opens. Your boss is standing there")
            time.sleep(2)
            type("'You need to leave. Now.' she says")
            time.sleep(2)
            type("Before you could say anything, she continues her sentence:")
            time.sleep(2)
            type("You have been found guilty of treason by an internal investigation and if you do not leave you will be sentenced to death")
            time.sleep(2)
            type("Seeing no hope, you stand up and leave...")
            Death()

        elif answer8.lower() == "assembly code":
            type("One question down...")
            time.sleep(2)
            type("Next question:")
            time.sleep(2)
            type("True or False? Assembly Code is hardware dependent")
            answer9 = input("")
            if answer9.lower() != "true":
                type("Suddenly your door opens. Your boss is standing there")
                time.sleep(2)
                type("'You need to leave. Now.' she says")
                time.sleep(2)
                type("Before you could say anything, she continues her sentence:")
                time.sleep(2)
                type("You have been found guilty of treason by an internal investigation and if you do not leave you will be sentenced to death")
                time.sleep(2)
                type("Seeing no hope, you stand up and leave...")
                Death()

            elif answer9.lower() == "true":
                type("Obviously that's true! It can run faster and takes less space because it is hardware dependent!")
                time.sleep(2)
                type("Next question:")
                time.sleep(2)
                type("What are the two operation codes that are in Machine Code?")
                answer10 = input("")
                if answer10.lower() != "opcode and operand" or "opcode operand" or "opcode, operand" or "operand, opcode" or "operand opcode" or "operand and opcode":
                    type("Suddenly your door opens. Your boss is standing there")
                    time.sleep(2)
                    type("'You need to leave. Now.' she says")
                    time.sleep(2)
                    type("Before you could say anything, she continues her sentence:")
                    time.sleep(2)
                    type("You have been found guilty of treason by an internal investigation and if you do not leave you will be sentenced to death")
                    time.sleep(2)
                    type("Seeing no hope, you stand up and leave...")
                    Death()

                elif answer10.lower() == "opcode and operand" or "opcode operand" or "opcode, operand" or "operand, opcode" or "operand opcode" or "operand and opcode":
                    type("Almost there...")
                    time.sleep(2)
                    type("Just another couple questions:")
                    time.sleep(2)
                    type("True or False? Another name of Imperative Language is Procedural Language")
                    answer11 = input("")
                    if answer11.lower() != "true":
                        type("Suddenly your door opens. Your boss is standing there")
                        time.sleep(2)
                        type("'You need to leave. Now.' she says")
                        time.sleep(2)
                        type("Before you could say anything, she continues her sentence:")
                        time.sleep(2)
                        type("You have been found guilty of treason by an internal investigation and if you do not leave you will be sentenced to death")
                        time.sleep(2)
                        type("Seeing no hope, you stand up and leave...")
                        Death()

                    elif answer11.lower() == "true":
                        type("'Obvious that one! It works by typing a list of instructions which are known as procedures' you think to yourself")
                        time.sleep(2)
                        type("Next one:")
                        time.sleep(2)
                        type("Does an assembler translate assembly code into machine code before it can be executed? Yes or No?")
                        answer12 = input("")
                        if answer12.lower() != "yes":
                            type("Suddenly your door opens. Your boss is standing there")
                            time.sleep(2)
                            type("'You need to leave. Now.' she says")
                            time.sleep(2)
                            type("Before you could say anything, she continues her sentence:")
                            time.sleep(2)
                            type("You have been found guilty of treason by an internal investigation and if you do not leave you will be sentenced to death")
                            time.sleep(2)
                            type("Seeing no hope, you stand up and leave...")
                            Death()

                        elif answer12.lower() == "yes":
                            type("Right then. Nearly finished")
                            time.sleep(2)
                            type("So as you already know that SQL is a type of declarative language...")
                            time.sleep(2)
                            type("And that Bytecode is an instruction set that can be executed using a virtual machine...")
                            time.sleep(2)
                            type("Last Question:")
                            time.sleep(2)
                            type("If the input of an assembler is called the Source Code, what is the output called?")
                            answer13 = input("")
                            if answer13.lower() != "object code":
                                type("Suddenly your door opens. Your boss is standing there")
                                time.sleep(2)
                                type("'You need to leave. Now.' she says")
                                time.sleep(2)
                                type("Before you could say anything, she continues her sentence:")
                                time.sleep(2)
                                type("You have been found guilty of treason by an internal investigation and if you do not leave you will be sentenced to death")
                                time.sleep(2)
                                type("Seeing no hope, you stand up and leave...")
                                Death()

                            elif answer13.lower == "object code":
                                type("The paper is finished")
                                time.sleep(2)
                                type("'That wasn't so bad' you think to yourself")
                                time.sleep(2)
                                type("You stand up and go to leave...")
                                time.sleep(2)

    type("'He is attempting to resist!' you hear a voice shout")
    time.sleep(2)
    type("'Find that memory now!' shouted a woman")
    time.sleep(2)
    type("'Stop resisting! Its the only way to help you!' you hear the woman shout")
    time.sleep(2)
    type("You concentrate and let the memories flow...")

    current_room = forth_room
        

##while dead == True:
##    Menu()
    
