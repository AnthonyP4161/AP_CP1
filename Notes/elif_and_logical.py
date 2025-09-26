#AP, 1st Period, Elif and logical operators notes

grade = 100

if grade > 100:
    print("You did extra credit..... why?")

elif grade > 92:
    print("You got an A")

else:
    print("You didn't get an A or extra credit so you should just give up")

username = "bob"
password = "67"
user = input("Enter your username: ")
pword = input("Enter your password: ")

if user == username and password == pword:
    print("Welcome Bob")
elif user == username:
    print("Incorrect password")
else:
    print("Incorrect info")