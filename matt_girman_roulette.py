"""
Matthew Girman

Roulette Wheel Colors
9/30/19
"""

pocket = int(input("Select a pocket number (0 to 36):"))

if pocket == 0:
    print("Green")
elif pocket >= 1 and pocket <= 10 and pocket %2 == 1:
    print("Red")
elif pocket >= 1 and pocket <= 10 and pocket %2 == 0:
    print("Black")
elif pocket >= 11 and pocket <= 18 and pocket %2 == 1:
    print("Black")
elif pocket >= 11 and pocket <= 18 and pocket %2 == 0:
    print("Red")
elif pocket >= 19 and pocket <= 28 and pocket %2 == 1:
    print("Red")
elif pocket >= 19 and pocket <= 28 and pocket %2 == 0:
    print("Black")
elif pocket >= 29 and pocket <= 36 and pocket %2 == 1:
    print("Black")
elif pocket >= 29 and pocket <= 36 and pocket %2 == 0:
    print("Red")
else:
    print("Error. Please enter a number between 0 and 36")