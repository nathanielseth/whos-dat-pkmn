import random
import sys
from os import system, name
from string_bank import word_list, stages, logo, win

# clear function
def clear():
    # for windows
    if name == "nt":
        _ = system("cls")
    # for mac and linux
    else:
        _ = system("clear")


# menu
print(logo)
command = int(input("=> "))
if command == 1:
    command = 1
    clear()
while command != 1:
    if command == 2:
        print("See you next time!")
        sys.exit(1)
    elif command == 3:
        print(
            "★ Guess a letter to reveal the pokémon! You have 6 chances to guess the pokémon. When you guess a correct letter in the word, the letter will be revealed, otherwise your lives will be reduced by one. ★"
        )
        start_prompt = input("\nStart the game? (Y) / (N) => ").upper()
        if start_prompt == "Y":
            game_over = False
            command = 1
            clear()
        else:
            print("See you next time!")
            sys.exit(1)
    else:
        print("Invalid input.")

# game
def play_game():
    game_over = False
    lives = 6
    word = random.choice(word_list)
    word_length = len(word)
    display = []
    for _ in range(word_length):
        display += "_"
    while not game_over:
        guess = input("Trainer, please guess a letter => ").lower()
        clear()
        if guess in display:
            print(f"You've already guessed {guess}!")
        for position in range(word_length):
            letter = word[position]
            if letter == guess:
                display[position] = letter
        print(f"{' '.join(display)}")

        if guess not in word:
            print(f"\n{guess.upper()} is wrong!")
            lives -= 1
            if lives > 0:
                print(f"Your guesses left: {lives}")
            if lives == 0:
                game_over = True
                clear()
                print(stages[lives])
                print(f"You lost the game. The Pokémon was {word.upper()}!\n")
                sys.exit(1)
        if "_" not in display:
            print(win)
            print(f"\n  🎉 You found {word.upper()}! 🎉\n")
            game_over = True
        if lives > 0 and game_over == False:
            print(stages[lives])


play_game()

wins = 0
# replay
while True:
    wins += 1
    print(f"Pokémon catched: {wins}")
    replay_prompt = input("Would you like to play again? (Y) / (N) => ").upper()
    if replay_prompt == "Y":
        clear()
        play_game()
    elif replay_prompt == "N":
        clear()
        sys.exit()
