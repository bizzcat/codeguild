len([1, 2, 3, 4, 6, 7, 10])     # 7 - for seven values in list
reversed([1, 2, 5, 3])          # [3, 5, 2, 1]
sorted([5, 3, 1, 2])            # [1, 2, 3, 5]

set([1, 2, 2])                  # {1, 2}
list({1, 2})                    # [1, 2]
tuple([1, 2, 2])




    product_to_price_cents = {
        'apple': 99,
        'pear': 150
    }
    product_to_price_dollars = {
       product: price_cents / 100
       for product, price_cents
       in product_to_price_cents.items()
    }

    {value: key for key, value in d.items()}

    prices_in_dollars = [1.50, 0.75]
    prices_in_cents = [dollar_val * 100 for dollar_val in prices_in_dollars]

    words_in_document = {'the', 'cat', 'hat'}
    uppercase_words_in_document = {word.upper() for word in words_in_document}

    (1, 2) + (3, 4) == (1, 2, 3, 4)

len([1, 2, 3]) # 3
reversed([1, 2, 2]) # [2, 2, 1]
sorted([5, 3, 1, 2]) # [1, 2, 3, 5]

set([1, 2, 2]) # {1, 2}
list({1, 2}) # [1, 2]
tuple([1, 2, 2]) # (1, 2, 2)
dict([('apple', 99), ('pear', 150)])
dict.items()

dict(somedict.items()) == somedict

enumerate(['a', 'b', 'c']) # [('a', 0), ('b', 1), ('c', 2)]
# (item, index)

    names = ['Al', 'Alice']
    for name, i in enumerate(names):
        print('Name #{}: {}'.format(i, name))

zip(['apple', 'pear'], [99, 150]) # [('apple', 99), ('pear', 150)]

range(5) # [0, 1, 2, 3, 4]
for i in range(5):
    whatever
