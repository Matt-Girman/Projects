# -*- coding: utf-8 -*-
"""
Matt Girman

Paint Job Estimator
10/9/19
"""

"""
I am assuming that the labor hours will be rounded up to the next whole number,
rather than charging for a fraction of an hour.
"""

import math

sf = float(input("Enter the square feet of wall space: "))
paint_price = float(input("Enter the price of paint per gallon: "))

gallons = sf/112
gallons = math.ceil(gallons)

hours = sf*8/112
hours = math.ceil(hours)

paint_cost = paint_price*gallons
labor_cost = hours * 35

total = paint_cost + labor_cost

print("Gallons of paint required: "+str(gallons))
print("Hours of labor required: "+str(hours))
print("Cost of paint: $"+str(format(paint_cost,'.2f')))
print("Cost of labor: $"+str(format(labor_cost,'.2f')))
print("Total cost of paint job: $"+str(format(total,'.2f')))