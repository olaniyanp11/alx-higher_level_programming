#!/usr/bin/python3
for i in range(10):
        for k in range(i+1,10):
            if i < 8:
                print("{}{}{:c}{:c}".format(i,k,44,32), end="")
            else:
                print("{}{}".format(i,k))
