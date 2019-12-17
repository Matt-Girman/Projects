# -*- coding: utf-8 -*-
"""
Matt Girman

Population
10/9/19
"""

pop = int(input("Starting number of organisms: "))
inc = int(input("Average daily increase (%): "))
days = int(input("Number of days to multiply: "))


print("Day          Approximate Population")
print("-----------------------------------")
print(str(1)+"               "+str(pop))

x=2

while x <= days:
    pop = pop + pop*inc/100
    print(str(x)+"               " +str(pop))
    x+=1