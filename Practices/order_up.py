#AP 1st Period, Order Up
#dictionary for the main courses
main_course = {
    "Burger":5.99,
    "Sandwhich":4.99,
    "Grilled cheese":4.32,
    "Steak":67.67,
    "Eggs":5.49
}
#dictionary for the drinks
drink = {
    "Coke":3.99,
    "Canta":3.99,
    "Sprite":3.99,
    "Pepsi":3.99
}
#dictionary for the side dishes
side_dish = {
    "Mac and cheese":2.99,
    "Mashed potatoes":3.99,
    "Bread sticks":2.99,
    "Fries":3.50,
    "Onion rings":3.99
}
#print the main courses with the prices
print("The main courses we have are:")
for i in main_course:
    key = main_course[i]
    print(f"{i}: ${key}")
#Check what the user wants and make sure its an option
while True:
    main_choice = input("What would you like to order, type none if you dont want any: ").capitalize().strip()
    if main_choice in main_course.keys():
        total = main_course[main_choice]
        break
    elif main_choice == "None":
        main_choice = "nothing"
        break
    else:
       print("Please choose a valid option")
       continue

#make a function for the side dishes
def get_side_dish():
    #print the side dishes and prices
    print("The side dishes we have are:")
    for i in side_dish:
        key = side_dish[i]
        print(f"{i}: ${key}")
#check what the user wants and make sure its an option
    while True:
        side_choice = input("What would you like to order, type none if you dont want any: ").capitalize().strip()
        if side_choice in side_dish.keys():
            break
        elif side_choice == "None":
            side_choice = "nothing"
            break
        else:
           print("Please choose a valid option")
           continue
    return side_choice
#Print what drinks there are
print("The drinks we have are:")
for i in drink:
    key = drink[i]
    print(f"{i}: ${key}")
#Check what the user wants and make sure its an option
while True:
    drink_choice = input("What would you like to order, type none if you dont want any: ").capitalize().strip()
    if drink_choice in drink.keys():
        total += drink[drink_choice]
        break
    elif drink_choice == "None":
        drink_choice = "nothing"
        break
    else:
       print("Please choose a valid option")
       continue

#set the side dishes from the functions as variables to use and check if the side dishes are an option
while True:
    side_dish1 = get_side_dish()
    if side_dish1 in side_dish.keys():
        total += side_dish[side_dish1]
    else:
        print("Please choose a valid option")
        continue
    side_dish2 = get_side_dish()
    if side_dish2 in side_dish.keys():
        total += side_dish[side_dish2]
        break
    else:
        print("Please choose a valid option")
        continue
#print out the order and total price
print(f"Your order:\nMain Dish: {main_choice}\nSide Dishes: {side_dish1} & {side_dish2} \nDrink: {drink_choice}\nTotal Price: ${total}")