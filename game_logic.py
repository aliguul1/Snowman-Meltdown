import random
from ascii_art import STAGES

WORDS = ["python", "terminal", "algorithm", "developer", "software"]


def get_random_word():
    return random.choice(WORDS)


def get_valid_input(guessed_letters):
    """Ensures the user provides a single, new, alphabetic character."""
    while True:
        guess = input("\nGuess a letter: ").lower().strip()

        if len(guess) != 1:
            print(">> Please enter exactly one letter.")
        elif not guess.isalpha():
            print(">> That is not a letter. Please try again.")
        elif guess in guessed_letters:
            print(f">> You already tried '{guess}'. Pick a new one!")
        else:
            return guess


def display_game_state(mistakes, secret_word, guessed_letters):
    print("\n" + "=" * 30)
    print(STAGES[mistakes])

    display_word = [letter if letter in guessed_letters else "_" for letter in secret_word]
    print("\nWord Progress: ", " ".join(display_word))
    print(f"Guessed so far: {', '.join(guessed_letters)}")
    print("=" * 30)


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("\n--- SNOWMAN MELTDOWN ---")

    while mistakes < max_mistakes:
        display_game_state(mistakes, secret_word, guessed_letters)

        guess = get_valid_input(guessed_letters)
        guessed_letters.append(guess)

        if guess in secret_word:
            print(f"Yes! '{guess}' is in the word.")
            # Check for win
            if all(letter in guessed_letters for letter in secret_word):
                display_game_state(mistakes, secret_word, guessed_letters)
                print("\nCONGRATULATIONS! You saved the snowman! 🎉")
                return
        else:
            mistakes += 1
            print(f"Nope! '{guess}' is not there. The sun gets hotter...")

    display_game_state(mistakes, secret_word, guessed_letters)
    print(f"\nMELTDOWN! The snowman is gone. The word was: {secret_word.upper()}")