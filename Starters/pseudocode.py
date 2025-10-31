import random

grid = [['1', '2', '3'],
        ['4','5','6'],
        ['7', '8', '9']]
print(grid)


for list in grid:
    print(f"{list[0]} | {list[1]} | {list[2]}\n --+--+--")

chosen =[]
while True:
    computer_choice = random.randint(1,9)
    chosen.append(computer_choice)
    if computer_choice in chosen:
        computer_choice = random.randint(1,9)
        continue
    if computer_choice == 1:
        grid[0] = "O"
    elif computer_choice == 2:
        grid[1] = "O"
    elif computer_choice == 3:
        grid[2] = "O"
    elif computer_choice == 4:
        grid[3] = "O"
    elif computer_choice == 5:
        grid[4] = "O"
    elif computer_choice == 6:
        grid[5] = "O"
    elif computer_choice == 7:
        grid[6] = "O"
    elif computer_choice == 8:
        grid[7] = "O"
    elif computer_choice == 9:
        grid[8] = "O"
    print(grid)