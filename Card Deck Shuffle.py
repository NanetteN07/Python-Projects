#Program: Card Deck Shuffle
#Author: Nanette n.
#Date: 16/02/2025
 
 
#imports random
import random
 
#Declare Variables - make a deck
suits = ['Hearts', 'Spades', 'Diamonds', 'Clubs']
placeVal = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
 
deck = []
shuffledDeck = []
 
def createDeck():
 
    for i in range(0, len(suits), 1):
        for j in range(0, len(placeVal), 1):
            card = placeVal[j] + ' ' + suits[i]
            deck.append(card)
 
def shuffleDeck():
    for i in range(0, len(deck), 1):
        limit = (len(deck) - 1)
        #print(limit)
        pick = random.randint(0, limit)
        shuffledDeck.append(deck[pick])
        deck.pop(pick)
def main():
    createDeck()
    print(len(deck))    
    print(deck)
    shuffleDeck()
    print(shuffledDeck)
    print(len(shuffledDeck))
main()
