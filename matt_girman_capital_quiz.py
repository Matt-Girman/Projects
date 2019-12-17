# -*- coding: utf-8 -*-
"""
Matt Girman

Capital Quiz
10/30/19
"""

import random

capitals = {"Washington":"Olympia","Oregon":"Salem",\
                "California":"Sacramento","Ohio":"Columbus",\
                "Nebraska":"Lincoln","Colorado":"Denver",\
                "Michigan":"Lansing","Massachusetts":"Boston",\
                "Florida":"Tallahassee","Texas":"Austin",\
                "Oklahoma":"Oklahoma City","Hawaii":"Honolulu",\
                "Alaska":"Juneau","Utah":"Salt Lake City",\
                "New Mexico":"Santa Fe","North Dakota":"Bismarck",\
                "South Dakota":"Pierre","West Virginia":"Charleston",\
                "Virginia":"Richmond","New Jersey":"Trenton",\
                "Minnesota":"Saint Paul","Illinois":"Springfield",\
                "Indiana":"Indianapolis","Kentucky":"Frankfort",\
                "Tennessee":"Nashville","Georgia":"Atlanta",\
                "Alabama":"Montgomery","Mississippi":"Jackson",\
                "North Carolina":"Raleigh","South Carolina":"Columbia",\
                "Maine":"Augusta","Vermont":"Montpelier",\
                "New Hampshire":"Concord","Connecticut":"Hartford",\
                "Rhode Island":"Providence","Wyoming":"Cheyenne",\
                "Montana":"Helena","Kansas":"Topeka",\
                "Iowa":"Des Moines","Pennsylvania":"Harrisburg",\
                "Maryland":"Annapolis","Missouri":"Jefferson City",\
                "Arizona":"Phoenix","Nevada":"Carson City",\
                "New York":"Albany","Wisconsin":"Madison",\
                "Delaware":"Dover","Idaho":"Boise",\
                "Arkansas":"Little Rock","Louisiana":"Baton Rouge"}


correct = 0
incorrect = 0

print("Capital Quiz")
print("Enter q at any time to quit the game.")

while len(capitals)>0:
    state = random.choice(list(capitals.keys()))
    correct_answer = capitals.get(state)
    answer = input("What is the capital city of " +state +"? ")
    
    if answer.lower() == "q":
        break
    
    elif answer.lower() == correct_answer.lower():
        print("Correct!\n")
        del capitals[state]
        correct += 1
        
    else:
        print("Incorrect.\n")
        print("The correct answer is " +str(correct_answer) +"\n")
        incorrect += 1
        
    print("Score")
    print("-----")
    print("Correct: " +str(correct))
    print("Incorrect: " +str(incorrect))
    
print("\nFinal Score")
print("-----------")
print("Correct: " +str(correct))
print("Incorrect: " +str(incorrect))
        