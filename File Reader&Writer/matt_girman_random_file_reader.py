# -*- coding: utf-8 -*-
"""
Matt Girman

Random Number File Reader
11/8/19
"""

total = 0
count = 0

with open('numbers.txt', mode='r') as numbers:
    for x in numbers.readlines():
        total += int(x)
        count += 1
        
print("The total of the numbers is " +str(total))
print("The number of random numbers is " +str(count))