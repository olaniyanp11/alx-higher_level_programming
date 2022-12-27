#!/usr/bin/python3
def weight_average(my_list=[]):
    div = 0
    value = 0
    if my_list == []:
        return 0
    for i in range(0, len(my_list)):
        value += my_list[i][0] * my_list[i][1]
        div += my_list[i][1]
    return value / div
