#Jake Eaton
#Menu

import time
from typing import type, type2
from main_game import Main_Game                                                     #Imports time, system and name Modules
from view_leaderboard import View_LB                                                #Imports defined code with the names type, type 2, Main_Game and View_LB
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


type("Now then...")
time.sleep(2)
type("What do you want to do? Just type in the number of the option you want!")
time.sleep(2)
def Main_Menu():                                                                    #Defines all indented code as Main_Menu
    menu = input("""
[1] - Start Game!
[2] - View Leaderboard  
[3] - Exit Game

""")                                                                                #The triple speech marks allow the Menu to go over multiple lines with only one code

    if menu == "1":
        clear()                                                                     #Calls Clear Definition to clear Terminal Screen
        Main_Game()

    elif menu == "2":
        print("")
        View_LB()                                                                   #Calls View_LB Definition to view leaderboard
        time.sleep(2)
        print("")
        Main_Menu()

    elif menu == "3":
        exit()                                                                      #Exits the game

    else:
        type("Please type in one of the numbers above...\n")
        Main_Menu()                                                                 #Loops back round if the user doesn't enter one of the numbers
        
Main_Menu()                                                                         #Allows the Menu to loop
