import random

class Cards:
    number_value = ['Ace', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']
    suit = ['Spade', 'Heart', 'Diamond', 'Club']

    def __init__(self):
        pass

    def shuffleCards(self):
        random.shuffle(self.number_value)
        random.shuffle(self.suit)
        for number in self.number_value:
            for suit_value in self.suit:
                print(number, suit_value)
            


deck = Cards()
deck.shuffleCards()