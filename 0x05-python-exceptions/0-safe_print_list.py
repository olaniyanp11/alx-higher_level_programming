#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for elements in my_list:
        try:
            if count < x:
                print("{:d}".format(elements), end="")
        except (TypeError, ValueError):
            break
        count += 1
    print()
    return count
