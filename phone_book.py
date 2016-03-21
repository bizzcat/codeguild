import os

d_book = {}

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
        name = input('> ').capitalize()
        os.system('clear')

        print ('Please add your phone number:')
        number = input('> ')
        os.system('clear')

        if name in d_book:
            print ("Please choose a name that does not already exist.")

        else:
            d_book[name] = number
            print ('Added', name, '-', number, 'to phone book.', '\n\n')
            action = 'Z'

        action = 'Z'

    if action == 'B':
        print ('Please enter the name for the phone number you would like to change:',)
        name = input('> ').capitalize()
        os.system('clear')

        if name in d_book:
            print ('Please the number you would like to change for', name, ':')
            new_number = input('> ')
            os.system('clear')
            d_book[name] = new_number
            print ('Great!', new_number, 'has been updated to', name, '\n\n')

        else:
            print ('Name does not exist in phonebook.', '\n\n')

        action = 'Z'

    if action == 'C':
        print ('Enter the name you would like the phone number for:')
        search_name = input('> ').capitalize
        os.system('clear')

        if search_name in d_book:
            print ('Aha! Found', search_name, 'in phonebook.\n')
            print ('The phone number for', search_name, 'is:')
            print (d_book[search_name], '\n\n')

        else:
            print ('Name not found.', '\n\n')

        action = 'Z'

    if action == 'D':
        print ('Printing the phonebook:')
        print (d_book, '\n\n')
        action = 'Z'

    if action == 'Q':
        cont = False

    else:
        cont = True

quit()






#
