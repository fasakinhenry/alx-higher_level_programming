#!/usr/binpython3

""" replaces an element in a list at a specific position
without modifying the original list (like in C) """

def new_in_list(my_list, idx, element):
    if idx not in range(0, len(my_list)):
        return my_list.copy()
    new_list = my_list.copy()
    new_list[idx] = element
    return new_list
    
