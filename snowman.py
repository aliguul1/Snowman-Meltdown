import random

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

def get_random_word():
    """Selects a random word from the list."""
    # Using random.choice is more efficient for lists
    return random.choice(WORDS)

def play_game():
    secret_word = get_random_word()
    print("Welcome to Snowman Meltdown!")
    print(f"Secret word selected: {secret_word} (testing only)")

    game_over = False

    # The Game Loop
    while not game_over:
        guess = input("\nGuess a letter (or type 'quit' to exit): ").lower().strip()

        # Check if user wants to quit
        if guess == 'quit':
            print("Thanks for playing! Goodbye.")
            game_over = True
        elif len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
        else:
            print(f"You guessed: {guess}")
            # Later logic: check if guess is in secret_word,
            # update snowman status, etc.

if __name__ == "__main__":
    play_game()