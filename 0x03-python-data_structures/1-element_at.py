#!/usr/binpython3

# Retrieves an element from a list like in C
def element_at(my_list, idx):
    if idx not in range(0, len(my_list)):
        return None
    return my_list[idx]
        
