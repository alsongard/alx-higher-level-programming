#!/usr/bin/python3
# add each integer in both list and if list not equal pad result
def summation_list(list1,list2):
    #acquire the length of each list and compare which list is shorter
    shorter_length = min(len(list1), len(list2))
    #create new list
    new_list = []
    #perform addition
    for a, b in zip(my_list1[:shorter_length], my_list2[:shorter_length]):
        new_list.append(a+b)

    # for unequal list we extend
    if len(my_list1) > shorter_length:
        new_list.extend([my_list1[i] for i in range(shorter_length, len(my_list2))])
    elif len(my_list2) > shorter_length:
        new_list.extend([my_list2[i] for i in range(shorter_length, len(my_list2))])
    print(new_list)

    

my_list1 = [1,2,3,4]
my_list2 = [6,7,8,9,10]
shorter_length = summation_list(my_list1, my_list2)
print(shorter_length)
print(my_list1[:shorter_length])
print(my_list2[:shorter_length])
