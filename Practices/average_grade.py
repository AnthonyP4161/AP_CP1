#AP 1st period, Average Grade

#welcomes user
print("Welcome to the grade calculator. Please input your grades as numbers (ex. 84.54)")

#gets the number grade for all classes
class1 = float(input("What is your grade in your first class: "))
class2 = float(input("What is your grade in your next class: "))
class3 = float(input("What is your grade in your next class: "))
class4 = float(input("What is your grade in your next class: "))
class5 = float(input("What is your grade in your next class: "))
class6 = float(input("What is your grade in your next class: "))
class7 = float(input("What is your grade in your final class: "))

#calculates average number grade
total = class1 + class2 + class3 + class4 + class5 + class6 + class7
grade = total/7
grade = round(grade, 2)

#calculates letter grade and gpa
if grade >= 94:
    letter = "A"
    gpa = 4.0
elif grade >= 90:
    letter = "A-"
    gpa = 3.7
elif grade >= 87:
    letter ="B+"
    gpa = 3.3
elif grade >= 83:
    letter = "B"
    gpa = 3.0
elif grade >= 80:
    letter = "B-"
    gpa = 2.7
elif grade >= 77:
    letter = "C+"
    gpa = 2.3
elif grade >= 73:
    letter = "C"
    gpa = 2.0
elif grade >= 70:
    letter = "C-"
    gpa = 1.7
elif grade >= 67:
    letter = "D+"
    gpa = 1.3
elif grade >= 60:
    letter = "D"
    gpa = 1.0
else:
    letter = "F"
    gpa = 0.0

#gives the info to the user
print("You're average grade is", grade,"which is a(n)", letter,"and your GPA is",gpa)