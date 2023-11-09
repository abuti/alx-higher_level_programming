#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
             'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
    n = 0
    for i in range(len(roman_string)):
        if i != len(roman_string) - 1:
            if roman[roman_string[i]] < roman[roman_string[i + 1]]:
                n = n - roman[roman_string[i]]
                continue
        n += roman[roman_string[i]]
    return n
