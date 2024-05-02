#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = 1
    if len(sys.argv[1:]) > 1:
        print("{} arguments:".format(len(sys.argv[1:])))
        while i <= len(sys.argv[1:]):
            print("{} : {}".format(i, sys.argv[i]))
            i += 1
    elif len(sys.argv[1:]) == 1:
        print("{} argument:".format(len(sys.argv[1:])))
        print("{} : {}".format(i, sys.argv[i]))
    else:
        print("0 arguments.")
