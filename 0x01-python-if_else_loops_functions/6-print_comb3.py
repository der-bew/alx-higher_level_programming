#!/usr/bin/python3
for x in range(0, 100):
    i = x // 10
    j = x % 10
    if i < j:
        if i == 8 and j == 9:
            print(89)
        else:
            print("{}{}".format(i, j), end=", ")
