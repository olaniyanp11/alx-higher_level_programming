#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, "r", encryption="UTF8") as fil:
        for line in fil:
            print(line, end='')