from game_classes.cards import Cards
from game_classes.player import Player
from game_classes.dealer import Dealer

RUNNING = True

while RUNNING:
    print("Welcome to Blackjack!")
    name = input("Please enter your name: ")
    wallet = int(input("Please deposit a sum into your wallet.\nYou'll pull from your wallet throughout the game to place bets.\nEnter Sum: "))

    P1 = Player(wallet)
    D1 = Dealer()

    print("Welcome " + name + "!")
    print("Player name: " + name)
    print("Current wallet balance: " + str(wallet))

    P1.get_name()
    P1.get_wallet()
    withdraw = int(input("Please enter your bet: "))
    pot = D1.match_bet(withdraw)
    P1.get_bet(withdraw)

    print("Pot: " + str(pot))
    print("Current wallet: " + str(P1.get_wallet()))

    D1.shuffle_cards()
    D1.deal_cards()

    next_play = input("Would you like to HIT or STAND? ")

    if next_play == "HIT".lower():
        player_hand = D1.next_card()
        print("Here's your next card: \n")
        print(player_hand)

    if next_play == "STAND".lower():
        stand = D1.stand_play()
        print("Dealer's Hand: \n")
        print(stand)

    if next_play == "E".lower():
        print("Thank you for playing!")
        RUNNING = False
    else:
        print("Please enter HIT, STAND, or E to exit.")




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


    

