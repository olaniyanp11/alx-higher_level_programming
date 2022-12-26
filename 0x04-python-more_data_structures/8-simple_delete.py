#!/usr/bin/pythn3
def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        for kkys in a_dictionary:
            if key == kkys:
                del(a_dictionary[kkys])
                return a_dictionary
    return a_dictionary
