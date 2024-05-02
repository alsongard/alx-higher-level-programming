#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_length = len(sys.argv) - 1
    i = 1
    if arg_length == 0:
        print("{} arguments.".format(arg_length))
    elif arg_length ==  1:
        print("{} argument:".format(arg_length))
        print("{} : {}".format(i, sys.argv[i]))
    elif arg_length > 1:
        print("{} arguments:".format(arg_length))
        while i < arg_length:
            print("{} : {}".format(i, sys.argv[i]))
            i += 1
