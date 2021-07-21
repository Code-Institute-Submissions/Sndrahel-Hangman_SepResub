import random
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


def get_random_team():
    secret_team = random.choice(teams_list)
    return secret_team.upper()


def play_game(secret_team):
    team_completion = "_" * len(secret_team)
    team_is_guessed = False
    guessed_character = []
    game_life = 9
    show_current_score()

    print("Welcome to Sport Teams Hangman.")
    print("Try and guess the team before the man is hung!")
    print("Let's play a game!")
    print(display_hangman(game_life))
    print("Current team: ", team_completion)
    print("\n")

    while not team_is_guessed and game_life > 0:
        guess = input("Guess a character: ").upper()
        if len(guess) == 1 and guess.isalnum():
            if guess in guessed_character:
                print("\nYou already guessed that character", guess)
            elif guess not in secret_team:
                print("\n", guess, "is not a correct guess.")
                game_life -= 1
                guessed_character.append(guess)
            else:
                print("\nWell done,", guess, "it's a correct guess!")
                guessed_character.append(guess)
                word_as_list = list(team_completion)
                indices = [i for i, letter in enumerate(secret_team) if letter == guess]  # or letter == '_'
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
        print("Current team: ", team_completion)
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
    while input("Play Again? (Y/N) ").upper() == "Y":
        secret_team = get_random_team()
        play_game(secret_team)


if __name__ == "__main__":
    main()
