import random

secret_number = random.randint(1, 100)
attempts = 0

print("================================")
print("     NUMBER GUESSING GAME")
print("================================")
print("Guess a number between 1 and 100!")

while True:
    guess = int(input("Enter your guess: "))
    attempts = attempts + 1

    if guess < secret_number:
        print("Too Low! Try a bigger number.")
    elif guess > secret_number:
        print("Too High! Try a smaller number.")
    else:
        print("Congratulations! You won!")
        print("Total attempts:", attempts)
        break