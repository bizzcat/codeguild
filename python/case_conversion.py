# Practice: Case Conversion
# Write a program that prompts the user for a word in snake_case, then converts and prints it out in CamelCase. Also do
# the reverse conversion.
#
# Advanced
#
# Write functions to handle kebab-case and CONSTANT_CASE.
# Write functions to auto-detect which case is input.
# Automatically print out all other cases on input.
# Come up with a original-case-agnostic intermediate representation.

import re
#
# def word_to_camel(word):
#     return ''.join(x.capitalize() or '_' for x in word.split('_'))
#
# def word_to_snake(word):
#     string = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', word)
#     print(string)
#     return re.sub('([a-z0-9])([A-Z])', r'\1_\2', string).lower()

# string = re.sub('([A-Z][a-z]+)', r' /1 ', word)

def get_word():
    return input('Your word for conversion:  ')

def word_to_title(word):
    return word.title().replace('_', ' ').replace('-', ' ')

def title_to_camel(title_word):
    return title_word.replace(' ', '').replace('_', '').replace('-', '')

def title_to_snake(title_word):
    return title_word.lower().replace(' ', '_').replace('-', '_')

def title_to_constant(title_word):
    constant_word = title_word.upper().replace(' ', '_').replace('-', '_')
    return constant_word

def title_to_kebab(title_word):
    kebab_word = title_word.lower().replace(' ', '-').replace('_', '-')
    return kebab_word

def identify_word_case(word):
    if word == word_to_title(word): return "\nOriginal Word In Title Format"
    title_word = word_to_title(word)
    if word == title_to_camel(title_word): return "\nOriginalWordInCamelCase"
    if word == title_to_snake(title_word): return "\noriginal_word_in_snake_case"
    if word == title_to_constant(title_word): return "\nORIGINAL_WORD_IN_CONSTANT_CASE"
    if word == title_to_kebab(title_word): return "\noriginal-word-in-kebab-case"


def main():
    word = get_word()
    print("\nWord: " + word)
    print(identify_word_case(word))
    title_word = word_to_title(word)
    print("\nTitle word: " + title_word)
    camel_word = title_to_camel(title_word)
    print("\nCamel word: " + camel_word)
    snake_word = title_to_snake(title_word)
    print("\nSnake word: " + snake_word)
    constant_word = title_to_constant(title_word)
    print("\nConstant word: " + constant_word)
    kebab_word = title_to_kebab(title_word)
    print("\nKebab word: " + kebab_word)




if __name__ == "__main__":
    main()
