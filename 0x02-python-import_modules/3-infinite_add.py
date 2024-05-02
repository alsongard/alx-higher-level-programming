#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    for number in sys.argv[1:]:
        number = int(number)
        sum += number
    print("{}".format(sum))
