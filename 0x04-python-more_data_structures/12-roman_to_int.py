#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string == "" or type(roman_string) is not str:
        return 0
    r = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    # r is dictionary containing roman numeral characters as
    # the keys and their corresponding values
    d = 0
    # d is used to store integer value of roman numeral
    rs = roman_string
    for i in range(len(roman_string)):
        d += r[rs[i]]
        if i < len(rs) - 1:
            if r[rs[i + 1]] > r[rs[i]]:
                d -= (2 * r[rs[i]])
            else:
                continue
    return d
