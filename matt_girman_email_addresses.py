# -*- coding: utf-8 -*-
"""
Matt Girman

Name and Email Addresses
10/30/19
"""

addresses = {"John":"john@gmail.com","Mike":"mike@yahoo.com",\
             "Sally":"sally@hotmail.com"}

choice = 0

while choice != 5:
    print("Enter 1 to look up an email address.")
    print("Enter 2 to add a name and email address.")
    print("Enter 3 to change an existing email address.")
    print("Enter 4 to delete a name and email address.")
    print("Enter 5 to quit.")

    choice = int(input("What would you like to do? "))

    if choice == 1:
        name = input("Please enter a name: ")
        print(addresses[name] +"\n")
        
    elif choice == 2:
        name = input("Please enter a name: ")
        email = input("Please enter the email address: ")
        addresses[name] = email
        
    elif choice == 3:
        name = input("Whose email do you want to change? ")
        email = input("Enter the new email: ")
        addresses[name] = email
        
    elif choice == 4:
        name = input("Whose information would you like to delete? ")
        addresses.pop(name)
        
    print(addresses)
    