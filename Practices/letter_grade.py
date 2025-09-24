#AP, 1st period, What is my grade

grade = float(input("What is your grade percentage(EX. 67): "))

if grade>=92:
    letter_grade="A"
elif grade>=90:
    letter_grade="A-"
elif grade>=88:
    letter_grade="B+"
elif grade>=82:
    letter_grade="B"
elif grade>=80:
    letter_grade="B-"
elif grade>=78:
    letter_grade="C+"
elif grade>=72:
    letter_grade="C"
elif grade>=70:
    letter_grade="C-"
elif grade>=68:
    letter_grade="D+"
elif grade>=62:
    letter_grade="D"
elif grade>=60:
    letter_grade="D-"
else:
    letter_grade="F"

print(f"Your grade is a {grade}%, which is a {letter_grade}")