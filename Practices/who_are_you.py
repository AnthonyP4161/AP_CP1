#AP, 1st Period, Who Are You
import os
def quiz():
    name = input("What is your name: ")
    favcolor = input("What is your favorite color: ")
    age = input("How old are you, just a number please: ")
    print("Hello "+name+", your favorite color is "+favcolor+" and you're "+age+" years old?")
    os.system("cls" if os.name == "nt" else "clear")
    print("RESET")
    quiz()
quiz()