#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary == {}:
        return a_dictionary
    itr = []
    for i, j in a_dictionary.items():
        itr.append((i, j))
    for a in itr:
        if a[1] == value:
            a_dictionary.pop(a[0], None)

    return a_dictionary
