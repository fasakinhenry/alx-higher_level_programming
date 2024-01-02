#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
if number < 0:
    last_digit = -last_digit
prefix = f"Last digit of {number:d} is {last_digit:d} and is"
if (last_digit) > 5:
    print(f"{prefix} greater than 5")
elif (last_digit == 0):
    print(f"{prefix} 0")
elif (last_digit < 6) and (last_digit) != 0:
    print(f"{prefix} less than 6 and not 0")
