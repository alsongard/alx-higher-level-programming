#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = [key for key in a_dictionary.keys()]
    keys.sort()
    for item in keys:
        print("{}: {}".format(item, a_dictionary[item]))
