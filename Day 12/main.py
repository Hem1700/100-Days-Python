# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).


from art import logo
import random

print(logo)
print("Welcome to the Number Guessing Game")
print("I am thinking of a number between 1 and 100.")
difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if difficulty_level == 'easy':
    lives = 10
else:
    lives = 5
random_number = random.randint(1, 100)

def guess_game(lives):
    while lives != 0:
        guess = int(input("Guess any number between 1 and 100:\n "))
        if guess == random_number:
            print("You guessed it right. You win")
        elif guess != random_number:
            print("It's wrong. Try again.")
            lives -= 1
            print("You have " + "" + str(lives) + " " + "lives remaining")
    if lives == '0':
        print("You've run out of guesses, you loose")


guess_game(lives)
