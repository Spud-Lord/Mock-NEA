#Jake Eaton

def Main_Game():
    from room import Room
    from introduction import Intro
    from death import Death                                                         #Imports Room, Intro, Death, Victory, type, type2 and Main_Menu Definitions
    from victory import Victory
    from typing import type, type2
    from menu import Main_Menu
    import csv                                                                      #Imports CSV, Time, OS, Sys and Pygame Modules
    import time
    import os
    import sys
    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"                               #Hides Welcome to Pygame Message
    from pygame import mixer

    Intro()                                                                         #Calls Introduction Definition

    first_room = Room("The old ruins of an ancient Castle")
    first_room.set_description("You recognise the old castle as the place you lost your friend. She fell from the tallest tower. The castle has remained closed ever since. But wasn't it destroyed recently?")

    second_room = Room("The frozen isle of a Supermarket")
    second_room.set_description("It has been nearly twenty years since you were here. Last time you were here, you messed with the temperature controls and caused all the products to defrost. You were banned from entering. But why do they want to know about this?\n")
    #This set defines each of the different rooms used in the game
    third_room = Room("An office filled with computers")
    third_room.set_description("Your first job. After succeeding at University you quickly rose the ranks to become the leader of a tech team for the GCHQ. You recognise the motherboard on your desk. You also notice a test paper you were meant to fill in weeks ago. Last time you wer here, you had to test the board and complete the test... should you do the same?\n")

    forth_room = Room("A riverside resturant")
    forth_room.set_description("One of the darkest days of your life. It was here where you were betrayed. You were just enjoying a friendly meal until you started to lose your breath. Poisoned by your trusted ally... is she the key to all this?\n")

    fifth_room = Room("The Artemis")
    fifth_room.set_description("You don't remember this... is this even your memory?")

    mixer.init()
    mixer.music.load("Battle.Of.The.Heroes.mp3")                                    #Plays mp3 file
    mixer.music.play(10)

    current_room = first_room                                                       #Sets the current room as the first room
    inventory = []

    dead = False                                                                    #Sets dead state to be False

    while dead == False:
        score = 0                                                                   #Sets score to 0

        type("You suddenly find youself focusing on one memory...\n")

        time.sleep(2)

        current_room.get_details()                                                  #Gets details of the current room

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
        answer1 = input("")                                                         #Takes User answer in a input
        if answer1.lower() != "a":                                                  #If the user is wrong, this indented code runs - This is the same throughout the whole game
            type("'Incorrect! The correct answer is a!'")
            time.sleep(2)
            type("The guard raises his sword and cuts you down where you stand...\n")
            time.sleep(2)
            type("Please enter your name for the Leaderboard")
            name = input("")
            with open('Leaderboard.csv', 'a', newline='') as file:
                writer = csv.writer(file)                                           #Appends the Leaderboard.csv File with the new Score
                writer.writerow((name, score))                                      #Appends it using the variables name and score
            Death()                                                                 #Calls and runs Death Definition
            dead = True                                                             #Sets dead state to true

        elif answer1.lower() == "a":                                                #If the user is correct, this code runs
            score = score + 1
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
                type("Please enter your name for the Leaderboard")
                name = input("")
                with open('Leaderboard.csv', 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow((username, score))
                Death()
                dead = True

            elif answer2.lower() == "false":
                score = score + 1
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
                    type("Please enter your name for the Leaderboard")
                    name = input("")
                    with open('Leaderboard.csv', 'a', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow((username, score))
                    time.sleep(2)
                    Death()
                    dead = True

                elif answer3.lower() == "c":
                    score = score + 1
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
                    type("Lost... you stood up on the wall and prepared to jump...\n")
                    time.sleep(2)

        current_room = second_room                                                          #Sets current room to be the second room

        type("You suddenly find youself focusing on another memory...\n")
        time.sleep(2)

        current_room.get_details()                                                          #Gets details of the current room

        time.sleep(4)
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
        type("""A= 1
B = 0
C = 1
D = 1
E = 0""")                                                                                   #The triple speech marks allow the type to go over multiple lines in list form
        answer4 = input("")
        if answer4 != "1":
            type("Your laptop suddenly shuts down")
            time.sleep(2)
            type("'OI! WHAT DO YOU THINK YOU'RE DOING?' shouted a voice")
            time.sleep(2)
            type("Before you could even look up, you were shot in the back with a taser")
            time.sleep(2)
            type("Please enter your name for the Leaderboard")
            name = input("")
            with open('Leaderboard.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow((username, score))
            time.sleep(2)
            Death()
            dead = True

        elif answer4 == "1":
            score = score + 1
            type("Your laptop accepted the answer and you waited for it to continue")
            time.sleep(2)
            type("One of the shopkeepers approached you...")
            time.sleep(2)
            type("'What are you doing Sir?' he asked")
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
                type("Please enter your name for the Leaderboard")
                name = input("")
                with open('Leaderboard.csv', 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow((username, score))
                time.sleep(2)
                Death()
                dead = True

            elif answer5.lower() == "exclusive or":
                score = score + 1
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
                    type("Please enter your name for the Leaderboard")
                    name = input("")
                    with open('Leaderboard.csv', 'a', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow((username, score))
                    time.sleep(2)
                    Death()
                    dead = True

                elif answer6.lower() == "brackets, not, and, or":
                    score = score + 1
                    type("Your laptop accepted the answer")
                    time.sleep(2)
                    type("This seemed to be the last question as suddenly the freezer stopped making any sort of sound")
                    time.sleep(2)
                    type("You quickly pack up the laptop and leave...\n")

        current_room = third_room
        time.sleep(2)

        type("Yet another memory was filling your brain...\n")

        time.sleep(4)
        current_room.get_details()

        type("Why on earth do they want this memory?")
        time.sleep(2)
        type("Sitting at your desk, you plugged all the cables, inserted the RAM and placed the AMTel CPU in the socket")
        time.sleep(2)
        type("Upon attempting to boot it, you remember what was wrong")
        time.sleep(2)
        type("Some of its Half Adders were not functioning correctly")
        time.sleep(2)
        type("'How do people break these things?' you think to yourself")
        time.sleep(2)
        type("You try to remember what makes a Half Adder ...")
        time.sleep(2)
        type("You remember it has a AND Gate... but what is the other one?")
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
             type("'You have been found guilty of treason by an internal investigation and if you do not leave you will be sentenced to death'")
             time.sleep(2)
             type("Seeing no hope, you stand up and leave...")
             type("Please enter your name for the Leaderboard")
             name = input("")
             with open('Leaderboard.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow((username, score))
             time.sleep(2)
             Death()
             dead = True

        elif answer7.lower() == "xor":
            score = score + 1
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
                type("'You have been found guilty of treason by an internal investigation and if you do not leave you will be sentenced to death'")
                time.sleep(2)
                type("Seeing no hope, you stand up and leave...")
                type("Please enter your name for the Leaderboard")
                name = input("")
                with open('Leaderboard.csv', 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow((username, score))
                time.sleep(2)
                Death()
                dead = True

            elif answer8.lower() == "assembly code":
                score = score + 1
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
                    type("'You have been found guilty of treason by an internal investigation and if you do not leave you will be sentenced to death'")
                    time.sleep(2)
                    type("Seeing no hope, you stand up and leave...")
                    type("Please enter your name for the Leaderboard")
                    name = input("")
                    with open('Leaderboard.csv', 'a', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow((username, score))
                    time.sleep(2)
                    Death()
                    dead = True

                elif answer9.lower() == "true":
                    type("Obviously that's true! It can run faster and takes less space because it is hardware dependent!")
                    time.sleep(2)
                    type("Next question:")
                    time.sleep(2)
                    type("What are the two operation codes that are in Machine Code?")
                    answer10 = input("")
                    if answer10.lower() != "opcode and operand":
                        score = score + 1
                        type("Suddenly your door opens. Your boss is standing there")
                        time.sleep(2)
                        type("'You need to leave. Now.' she says")
                        time.sleep(2)
                        type("Before you could say anything, she continues her sentence:")
                        time.sleep(2)
                        type("'You have been found guilty of treason by an internal investigation and if you do not leave you will be sentenced to death'")
                        time.sleep(2)
                        type("Seeing no hope, you stand up and leave...")
                        type("Please enter your name for the Leaderboard")
                        name = input("")
                        with open('Leaderboard.csv', 'a', newline='') as file:
                            writer = csv.writer(file)
                            writer.writerow((username, score))
                        time.sleep(2)
                        Death()
                        dead = True

                    elif answer10.lower() == "opcode and operand":
                        type("Almost there...")
                        time.sleep(2)
                        type("Just another couple questions:")
                        time.sleep(2)
                        type("True or False? Another name for Imperative Language is Procedural Language")
                        answer11 = input("")
                        if answer11.lower() != "true":
                            type("Suddenly your door opens. Your boss is standing there")
                            time.sleep(2)
                            type("'You need to leave. Now.' she says")
                            time.sleep(2)
                            type("Before you could say anything, she continues her sentence:")
                            time.sleep(2)
                            type("'You have been found guilty of treason by an internal investigation and if you do not leave you will be sentenced to death'")
                            time.sleep(2)
                            type("Seeing no hope, you stand up and leave...")
                            type("Please enter your name for the Leaderboard")
                            name = input("")
                            with open('Leaderboard.csv', 'a', newline='') as file:
                                writer = csv.writer(file)
                                writer.writerow((username, score))
                            time.sleep(2)
                            Death()
                            dead = True

                        elif answer11.lower() == "true":
                            score = score + 1
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
                                type("'You have been found guilty of treason by an internal investigation and if you do not leave you will be sentenced to death'")
                                time.sleep(2)
                                type("Seeing no hope, you stand up and leave...")
                                type("Please enter your name for the Leaderboard")
                                name = input("")
                                with open('Leaderboard.csv', 'a', newline='') as file:
                                    writer = csv.writer(file)
                                    writer.writerow((username, score))
                                time.sleep(2)
                                Death()
                                dead = True

                            elif answer12.lower() == "yes":
                                score = score + 1
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
                                    type("'You have been found guilty of treason by an internal investigation and if you do not leave you will be sentenced to death'")
                                    time.sleep(2)
                                    type("Seeing no hope, you stand up and leave...")
                                    type("Please enter your name for the Leaderboard")
                                    name = input("")
                                    with open('Leaderboard.csv', 'a', newline='') as file:
                                        writer = csv.writer(file)
                                        writer.writerow((username, score))
                                    time.sleep(2)
                                    Death()
                                    dead = True

                                elif answer13.lower() == "object code":
                                    score = score + 1
                                    type("The paper is finished")
                                    time.sleep(2)
                                    type("'That wasn't so bad' you think to yourself")
                                    time.sleep(2)
                                    type("You stand up and go to leave...\n")
                                    time.sleep(2)

        type("'He is attempting to resist!' you hear a voice shout")
        time.sleep(2)
        type("'Find that memory now!' shouted a woman")
        time.sleep(2)
        type("'Stop resisting! Its the only way to help you!' you hear the woman shout")
        time.sleep(2)
        type("You concentrate and let the memories flow...\n")

        current_room = forth_room
        time.sleep(2)

        type("You prayed this was the last memory...\n")

        time.sleep(4)
        current_room.get_details()

        time.sleep(2)
        type("No")
        time.sleep(2)
        type("Why?")
        time.sleep(2)
        type("Why would they choose this memory?")
        time.sleep(2)
        type("You look at the person sitting opposite you and recognise her")
        time.sleep(2)
        type("Eve. The woman who betrayed your heart")
        time.sleep(2)
        type("You wanted nothing more than to lunge at her and kill her...")
        time.sleep(2)
        type("But you knew you had to let the memory flow")
        time.sleep(2)
        type("You can't change the past...")
        time.sleep(2)
        type("One of the waiters walk up to you")
        time.sleep(2)
        type("'Excuse me Sir, we appear to be having trouble with our card machine.' the waiter said")
        time.sleep(2)
        type("'I don't think you will be able to pay by card' the waiter continued")
        time.sleep(2)
        type("You take the machine and use your screwdrivers in your pocket to open the back")
        time.sleep(2)
        type("There was a puzzle...")
        time.sleep(2)
        type("'Well this is confusing.' you say. You show Eve and she smiles")
        time.sleep(2)
        type("'Go on! You can solve it!' she says")
        time.sleep(2)
        type("You look at the puzzle again:")
        time.sleep(2)
        type("The Output (Q) is 1")
        type("Work out what the input D has to be for the output to be True")
        type("Q = (NOT ( C OR (A AND B))) AND (XOR ( F ( D NAND E)))")
        type("""A = 1
B = 0
C = 0
E = 1
F = 1
Q = 1""")
        answer14 = input("")
        if answer14 != "1":
            type("You attempt to fix the puzzle...")
            time.sleep(2)
            type("Your input failed...")
            time.sleep(2)
            type("With no cash to pay for it, you are dragged away and placed in the local prison to pay for your crime")
            type("Please enter your name for the Leaderboard")
            name = input("")
            with open('Leaderboard.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow((username, score))
            time.sleep(2)
            Death()
            dead = True

        elif answer14 == "1":
            score = score + 1
            type("You attempt to fix the puzzle...")
            time.sleep(2)
            type("It succeeds and the card machine glows signifying it is now on")
            time.sleep(2)
            type("Handing the card machine back, the waiter thanks you and walks away")
            time.sleep(2)
            type("'Well done!' Eve says winking at you")
            time.sleep(2)
            type("'Have a drink.' she says pushing your wine towards you")
            time.sleep(2)
            type("You thank her and take a sip")
            time.sleep(2)
            type("You throat suddenly burns and you clutch at your chest")
            time.sleep(2)
            type("Eve begins to laugh as you stand up and attempt to walk out")
            time.sleep(2)
            type("Falling over on the way, you just make out the waiter holding a gun at you")
            time.sleep(2)
            type("Just before you close your eyes, you just make out everyone else in the resturant pointing a gun at you as well")
            time.sleep(2)
            type("You close your eyes...\n")

        current_room = fifth_room
        time.sleep(2)

        type("'I found it!' shouted a voice")
        time.sleep(2)
        type("'Focus on that memory!' replied a woman")
        time.sleep(2)
        type("'Last memory...' you think to yourself. You don't think you can survive much longer...\n")
        time.sleep(2)

        current_room.get_details()

        time.sleep(4)
        type("Breathing calmly, you lean your head back to not see what is going on")
        time.sleep(2)
        type("Held tightly against a weird looking machine, you suddenly find youself being rotated backwards so you are led down")
        time.sleep(2)
        type("'Test Subject 66 is ready for Preliminary Tests' you hear a voice call out")
        time.sleep(2)
        type("'Preparing injections' another voice says")
        time.sleep(2)
        type("You suddenly realise that you are topless and you hear the machine whirring")
        time.sleep(2)
        type("You close your eyes and breath gently")
        time.sleep(2)
        type("'Injecting Subject' said one of the voices")
        time.sleep(2)
        type("You may have had injections before but these were painful")
        time.sleep(2)
        type("The pain only lasted a few seconds")
        time.sleep(2)
        type("'Test Subject 66 accepted primary injections. Preparing secondary.' said the first voice")
        time.sleep(2)
        type("'Its not over?' you think to yourself as the machine whirred again")
        time.sleep(2)
        type("'Injecting Subject.' said the second voice")
        time.sleep(2)
        type("Before you could brace youself, you suddenly felt a burning sensation over your entire body")
        time.sleep(2)
        type("You begin to yell out in pain")
        time.sleep(2)
        type("'Secondary Injections complete!' cried the first voice")
        time.sleep(2)
        type("'Why am I still burining alive?' you thought to yourself")
        time.sleep(2)
        type("It took at least 30 seconds for the burning to stop but it felt like an eternity")
        time.sleep(2)
        type("When it finally did stop, one of the people asked you a question:")
        time.sleep(2)
        type("Is Machine Code an example of a Low-Level Programming Language? Yes or No?")
        answer15 = input("")
        if answer15.lower() != "yes":
            type("'Test Subject 66 failed. Begin Termination Sequence!' shouted the voice")
            time.sleep(2)
            type("'Wait!' you shout. But it is no use")
            time.sleep(2)
            type("Before you could do or say anything else, you are injected with another liquid and you instantly black out and stop breathing")
            type("Please enter your name for the Leaderboard")
            name = input("")
            with open('Leaderboard.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow((username, score))
            time.sleep(2)
            Death()
            dead = True

        elif answer15.lower() == "yes":
            score = score + 1
            type("'Test Subject 66 completed secondary injections.'")
            time.sleep(2)
            type("'What is your name?' one of them asked")
            name = input(">> ")
            type("'My name is "+ name +".'")
            time.sleep(2)
            type("'Just so you know we were just testing your brain activity with that question.' he said")
            time.sleep(2)
            type("'The augmentation was successful. We just have one more injection sequence to run then we can complete other tests'")
            time.sleep(2)
            type("'This last sequence will be painless. Just relax.' continued the person")
            time.sleep(2)
            type("You close your eyes again and wait for the final step to complete...")

        time.sleep(4)
        type("Your eyes fly open and you scream in pain as the neural implant is removed from your neck")
        time.sleep(2)
        type("'"+name+"!' said a woman's voice")
        time.sleep(2)
        type("'Thank you!' the woman said")
        time.sleep(2)
        type("You open your eyes to see the woman you saw earlier")
        time.sleep(2)
        type("'Eve!' you shout. You try to lunge at her")
        time.sleep(2)
        type("Still equipped into the machine though, you breath heavily trying to catch your breath")
        time.sleep(2)
        type("'A deal is a deal. Get me out and remove the memory' you say")
        time.sleep(2)
        type("The woman nods and goes to get something. You wait for her to return")
        time.sleep(2)
        type("When she does return, she has something behind her back")
        time.sleep(2)
        type("'We have identified the scientists who experimented on you in our database through their voices.' she said")
        time.sleep(2)
        type("'We would like to thank you for your cooperation.' the woman said")
        time.sleep(2)
        type("'Why was I on this station in the memory?' you ask")
        time.sleep(2)
        type("'It appears that it was this very station where you became you. As such, we have what we need.' the woman said")
        time.sleep(2)
        type("'It is time for us to help you and remove the memory from your mind.'")
        time.sleep(2)
        type("You await for something to happen...")
        type("Please enter your name for the Leaderboard")
        name = input("")
        with open('Leaderboard.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow((name, score))
        Victory()                                               #Calls and runs the Victory Definition
        dead = True                                             #Sets dead state to true

    while dead == True:                                         #When the dead state is true, this indented code runs
        time.sleep(3)
        mixer.music.stop()                                      #Stops music
        type("Thank you for playing!\n")
        time.sleep(2)
        Main_Menu()                                             #Calls and runs Main_Menu Definition
