#AP 1st Period, Idiot Proof Practice

#gets full name
first_name = input("What is your first name: ").capitalize().strip()
last_name = input("What is your last name: ").capitalize().strip()
full_name = first_name + " " + last_name

#gets number and formats it
def number_check():
    phone_number = input("What is your phone number, please enter as one whole number EX 1234567890: ")

    #checks if number is only numbers and ten digits
    if phone_number.isdigit() == True and len(phone_number) == 10:
        first = "("+phone_number[:3]+")"
        second = phone_number[3:6]
        third = phone_number[6:]
        phone_number = first + " " + second + " " + third
        return phone_number
    else:
        print("Invalid, try again")
        phone_number = number_check()
        return phone_number

#runs number check and gets output
phone_number = number_check()

#get gpa and format it
gpa = float(input("What is your gpa: "))
gpa = round(gpa,1)

#print output
print(full_name)
print(phone_number)
print(gpa,"gpa")