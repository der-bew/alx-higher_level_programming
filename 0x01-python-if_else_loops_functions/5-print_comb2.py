#!/usr/bin/python3
for x in range(0, 100):
    i = x // 10
    j = x % 10
    if j == 9 and i == 9:
        print(99)
    else:
        print("{}{}".format(i, j), end=", ")
