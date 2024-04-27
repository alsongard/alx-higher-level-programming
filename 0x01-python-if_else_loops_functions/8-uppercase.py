#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        upper_case_array = list(range(32, 91))
        if ord(letter) in upper_case_array:
            print("{}".format(letter), end="")
        else:
            lower_int = ord(letter)
            upper = lower_int - 32
            print("{}".format(chr(upper)), end="")
