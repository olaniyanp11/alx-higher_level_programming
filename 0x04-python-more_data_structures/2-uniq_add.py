#!/usr/bin/python3
def uniq_add(my_list=[]):
    test = set(my_list)
    add = 0
    for num in test:
        add += num
    return add
