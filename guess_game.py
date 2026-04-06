import random

secret_number = random.randint(1, 10)
attempts = 5

while attempts > 0:
    try:
        guess = int(input("Guess a number between 1 and 10: "))
    except:
        print("Invalid input!")
        continue

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