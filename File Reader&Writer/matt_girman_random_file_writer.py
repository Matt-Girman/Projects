# -*- coding: utf-8 -*-
"""
Matt Girman

Random Number File Writer
11/8/19
"""

import random

y = int(input("How many numbers would you like the file to hold? "))

with open('numbers.txt', mode='w') as numbers:
    for x in range(y):
        numbers.write(str(random.randint(1,501))+'\n')