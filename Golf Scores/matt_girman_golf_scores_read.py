# -*- coding: utf-8 -*-
"""
Matt Girman

Golf Scores Part 2
11/12/19
"""

golf = open('golf.txt', 'r')

line = 'a'

while line != '':
    line = golf.readline()
    print(line)