#!/usr/bin/python3
def print_last_digit(number):
    str_number = str(number)
    last_digit = str_number[-1]
    return last_digit

print(f"{print_last_digit(-123)}")