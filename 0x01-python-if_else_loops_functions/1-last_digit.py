#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# Get the last digit of the number
last_digit = abs(number) % 10
prefix = f"Last digit of {number} is {last_digit} and is"
if (last_digit) > 5:
    print(f"{prefix} greater than 5")
elif (last_digit == 0):
    print(f"{prefix} 0")
elif (last_digit < 6) and (last_digit) != 0:
    print(f"{prefix} less than 6 and not 0")
