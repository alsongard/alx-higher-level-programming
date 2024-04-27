#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        upper_case_array = list(range(65, 91))
        if ord(letter) == 32 or ord(letter) == 44 or ord(letter) in upper_case_array:
            print("{}".format(letter), end="")
        else:
            lower_int = ord(letter)
            upper = lower_int - 32
            print("{}".format(chr(upper)), end="")
uppercase("Holberton School, 98 battery street")