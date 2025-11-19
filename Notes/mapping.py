#AP 1st Period, Mapping Notes

numbers = [12,5,42632,6,1531531,15,326,4,6,3154,26,432,65321,542,31,5326,32,67]
"""new_nums =[]
for number in numbers:
    new_nums.append(number/3)"""

def divide(num):
    return num/3

new_nums = map(lambda num: num/3,numbers)
print(list(new_nums))
for num in new_nums:
    print(num)