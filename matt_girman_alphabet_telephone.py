# -*- coding: utf-8 -*-
"""
Matt Girman

Alphabetic Telephone Number Translator
11/6/19
"""

# Dictionary that holds letter to number translations

translator = {'A':'2', 'B':'2', 'C':'2',
              'D':'3', 'E':'3', 'F':'3',
              'G':'4', 'H':'4', 'I':'4',
              'J':'5', 'K':'5', 'L':'5',
              'M':'6', 'N':'6', 'O':'6',
              'P':'7', 'Q':'7', 'R':'7', 'S':'7',
              'T':'8', 'U':'8', 'V':'8',
              'W':'9', 'X':'9', 'Y':'9', 'Z':'9'}

# Ask the user for a phone number
number = input("Please enter a 10-character telephone number in the format XXX-XXX-XXXX: ")

new_number = ''

#Convert each letter to a number
for letter in number.upper():
    if (letter != '-' and letter.isalpha()):
        new_number += translator[letter]
        
    elif letter.isdigit():
        new_number += letter
        
    else:
        new_number += '-'
        
print(new_number)