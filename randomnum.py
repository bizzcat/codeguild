import random

number = random.randint(1, 100)

print ("Guess my number between 1 and 100")
guess = int(input("> "))

if guess == number:
    print ("Correct!")

elif guess > number:
    print ("Lower! Guess again")

elif guess < number:
    print ("Higher! Guess again")

while guess != number:
    guess = int(input())

    if guess == number:
        prompt = "Correct!"

    elif guess > number:
        prompt = "Lower! Guess again"

    elif guess < number:
        prompt = "Higher! Guess again"

    print (prompt)


    
