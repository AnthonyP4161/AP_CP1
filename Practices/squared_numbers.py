#AP 1st Period, Squard Numbers
#welcome user
print("Welcome to the squared number calculator")
#set up the lists before hand
og_numbers = []
numbers = []
#loop the code
while True:
    #get the input
    number = input("What number would you like to use, type done to be done: ").strip().lower()
    #check the input to make sure its valid and can be exited
    if number == "done":
        break
    elif number.isdigit():
        og_numbers.append(int(number))
        numbers.append(int(number))
    else:
        print("Enter a valid input")
        continue
#get the squard values
squared = list(map(lambda num:num*num,numbers))
#print the original and squared values
length = len(numbers)
for i in range(0,length):
    print(f"Original:{og_numbers[i]}, New:{squared[i]}")