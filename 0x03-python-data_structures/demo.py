#!/usr/bin/python3
def print_list(myList):
    for i in myList:
        print(f"Value is {i} and type is {type(i)}")

print_list([1,2,3,4,5])

def print_dec(myList):
    for i in myList:
        print(f"Value is {i:d} and type is {type(i)}")


print_dec([1,2,4,3,9,4,16,5,25,6,36,7,49,8,64])

