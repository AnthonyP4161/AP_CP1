#AP 1st Period, Shopping List Manager

print("This is to make a shopping list. Type what you want to add, print to view the list, and exit to be done")
shopping_list = []

while True:
    action = input("What do you want to add to your list: ")
    if action == "print":
        print("Your list:")
        for item in shopping_list:
            print(item)
    elif action == "exit":
        break
    else:
        shopping_list.append(action)