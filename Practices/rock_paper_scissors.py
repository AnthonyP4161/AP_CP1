#AP 1st Period, Rock Paper Scissors
import random
player_score = 0
computer_score = 0
while True:
    computer_choice = random.randint(1,3)
    print("Welcome to rock paper scissors")
    choice = input("Enter rock, paper, or scissors, or exit to leave: ").lower().strip()
    if choice == "rock":
        if computer_choice == 1:
            print("Computer chose rock")
            print("You tied!")
        elif computer_choice == 2:
            print("Computer chose paper")
            print("You won!")
            player_score += 1
        else:
            print("Computer chose scissors")
            print("You lost!")
            computer_score += 1
    elif choice =="paper":
        if computer_choice == 2:
            print("Computer chose paper")
            print("You tied!")
        elif computer_choice == 1:
            print("Computer chose rock")
            print("You won!")
            player_score += 1
        else:
            print("Computer chose scissors")
            print("You lost!")
            computer_score += 1
    elif choice == "scissors":
        if computer_choice == 3:
            print("Computer chose scissors")
            print("You tied!")
        elif computer_choice == 2:
            print("Computer chose paper")
            print("You won!")
            player_score += 1
        else:
            print("Computer chose rock")
            print("You lost!")
    elif choice == "exit":
        break
    else:
        print("Please enter something valid")
    if player_score >= 3:
        print(f"You won, your score was {player_score} and the computers was {computer_score}")
        break
    elif computer_score >=3:
        print(f"You lost, your score was {player_score} and the computers was {computer_score}")
        break
