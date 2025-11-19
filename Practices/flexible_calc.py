#AP 1st Period, Flexible Calculator
#define the function to get sum
def sum(*numbers):
    total = 0
    for i in numbers:
        total += i
    return total
#define the function to get average
def average(*numbers):
    amount = len(numbers)
    total = 0
    for i in numbers:
        total += i
    return total/amount
#define the function to get maximum
def maximum(*numbers):
    max = numbers[1]
    for i in numbers:
        if i > max:
            max = i
        else:
            continue
    return max
#define the function to get minimum
def minimum(*numbers):
    min = numbers[1]
    for i in numbers:
        if i < min:
            min = i
        else:
            continue
    return min
#define the function to get product
def product(*numbers):
    total = 1
    for i in numbers:
        total *= i
    return total
#welcome the user
print("Welcome to the felxible calculator")
#make a list
numbers = []
#loop the code
while True:
    #ask the user what they want to do
    choice = input("Would you like to calculate the sum, the average, the max, the min, or the product, or type quit to be done: ").strip().lower()
    #if choice is sum, use the sum function
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
    #if choice is average, use the average function
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
    #if choice is max, use the max function
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
    #if choice is min, use the min function
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
    #if choice is product, use the product function
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
    #if choice is quit, exit the function
    elif choice == "quit":
        break
    #if choice isn't valid, make them reenter
    else:
        print("Enter a valid input")
        continue#