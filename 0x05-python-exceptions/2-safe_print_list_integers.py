#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for elements in my_list:
        try:
            if count < x:
                print("{:d}".format(elements), end="")
                count += 1
        except (TypeError, ValueError):
            continue
    print()
    return count
