#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        unicode_char = ord(letter)
        result = unicode_char - 32
        print("{}", .format(chr(result)), end="")
