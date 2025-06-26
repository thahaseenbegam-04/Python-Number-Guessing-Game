# Python-Number-Guessing-Game
A simple number guessing game using Python

# Number Guessing Game 🎯

A beginner-friendly Python project where the user guesses a randomly generated number between 1 and 100.

## How to Run

1. Make sure you have Python installed
2. Run the script:

FULL CODE:

import random
number = random.randint(1, 100)
tries = 0
while True:
    guess = int(input("Guess the number (1-100): "))
    tries += 1
    if guess == number:
        print(f"Correct! You guessed it in {tries} tries.")
        break
    elif guess < number:
        print("Too low.")
    else:
        print("Too high.")

        
🔍 STEP-BY-STEP EXPLANATION

1. import random
This imports Python’s random module which allows us to generate random numbers.

2. number = random.randint(1, 100)
This line picks a random number between 1 and 100 (inclusive).

This is the secret number the user has to guess.

3. tries = 0
A counter to keep track of how many guesses the user takes.

4. while True:
This creates an infinite loop — it will only stop when the correct guess is made and we break it.

It keeps asking the user for input until the right number is guessed.

5. guess = int(input("Guess the number (1-100): "))
Takes input from the user.

input() returns a string, so we use int() to convert it to an integer.

6. tries += 1
Every time the user enters a guess, we increment the guess count by 1.

7. if guess == number:
Checks if the user's guess is correct.

If yes: 🎉 congratulates them and shows the number of tries.

Then, break stops the loop.

8. elif guess < number:
If the guess is too low, it gives a hint.

9. else:
If it's too high, it also gives a hint.


🧪 Sample Run:

Guess the number (1-100): 50
Too low.
Guess the number (1-100): 75
Too high.
Guess the number (1-100): 60
Too low.
Guess the number (1-100): 68
Correct! You guessed it in 4 tries.
