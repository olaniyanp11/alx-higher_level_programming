#!/usr/bin/python3
for i in range(0, 26, 2):
    print("{:c}{:c}".format((122 - i), (89 - i)), end="")
