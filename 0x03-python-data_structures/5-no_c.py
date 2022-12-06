#!/usr/bin/python3
def no_c(my_string):
    my_list = list(my_string)
    count = 0
    for i in my_list:
        if (i == 'c') or (i == 'C'):
            my_list[count] = ""
        count += 1
    return "".join(my_list)
