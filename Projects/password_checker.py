#AP 1st Period, Password Strength Checker
#loop everything
while True:
#get the users password
    #Set a variable of the special characters to check for
    special_char = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    password = input("Please enter a password to set as your password: ")
    score = 0
#Checks if the password is long enough and adds point if it does
    if len(password) >= 8:
       score += 1
#Checks if the password contains an uppercase letter and adds point if it does
    for i in password:
        if i.isupper():
            score += 1
            break
#CHecks if the password contains a number and adds point if it does
    for i in password:
        if i.isnumeric():
            score +=1
            break
#Checks if the password contains a lowercase letter and adds point if it does
    for i in password:
        if i.islower():
            score+=1
            break
#Checks if the password contains a special character and adds point if it does
    for i in password:
        if i in special_char:
            score+=1
            break
#Checks the strength and prints how strong it is
    if score == 5:
        print("5/5 Very strong password")
    elif score == 4:
        print("4/5 Strong password")
    elif score == 3:
        print("3/5 Moderate password")
    elif score > 0:
        print(f"{score}/5 Weak password")
    else:
        print("Terrible password, did you even try?")
