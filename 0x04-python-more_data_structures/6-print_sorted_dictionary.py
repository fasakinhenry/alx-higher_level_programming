#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary == {}:
        return
    dlist = []
    for i, j in a_dictionary.items():
        dlist.append(i)
    dlist.sort()
    for a in dlist:
        print("{}: {}".format(a, a_dictionary[str(a)]))
