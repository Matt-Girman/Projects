# -*- coding: utf-8 -*-
"""
Matt Girman

Falling Distance
10/9/19
"""

def falling_distance(t):
    return t**2*9.8/2

print("Time (s)     Distance (m)")
print("-------------------------")

for x in range(10):
    distance = falling_distance(x+1)
    print(str(x+1)+"            "+str(format(distance,'.2f')))