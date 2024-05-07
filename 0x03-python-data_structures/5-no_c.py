#!/usr/bin/python3
def no_c(my_string):
    for i in range(len(my_string)):
        if my_string[i] == "C":
            new_string = my_string[:i] + my_string[i + 1: ]
            for i in range(len(new_string)):
                if new_string[i] == "c":
                    string = new_string[:i] + new_string[i+1:]

    print(f"The result of new_string is {string}")
no_c("Best School Chicago")