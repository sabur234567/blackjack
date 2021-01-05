# Name: Christopher Terni, Sabur Khan
# Date: 11/11/2019
# Course: COSC 2316 Fall 2019 (Dr. Shebaro)
# Program Description: A game of blackjack that tracks user information

#####THIS FILE IS FOR USER CLASS##########

######### Algorithm/Psuedocode ########

# 1. Class For Users
# 2. Add / Subtract
# 3. Keep track of other values

# 1. Read User from file
# 2. Look for empty line, next line starts user
# 3. Read name, bank, peak, mostwon, and mostlost
# 4. Create instance of user and return to main program

# 1. Write user to file
# 2.

############# Python Code #############

# Class Description: User Instances
class user:
    def __init__(self, name, bank=100, peak=0, mostw=0, mostl=0, rebuys=0):
        self.name = name
        self.bank = bank
        self.peak = peak
        self.mostw = mostw
        self.mostl = mostl
        self.rebuys = rebuys

    # subtracts amount from bankroll
    def sub(self, amt):
        self.bank -= amt
        if amt > self.mostl:
            self.mostl = amt

    # adds amount to bankroll
    def add(self, amt):
        self.bank += amt
        if amt > self.mostw:
            self.mostw = amt
        if self.bank > self.peak:
            self.peak = self.bank

    # Bankroll set to 100, rebuy +1
    # Precondition: current bankroll < 100
    def rebuy(self):
        self.bank = 100
        self.rebuys += 1

