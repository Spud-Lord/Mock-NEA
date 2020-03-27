#Jake Eaton
#Menu

import time
from typing import type, type2
from main_game import Main_Game
from view_leaderboard import View_LB
from os import system, name

def clear():
    if name =='nt':                                                                 #Defines the clear command for the Terminal
        _ = system('cls')


type("Welcome\n")
time.sleep(2)
type("Welcome to the only Text Adventure you will ever need to play in order to learn!\n")
time.sleep(2)
type("This Text Adventure covers the AQA A-level Computer Science Topic 4.6\n")
time.sleep(2)
type("Please remember that this is still in Beta and may never have a full 1.0 release\n")
time.sleep(2)
type("All releases and the source code can be found on Github using the link: https://github.com/Spud-Lord/Mock-NEA\n")
time.sleep(2)
type("To view the releases, just click on the releases tab on the Github Page\n")
time.sleep(2)
type("So let us begin!")
time.sleep(2)

#Log_In()

type("Now then...")
time.sleep(2)
def Main_Menu():
    type("What do you want to do? Just type in the number of the option you want!")
    time.sleep(2)
    menu = input("""
[1] - Start Game!
[2] - View Leaderboard
[3] - Exit Game

""")

    if menu == "1":
        clear()
        Main_Game()

    elif menu == "2":
        View_LB()

    elif menu == "3":
        exit()

    else:
        type("Please type in one of the numbers above...\n")
        Main_Menu()
        
Main_Menu()
