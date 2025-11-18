#AP 1st Period, Flexible Calculator
def sum(*numbers):
    total = 0
    for i in numbers:
        total += i
    return total
def average(*numbers):
    amount = 0
    total = 0
    for i in numbers:
        total += i
        amount +=1
    return total/amount
def max(*numbers):
    for i in numbers:
        if i > max:
            max = i
        else:
            continue
    return max
def min(*numbers):
    for i in numbers:
        temp=i
        if i < temp:
            max = i
        else:
            continue
    return max
def product(*numbers):
    for i in numbers:
        total = 1
        total *= i

print("Welcome to the felxible calculator")
numbers = []
while True:
    choice = input("Would you like to calculate the sum, the average, the max, the min, or the product: ").strip().lower()
    if choice == "sum":
        while True:
            number = input("What number would you like to add, type done to be done: ").strip().lower()
            if number == "done":
                break
            elif number.isdigit():
                numbers.append(float(number))
            else:
                print("Enter a valid input")
                continue
        print(sum(*numbers))
    elif choice == "average":
        while True:
            number = input("What number would you like to add, type done to be done: ").strip().lower()
            if number == "done":
                break
            elif number.isdigit():
                numbers.append(float(number))
            else:
                print("Enter a valid input")
                continue
        print(average(*numbers))
    elif choice == "max":
        while True:
            number = input("What number would you like to add, type done to be done: ").strip().lower()
            if number == "done":
                break
            elif number.isdigit():
                numbers.append(float(number))
            else:
                print("Enter a valid input")
                continue
        print(max(*numbers))