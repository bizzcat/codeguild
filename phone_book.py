# IMPORTS & INDICES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import os
import time
phonebook = {}

# FUNCTIONS LIST ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def clear_terminal():
    time.sleep(1)
    os.system('clear')

def welcome_to_phonebook():
    """
    Inputs: none
    Arguements: none
    Return Value: none
    Outputs: prints a welcoming message to PhoneBook
    """
    print ('Welcome to PhoneBook. Your locally developed, simplified contact organizer. Name and phonenumber only, none of that modern day noise.')


def print_directory():
    print ('What would you like to do?')
    print ('A -',, 'Add a name and phone number')
    print ('B -',, 'Change a phone number')
    print ('C -',, 'Find a phone number using a name')
    print ('D -',, 'Print the phonebook')
    print ('Q -',, 'Exit')

def retrieve_name():
    print ('Please type in name:')
    name = input('> ').upper()
    return name

def retrieve_number():
    print ('Please type in phone number:')
    number = input('> ')
    return number

def add_name_to_phonebook(name):
    if name in phonebook:
        print ("Please choose a name that does not already exist.")



def add_number_to_phonebook():

def change_number():

def find_number_by_name():

def print_whole_book():

def exit():

def call_functions_off_directory():





# CALLING FUNCTIONS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~









cont = True
while cont:
    print ('What would you like to do?')
    print ('A -', 'Add a name and phone number')
    print ('B -', 'Change a phone number')
    print ('C -', 'Find a phone number using a name')
    print ('D -', 'Print the phonebook')
    print ('Q -', 'Exit')
    action = input('> ').upper()
    print ('\n\n')
    os.system('clear')

    if action == 'A':
        print ('Please add your name:')
        name = input('> ').upper()
        os.system('clear')

        print ('Please add your phone number:')
        number = input('> ')
        os.system('clear')

        if name in phonebook:
            print ("Please choose a name that does not already exist.")

        else:
            phonebook[name] = number
            print ('Added', name, '-', number, 'to phone book.', '\n\n')
            action = 'Z'

        action = 'Z'

    if action == 'B':
        print ('Please enter the name for the phone number you would like to change:',)
        name = input('> ').capitalized()
        os.system('clear')

        if name in phonebook:
            print ('Please the number you would like to change for', name, ':')
            new_number = input('> ')
            os.system('clear')
            phonebook[name] = new_number
            print ('Great!', new_number, 'has been updated to', name, '\n\n')

        else:
            print ('Name does not exist in phonebook.', '\n\n')

        action = 'Z'

    if action == 'C':
        print ('Enter the name you would like the phone number for:')
        search_name = input('> ').capitalized
        os.system('clear')

        if search_name in phonebook:
            print ('Aha! Found', search_name, 'in phonebook.\n')
            print ('The phone number for', search_name, 'is:')
            print (phonebook[search_name], '\n\n')

        else:
            print ('Name not found.', '\n\n')

        action = 'Z'

    if action == 'D':
        print ('Printing the phonebook:')
        print (phonebook, '\n\n')
        action = 'Z'

    if action == 'Q':
        cont = False

    else:
        cont = True

quit()






#
