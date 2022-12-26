#!/usr/bin/python3
def best_score(a_dictionary):
    biggest = 0
    keys = {}
    if not a_dictionary:
        return None
    else:
        for key, value in a_dictionary.items():
            if value > biggest:
                biggest = value
                keys = key
                continue
            else:
                continue
        return keys
