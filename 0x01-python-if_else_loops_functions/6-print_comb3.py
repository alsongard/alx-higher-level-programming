#!/usr/bin/python3
x = 0
while x < 10:
    for y in range(0,10):
        if x== 9 and y == 9:
            print(f"{x}{y}", end="\n")
            continue
        print(f"{x}{y}", end=", " )
    x+=1

"""
for i in range(0, 10):
    for a in range(0,10):
        print(f"{i}{a}")
"""
