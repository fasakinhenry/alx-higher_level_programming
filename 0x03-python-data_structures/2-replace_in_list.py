#!/usr/binpython3

# Replaces an element of a list at a specific position (like in C).
def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return None
    my_list[idx] = element
    return my_list
