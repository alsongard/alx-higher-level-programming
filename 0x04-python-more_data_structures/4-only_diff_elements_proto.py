#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    my_list = []
    for item_1 in set_1:
        for item_2 in set_2:
            if item_2 == item_1:
                my_list.append(item_2)
    return set(my_list)
