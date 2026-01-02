# main.py
from game_logic import play_game


def main():
    while True:
        play_game()

        replay = input("\nWould you like to play again? (y/n): ").lower().strip()
        if replay != 'y':
            print("Thanks for playing Snowman Meltdown! Goodbye.")
            break


if __name__ == "__main__":
    main()