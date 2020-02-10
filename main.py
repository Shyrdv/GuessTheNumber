import random

hidden = random.randrange(1, 20)
guess = int(input("Enter your guess: "))

while guess != hidden:
    if guess == hidden:
        break
    elif guess < hidden:
        print("Number is too low!")
        guess = int(input("Enter your guess: "))
    else:
        print("Number is too high!")
        guess = int(input("Enter your guess: "))
print("You got it!")

