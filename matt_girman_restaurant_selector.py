"""
Matthew Girman

Restaurant Selector
10/1/19
"""

vegetarian = input("Are you vegetarian? (yes/no) ")
vegan = input("Are you vegan? (yes/no) ")
gluten = input("Are you gluten-free? (yes/no) ")

if vegetarian == "no" and vegan == "no" and gluten == "no":
    print("Possible restaurants: The Chef's Kitchen, Corner Cafe, Joe's Gourmet Burgers, Main Street Pizza Company, Mama's Fine Italian")

elif vegetarian == "yes" and vegan == "no" and gluten == "no":
    print("Possible restaurants: The Chef's Kitchen, Corner Cafe, Main Street Pizza Company, Mama's Fine Italian")
    
elif vegetarian == "yes" and vegan == "no" and gluten == "yes":
    print("Possible restaurants: The Chef's Kitchen, Corner Cafe, Main Street Pizza Company")

else:
    print("Possible restaurants: The Chef's Kitchen, Corner Cafe")