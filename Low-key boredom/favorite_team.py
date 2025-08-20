#Favorite F1 Team
def quiz():
    team = input("What is your favorite F1 team, enter help for a list of all teams: ")
    if team == "help":
        print("")

def watches_check():
    watches = input("ENTER YES OR NO, NOTHING ELSE. Do you watch F1 often:")
    if watches == "yes":
        quiz()
    elif watches == "no":
        print("Okey dokey, bye bye!")
    else:
        print("you sold, enter something valid")
        watches_check()
watches_check()