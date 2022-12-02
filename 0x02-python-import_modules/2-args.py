#!/usr/bin/python3
import sys
if len(sys.argv) == 1:
    print("{} arguments.".format(len(sys.argv)-1))
elif len(sys.argv) == 2:
    print("{} argument :".format(len(sys.argv) -1))
    print("1: {}".format(sys.argv[1]))
if len(sys.argv) > 1:
    for i in range(1,len(sys.argv[i])):
        print("{}: {}".format(i,len(sys.argv[i])))
