#!/usr/bin/python3
x = 97

while(x <= 122):
    if x != 101 and x != 113:
        print("{}".format(chr(x)), end='')
    x += 1
