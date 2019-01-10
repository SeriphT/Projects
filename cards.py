import random

deck = []

player1_Hand = [] 
player2_Hand = []

def makeDeck(deck):
    """ Populate the deck of cards"""
    SUITS = ["hearts","spades","diamonds","clubs"]
    VALUES = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    for e in SUITS:
        for i in VALUES:
            card = i+" "+e
            deck.append(card)

def shuffleCards(deck):
    for i in range(len(deck)):
        j = random.randrange(len(deck))
        temp = deck[i]
        deck[i] = deck[j]
        deck[j] = temp

def dealCards(deck,player1_Hand,player2_Hand):
    for i in range(5):
        card = deck.pop(0)
        player1_Hand.append(card)
        card = deck.pop(0)
        player2_Hand.append(card)

makeDeck(deck)
print(deck)
print()
shuffleCards(deck)
print(deck)
dealCards(deck,player1_Hand,player2_Hand)
print()
print(player1_Hand)
print(player2_Hand)
print(len(deck))
