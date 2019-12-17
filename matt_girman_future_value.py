# -*- coding: utf-8 -*-
"""
Matt Girman

Future Value
10/9/19
"""

def future_value(p,i,t):
    return p*(1+(i/100))**t

p = float(input("Enter the account's present value: "))
i = float(input("Enter the monthly interest rate (%): "))
t = int(input("Enter the number of months that the money will be left in the account: "))

fv = future_value(p,i,t)

print("Future value = $" +str(format(fv,'.2f')))