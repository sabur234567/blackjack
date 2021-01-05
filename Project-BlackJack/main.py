# Name: Christopher Terni, Sabur Khan
# Date: 11/11/2019
# Course: COSC 2316 Fall 2019 (Dr. Shebaro)
# Program Description: A game of blackjack that tracks user information

#####THIS FILE IS JUST FOR MENUS AND THE DRIVER PROGRAM##########

######### Algorithm/Psuedocode ########

# 0. Main Menu:
# 1. Login
#   1A. Enter Username / Exit
#   1B. Login Menu:
#       1a. Play BlackJack
#       1b. BankRoll / Re-Buy
#       1c. User Statistics
#       1d. How To Play
#       1e. Exit
# 2. New User
#   2A. Enter Username / Exit
#   2B. Login Menu (1B)
# 3. LeaderBoard
#   3A. Display accounts with top payrolls
# 4. How To Play
#   4A. Display rules of blackjack
# 5. Exit

############# Python Code #############

import userutils
from playgame import playblackjack

# Function Description: Main Menu
# Precondition: None
# Postcondition: Returns int option value
def mainmenu():
    option = 0
    while option < 1 or option > 5:
        print("""
~~~~~~~~~~~ BLACKJACK ~~~~~~~~~~~~~
~~~~~~~~~~~ MAIN MENU ~~~~~~~~~~~~~

1. Login
2. New User
3. LeaderBoard
4. How To Play
5. Exit
""")
        try:
            option = int(input("Select An Option (1-5):  "))
        except:
            print("INVALID INPUT")
    return option

# Function Description: Login Menu
# Precondition: None
# Postcondition: Returns int option value
def loginmenu():
    option = 0
    while option < 1 or option > 5:
        print("""
~~~~~~~~~~~~ BLACKJACK ~~~~~~~~~~~~~
~~~~~~~~~~~ LOGIN MENU ~~~~~~~~~~~~~

1. Play BlackJack
2. BankRoll / Re-Buy
3. User Statistics
4. How To Play
5. Exit To Main Menu
""")
        try:
            option = int(input("Select An Option (1-5):  "))
        except:
            print("INVALID INPUT")
    return option

# Function Description: Login: asks for user input, creates user instance from file
# Precondition: Userfile given
# Postcondition: Returns user instance to be used
def login(file):
    try:
        username = input("Enter Username::: ")
    except:
        print("INVALID INPUT")
    return userutils.findFromFile(file, username)

# Function Description: NewUser: asks for user input, creates new user instance
# Precondition: Userfile given
# Postcondition: Returns user instance to be used
def newuser(file):
    try:
        username = input("Enter Username::: ")
    except:
        print("INVALID INPUT")
    user = userutils.findFromFile(file, username)
    if  user == False:
        user = userutils.writeToFile(file, username)
    else:
        return False
    return user

# Function Description: Displays how to play info
# Precondition: none
# Postcondition: prints how to play
def howtoplay():
    print("""
~~~~~~~~~~~~~~~~~ HOW TO PLAY ~~~~~~~~~~~~~~~~~~
Source ::: https://www.gamblingsites.org/casino/blackjack/beginners-guide/

Ace – Worth 1 or 11 points.
Face cards – Worth 10 points.
All other cards – Worth their rank in points.
For example, the 3 is worth 3 points, the 4 is worth 4 points, and so on.
            
To calculate the score for a hand of blackjack, you simply add the points up for
 all the cards in the hand. The hand with the HIGHER total is the winner.

Notice we use the word "higher", not "highest". That's because you only use the superlative 
("highest") when comparing 3 or more items. In blackjack, you're ALWAYS only comparing 2 hands
'the player's hand versus the dealer's hand. Other hands might be in play, but for purposes of 
calculating a win, there are only 2 hands that matter.

There's one other catch. Any hand with a total of 22 or higher is considered a bust, which is a 
dead hand and automatically loses immediately.

Blackjack pays 3 to 2.
Dealer must hit soft 17.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    """)

# Driver Program
def driver():
    userfile = "users.txt"

    option = mainmenu()
    while option != 5:
        if option == 1:
            currentuser = login(userfile)
            if currentuser == False:
                print("~~~~~ User does not exist. ~~~~~")
                input("~~ Press Enter To Return to Menu ~~")
            else:
                loginopt = loginmenu()
                while loginopt != 5:
                    if loginopt == 1:
                        playblackjack(currentuser)
                        userutils.updateFile(userfile, currentuser)
                    elif loginopt == 2:
                        if currentuser.bank < 100:
                            currentuser.rebuy()
                            print("~~~ REBUYS +1 ~~~")
                        print("~~~ CURRENT BANKROLL :::  $", currentuser.bank, " ~~~")
                        input("~~ Press Enter To Return to Menu ~~")
                    elif loginopt == 3:
                        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                        print("BANKROLL:", currentuser.bank)
                        print("PEAK BANKROLL:", currentuser.peak)
                        print("MOST WON IN SINGLE HAND:", currentuser.mostw)
                        print("MOST LOST IN SINGLE HAND:", currentuser.mostl)
                        print("TOTAL REBUYS:", currentuser.rebuys)
                        input("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n~~ Press Enter To Return to Menu ~~")
                    elif loginopt == 4:
                        howtoplay()
                        input("~~ Press Enter To Return to Menu ~~")
                    userutils.updateFile(userfile, currentuser)
                    loginopt = loginmenu()
        elif option == 2:
            currentuser = newuser(userfile)
            if currentuser == False:
                print("~~~~~ User already exists. ~~~~~")
                input("~~ Press Enter To Return to Menu ~~")
            else:
                print("~~~~~~~~~ User created. ~~~~~~~~~")
                input("~~ Press Enter To Return to Menu ~~")
        elif option == 3:
            leaders = userutils.leaderboard(userfile)
            print(f"""
~~~~~~~~~~~~~~~~ LeaderBoard ~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~ BANKROLLS ~~~~~~~~~~~~~~~~~~~
1. {leaders[0].name} ::::::: ${leaders[0].bank}
2. {leaders[1].name} ::::::: ${leaders[1].bank}
3. {leaders[2].name} ::::::: ${leaders[2].bank}
          
           """)
            input("~~ Press Enter To Return to Menu ~~")
        elif option == 4:
            howtoplay()
            input("~~ Press Enter To Return to Menu ~~")
        else:
            print("Unexpected Error")
        option = mainmenu()
driver()
