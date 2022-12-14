#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False
        print("ValueError", file=sys.stderr)
        print("TypeError", file=sys.stderr)
