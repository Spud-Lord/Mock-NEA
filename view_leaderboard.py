#Jake Eaton
#View Leaderboard

import csv

def View_LB():
    with open('Leaderboard.csv', 'r', newline='') as file:
        score_list = list(csv.reader(file))
        for row in score_list:
            print(row)
