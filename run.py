import random
from teams import teams_list

#  Variables to hold score (games won and lost)
games_won = 0
games_lost = 0


def score():
    print(" ")
    print("  Score")
    print("  -----")
    print("  Won: " + str(games_won) + "    Lost: " + str(games_lost))


def get_random_team():
    secret_team = random.choice(teams_list)
    return secret_team.upper()


def play_game(secret_team):
    guess_completion = "_" * len(secret_team)
    guessed = False
    guessed_character = []
    lives = 9
    score()

    print("Welcome to Sport Teams Hangman. Try and guess the team before the man is hung! Let's play a game!")
    print(display_hangman(lives))
    print(guess_completion)
    print("\n")

    while not guessed and lives > 0:
        guess = input("Please guess a character: ").upper()
        if len(guess) == 1 and guess.isalnum():
            if guess in guessed_character:
                print("You already guessed that character", guess)
            elif guess not in secret_team:
                print(guess, "is not a correct guess.")
                lives -= 1
                guessed_character.append(guess)
            else:
                print("Well done,", guess, "it's a correct guess!")
                guessed_character.append(guess)
                word_as_list = list(guess_completion)
                indices = [i for i, letter in enumerate(secret_team) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                guess_completion = "".join(word_as_list)
                if "_" not in guess_completion:
                    guessed = True
        else:
            print("Not a valid guess.")
        print(display_hangman(lives))
        print(guess_completion)
        print("\n")
    if guessed:
        global games_won
        games_won += 1
        print("Congrats, you got the right team! You are awesome!")
    else:
        global games_lost
        games_lost += 1
        print("Sorry, you ran out of lives. The team was " + secret_team + ". Maybe next time!")


def display_hangman(lives):
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
    return stages[lives]


def main():
    secret_team = get_random_team()
    play_game(secret_team)
    while input("Play Again? (Y/N) ").upper() == "Y":
        secret_team = get_random_team()
        play_game(secret_team)


if __name__ == "__main__":
    main()
