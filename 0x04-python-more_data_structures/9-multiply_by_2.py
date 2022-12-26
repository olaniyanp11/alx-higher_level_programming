#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = {}
    keys = {}
    for kky, value in a_dictionary.items():
        value = value * 2
        keys = {kky: value}
        new_dic.update(keys)
    return new_dic
