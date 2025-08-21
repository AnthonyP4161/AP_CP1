#Favorite F1 Team
def quiz():
    team = input("What is your favorite F1 team, enter help for a list of all teams: ").strip().lower()
    if team == "Help":
        print("The current F1 teams, as of 2025, are as follows: Alpine\nMercedes\nRedBull Racing\nFerrari\nWilliams\nAston Martin\nKick Sauber\nRacing Bulls\nHaas\nMcLaren.")
        quiz()

    elif team == "alpine":
        print("The current racers for Alpine are Pierre Gasly and Franco Colapinto.")

    elif team == "mercedes":
        print("The current racers for Mercedes are Geroge Russell and Kimi Antonelli.")

    elif team == "redbull racing":
        print("The current racers for RedBull Racing are Max Verstappen and Yuki Tsunoda.")

    elif team == "ferrari":
        print("The current racers for Ferrari are Charles Leclerc and Lewis Hamilton.")

    elif team == "williams":
        print("The current racers for Williams are Alexander Albon and Carlos Sainz.")

    elif team == "aston martin":
        print("The current racers for Aston Martin are Lance Stroll and Fernando Alonso.")

    elif team == "kick sauber":
        print("The current racers for Kick Sauber are Nico Hulkenburg and Gabriel Bortoleto.")

    elif team == "racing bulls":
        print("The current racers for Racing Bulls are Liam Lawson and Isack Hadjar.")

    elif team == "haas":
        print("The current racers for Haas are Esteban Ocon and Oliver Bearman.")

    elif team == "mclaren":
        print("The current racers for McLaren are Oscar Piastri and Lando Norris.")

    else:
        print("Woah, please enter a valid team my guy.")
        quiz()

def watchesCheck():
    watches = input("Do you watch F1 often(yes or no): ").strip().lower()
    if watches == "yes":
        quiz()
    elif watches == "no":
        print("Okey dokey, bye bye!")
    else:
        print("you sold, enter something valid")
        watchesCheck()
watchesCheck()