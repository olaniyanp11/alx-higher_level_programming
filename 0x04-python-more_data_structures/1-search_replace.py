#!/usr/bin/python3
def search_replace(my_list, search, replace):
    count = 0
    new_list = my_list[:]
    for element in new_list:
        if element == search:
            new_list[count] = replace
        count += 1
    return new_list
