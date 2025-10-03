#AP 1st Period, Rock Paper Scissors
import random
while True:
    print("Welcome to rock paper scissors")
    choice = ("Enter rock, paper, or scissors")
    if choice != "rock" or "paper" or "scissors":
        print("Please choose a valid input")
        continue
    computer_choice = random.randint(1,3)
    if computer_choice==1:
        computer_choice="rock"
    elif computer_choice==2:
        computer_choice="paper"
    else:
        computer_choice="scissors"
