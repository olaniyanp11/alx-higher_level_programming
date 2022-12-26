#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    mini = {key: value}
    a_dictionary.update(mini)
    return a_dictionary
