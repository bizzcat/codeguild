import random

number = random.randint(1, 100)

print ("Guess my number between 1 and 100")

guess = -1
while guess != number:
    guess = int(input())

    if guess == number:
        prompt = "Correct!"
    elif guess > number:
        prompt = "Lower! Guess again"
    elif guess < number:
        prompt = "Higher! Guess again"

    print (prompt)

guess_count = guess += 1
if guess_count == 6
    print "Out of guesses!"
