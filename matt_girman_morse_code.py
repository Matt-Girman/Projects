# -*- coding: utf-8 -*-
"""
Matt Girman

Morse Code Converter
11/1/19
"""

# Dictionary that holds the morse code conversions
morse = { 'A':'.-', 'B':'-...', 
         'C':'-.-.', 'D':'-..', 'E':'.', 
         'F':'..-.', 'G':'--.', 'H':'....', 
         'I':'..', 'J':'.---', 'K':'-.-', 
         'L':'.-..', 'M':'--', 'N':'-.', 
         'O':'---', 'P':'.--.', 'Q':'--.-', 
         'R':'.-.', 'S':'...', 'T':'-', 
         'U':'..-', 'V':'...-', 'W':'.--', 
         'X':'-..-', 'Y':'-.--', 'Z':'--..', 
         '1':'.----', '2':'..---', '3':'...--', 
         '4':'....-', '5':'.....', '6':'-....', 
         '7':'--...', '8':'---..', '9':'----.', 
         '0':'-----', ', ':'--..--', '.':'.-.-.-', 
         '?':'..--..', '/':'-..-.', '-':'-....-', 
         '(':'-.--.', ')':'-.--.-'}

# Asks the user for a message
print("Enter a message that you would like converted to morse code: ")
message = input()

# Converts the message to all caps
message = message.upper()

translation = ''

for letter in message:
    if (letter != ' '):
        translation += morse[letter] + ' '
        
    else:
        translation += ' '

print(translation)