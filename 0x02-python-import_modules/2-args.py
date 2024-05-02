#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    print("{} arguments. ".format(len(sys.argv[1:])))
    i = 0
    while i < len(sys.argv[1:]):
        print("{}: {}".format(i, sys.argv[i]))
        i += 1
    # print("{}".format(len(list((sys.argv[1:])))))
