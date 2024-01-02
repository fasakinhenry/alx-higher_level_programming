#!/usr/bin/python3

# For loop to print all the numbers from 0 to 99
# Numbers must be separated by ,, followed by a space
# Numbers should be printed in ascending order, with two digits

for i in range(0, 100):
    if i != 99:
        print("{:02d}".format(i), end=", ")
    else:
        print("{:02d}".format(i))
