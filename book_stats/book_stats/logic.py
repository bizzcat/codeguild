
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


file_name = '/Users/Kyo/codeguild/book_stats/book_stats/gitanjali.txt'
sample_text = open_text_file(file_name)
word_list = file_into_word_list(sample_text)
word_dict_with_count = list_into_word_count_dict(word_list)
