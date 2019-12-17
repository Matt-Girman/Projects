# -*- coding: utf-8 -*-
"""
Matt Girman

Celsius to Fahrenheit Table
10/9/19
"""

c = 0

print("Celsius     Fahrenheit")
print("----------------------")

for c in range(21):
    f=c*9/5+32
    print(str(c)+"\u00b0         "+str(f)+"\u00b0")