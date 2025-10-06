import random

def enemy_choice():
    return random.choice(choices)

def player_choice():
    while True:
        playerchoice = input("Rock, Paper or Scissors? (r/p/s): ").lower()
        if playerchoice in choices:
            return playerchoice
        else:
            print("Invalid choice!")

def display_choices(playerchoice, enemychoice):
    print(f"You chose: {emojis[playerchoice]}")
    print(f"Enemy chose: {emojis[enemychoice]}")

def check_winner(f_playerchoice, f_enemyfhoice, f_scores):
    if f_playerchoice == f_enemyfhoice:
        print("Tie!")
        f_scores["ties"] += 1
    elif (
            (f_playerchoice == ROCK and f_enemyfhoice == SCISSORS) or
            (f_playerchoice == PAPER and f_enemyfhoice == ROCK) or
            (f_playerchoice == SCISSORS and f_enemyfhoice == PAPER)):
        print("Player scores!")
        f_scores["playerWins"] += 1
    else:
        print("Enemy scores!")
        f_scores["enemyWins"] += 1

def choose_gamemode():
    while True:
        gamemode = input("Do you want to play PvP or PvE? (p/e): ").lower()
        if gamemode in gameModeChoices:
            return gamemode
        else:
            print("Invalid choice!")

def game_loop():
    while True:
        playerchoice = player_choice()
        if gameMode == PAPER:
            enemychoice = player_choice()
        else:
            enemychoice = enemy_choice()

        display_choices(playerchoice, enemychoice)

        check_winner(playerchoice, enemychoice, scores)

        print(f"Player wins: {scores["playerWins"]} | Enemy wins: {scores["enemyWins"]} | Ties: {scores["ties"]}")

        if scores["playerWins"] == 2:
            print("Player won!")
            break
        elif scores["enemyWins"] == 2:
            print("Enemy won!")
            break

ROCK = "r"
PAPER = "p"
SCISSORS = "s"
emojis = {ROCK:"🪨", PAPER:"📃", SCISSORS:"✂️"}
choices = tuple(emojis.keys())
gameModeChoices = ("p", "e")

while True:
    scores = {"playerWins": 0, "enemyWins": 0, "ties": 0}

    gameMode = choose_gamemode()

    game_loop()

    answer = input("Game over! Play again? (y/n): ").lower()
    if answer == "n":
        break