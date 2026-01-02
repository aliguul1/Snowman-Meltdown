import random

# Snowman ASCII Art stages
STAGES = [
    # Stage 0: Full snowman
    """
     ___  
    /___\\ 
    (o o) 
    ( : ) 
    ( : ) 
    """,
    # Stage 1: Bottom part starts melting
    """
     ___  
    /___\\ 
    (o o) 
    ( : ) 
    """,
    # Stage 2: Only the head remains
    """
     ___  
    /___\\ 
    (o o) 
    """,
    # Stage 3: Snowman completely melted
    """
     ___  
    /___\\ 
    """
]

WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return random.choice(WORDS)


def display_game_state(mistakes, secret_word, guessed_letters):
    """Displays the current snowman stage and the hidden word."""
    # 1. Print the snowman stage
    print(STAGES[mistakes])

    # 2. Build the display word (e.g., "p _ t h _ n")
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word: ", display_word)
    print("-" * 20)  # Visual separator


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    game_over = False

    print("Welcome to Snowman Meltdown!")

    while not game_over:
        # Show the current state of the game
        display_game_state(mistakes, secret_word, guessed_letters)

        guess = input("Guess a letter (or type 'quit'): ").lower().strip()

        if guess == 'quit':
            break

        # Basic validation
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter one letter.")
            continue

        # For testing Step 2: Add the guess to the list and print it
        guessed_letters.append(guess)
        print(f"You guessed: {guess}")

        # Testing logic: If you want to see the snowman melt,
        # let's temporarily increment mistakes every turn
        # mistakes += 1

        # End game if we run out of stages
        if mistakes >= len(STAGES) - 1:
            display_game_state(mistakes, secret_word, guessed_letters)
            print("GAME OVER: The snowman has melted!")
            game_over = True


if __name__ == "__main__":
    play_game()