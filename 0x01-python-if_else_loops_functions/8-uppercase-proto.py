#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        lower_case_array = list(range(97, 123))
        if ord(letter) in lower_case_array:
            upper = ord(letter) - 32
            print("{}".format(chr(upper)), end="")
        else:
            print("{}".format(letter), end="")
