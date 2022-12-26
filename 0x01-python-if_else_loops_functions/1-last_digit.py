#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    num = number * -1
    dev = num % 10
    if dev == 0:
        print("Last digit of {} is 0 and is 0".format(number))
    if dev > 5:
        print("Last digit of {} is {} and is greater than 5".format(number, dev))
    if dev < 6 and dev != 0:
        print("Last digit of {} is {} and is less than 6 and not 0".format(number, dev))
else:
    dev = number % 10
    if dev == 0:
        print("Last digit of {} is 0 and is 0".format(dev))
    if dev > 5:
        print("Last digit of {} is {} and is greater than 5".format(number, dev))
    if dev < 6 and dev != 0:
        print("Last digit of {} is {} and is less than 6 and not 0".format(number, dev))
