#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    number_str = str(number)[1:]
    last_digit = int(number_str[-1]) * -1
else:
    number_str = str(number)
    last_digit = int(number_str[-1])
if int(last_digit) > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
elif int(last_digit) == 0:
    print(f"Last digit of {number} is {last_digit} and is 0")
elif int(last_digit) < 6 and int(last_digit) != 0:
    print(f"Last digit of {number} is {last_digit} and is less than ", end="")
    print("6 and not 0")
