import random
from teams import teams_list


def get_random_team():
    word = random.choice(teams_list)
    return word.upper()


def play_game(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_character = []
    guessed_teams = []
    used_letters = set()  #
    lives = 6

    print("Let's play a game!")
    print(display_hangman(lives))
    print(word_completion)
    print('You have used these letters: ', ' '.join(used_letters))  #
    print("\n")

    while not guessed and lives > 0:
        guess = input("Please guess a character or a team: ").upper()
        if len(guess) == 1 and guess.isalnum():
            if guess in guessed_character:
                print("You already guessed that character", guess)
            elif guess not in word:
                print(guess, "is not a correct guess.")
                lives -= 1
                guessed_character.append(guess)
            else:
                print("Well done,", guess, "it's a correct guess!")
                guessed_character.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalnum():
            if guess in guessed_teams:
                print("You already tried that character", guess)
            elif guess != word:
                print(guess, "is not the team.")
                lives -= 1
                guessed_teams.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        print(display_hangman(lives))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congrats, you got the right team! You win!")
    else:
        print("Sorry, you ran out of lives. The team was " + word + ". Maybe next time!")


def display_hangman(lives):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |
                   |
                   |
                   |
                   -
                """
    ]
    return stages[lives]


def main():
    word = get_random_team()
    play_game(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_random_team()
        play_game(word)


if __name__ == "__main__":
    main()
