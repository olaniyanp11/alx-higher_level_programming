#!/usr/bin/python3
for num in range(99):
    if num < 10:
        print("0{}".format(num),end="")
        print("{:c}{:c}".format(44, 32),end="")
    else:
        print("{}".format(num),end="") 
        print("{:c}{:c}".format(44, 32),end="")
print("{}".format(99)) 
