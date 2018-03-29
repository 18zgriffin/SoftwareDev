playerList = []
totalscoresList = []
indscoreList = []
allscoresList = []
dataLoaded = 0

def EnterData(playerList, indscoreList):
    matchFile = input("Enter the name of the played match: ")
    file = open(matchFile, "a")
    x = 1
    while x == 1:
        totalScore = "0"
        print("Player data is entered like this: John 1 2 3 4 5 6")
        player = input("Players name followed by each score: ")
        if player == "":
            x = 0
        player = player.split(" ")
        playerList.append(player[0])
        playerScores = player[1:]
        for score in playerScores:
                totalScore = int(totalScore) + int(score)
        indscoreList.append(playerScores)
        allscoresList = indscoreList
        print(allscoresList)
        totalscoresList.append(totalScore)
        writing = (player[0] + " " + (" ".join(playerScores)))
        print(writing)
        file.write(writing)
        file.write("\n")
    file.close()
    return playerList, indscoreList, totalscoresList, allscoresList

def LoadData(playerList, allscoresList):
    allscoresList = []
    totalscoresList = []
    playerList = []
    totalScore = 0
    while True:
        try:
            matchFile = input("Enter the name of the played match: ")
            file = open(matchFile, "r")
        except FileNotFoundError:
            print("That directory does not exist, please enter a new one")
        else:
            break
    for line in file:
        line = line.strip("\n")
        line = line.split(" ")
        indscoreList = (line[1:])
        allscoresList.append(indscoreList)
        playerList.append(line[0])
        for score in indscoreList:
            totalScore = int(totalScore) + int(score)
        totalscoresList.append(totalScore)
    print(playerList)
    return playerList, allscoresList, totalscoresList

def SearchDisplay(playerList, dataLoaded):
    print(playerList)
    if dataLoaded != 0:
        position = -1
        targetPlayer = input("Enter name of target player: ")
        for player in playerList:
            position = position + 1
            if player == targetPlayer:
                analyse(position, allscoresList)
        return
    else:
        print("There is currently no data loaded, run either enter data or load data first")

def Exit():
    exit(0)
    return

def analyse(position, allscoresList):
    print(allscoresList)
    print(position)
    playerscoreList = (allscoresList[position])
    player = (playerList[position])
    gamesplayed = len(playerscoreList)
    playertotalScore = (totalscoresList[position])
    ppg = (playertotalScore/gamesplayed)
    playerscoreList = [int(x) for x in playerscoreList]
    maxscore = max(playerscoreList)
    print(player, "has a max score of " + str(maxscore) + ",")
    print("a points per game (ppg) of", ppg)
    print("and a total played games of", gamesplayed)
    return

while True:
    #gives the user the selections they can make
    print("Please enter the number of the option you wish to select")
    print("    1. Enter data for a new game")
    print("    2. Load previous data")
    print("    3. Search and Display")
    print("    4. Save and exit")
    #takes selection via input
    menuOption = input("Selection: ")
    #performs the specified function
    if menuOption == "1":
        EnterData(playerList, indscoreList)
        dataLoaded = 1
    elif menuOption == "2":
        LoadData(playerList, allscoresList)
        dataLoaded = 1
    elif menuOption == "3":
        SearchDisplay(playerList, dataLoaded)
    elif menuOption == "4":
        Exit()
    else:
        #reloops the menu because their selection made did not exist
        print("Menu option selection does not exist: ")
        menuOption = 0