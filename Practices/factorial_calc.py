#AP 1st Period, Factorial Calculator
#define calculator function with num
def calculate(num):
    #define total as 1
    total = 1
    #whie the num is greater than 1
    while num >1:
        #total times the num
        total*=num
        #num minus 1
        num-=1
    #return the total
    return total
#print the instructions for the user
print("Welcome to the factorial calculator")
#have the user input something
num = input("Please input a whole, positive number: ")
#while the input isn't an integer or a negative sign in the input
while type(num) != "int" or "-" in num:
    #have the user input something else
    try:
        num = int(input("Please input a whole, positive number: "))
    except ValueError:
        continue
#make the input an integer
int(num)
#set a variable and make it equal to the function with input
total = calculate(num)
#print the original number and total
print(num,total)