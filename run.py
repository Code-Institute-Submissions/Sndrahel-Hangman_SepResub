"""
Sport Teams Hangman is a word guessing game.

It´s up to the player to identify a hidden sport team.
The sport teams are from USA leagues: NBA, NFL, NHL and NPSL.

Game code and logic has been adapded and mainly copied from:
https://github.com/kiteco/python-youtube-code/blob/master/build-hangman-in-python/hangman.py
https://www.youtube.com/watch?v=m4nEnsavl6w

Game score function and variables has been copied from:
https://gist.github.com/jverbosky/a2e83d75bae7234e2342b3e6cfa72efe

"""

import random
import time
from teams import teams_list

#  Variables to hold score (games won and lost)
games_won = 0
games_lost = 0


def show_current_score():
    print(" ")
    print("  Score")
    print("  -----")
    print("  Won: " + str(games_won) + "    Lost: " + str(games_lost))
    print("\n")


#  Statment to pick random team from teams_list
def get_random_team():
    secret_team = random.choice(teams_list)
    return secret_team.upper()


def play_game(secret_team):
    team_is_guessed = False  # game over
    guessed_character = []
    game_life = 9
    show_current_score()

#  Variables to create an empty list of letters/characters in the team
    team_completion = []
    for i in range(0, len(secret_team)):
        if secret_team[i] == " ":
            team_completion.append(" ")
        else:
            team_completion.append("_")

    print("Welcome to Sport Teams Hangman.")
    print("Try and guess the team before the man is hung!")
    print("Teams are from USA leagues: NBA, NFL, NHL and NPSL.")
    print("Let's play a game!")
    print(display_hangman(game_life))
    print("Current team: ", "".join(team_completion))
    print("\n")

    while not team_is_guessed and game_life > 0:
        guess = input("Guess a character: \n").upper()
        if len(guess) == 1 and guess.isalnum():
            if guess in guessed_character:
                print("\nYou already guessed that character", guess)
            elif guess not in secret_team:
                print("\n", guess, "is not a correct guess.")
                game_life -= 1  # takes away 1 life when wrong
                guessed_character.append(guess)
            else:
                print("\nWell done,", guess, "it's a correct guess!")
                guessed_character.append(guess)
                word_as_list = list(team_completion)
                indices = [i for i, letter in enumerate(secret_team) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                team_completion = "".join(word_as_list)
                if "_" not in team_completion:
                    team_is_guessed = True
        else:
            print("\nNot a valid guess.")
        print("\nYou have", game_life, "lives left")
        print("You have used these characters: ", " ".join(guessed_character))
        print(display_hangman(game_life))
        print("Current team: ", "".join(team_completion))
        print("\n")
    if team_is_guessed:
        global games_won
        games_won += 1
        print("Congrats, you got the right team! You are awesome!")
    else:
        global games_lost
        games_lost += 1
        print("Game Over! You ran out of lives.")
        print("The team was " + secret_team + ". Maybe next time!")


def display_hangman(game_life):
    stages = [  # stage 10, final state: Game over
        """
                x------x
                |      |
                |      O
                |     \\|/
                |      |
                |     / \\
             ___|___
        """,
        # stage 9
        """
                x------x
                |      |
                |      O
                |     \\|/
                |      |
                |     /
             ___|___
        """,
        # stage 8
        """
                x------x
                |      |
                |      O
                |     \\|/
                |      |
                |
             ___|___
        """,
        # stage 7
        """
                x------x
                |      |
                |      O
                |     \\|
                |      |
                |
             ___|___
        """,
        # stage 6
        """
                x------x
                |      |
                |      O
                |      |
                |      |
                |
             ___|___
        """,
        # stage 5
        """
                x------x
                |      |
                |      O
                |
                |
                |
             ___|___
        """,
        # stage 4
        """
                x------x
                |      |
                |
                |
                |
                |
             ___|___
        """,
        # stage 3
        """
                x------x
                |
                |
                |
                |
                |
             ___|___
        """,
        # stage 2
        """

                |
                |
                |
                |
                |
             ___|___
        """,
        # stage 1, initial state
        """






             ___ ___
        """
    ]
    return stages[game_life]


def main():
    secret_team = get_random_team()
    play_game(secret_team)
    while True:
        choice = input("Play Again? (Y/N) \n").upper()
        if choice == "Y":
            secret_team = get_random_team()
            play_game(secret_team)
        elif choice == "N":
            print("Thanks for playing!")
            time.sleep(3)
            break
        else:
            print("Input was not valid, try again!")


if __name__ == "__main__":
    main()
