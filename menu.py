#Jake Eaton
#Menu

import time
from main_game import Main_Game                                                     #Imports time, system and name Modules
from view_leaderboard import View_LB                                                #Imports defined code with the names print, print 2, Main_Game and View_LB
from os import system, name

def clear():
    if name =='nt':                                                                 #Defines the clear command for the Terminal
        _ = system('cls')

print("Welcome\n")
time.sleep(2)
print("Welcome to the only Text Adventure you will ever need to play in order to learn!\n")
time.sleep(2)
print("This Text Adventure covers the AQA A-level Computer Science Topic 4.6\n")
time.sleep(2)
print("Please remember that this is still in Beta and may never have a full 1.0 release\n")
time.sleep(2)
print("All releases and the source code can be found on Github using the link: https://github.com/Spud-Lord/Mock-NEA\n")
time.sleep(2)
print("To view the releases, just click on the releases tab on the Github Page\n")
time.sleep(2)
print("You can read the book now!")
time.sleep(2)
print("Read it as it is published at https://www.wattpad.com/story/245646734-the-formula-front-war-part-of-the-world-space")
time.sleep(2)
print("So let us begin!\n")
time.sleep(2)


print("Now then...\n")
time.sleep(2)
print("What do you want to do? Just type in the number of the option you want!")
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
        print("Please print in one of the numbers above...\n")
        Main_Menu()                                                                 #Loops back round if the user doesn't enter one of the numbers

Main_Menu()                                                                         #Allows the Menu to loop
