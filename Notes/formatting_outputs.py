#AP 1st Period, Formatting Outputs Notes
import os

name = "Mango Mustard"
age = 676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767
dollar_dollar = 67.67
percent = .67

print("Hello {}, you are {:,} years old, my gosh you're old. You have ${:.2f}, you broke boy. You get a random percent. which is {:%}".format(name, age, dollar_dollar, percent))


print(f"Hello {name}, you are {age:,} years old, my gosh you're old. You have ${dollar_dollar:.2f}, you broke boy. You get a random percent, which is {percent + 1}.")