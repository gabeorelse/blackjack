import random

class Cards:
    number_value = ['Ace', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']
    suit = ['Spades', 'Hearts', 'Diamonds', 'Clubs']

    def __init__(self):
        pass
    
    def createDeck(self):
        deck = [(str(number_value) + ' of ' + suit) for number_value in self.number_value for suit in self.suit]
        return deck

        
    def shuffleCards(self, deck):
        random.shuffle(deck)
        print(deck[0])
        print(deck[1])

shuffle = Cards()
new_deck = shuffle.createDeck()
shuffle.shuffleCards(new_deck)
