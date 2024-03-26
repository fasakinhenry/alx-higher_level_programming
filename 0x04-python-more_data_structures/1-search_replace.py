#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list == []:
        return my_list
    replaced = my_list[:]
    for i in range(len(replaced)):
        if replaced[i] == search:
            replaced[i] = replace
    return replaced
