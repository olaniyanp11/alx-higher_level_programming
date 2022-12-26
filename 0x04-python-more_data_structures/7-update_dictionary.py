#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if (type(a_dictionary)) is dict:
        sort = sorted(a_dictionary.items())
        for dic,kky in sort:
            if dic == key:
                kky = value
            return a_dictionary
            continue
