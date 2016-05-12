# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ IMPORTS & INDICES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import random
punctuation_list = ['.', ',', '\'', '"', '-', '_', ';', ':', '!', '?', '[]', '()', ' ', '=', '+', '~']
punctuation_string = '.,\'"-_;:!?[]() =+*~'

file_name = 'gitanjali.txt'

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ WORD COUNT FUNCTIONS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def get_file_name_from_user():
#     print ('Please select the .txt file you would like to analyse:')
#     file_name = input('')
#     return file_name

def open_text_file(file_name):
    with open(file_name) as sample_text_file:
        sample_text = sample_text_file.readlines()
    return sample_text

def file_into_word_list(sample_text):
    word_list = ''.join(sample_text).lower().split()
    return word_list

def list_into_word_count_dict(word_list):
    word_dict_with_count = {}
    for word in word_list:
        word_dict_with_count.update(dict(zip([word], [word_list.count(word)])))
    return word_dict_with_count

def reverse_keys_and_values(word_dict_with_count):
    value_key_pairing = [(v, k) for (k, v) in word_dict_with_count.items()]
    return value_key_pairing

def rank_value_key_pairing(value_key_pairing):
    value_key_pairing.sort(reverse = True)
    # ''.join(value_key_pairing)
    return value_key_pairing

def get_word_probability(word_list, total_word_count):
    word_dict_with_probability = {}
    for word in word_list:
        word_dict_with_probability.update(dict(zip([word], [((word_list.count(word)) / total_word_count)])))
    return word_dict_with_probability

def get_largest_word(word_list):
    largest_word = max(word_list, key=len)
    return largest_word

def get_total_word_count(word_list):
    total_word_count = len(word_list)
    return total_word_count

def get_total_unique_words(word_dict_with_count):
    unique_words = len(word_dict_with_count.keys())
    return unique_words

def display_top_ten_words(value_key_pairing, file_name):
    placement = 1
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print("Top 10 words in", file_name +":\n")
    for k, v in value_key_pairing[0:10]:
        print ("\n\t" + str(placement) + " :   '" + v + "'\twas used", str(k), "times.")
        placement += 1
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ PAIR COUNT FUNCTIONS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def get_pair_list(word_list):
    pair_list = list(zip(word_list, word_list[1:]))
    return pair_list

def count_pairs_in_list(pair_list):
    pair_list_with_count = []
    for pair in pair_list:
        pair_list_with_count.append((pair[0], pair[1], pair_list.count(pair)))
    return pair_list_with_count

# def get_pair_probability(pair_list_with_count):
def list_into_empty_dict(word_list):
    empty_dict = {}
    for word in word_list:
        empty_dict.update(dict(zip([word], [{}])))
    return empty_dict


def get_dict_of_pairs(pair_list_with_count, empty_dict):
    pair_dict_with_count = empty_dict
    for pair in pair_list_with_count:
        pair_dict_with_count[pair[0]].update(dict(zip([pair[1]], [pair[2]])))
    return pair_dict_with_count

def get_values_first_pair_list(pair_list_with_count):
    values_first_pair_list = [(c, a, b) for (a, b, c) in pair_list_with_count]
    return values_first_pair_list

def sort_values_first_pair_list(values_first_pair_list):
    pairs_sorted_by_values = sorted(values_first_pair_list, reverse=True)
    return pairs_sorted_by_values

def sorted_pairs_into_dict(pairs_sorted_by_values):
    sorted_pairs_dict = {}
    for pair in pairs_sorted_by_values:
        sorted_pairs_dict[str(pair[0])].update(dict(zip([pair[1], [pair[2]]])))
#WHAT NEEDS TO BE DONE NEXT IS TO ELIMINATE DUPLIACTES IN THE
#TOP SCORING PAIRS, SO THAT WHEN THE TOP TEN ARE DISPLAYED IT ACTUALLY SHOWS THE TOP TEN
#AFTER THAT THE PAIR PROBABILITIES NEED TO BE PERCENTIFIED AND THEN RANKED INTO TOP 3
#THEN A DISPLAY NEED TO BE MADE THAT CAN GUIDE THE USER TO WRITING A N-O-T-E BASED OFF
#THE AUTHORS STYLE OF WRITING.


