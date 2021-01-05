# Name: Christopher Terni, Sabur Khan
# Date: 11/11/2019
# Course: COSC 2316 Fall 2019 (Dr. Shebaro)
# Program Description: A game of blackjack that tracks user information

#####THIS FILE IS JUST FOR THE BLACKJACK GAME ITSSELF##########

######### Algorithm/Psuedocode ########

# 1. Option to Place Bet or exit
# 2. Create / Shuffle deck
# 3. Deal Cards
# 4. If not Blackjack, Else showdown
#   4a. Player Options::
#   4b. Hit, Stand
#   4c. Give options until: Stand, Bust or 21
#   4d. When player turn over: Play dealers cards (Flip covered card)::
#       D1: If not blackjack:
#       D2: If under 17: Hit
#       D3: Hit until => 17 or BUST
#           d1: ::::::PAYOUTS::::::
#           d2: Player BlackJack = x1.5 bet
#           d3: Player Win (cards > dealer, or dealer bust, must be non-bust) = x1.0 bet
#           d4: Player bust --Bet
#           d5: Player cards = dealers; --Bet
# 5. Option to Place Bet or exit
# 6. Check num of cards left in total deck: if < enough for another hand::
#   6a. Create / Shuffle deck
# 7. Loop game until exit or bankroll < 1

############# Python Code #############

import random
import userutils

#########Dict to show value of each card#############
cardvals = {
        "2":2,
        "3":3,
        "4":4,
        "5":5,
        "6":6,
        "7":7,
        "8":8,
        "9":9,
        "10":10,
        "J":10,
        "Q":10,
        "K":10,
        "A":11
    }

# Function Description: Builds deck
# Precondition: New Deck Needed 14 cards per deck x4
# Postcondition: A full, shuffled deck
def deck():
    ####ADD CARDS TO DECK######
    deck = []
    for key in cardvals.keys():
        for i in range(24):
            deck.append(key)
    #######SHUFFLE DECK########
    random.shuffle(deck)
    return deck

# Function Description: Deal
# Precondition: Deck is created
# Postcondition: cards will be dealt to player and dealer, deck return to main
def deal(phand, dhand, deck):
    phand.append(deck.pop(0))
    dhand.append(deck.pop(0))
    phand.append(deck.pop(0))
    dhand.append(deck.pop(0))

# Function Description: Option Menu
# Precondition: Player has cards, not bust, not 21
# Postcondition: player option return
def options(phand):
    option = 0
    while option < 1 or option > 2:
        try:
            option = int(input("1:HIT, 2:STAND,  :::  "))
        except:
            print("INVALID INPUT")
    return option

# Function Description: HIT, adds card to hand
# Precondition: Has cards, not bust, not 21
# Postcondition: adds card to hand, deck -1 and returned
def hit(phand, deck):
    phand.append(deck.pop(0))

# Function Description: Dealers turn
# Precondition: Has cards, player turn over
# Postcondition: Dealers turn ends, dealer hand updated, return value of cards
def dealerturn(dhand, deck):
    value = 0
    value += cardvals[dhand[0]] + cardvals[dhand[1]]
    if value == 22:
        for i in range(len(dhand)):
            if dhand[i] == "A":
                dhand[i] = "a"
                value -= 10
                break
    while value < 17:
        dhand.append(deck.pop(0))
        value += cardvals[dhand[len(dhand)-1]]
        if value > 21 and 'A' in dhand:
            for i in range(len(dhand)):
                if dhand[i] == "A":
                    dhand[i] = "a"
                    value -= 10
                    break
    return value

# Function Description: Displays Table
# Precondition: Cards are dealt, player has cards, dealer has cards
# Postcondition: Prints a readable display of the table and cards in play
def display(phand,dhand):
    print(f"""
|~~~~~~~~~~~~~~~~TABLE~~~~~~~~~~~~~~~~~~
| :::DEALER:::   {dhand[0]},X   :::VALUE:::   ??
|
| :::PLAYER:::   {",".join(phand)}   :::VALUE:::   {valof(phand)}
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~""")

# Function Description: Displays Table (INCLUDING DEALER TURN)
# Precondition: Cards are dealt, player has cards, dealer has cards
# Postcondition: Prints a readable display of the table and cards in play
def displaydone(phand,dhand):
    print(f"""
|~~~~~~~~~~~~~~~~~TABLE~~~~~~~~~~~~~~~~~
| :::DEALER:::   {",".join(dhand)}   :::VALUE:::   {valof(dhand)}
|
| :::PLAYER:::   {",".join(phand)}   :::VALUE:::   {valof(phand)}
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~""")

# Function Description: Returns value of hand
# Precondition: Valid hand given
# Postcondition: Returns int value of hand
def valof(hand):
    value = 0
    for i in hand:
        if i == "a":
            value += 1
        else:
            value += cardvals[i]
    if value > 21 and 'A' in hand:
        for i in range(len(hand)):
            if hand[i] == "A":
                hand[i] = "a"
                value -= 10
                break
    return value

# Function Description: Returns if player has won or not
# Precondition: Both player and dealer values given
# Postcondition: Returns true if player has won, else false
def iswin(pval, dval):
    if pval > 21:
        return False
    if dval > 21:
        return True
    if dval >= pval:
        return False
    else:
        return True

# Function Description: Retrieves bet or option to exit from user
# Precondition: none
# Postcondition: Returns bet (or option to exit 0)
def betopt(user):
    bet = -1
    while user.bank - bet < 0 or bet < 0:
        print("~~~~~ CURRENT BANKROLL ::: $", user.bank, "~~~~~")
        print("::::Place Bet (Input 0 to exit game)::::")
        try:
            bet = int(input("==>  $"))
        except:
            print("INVALID INPUT")
        if bet == 0:
            break
    return bet

#GAME DRIVER
def playblackjack(user):
    bet = betopt(user)

    mydeck = deck()
    while bet > 0:
        outcome = True
        phand = []
        dhand = []
        deal(phand,dhand,mydeck)
        display(phand,dhand)
        if valof(phand) == 21 and valof(dhand) != 21:
            print(f"""
!!!!!!!!!!!!!!!!!!!!!!!!!!!
~~~~~~~ BLACKJACK! ~~~~~~~~
!!!!!!!!!!!!!!!!!!!!!!!!!!!
~~~~~ PAYOUT = {bet * 1.5}~~~
""")
            user.add(bet * 1.5)
        else:
            while valof(phand) < 21:
                opt = options(phand)
                if opt == 1:
                    hit(phand, mydeck)
                    display(phand,dhand)
                else:
                    break
            finalval = dealerturn(dhand, mydeck)
            if valof(phand) > 21:
                print("~~~~ PLAYER BUST ~~~~")
                input("Press Enter to Continue")
                outcome = False
            displaydone(phand,dhand)
            if valof(phand) == finalval and outcome:
                outcome = " ~~PUSH~~ "
            else:
                outcome = iswin(valof(phand), finalval)
            print("PLAYER WIN: ", outcome, "\n")
            if outcome == True:
                user.add(bet)
            elif outcome == False:
                user.sub(bet)
        if len(mydeck) < 30:
            mydeck = deck()
        bet = betopt(user)
