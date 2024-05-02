#!/usr/bin/python3
import sys
if len(sys.argv) < 1:
    print("0 arguments: ")
else:
    print("{} arguments:".format(len(sys.argv[1:])))
    i = 1
    while i < len(sys.argv):
        print("{}: {} ".format(i, sys.argv[i]))
        i += 1
    # print("{}".format(len(list((sys.argv[1:])))))
