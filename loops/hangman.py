# Our main hangman program

import random
from hangman_list import word_list

print("Welcome to hangman game, lets get started!")
chosen_word = random.choice(word_list)
# print("Solution: {}".format(chosen_word))
lives = 5
display = []
for _ in chosen_word:
    display += "_"
print(display)

end_game = False
while not end_game:
    guess = input("Guess a letter: ").lower()
    for pos in range(len(chosen_word)):
        letter = chosen_word[pos]
        if letter == guess:
            display[pos] = letter
    if guess not in chosen_word:
        lives -= 1
        print("{} lives remaining".format(lives))
        if lives == 0:
            end_game = True
            print("You lose")
    print(display)

    if "_" not in display:
        end_game = True
        print("You win")
