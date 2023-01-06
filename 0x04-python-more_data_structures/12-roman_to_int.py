#!/usr/bin/python3
def roman_to_int(roman_string):
    single = { 'X': 10,'D': 500,'M': 1000,'C': 100,'I': 1,'V': 5,'L': 50}
    double = {'IX': 9, 'IV': 4, 'CD': 900, 'XL': 40, 'XC': 90}
    for i in range(0,len(roman_string),2):
        for j, k in double.items():
            if i == j:
                value += k
            for 
