#!/usr/bin/python3
for num in range(100):
    if num < 99:
        print("{:02d}{:c}{:c}".format(num, 44, 32), end="")
    elif num == 99:
        print("{}".format(num))
