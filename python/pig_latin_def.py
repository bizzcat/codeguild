# DEFINITIONS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def retrieve_sentence():
    """
    Input: user input
    Arguements: 0
    Output: string sentence form
    Return value: user sentence in string format
    """
    print ('\nPlease enter the sentence you would like to convert!\n')
    sent_to_convert = input('')
    return sent_to_convert

def split_sentence(sent_to_convert):
    '''Input: any sentence -- Output: list of split words based off input'''
    splitted = sent_to_convert.split()
    return splitted
#
# english_words
#
# def f_sent_latinizer():
#
# def f_word_latinizer():
#
#

def word_latinizer(splitted):
    '''Input: split compilation of words -- Output: pig latinized words in list form as output'''
    pig_splitted = []
    vowels = ['a', 'e', 'i', 'o', 'u']
    for word in splitted:
        word = word.lower()
        if word[0] in vowels:
            pig_word = word + 'ay'
            pig_splitted.append(pig_word)
        else:
            pig_word = word[1:] + word[0] + 'ay'
            pig_splitted.append(pig_word)
    return pig_splitted

def pig_splitted_to_joined(pig_splitted):
    '''Input: split list of words -- Output: a punctually corrected sentence in string format'''
    pig_joined = str((' '.join(pig_splitted)).capitalize()) + '.\n'
    return pig_joined

def pig_joined_to_finished_sentence(pig_joined):
    '''Input: any sentence -- Output: presentation of 'Your sentence >>>' added to sentence'''
    finished_sentence = '\n\nYour sentence >>> ' + pig_joined
    return finished_sentence

def print_sentence(finished_sentence):
    '''Input: any sentence -- Output: that sentence printed'''
    print ('\n\n', finished_sentence, '\n')

def continue_or_not():
    '''Input: user input as Y or N -- Output: Boolean value where user input 'Y' is True, and all else is False'''
    print ('\n\n\n\n\n\n\n\n\n\nWould you like to convert a sentence? (Y or N)\n')
    answer = input('> ').capitalize()
    return answer == 'Y'

# PROGRAM INITIATION ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print ('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
print('Welcome to the Pig Latin word sequencer!\n(Elcomeway to the Ipgay Atinlay Ordway Equencersay!)')

cont = continue_or_not()
while cont:
    sent_to_convert = retrieve_sentence()
    splitted = split_sentence(sent_to_convert)
    pig_splitted = word_latinizer(splitted)
    pig_joined = pig_splitted_to_joined(pig_splitted)
    finished_sentence = pig_joined_to_finished_sentence(pig_joined)
    print (finished_sentence)
    cont = continue_or_not()

quit()
