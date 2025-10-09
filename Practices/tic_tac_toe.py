#AP 1st Period, Tic Tac Toe
import random
import os

spot1 = 1
spot2 = 2
spot3 = 3
spot4 = 4
spot5 = 5
spot6 = 6
spot7 = 7
spot8 = 8
spot9 = 9

while True:
    board = f"""{spot1}|{spot2}|{spot3}
-----
{spot4}|{spot5}|{spot6}
-----
{spot7}|{spot8}|{spot9}"""
    print(board)
    choice = int(input("Where would you like to go: "))
    if choice == 1:
        spot1 = "X"
    elif choice == 2:
        spot2 = "X"
    elif choice == 3:
        spot3 = "X"
    elif choice == 4:
        spot4 = "X"
    elif choice == 5:
        spot5 = "X"
    elif choice == 6:
        spot6 = "X"
    elif choice == 7:
        spot7 = "X"
    elif choice == 8:
        spot8 = "X"
    elif choice == 9:
        spot9 = "X"
    os.system("cls" if os.name == "nt" else "clear")