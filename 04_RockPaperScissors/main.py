import random
import sys
import requests

#run before start
#flask --app flaskserver run

#TODO remove
url = 'http://127.0.0.1:5000/'


def keyIsWinner(compChoice, playerChoice):

    toKey ={
        "Rock": "stein_count",
        "Paper": "papier_count",
        "Scissors": "schere_count",
        "Lizzard": "echse_count",
        "Spock": "spock_count"
    }

    rules = {
        "Rock" : ["Scissors", "Lizzard"],
        "Paper" : ["Rock", "Spock"],
        "Scissors" : ["Paper", "Lizzard"],
        "Lizzard" : ["Spock", "Paper"],
        "Spock" : ["Rock", "Scissors"]
    }

    if(compChoice in rules.keys() and playerChoice in rules.get(compChoice)):
        response = requests.post(url + "update_score", json={'user_name': "Computer"})
        print(response.text)
        response = requests.post(url + "update_symboles", json={'user_name': "Computer", 'field_name': toKey[compChoice]})
        print(response.text)
        response = requests.post(url + "update_symboles", json={'user_name': user_name, 'field_name': toKey[playerChoice]})
        print(response.text)
        return "Computer"

    elif(compChoice == playerChoice):
        return "Draw"

    elif(playerChoice in rules.keys() and compChoice in rules.get(playerChoice)):
        response = requests.post(url + "update_score", json={'user_name': user_name})
        print(response.text)
        response = requests.post(url + "update_symboles", json={'user_name': user_name, 'field_name': toKey[playerChoice]})
        print(response.text)
        response = requests.post(url + "update_symboles", json={'user_name': "Computer", 'field_name': toKey[compChoice]})
        print(response.text)
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

    print("What is your name? ")
    user_name = input()

    while True:
        print("What do you want to do?")
        print("1. Play a game")
        print("4. Show Score")
        print("5 Show SymbolCount")
        print("6 Delete User")
        choice = input()
        if choice == "1":
            countChoices, countWins = playGame(countChoices, countWins)
        elif choice == "2":
            print(countChoices)
            print(countWins)
        elif choice == "3":
            print("exit")
            sys.exit()
        elif choice == "4":
            response = requests.get(url + "get_score", params={'user_name': user_name})
            print(response.text)
        elif choice == "5":
            response = requests.get(url + "get_symboles", params={'user_name': user_name})
            print(response.text)
        elif choice == "6":
            response = requests.post(url + "delete_score", json={'user_name': user_name})
            print(response.text)
            response = requests.post(url + "delete_symboles", json={'user_name': user_name})
            print(response.text)


