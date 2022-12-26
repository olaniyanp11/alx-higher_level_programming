#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort = sorted(a_dictionary.items())
    for dic, key in sort:
        print(f"{dic}: {key}")
