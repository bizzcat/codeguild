# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ INITIAL SETUP ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ********************************************* IMPORTS, INDICES, VARIABLES *********************************************
import random



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ DEFINING FUNCTIONS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ********************************************* FILE FUNCTIONS *********************************************
def get_file_name_from_user():
    print ('Please select the .txt file you would like to analyse:')
    file_name = input('')
    return file_name
def file_into_strings(file_name):
    with open(file_name) as text_file:
        line_strings = text_file.readlines()
    return line_strings

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ WORD COUNT FUNCTIONS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def file_strings_into_word_list(file_name):
    word_list = ''.join(sample_text).lower().split()
    return word_list
def list_into_word_count_dict(word_list):
    word_to_count = {}
    for word in word_list:
        word_to_count.update(dict(zip([word], [word_list.count(word)])))
    return word_to_count
def reverse_keys_and_values(word_to_count):
    count_to_word = [(v, k) for (k, v) in word_to_count.items()]
    count_to_word = count_to_word.sort(reverse = True)
    return count_to_word
def get_total_word_count(word_list):
    total_word_count = len(word_list)
    return total_word_count
def update_count_with_probability(word_list, total_word_count):
    word_probability_dict = {}
    for word in word_list:
        word_probability_dict.update(dict(zip([word], [((word_list.count(word)) / total_word_count)])))
    return word_probability_dict
def


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ CALLING FUNCTIONS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ********************************************* FILE FUNCTIONS *********************************************
file_name = get_file_name_from_user()
line_strings = file_into_line_strings(file_name)

# ********************************************* FILE FUNCTIONS *********************************************
word_list = file_strings_into_word_list(file_name)
word_to_count = list_into_word_count_dict(word_list)
count_to_word = reverse_keys_and_values(word_to_count)
total_word_count = get_total_word_count(word_list)
word_probability_dict = update_count_with_probability(word_list, total_word_count)



























#
