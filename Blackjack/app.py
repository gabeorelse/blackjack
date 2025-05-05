from game_classes.cards import Cards
from game_classes.player import Player
from game_classes.dealer import Dealer

RUNNING = True

while RUNNING:
    print("Welcome to Blackjack!")
    name = input("Please enter your name: ")
    wallet = int(input("Please deposit a sum into your wallet.\nYou'll pull from your wallet throughout the game to place bets.\nEnter Sum: "))

    P1 = Player(name, wallet)
    

    print("Welcome " + name + "!")
    print("Player name: " + name)
    print("Current wallet balance: " + str(wallet))

    bet = int(input("Place your bet: "))
    D1 = Dealer(bet)
    pot = D1.match_bet()
    wallet -= bet
    print("Pot: " + str(pot))
    print("Current wallet: " + str(wallet))

    D1.deal_cards()




    '''
    start_game = input("Ready to play? Y/N\n")
    if start_game == "Y".lower():
        break
    if start_game == "N".lower():
        break
    else:
        print("Please enter Y or N.")
        break
    '''


    

