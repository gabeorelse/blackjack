from .dealer import Dealer

class Player:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet

    def get_name(self):
        return self.name
    
    def get_wallet(self):
        return self.wallet
