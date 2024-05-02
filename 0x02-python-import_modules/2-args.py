#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv[1:]) >= 1:
        print("{} argument:".format(len(sys.argv[1:])))
        i = 1
        while i <= len(sys.argv[1:]):
            print("{} : {}".format(i, sys.argv[i]))
            i += 1
    else:
        print("0 arguments.")
