#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    divisibility_list = []
    for i in my_list:
        divisibility_list.append(i % 2 == 0)
    print(divisibility_list)

mylist = [1,2,3,4,5,6,7,8,9]
divisible_by_2(mylist)