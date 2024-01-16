import random
import sys


def keyIsWinner(compChoice, playerChoice):

    rules = {
        "Rock" : ["Scissors", "Lizzard"],
        "Paper" : ["Rock", "Spock"],
        "Scissors" : ["Paper", "Lizzard"],
        "Lizzard" : ["Spock", "Paper"],
        "Spock" : ["Rock", "Scissors"]
    }

    if(compChoice in rules.keys() and playerChoice in rules.get(compChoice)):
        return "Computer"

    elif(compChoice == playerChoice):
        return "Draw"

    elif(playerChoice in rules.keys() and compChoice in rules.get(playerChoice)):
        return "Player"


def playGame(countChoices, countWins):

    availableChoice = ["Rock", "Paper", "Scissors", "Lizzard", "Spock"]

    print("\n Please choose one of the following options:\n", availableChoice)
    playerChoice = input()
    compChoice = random.choice(availableChoice)
    print("\nThe computer chose:", compChoice)

    countChoices[playerChoice] += 1
    countChoices[compChoice] += 1

    x = keyIsWinner(compChoice, playerChoice)

    countWins[x] += 1

    print("\nGamescore: \nPlayer: ", countWins["Player"], "\nComputer: ", countWins["Computer"], "\nDraws: ", countWins["Draw"])

    return countChoices, countWins


if __name__ == '__main__':

    countChoices = {
        "Rock": 0,
        "Paper": 0,
        "Scissors": 0,
        "Lizzard": 0,
        "Spock": 0
    }

    countWins = {
        "Computer" : 0,
        "Player" : 0,
        "Draw" : 0
    }

    while True:
        print("What do you want to do?")
        print("1. Play a game")
        print("2. Show statistics")
        print("3. Exit")
        choice = input()
        if choice == "1":
            countChoices, countWins = playGame(countChoices, countWins)
        elif choice == "2":
            print(countChoices)
            print(countWins)
        elif choice == "3":
            print("exit")
            sys.exit()


