#!/usr/bin/python3

# Prints all integers of a list, in reverse order
def print_reversed_list_integer(my_list=[]):
    if my_list:
        for i in reversed(my_list):
            print("{:d}".format(i))
