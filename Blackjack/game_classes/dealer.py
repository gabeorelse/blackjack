from .cards import Cards

class Dealer():
    def __init__(self, bet):
        self.bet = bet

    def take_bet(self):
        return self.bet

    def match_bet(self):
        self.bet += self.bet
        return self.bet
    
    def deal_cards(self):
        shuffle = Cards()
        new_deck = shuffle.createDeck()
        shuffle.shuffleCards(new_deck)
        print(new_deck[0])
        print(new_deck[1])
        dealer_play = [new_deck[2], new_deck[3]]
        print("Dealer's Hand: " + dealer_play[0])
