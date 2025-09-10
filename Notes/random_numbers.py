#AP 1st Period, Random Numbers Notes
import random

stat_one = random.randint(1,10) + random.randint(1,10)
stat_two = random.randint(1,10) + random.randint(1,10)
stat_three = random.randint(1,10) + random.randint(1,10)
stat_four = random.randint(1,10) + random.randint(1,10)
stat_five = random.randint(1,10) + random.randint(1,10)
stat_six = random.randint(1,10) + random.randint(1,10)
stat_seven = random.randint(1,10) + random.randint(1,10)

print(f"Your stat options are: {stat_one}, {stat_two}, {stat_three}, {stat_four}, {stat_five}, {stat_six}, {stat_seven}")
strength = int(input("Which stat do you want as your strength: "))+2


print(f"Random number between 0-1: {random.random()}")
print(f"Random number between 0-20: {random.randint(1,20)}")