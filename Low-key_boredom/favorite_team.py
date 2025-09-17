#Favorite F1 Team
import os
import time

def quiz():
    team = input("What is your favorite F1 team, enter help for a list of all teams: ").strip().lower()
    if team == "help":
        print("The current F1 teams, as of 2025, are as follows:\nAlpine\nMercedes\nRedBull Racing\nFerrari\nWilliams\nAston Martin\nKick Sauber\nRacing Bulls\nHaas\nMcLaren.")
        quiz()

    elif team == "alpine":
        print("The current racers for Alpine are Pierre Gasly and Franco Colapinto.\n\nHonestly I don't know F1, maybe these guys are cool.")
        quiz()

    elif team == "mercedes":
        print("The current racers for Mercedes are Geroge Russell and Kimi Antonelli.\n\nI'm not informed, but mercedes seems so basic of an answer")
        quiz()

    elif team == "redbull racing":
        print("The current racers for RedBull Racing are Max Verstappen and Yuki Tsunoda.\n\nRedBull was the only right answer, or at least until Max switches teams.\n\nI swear it's not glaze...")
        print("You get a little surprise now.\n")
        time.sleep(3)
        os.system("cls" if os.name == "nt" else "clear")
        time.sleep(1)
        print("Du Du Du Du")
        time.sleep(1.6)
        print("Max Verstappen")
        quiz()

    elif team == "ferrari":
        print("The current racers for Ferrari are Charles Leclerc and Lewis Hamilton.\n\nThis answer is acceptable because Leclerc.")
        justice_for_carlos = input(print("Does Carlos deserve justice, should he return to ferrari? PS, type yes or no")).strip().lower()
        if justice_for_carlos == "yes":
            print("Good job, Charles needs his bud back")
        quiz()

    elif team == "williams":
        print("The current racers for Williams are Alexander Albon and Carlos Sainz.\n\nWhy is the team name a more normal name that the racers names?")
        quiz()

    elif team == "aston martin":
        print("The current racers for Aston Martin are Lance Stroll and Fernando Alonso.\n\nFernando will forever be the best rookie")
        quiz()

    elif team == "kick sauber":
        print("The current racers for Kick Sauber are Nico Hulkenburg and Gabriel Bortoleto.\n\nNico finally got a podium, lets gooooooo.\nI don't know who Nico is, but he finally got one and that's awesome")
        quiz()

    elif team == "racing bulls":
        print("The current racers for Racing Bulls are Liam Lawson and Isack Hadjar.\n\nRedBull has two teams?")
        quiz()

    elif team == "haas":
        print("The current racers for Haas are Esteban Ocon and Oliver Bearman.\n\nNever heard of this team, but Esteban is a cool name")
        quiz()

    elif team == "mclaren":
        print("The current racers for McLaren are Oscar Piastri and Lando Norris.\n\nOscar Piastri is cool, but I don't know why.")
        quiz()
        
    else:
        print("Woah, please enter a valid team my guy.")
        quiz()

def watchesCheck():
    watches = input("Do you want to do da quiz(yes or no): ").strip().lower()
    if watches == "yes":
        quiz()
    elif watches == "no":
        print("Okey dokey, bye bye!")
    else:
        print("you sold, enter something valid")
        watchesCheck()
watchesCheck()