def print_top_pairs(pairs_sorted_by_values):
    print ("Top ten pairs are: ", pairs_sorted_by_values[0:10])

def get_pair_sums(values_first_pair_list):
    pair_sums = []
    for a, b, c in values_first_pair_list:
        pair_sums.append(a)
    pair_sums = sorted(pair_sums, reverse=True)
    return pair_sums

def get_user_word():
    user_word = input('What word would you like to find a probable adjacent word to?  >>>  ')
    return user_word

def supply_user_adjacent_words(user_word, pair_dict_with_count):
    print (pair_dict_with_count[user_word])

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ PAIR PROB FUNCTIONS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def get_total_pairs(pair_list):
    total_pairs = len(pair_list)
    return total_pairs

def count_pair_prob(total_pairs, pair_list_with_count):
    pair_list_with_prob = {}
    for a, b, c in pair_list_with_count:
        if (a, b) not in pair_list_with_prob:
            pair_list_with_prob[(a, b)] = c
    return pair_list_with_prob

def top_pairs(pair_list_with_prob):
    top_pair_list = []
    n = 10
    while n > 0:
        for k, v in pair_list_with_prob:
            t
            top_pairs.append()
            n -=1



# def count_pair_prob(total_pairs, pair_list_with_count):
#     pair_list_with_prob = {}
#     for a, b, c in pair_list_with_count:
#         if (a, b) not in pair_list_with_prob:
#             pair_list_with_prob[str(c)] = (dict(zip([a], [b])))
#     return pair_list_with_prob

# def count_pair_prob(total_pairs, pair_list):
#     pair_list_with_prob = []
#     for pair in pair_list:
#         pair_list_with_prob.append((pair[0], pair[1], (pair_list.count(pair) / total_pairs)))
#     return pair_list_with_prob

# def count_pair_prob(total_pairs, values_first_pair_list):
#     pair_list_with_prob = {}
#     for a, b, c in values_first_pair_list:
#         if  not in pair_list_with_prob:
#             (pair_list_with_prob[str(a)]).update(dict(zip([b], [c])))
#     return pair_list_with_prob
# def format_pair_prob(pair_list_with_prob):

# maybe I should put the list values last and put into dict, and then sort by values afterwards, as to remove duplicates

#
#  pair_dict_with_count = get_dict_of_pairs(pair_list_with_count, empty_dict)
# >>> pair_dict_with_count


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ CALLING FUNCTIONS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
file_name = get_file_name_from_user()

sample_text = open_text_file(file_name)

word_list = file_into_word_list(sample_text)

word_dict_with_count = list_into_word_count_dict(word_list)

total_word_count = get_total_word_count(word_list)
total_unique_words = get_total_unique_words(word_dict_with_count)



value_key_pairing = reverse_keys_and_values(word_dict_with_count)

value_key_pairing = rank_value_key_pairing(value_key_pairing)

# display_top_ten_words(value_key_pairing, file_name)

total_word_count = get_total_word_count(word_list)
total_unique_words = get_total_unique_words(word_dict_with_count)

# ------------------
pair_list = get_pair_list(word_list)
pair_list_with_count = count_pairs_in_list(pair_list)
empty_dict = list_into_empty_dict(word_list)
pair_dict_with_count = get_dict_of_pairs(pair_list_with_count, empty_dict)
# user_word = get_user_word()
# supply_user_adjacent_words(user_word, pair_dict_with_count)

values_first_pair_list = get_values_first_pair_list(pair_list_with_count)
pairs_sorted_by_values = sort_values_first_pair_list(values_first_pair_list)
# print_top_pairs(pairs_sorted_by_values)
pair_sums = get_pair_sums(values_first_pair_list)

# ------------------

total_pairs = get_total_pairs(pair_list)
# pair_list_with_prob = count_pair_prob(total_pairs, pair_list)
pair_list_with_prob = count_pair_prob(total_pairs, pair_list_with_count)
print (pair_list_with_prob)

