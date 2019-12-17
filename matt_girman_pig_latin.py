# -*- coding: utf-8 -*-
"""
Matt Girman

Pig Latin
11/8/19
"""

sentence = input("Type a sentence that you want converted to Pig Latin: ")

sentence = sentence.upper()

sentence = sentence.split(' ')

pig_latin = []

for x in sentence:
    if x[-1].isalpha():
        pig_latin.append(x[1:]+x[0]+'AY')
    else:
        pig_latin.append(x[1:-1] + x[0] + 'AY' + x[-1])
        
pig_sentence = ' '.join(pig_latin)

print(pig_sentence)