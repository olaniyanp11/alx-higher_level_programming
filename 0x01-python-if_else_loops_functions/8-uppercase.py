#!/usr/bin/python3
def uppercase(str):
    word = ""
    for i in str:
        if ord(str) > 64 and ord(str) < 91:
            t = ord(str) + 34
            word += t
        else:
            word += i
    print(word)


