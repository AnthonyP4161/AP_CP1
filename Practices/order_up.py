#AP 1st Period, Order Up
#list for the main courses
main_course = {
    "Burger":5.99,
    "Sandwhich":4.99,
    "Grilled cheese":4.32,
    "Steak":67.67,
    "Eggs":5.49
}
#list for the drinks
drink = {
    "Coke":3.99,
    "Canta":3.99,
    "Sprite":3.99,
    "Pepsi":3.99
}
#list for the side dishes
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
#print the side dishes and prices
print("The side dishes we have are:")
for i in side_dish:
    key = side_dish[i]
    print(f"{i}: ${key}")
#check what the user wants and make sure its an option
while True:
    side_choice1 = input("What would you like to order, type none if you dont want any: ").capitalize().strip()
    if side_choice1 in side_dish.keys():
        total += side_dish[side_choice1]
        break
    elif side_choice1 == "None":
        side_choice1 = "nothing"
        break
    else:
       print("Please choose a valid option")
       continue
#check what the user wants for their second side dish and make sure its an option
while True:
    side_choice2 = input("What would you like to order for your second side dish, type none if you dont want any: ").capitalize().strip()
    if side_choice2 in side_dish.keys():
        total += side_dish[side_choice2]
        break
    elif side_choice2 == "None":
        side_choice2 = "nothing"
        break
    else:
       print("Please choose a valid option")
       continue
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
#print out the order and total price
print(f"Your order:\nMain Dish: {main_choice}\nSide Dishes: {side_choice1} & {side_choice2}\nDrink: {drink_choice}\nTotal Price: ${total}")