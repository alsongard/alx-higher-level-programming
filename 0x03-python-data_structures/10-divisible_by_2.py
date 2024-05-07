#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    divisibility_list = []
    for i in my_list:
        if i % 2 == 0:
            divisibility_list.append(True)
        else:
            divisibility_list.append(False)
    return divisibility_list