# --------------------- Practice Area ------------------------------------
# This is that moment where I got through the initial challenge of pursuing my quest. Now leaving it will be more challenging, and less rewarding. I am increasingly identifying with myself through referencing this journey. My next big challenge will be both out of Portland successfully and into SF successfully.. I need to begin working now, 3 months prior to my goal of when to leave
# the people sitting next to me are the dumbest ofofs around i wish this guy woulds top saying ;in ISrael: this and this and this..........' it's kind of funny because he wont shut up about it. I really enjoy my conversation with Jess today and is the first time I feel i have truly conencted to others. There is really no other better medicine than to have a few good beers with a deeply knowledgable and uniquely vantaged friend whpo has gone through and triumphed over many struggles. What a beautiful human being. She understood me like no one else has in thelast few weeks, and not only listened to me deeply, but also
# pair_list = zip(word_list, word_list[1:])
#
# pair_dict = {}
#
# for k, v in pair_list:
#     pair_dict.update(dict(zip([k], [v])))
#
#
# word_pair_dict = {}
# for word in word_list:
#
#
# total_word_count = len(word_list)
# total_unique_words = len(word_dict_with_count.keys())




# I dont know what oiw ant to do but if if id I would put ()()

#
# def get_word_count(word):
#     return word_rank[word]
#
# words = word_dict_with_count.keys()
#
# print(sorted(words, key=word_dict_with_count.get))
#
#
# tuple_of_dict
#
# def get_second(pair):
#     return pair[1]
#
# print(sorted(tuple_of_dict, key=get_second(), reverse=True))
#










# def eliminate_punctuation(word_list):
#     for word in word_list:
#         word = word.strip('.,\'"-_:;*!?[]() =+&~/')
#     return word_list
#
#
# def eliminate_punctuation():
#
# #
# def eliminate_punctuation(word_list):
#     for word in word_list:
#         for punctuation in punctuation_list:
#             if punctuation in word:
#                 word = word.remove(punctuation)
#             return word
# #
# #
# #
#




# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ CALLING FUNCTIONS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~





#
#
# def text_into_sentence_list(sample_text):
#     sentence_list = []
#     for sentence in sample_text:
#         sentence = sentence.strip()
#         sentence_list.append(sentence)
#     return sentence_list
#
# def sentence_list_into_word_list(sentence_list):
#     word_list = []
#     for word in sentence_list:
#         word = word.strip()
#         word_list.append(word)
#     return word_list




# text_sentences_list = (sample_text.strip()).split()


#
# word_list = []
#
# with open('gitanjali.txt') as gitanjali_data:
#     for word in gitanjali_data:
#         word_list.append((word.lower()).strip().split())
#
# punctuation = ['.', ',', '\'', '"', '-', '_', ';', ':', '!', '?', '[]', '()', ' ', '=', '+', '~']
# for punctuation[0] in words:
#     no_punctuation = words.remove(punctuation[0])
#
# print (no_punctuation)
#
# for the in word_list:
#     sum_of_the = 'the'.count()
#     print(sum_of_the)

# sum_of_the = word_list.count('the')
# print (sum_of_the)

# print (words_listed)
# word_dict = {}
# for word in word_list:
#     word, sum_of_word =
#
#
# item_gitanjali = word_list.items()
# print (item_gitanjali)
#
# word_length = len(words)
# print (word_length)

# Well this is going to be a challenging day indeed I wish I could eaelly improve my typing skill so that I could become a better and faster writer of letters and code. COde is fun because it allows me to process processes, put a form to them and make them infinitely executable. How fun is thaT? I mean, anything you want to be done, in life at all, if you put in enough work (which is in fact very little, perhaps only a few hours) you could have that entire process optimized by code and eliminates the effort you would previosuly have to exert to accomplish a goal, while still accomplishing that goal, and often times with betetr results because computation does not err, only the code that you create. Meaning, if there's a rpobem, it's most certainly your fault! hah!.



























#
