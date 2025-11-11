#AP 1st Period, Order Up

main_course = {
    "Burger":5.99,
    "Sandwhich":4.99,
    "Grilled cheese":4.32,
    "Steak":67.67,
    "Eggs":5.49
}
drink = {
    "Coke":3.99,
    "Canta":3.99,
    "Sprite":3.99,
    "Pepsi":3.99
}
side_dish = {
    "Mac and Cheese":2.99,
    "Mashed Potatoes":3.99,
    "Bread Sticks":2.99,
    "Fries":3.50,
    "Onion Rings":3.99
}
print("The main courses we have are:")
for i in main_course:
    print(i)
main_choice = input("What would you like to order: ")