#AP 1st Period, User Sign In
username = "JohnChungus"
password = "MarcusPork"

user_check = input("Please enter your username: ")
password_check = input("Please enter your password: ")
if username == user_check:
    if password == password_check:
        print("Username and password accepted, welcome to the program!")
    else:
        print("Incorrect password")
elif password == password_check:
    print("Incorrect username")
else:
    print("Incorrect username and password")