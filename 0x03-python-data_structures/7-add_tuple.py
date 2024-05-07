#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    shorter_length = min(len(tuple_a), len(tuple_b))
    print(shorter_length)
    print("\n")
    for a, b in zip(my_tupple1[:shorter_length], my_tupple2[:shorter_length]):
        return (a + b)





my_tupple1 = (1,2,3,4)
my_tupple2 = (1,2,3,4,5,7)

add_tuple(my_tupple1, my_tupple2)