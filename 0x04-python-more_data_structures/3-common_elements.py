#!/usr/bin/python3
def common_elements(set_1, set_2):
    for item_1 in set_1:
        for item_2 in set_2:
            if item_1 == item_2:
                answer = item_2
    return answer

set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
c_set = common_elements(set_1, set_2)
print(sorted(list(c_set)))