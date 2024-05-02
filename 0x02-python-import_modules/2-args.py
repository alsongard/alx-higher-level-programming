#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_length = len(sys.argv) - 1
    if arg_length < 1:
        print("{} arguments.".format(arg_length))
    elif arg_length ==  1:
        print("{} argument:".format(arg_length))
    else:
        print("{} arguments:".format(arg_length))
    for number in range(arg_length):
        print("{} : {}".format(number + 1, sys.argv[number + 1]))
