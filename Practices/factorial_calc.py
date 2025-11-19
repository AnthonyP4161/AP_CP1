#AP 1st Period, Factorial Calculator
#welcome the user
print("Welcome to the factorial calculator")
while True:
    choice = int(input("What number would you like the factorial of: "))
    total = 1
    for i in range(1,choice+2):
        print(total*(choice-i))