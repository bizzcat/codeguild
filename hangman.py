# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ PROGRAM INSTRUCTIONS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
Pick a secret word. Prompt the user: Show the user blank spaces
for every un-guessed letter in that word and the actual letter
for those which have been guessed correctly. Show the user a
list of previously guessed incorrect letters. Let the user enter
a new letter, then repeat. Let the user make only up to six mistakes.

If the word was "cat", the prompt should look something like:
Word: _A_
Misses: B, D
Mistakes Remaining: 4

Advanced:
Try to minimize the number of variables you save outside of
your guessing loop. I claim you can do it in two variables.
In addition to printing out the the blank spaces, try printing
out a stick figure as mistakes are made.
"""

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ IMPORTS & INDICES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import os
import time

mystery_word = 'PENCIL'
listed_mystery_word = ['P', 'E', 'N', 'C', 'I', 'L']

word_with_hidden_letters = ['_', '_', '_', '_', '_', '_']
user_facing_word_display = ''.join(word_with_hidden_letters)

wrong_guesses = []
user_facing_wrong_guesses = str(' '.join(wrong_guesses))

guesses_left = 6
user_facing_guesses_left = str(guesses_left)

victory = False
defeat = False

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ FUNCTIONS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def display_welcome_message():
    """
    Input:
    Arguements:
    Output:
    Return value:
    """
    os.system('clear')
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print ("\nWelcome to Hangman!\n")
    print ("\n\nIn this game you are allowed six attempts to guess a word. \nAfter six failed attempts some poor guy named Steve will be in for a hanging. \nSo guess correctly... don't kill Steve.\n")
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

def begin_game():
    answer = input("\nBegin? (Y or N) \t > > >  ").upper()
    return answer == 'Y'

def display_correct_incorrect_and_remaining(user_facing_word_display, wrong_guesses, guesses_left):
    """
    Input:
    Arguements:
    Output:
    Return value:
    """
    os.system('clear')
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print ("\nMystery word:\t\t       ", user_facing_word_display, "\n")
    print ("\nUsed guesses:\t\t       ", str(' '.join(wrong_guesses)), "\n")
    print ("\nGuesses left:\t\t       ", guesses_left, "\n")
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

def take_user_guess():
    """
    Input:
    Arguements:
    Output:
    Return value:
    """
    user_letter_guess = (input("\nYour letter:\t\t > > >  ")).upper()
    return user_letter_guess

def scan_word_for_user_guess(user_letter_guess, mystery_word):
    """
    Input:
    Arguements:
    Output:
    Return value:
    """
    if user_letter_guess in mystery_word:
        result_of_scan = 'correct'
        return result_of_scan
    if user_letter_guess not in mystery_word:
        result_of_scan = 'incorrect'
        return result_of_scan

def correct_result_action(mystery_word, user_letter_guess, user_facing_word_display):
    """
    Input:
    Arguements:
    Output:
    Return value:
    """
    index_of_correct_letter = (mystery_word).index(user_letter_guess)
    user_facing_word_display = (user_facing_word_display[:index_of_correct_letter] + user_letter_guess + user_facing_word_display[(index_of_correct_letter + 1):])
    return user_facing_word_display

def update_wrong_guesses(wrong_guesses, user_letter_guess):
    """
    Input:
    Arguements:
    Output:
    Return value:
    """
    wrong_guesses.append(user_letter_guess)
    return wrong_guesses

def update_guesses_left(guesses_left):
    """
    Input:
    Arguements:
    Output:
    Return value:
    """
    guesses_left = (guesses_left - 1)
    return guesses_left

def scan_for_defeat(guesses_left):
    """
    Input:
    Arguements:
    Output:
    Return value:
    """
    if guesses_left == 0:
        defeat = True
        return defeat

def scan_for_victory(user_facing_word_display):
    """
    Input:
    Arguements:
    Output:
    Return value:
    """
    if user_facing_word_display == 'PENCIL':
        victory = True
        return victory

def display_defeat(mystery_word):
    """
    Input:
    Arguements:
    Output:
    Return value:
    """
    os.system('clear')
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print ("\n\nYou have been defeated!\n\n")
    print ("\nMystery word was:\t  ", mystery_word + "!\n\n")
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    time.sleep(5)
    os.system('clear')
    end_game()

def display_victory(mystery_word):
    """
    Input:
    Arguements:
    Output:
    Return value:
    """
    os.system('clear')
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print ("\n\nYou are victorious!\n\n")
    print ("\nMystery word was:\t  ", mystery_word + "!\n\n")
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    time.sleep(5)
    os.system('clear')
    end_game()

def end_game():
    os.system('clear')
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print ("\n\n\n\nPreparing for next round...\n\n\n\n")
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    time.sleep(1)
    os.system('clear')
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print ("\n\n\n\nPreparing for next round...\n\n\n\n")
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    time.sleep(1)
    os.system('clear')
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print ("\n\n\n\nPreparing for next round......\n\n\n\n")
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    time.sleep(1)
    os.system('clear')
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print ("\n\n\n\nPreparing for next round.........\n\n\n\n")
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    time.sleep(1)
    os.system('clear')
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print ("\n\n\n\nPreparing for next round............\n\n\n\n")
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    time.sleep(1)
    os.system('clear')
    cont = False
    return cont

def try_again(cont):
    os.system('clear')
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print ("\n\n\n\nHow fun! Try again?\n\n\n\n")
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    answer = input("\n(Y or N):\t\t     > > >  ").upper()
    if answer == 'Y':
        cont = True
    if answer == 'N':
        cont = False
    return cont

def outgoing_message():
    os.system('clear')
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print ("\n\n\n\nSee you next time!!!\n\n\n\n")
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ CALLING FUNCTIONS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
display_welcome_message()
cont = begin_game()

while cont:
    display_correct_incorrect_and_remaining(user_facing_word_display, wrong_guesses, guesses_left)
    user_letter_guess = take_user_guess()
    result_of_scan = scan_word_for_user_guess(user_letter_guess, mystery_word)
    if result_of_scan == 'correct':
        user_facing_word_display = correct_result_action(mystery_word, user_letter_guess, user_facing_word_display)
    elif result_of_scan == 'incorrect':
        wrong_guesses = update_wrong_guesses(wrong_guesses, user_letter_guess)
        guesses_left = update_guesses_left(guesses_left)
    defeat = scan_for_defeat(guesses_left)
    victory = scan_for_victory(user_facing_word_display)
    if victory:
        display_victory(mystery_word)
    if defeat:
        display_defeat(mystery_word)
    if victory or defeat:
        cont = try_again(cont)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ PLAY AGAIN? ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        if cont:
            mystery_word = 'RANGER'
            listed_mystery_word = ['R', 'A', 'N', 'G', 'E', 'R']

            word_with_hidden_letters = ['_', '_', '_', '_', '_', '_']
            user_facing_word_display = ''.join(word_with_hidden_letters)

            wrong_guesses = []
            user_facing_wrong_guesses = ' '.join(wrong_guesses)

            guesses_left = 6
            user_facing_guesses_left = str(guesses_left)

            victory = False
            defeat = False

outgoing_message()
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ FINISH ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

quit()























#
