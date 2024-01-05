#!/usr/bin/python3

# Retrieves an element from a list like in C
def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    for i in range(0, len(my_list)):
        print("{:}".format(my_list[i]))
