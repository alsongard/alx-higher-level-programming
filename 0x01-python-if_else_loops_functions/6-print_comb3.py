#!/usr/bin/python3
x = 0
while x < 10:
    for y in range(0,10):
        if x== 9 and y == 9:
            print("{}{}".format(x,y),  end="\n")
            continue
        print("{}{}".format(x,y),  end=", " )
    x+=1
