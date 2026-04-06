import random

print("Welcome to Number Guessing Game!")
secret_number = 5
attempts = 5

while attempts > 0:
    user_input = input("Guess a number between 1 and 10: ")

    if not user_input.isdigit():
        print("Invalid input! Please enter a number.")
        continue

    guess = int(user_input)
    attempts -= 1

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Correct!")
        break

    print("Attempts left:", attempts)

if attempts == 0:
    print("Game Over! Number was:", secret_number)
else:
    print("Congratulations! You guessed the number in", 5 - attempts, "attempts.")