# -*- coding: utf-8 -*-
"""
Matt Girman

Golf Scores Part 1
11/12/19
"""

golf = open('golf.txt', 'w')
golf.write("Name \tScore\n")
golf.write("--------------\n")
print("Press q at any time to quit.")

name = ''
score = ''

while name != 'q' and score != 'q':
    name = input("Please enter the golfer's name: ")
    if name == 'q':
        break
    score = input("Please enter the score: ")
    if score == 'q':
        break

    golf.write(name + '\t' + score +'\n')