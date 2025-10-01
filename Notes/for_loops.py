import time

nums = [67, 6, 7, 12, 124, 123, 875, 35, 562, 665, 75, 645, 64, 42, 79]

for num in nums:
    num/=2
    if num>100:
        print(f"{num} is only half of {num*2}. It is a large number")
    else:
        print(num)

for num in range(1,68,3):
    print(num)

for num in range(1,68):
    print(num)
    time.sleep(.67)