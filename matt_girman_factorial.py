# -*- coding: utf-8 -*-
"""
Matt Girman

Factorial
10/9/19
"""

num = int(input("Enter a non-negative integer: "))
factorial = num
original_num = num

while num > 1:
    factorial *= num-1
    num -= 1
    
print(str(original_num)+"! = " +str(factorial))