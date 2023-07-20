#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    roman_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    val_2 = 0
    val_1 = 0

    for char in reversed(roman_string):
        val = roman_num[char]
        if val >= val_1:
            val_2 += val
        else:
            val_2 -= val
        val_1 = val

    return val_2
