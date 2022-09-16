import random
from hangman_art import stages, logo
from hangman_words import word_list

print(logo)
random_word = random.choice(word_list)
print(random_word)
word_len = len(random_word)
game_over = False
lives = len(stages) - 1

display = []
for _ in random_word:
    display.append("_")
print(display)

while not game_over:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You've already guessed {guess}")
    for i in range(word_len):
        letter = random_word[i]
        if letter == guess:
            display[i] = letter
    if guess not in random_word:
        print("Guessed word" + " " + guess + " " + "is not in the word")
        lives -= 1
        if lives == 0:
            game_over = True
            print("You loose")

    print(display)

    if "_" not in display:
        game_over = True
        print("You win")

    print(stages[lives])