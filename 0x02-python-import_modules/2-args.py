#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    arg_length = len(argv) - 1
    if arg_length < 1:
        print("{} arguments.".format(arg_length))
    elif arg_length == 1:
        print("{} argument:".format(arg_length))
    else:
        print("{} arguments:".format(arg_length))
    for number in range(arg_length):
        print("{} : {}".format(number + 1, argv[number + 1]))
