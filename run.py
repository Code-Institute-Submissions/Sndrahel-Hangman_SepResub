import random
from teams import teams_list

#  Variables to hold score (games won and lost)
games_won = 0
games_lost = 0


# List to hold guessed letters that are not found in secret_team
wrong_letters = []


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
    guessed_teams = []
    lives = 9
    score()

    print("Let's play a game!")
    print(display_hangman(lives))
    print(guess_completion)
    print("\n")

    while not guessed and lives > 0:
        guess = input("Please guess a character or a team: ").upper()
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
        elif len(guess) == len(secret_team) and guess.isalnum():
            if guess in guessed_teams:
                print("You already tried that character", guess)
            elif guess != secret_team:
                print(guess, "is not the team.")
                lives -= 1
                guessed_teams.append(guess)
            else:
                guessed = True
                guess_completion = secret_team
        else:
            print("Not a valid guess.")
        print(display_hangman(lives))
        print(guess_completion)
        print("\n")
    if guessed:
        global games_won
        games_won += 1
        print("Congrats, you got the right team! You win!")
    else:
        global games_lost
        games_lost += 1
        print("Sorry, you ran out of lives. The team was " + secret_team + ". Maybe next time!")


def display_hangman(lives):
    stages = [  # stage 10, final state: Game over
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
        ___|___
        """,
        # stage 9
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     /
        ___|___
        """,
        # stage 8
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |
        ___|___
        """,
        # stage 7
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |
        ___|___
        """,
        # stage 6
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |
        ___|___
        """,
        # 5, head
        """
           --------
           |      |
           |      O
           |
           |
           |
        ___|___
        """,
        # 4,
        """
           --------
           |      |
           |
           |
           |
           |
        ___|___
        """,
        # 3,
        """
           --------
           |
           |
           |
           |
           |
        ___|___
        """,
        # 2,
        """

           |
           |
           |
           |
           |
        ___|___
        """,
        # 1, initial empty state
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
