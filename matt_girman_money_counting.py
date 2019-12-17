"""
Matthew Girman

Money Counting Game
9/30/19
"""

p = int(input("Enter the number of pennies: "))
n = int(input("Enter the number of nickels: "))
d = int(input("Enter the number of dimes: "))
q = int(input("Enter the number of quarters: "))

total = 0.01*p + 0.05*n + 0.1*d + 0.25*q

if total == 1:
    print("Congratulations! You have won the game.")
elif total > 1:
    print("The total is greater than one dollar.")
elif total < 1:
    print("The total is less than one dollar.")