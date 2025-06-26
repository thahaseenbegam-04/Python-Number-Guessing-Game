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
