#!/usr/bin/python3

# Print the ASCII alphabet in lowercase without a new line
for char in range(ord('a'), ord('z') + 1):
    if chr(char) not in {'q', 'e'}:
        print("{}".format(chr(char)), end='')
