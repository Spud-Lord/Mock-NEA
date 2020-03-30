#Jake Eaton
#Type Code

import sys                          #Imports System and Time Modules
import time

def type(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()          #This def will print strings in this way. When type is used instead of print, the program will now know to print each character separately wth a small time gap inbetween
        time.sleep(0.04)
    sys.stdout.write("\n")

def type2(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()          #This def will print strings in this way. When type is used instead of print, the program will now know to print each character separately wth a small time gap inbetween
        time.sleep(0.75)
    sys.stdout.write("\n")
