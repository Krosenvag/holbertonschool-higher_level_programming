#!/usr/bin/python3

def no_c(my_string):

    filtered_chars = []
    for char in my_string:
        if char != 'c' and char != 'C':
            filtered_chars.append(char)

    result = "".join(filtered_chars)
    return result