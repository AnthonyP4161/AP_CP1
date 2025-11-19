#AP 1st Period, Flexible Calculator
def sum(*numbers):
    total = 0
    for i in numbers:
        total += i
    return total
def average(*numbers):
    amount = len(numbers)
    total = 0
    for i in numbers:
        total += i
    return total/amount
def maximum(*numbers):
    max = numbers[1]
    for i in numbers:
        if i > max:
            max = i
        else:
            continue
    return max
def minimum(*numbers):
    min = numbers[1]
    for i in numbers:
        if i < min:
            min = i
        else:
            continue
    return min
def product(*numbers):
    total = 1
    for i in numbers:
        total *= i
    return total

print("Welcome to the felxible calculator")
numbers = []
while True:
    choice = input("Would you like to calculate the sum, the average, the max, the min, or the product, or type quit to be done: ").strip().lower()
    if choice == "sum":
        while True:
            number = input("What number would you like to use, type done to be done: ").strip().lower()
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
            number = input("What number would you like to use, type done to be done: ").strip().lower()
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
            number = input("What number would you like to use, type done to be done: ").strip().lower()
            if number == "done":
                break
            elif number.isdigit():
                numbers.append(float(number))
            else:
                print("Enter a valid input")
                continue
        print(maximum(*numbers))
    elif choice == "min":
        while True:
            number = input("What number would you like to use, type done to be done: ").strip().lower()
            if number == "done":
                break
            elif number.isdigit():
                numbers.append(float(number))
            else:
                print("Enter a valid input")
                continue
        print(minimum(*numbers))
    elif choice == "product":
        while True:
            number = input("What number would you like to use, type done to be done: ").strip().lower()
            if number == "done":
                break
            elif number.isdigit():
                numbers.append(float(number))
            else:
                print("Enter a valid input")
                continue
        print(product(*numbers))
    elif choice == "quit":
        break
    else:
        print("Enter a valid input")
        continue