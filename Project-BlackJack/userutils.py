# Name: Christopher Terni, Sabur Khan
# Date: 11/11/2019
# Course: COSC 2316 Fall 2019 (Dr. Shebaro)
# Program Description: A game of blackjack that tracks user information

#####THIS FILE IS FOR USER CLASS UTILS##########

######### Algorithm/Psuedocode ########

# 1. Read User from file
# 2. Look for next user
# 3. Read name, bank, peak, mostwon, and mostlost
# 4. Create instance of user and return to main program

# 1. Write user to file
# 2. At end of file, Add new user instance
# 3. Write name, bank, peak, mostwon, and mostlost

# 1. Update user info
# 2. Find and match given name
# 3. Write over and update following lines
# 4. bank, peak, mostwon, and mostlost

############# Python Code #############

import userclass

# Function Description: Reads user from file
# Precondition: Correct file given, name to find is given
# Postcondition: Returns user matching name, null if does not exist
def findFromFile(file, name):
    currentuser = False
    with open(file) as f:
        lines = f.read().splitlines()
    for i in range(len(lines)):
        if lines[i] == name:
            bank = int(lines[i+1])
            peak = int(lines[i + 2])
            mostw = int(lines[i + 3])
            mostl = int(lines[i + 4])
            rebuys = int(lines[i + 5])
            currentuser = userclass.user(name, bank, peak, mostw, mostl, rebuys)
    return currentuser

# Function Description: Writes new user to file
# Precondition: Correct file given, name is given
# Postcondition: Returns new user matching name
def writeToFile(file, name):
    newuser = userclass.user(name)
    with open(file, "a") as f:
        f.write(str(newuser.name))
        f.write("\n")
        f.write(str(newuser.bank))
        f.write("\n")
        f.write(str(newuser.peak))
        f.write("\n")
        f.write(str(newuser.mostw))
        f.write("\n")
        f.write(str(newuser.mostl))
        f.write("\n")
        f.write(str(newuser.rebuys))
        f.write("\n")
    return newuser

# Function Description: Updates user in file
# Precondition: Correct file given, user is given
# Postcondition: Returns nothing, updates file
def updateFile(file, user):
    with open(file) as f:
        lines = f.read().splitlines()
    for i in range(len(lines)):
        if lines[i] == user.name:
            lines[i + 1] = int(user.bank)
            lines[i + 2] = int(user.peak)
            lines[i + 3] = int(user.mostw)
            lines[i + 4] = int(user.mostl)
            lines[i + 5] = int(user.rebuys)
    with open(file, "w") as f:
        for line in lines:
            f.write(str(line))
            f.write("\n")

# Function Description:
# Precondition: Leaderboard is called, userfile is given
# Postcondition: Returns 3 users with highest bankroll
def leaderboard(file):
    with open(file) as f:
        lines = f.read().splitlines()
    templeader = [userclass.user("XXX"), userclass.user("XXX"), userclass.user("XXX")]
    for i in range(1, len(lines), 6):
        if int(lines[i]) > templeader[2].bank:
            name = lines[i-1]
            bank = int(lines[i])
            peak = int(lines[i + 1])
            mostw = int(lines[i + 2])
            mostl = int(lines[i + 3])
            rebuys = int(lines[i + 4])
            thisuser = userclass.user(name, bank, peak, mostw, mostl, rebuys)
            if thisuser.bank > templeader[1].bank:
                if thisuser.bank > templeader[0].bank:
                    templeader[2] = templeader[1]
                    templeader[1] = templeader[0]
                    templeader[0] = thisuser
                else:
                    templeader[2] = templeader[1]
                    templeader[1] = thisuser
            else:
                templeader[2] = thisuser
    return templeader







