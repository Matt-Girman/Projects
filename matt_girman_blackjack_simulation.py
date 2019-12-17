# -*- coding: utf-8 -*-
"""
Matt Girman

Blackjack Simulation
10/30/19
"""

import random

deck = {'Ace of Spades':11, '2 of Spades':2, '3 of Spades':3,
        '4 of Spades':4, '5 of Spades':5, '6 of Spades':6,
        '7 of Spades':7, '8 of Spades':8, '9 of Spades':9,
        '10 of Spades':10, 'Jack of Spades':10,
        'Queen of Spades':10, 'King of Spades': 10,
        'Ace of Hearts':11, '2 of Hearts':2, '3 of Hearts':3,
        '4 of Hearts':4, '5 of Hearts':5, '6 of Hearts':6,
        '7 of Hearts':7, '8 of Hearts':8, '9 of Hearts':9,
        '10 of Hearts':10, 'Jack of Hearts':10,
        'Queen of Hearts':10, 'King of Hearts': 10,
        'Ace of Clubs':11, '2 of Clubs':2, '3 of Clubs':3,
        '4 of Clubs':4, '5 of Clubs':5, '6 of Clubs':6,
        '7 of Clubs':7, '8 of Clubs':8, '9 of Clubs':9,
        '10 of Clubs':10, 'Jack of Clubs':10,
        'Queen of Clubs':10, 'King of Clubs': 10,
        'Ace of Diamonds':11, '2 of Diamonds':2, '3 of Diamonds':3,
        '4 of Diamonds':4, '5 of Diamonds':5, '6 of Diamonds':6,
        '7 of Diamonds':7, '8 of Diamonds':8, '9 of Diamonds':9,
        '10 of Diamonds':10, 'Jack of Diamonds':10,
        'Queen of Diamonds':10, 'King of Diamonds': 10}

player1 = 0
player2 = 0

while player1 <= 21 and player2 < 21:
    newCard1_name = random.choice(list(deck.keys()))
    newCard2_name = random.choice(list(deck.keys()))
    
    newCard1 = deck.get(newCard1_name)
    newCard2 = deck.get(newCard2_name)
    
    # Adds the new value to the total
    player1 = player1 + newCard1
    player2 = player2 + newCard2
    
    # If either player draws an ace and their total exceeds 21,
    # the value of the ace is reduced to 1
    if newCard1 == 11 and player1>21:
        player1 = player1 - 10
        
    if newCard2 == 11 and player2>21:
        player2 = player2 - 10
        
    #Removes the drawn cards from the deck
    del deck[newCard1_name]
    del deck[newCard2_name]
        

    
print("Player 1 Total = " +str(player1))
print("Player 2 Total = " +str(player2))
    
if player1 == 21 and player2 == 21:
    print("Both players win!")
    
elif player1 <= 21 and player2 > 21:
    print("Player 1 wins!")
    
elif player1 > 21 and player2 <= 21:
    print("Player 2 wins!")
    
else:
    print("No one wins.")