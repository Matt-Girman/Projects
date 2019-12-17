# -*- coding: utf-8 -*-
"""
Matt Girman

Rock, Paper, Scissors
10/9/19
"""

import random

while True:
    comp = random.randint(1,3)

    user = input("Enter rock, paper, or scissors: ")

    if user == "rock" and comp == 1:
        print("The computer has chosen rock. Try again.")
    elif user == "rock" and comp == 2:
        print("The computer has chosen paper. Paper wraps rock. You lose.")
        break
    elif user == "rock" and comp == 3:
        print("The computer has chosen scissors. Rock smashes scissors. You win!")
        break
    
    elif user == "paper" and comp == 1:
        print("The computer has chosen rock. Paper wraps rock. You win!")
        break
    elif user == "paper" and comp == 2:
        print("The computer has chosen paper. Try again.")
    elif user == "paper" and comp == 3:
        print("The computer has chosen scissors. Scissors cuts paper. You lose.")
        break
    
    elif user == "scissors" and comp == 1:
        print("The computer has chosen rock. Rock smashes scissors. You lose.")
        break
    elif user == "scissors" and comp == 2:
        print("The computer has chosen paper. Scissors cuts paper. You win!")
        break
    elif user == "scissors" and comp == 3:
        print("The computer has chosen scissors. Try again.")
        
    else:
        print("Try again.")