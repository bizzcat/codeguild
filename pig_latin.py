print ('\n')
print('Welcome to the Pig Latin word sequencer!\n\nElcomeway to the Ipgay Atinlay Ordway Equencersay!\n')

cont = True

while cont:
    print ('Please enter the sentence you would like to convert!\n')
    to_convert = input('')

    splitted = to_convert.split()
    pig_splitted = []
    vowels = ['a', 'e', 'i', 'o', 'u']

    for word in splitted:
        word = word.lower()
        print (word[0])

        if word[0] in vowels:
            pig_word = word + 'ay'
            pig_splitted.append(pig_word)

        else:
            pig_word = word[1:] + word[0] + 'ay'
            pig_splitted.append(pig_word)


    pig_sentence = '>>> ' + (' '.join(pig_splitted)).capitalize() + '.'
    print ('\n')
    print (str(pig_sentence))

    print ('\n\nWould you like to convert another sentence? (Y or N)')
    answer = input('> ').capitalize()
    print (answer)

    if answer == 'Y':
        cont = True
        print ('\n')

    if answer == 'N':
        cont = False
        print ('\n')

quit()
