from .cards import Cards
import random

class Dealer():
    def __init__(self):
        self.deck = []
        self.dealer_play = []

    def match_bet(self, bet):
        bet += bet
        return bet
    
    def shuffle_cards(self):
        shuffle = Cards()
        self.deck = shuffle.createDeck()
        shuffle.shuffleCards(self.deck)
        return self.deck
    
    def deal_cards(self):
        print("Your Hand is:\n")
        print(self.deck[0])
        print(self.deck[1])
        self.dealer_play = [self.deck[2], self.deck[3]]
        print("Dealer's Hand: " + self.dealer_play[0])

    def next_card(self):
        new_card = random.randint(4, len(self.deck)-1)
        return self.deck[new_card]

    def stand_play(self):
        return self.dealer_play