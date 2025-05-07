from .dealer import Dealer

class Player:
    def __init__(self, wallet):
        self.name = ""
        self.wallet = wallet

    def get_name(self):
        return self.name
    
    def get_wallet(self):
        return self.wallet
    
    def get_bet(self, bet):
        P1 = Player(self.wallet)
        self.wallet = P1.get_wallet() - bet
        return self.wallet
