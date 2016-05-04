
import statistics

raw_business_data = [
  {
    'business_name': 'Salt & Straw',
  },
  {
    'business_name': 'Voodoo Donuts',
  },
]
raw_user_data = [
  {'user_name': 'Abby'},
  {'user_name': 'Helen'},
  {'user_name': 'Bobby'},
]
raw_review_data = [
  {'user_name': 'Abby', 'business_name': 'Salt & Straw', 'rating': 5, 'text': 'Lucious ice cream!'},
  {'user_name': 'Bobby', 'business_name': 'Salt & Straw', 'rating': 4, 'text': 'Super tasty, but such a long line!'},
  {'user_name': 'Abby', 'business_name': 'Salt & Straw', 'rating': 2, 'text': 'Overrated, but I like sugar.'},
  {'user_name': 'Helen', 'business_name': 'Voodoo Donuts', 'rating': 1, 'text': 'I do not like bubblegum on my donuts.'},
  {'user_name': 'Bobby', 'business_name': 'Voodoo Donuts', 'rating': 5, 'text': 'Pink building is so cute!'},
  {'user_name': 'Abby', 'business_name': 'Voodoo Donuts', 'rating': 2, 'text': 'Diabetes inducing.'},
]


# Review(User(), Business(), rating, review_text)

# def get_biz_name_to_biz_object():
#     dict_of_biz_objects = {}
#     for dicts in raw_business_review_data:
#         business_name = dicts['business_name']
#         review_objects_to_biz_list = []
#         for review in dicts['reviews']:
#             rating = review['rating']
#             review_text = review['text']
#             review_objects_to_biz_list.append(Review(rating, review_text))
#         dict_of_biz_objects[business_name] = Business(business_name, review_objects_to_biz_list)
#     return dict_of_biz_objects

class Review:
    def __init__(self, user_name, business_name, rating, review_text):
        self.user_name = user_name
        self.business_name = business_name
        self.rating = rating
        self.review_text = review_text
    def __repr__(self):
        return 'Review({}, {}, {}, {})'.format(self.user_name, self.business_name, self.rating, self.review_text)

class Business:
    def __init__(self, business_name):
        self.business_name = business_name
    def __repr__(self):
        return 'Business({})'.format(self.business_name)

class User:
    def __init__(self, user_name):
        self.user_name = user_name
    def __repr__(self):
        return 'User({})'.format(self.user_name)

def get_user_name_object_list(raw_review_data):
    user_name_object_list = []
    for dicts in raw_review_data:
        user_name = dicts['user_name']
        user_name_object_list.append(User(user_name))
    return user_name_object_list
def get_business_object_list(raw_review_data):
    business_object_list = []
    for dicts in raw_review_data:
        business = dicts['business_name']
        business_object_list.append(Business(business))
    return business_object_list
def get_rating_list(raw_review_data):
    rating_list = []
    for dicts in raw_review_data:
        rating = dicts['rating']
        rating_list.append(rating)
    return rating_list
def get_text_list(raw_review_data):
    text_list = []
    for dicts in raw_review_data:
        text = dicts['text']
        text_list.append(text)
    return text_list

def get_review_object_list(raw_review_data, user_name_object_list, business_object_list, rating_list, text_list): #userobject_to_bizobject_to_reviewobject
    review_object_list = []
    x = 0

    while x < len(rating_list):
        user_name = user_name_object_list[x]
        business_name = business_object_list[x]
        rating = rating_list[x]
        text = text_list[x]
        review_object_list.append(Review(user_name, business_name, rating, text))
        x += 1

    return review_object_list


def get_user_business_search(raw_business_data):
    print("\n\nRestaurants:")
    for dicts in raw_business_data:
        business_name = dicts['business_name']
        print(business_name)
    user_business_search = input('\nWhat business would you like to see reviews of?  ')
    return user_business_search

def get_avg_rating_for_business(user_business_search, review_object_list):
    rating_list = []
    for review_object in review_object_list:
        print(review_object.business_name)
        if user_business_search == review_object.business_name:
            rating_list.append(review_object.rating)
    avg_rating = statistics.mean(rating_list)
    return avg_rating

# def get_avg_rating_for_business(user_restaurant_search, review_object_list):
#     rating_list = []
#     for review_object in review_object_list:
#         rating_list.append(review_object.rating)
#     avg_rating = statistics.mean(rating_list)
#     return avg_rating
# def get_one_review(self):


user_name_object_list = get_user_name_object_list(raw_review_data)
business_object_list = get_business_object_list(raw_review_data)
rating_list = get_rating_list(raw_review_data)
text_list = get_text_list(raw_review_data)
review_object_list = get_review_object_list(raw_review_data, user_name_object_list, business_object_list, rating_list, text_list)

user_business_search = get_user_business_search(raw_business_data)
avg_rating = get_avg_rating_for_business(user_business_search, review_object_list)

print('\n\n\n\n\n\n')
print(avg_rating)

print('\n\n\n\n\n\n')
for review_object in review_object_list:
    print(review_object)















#
#     review_rating_list = []
#     review_text_list = []
#
#     for dicts in raw_review_data:
#         user_name = dicts['user_name']
#         user_name_object_list.append(User(user_name))
#
#         business_name = dicts['business_name']
#         business_object_list.append(Business(business_name))
#
#         review_rating  = dicts['rating']
#         review_rating_list.append(review_rating)
#
#         review_text = dicts['text']
#         review_text_list.append(review_text)
#
#     big_object = Review(user_name_object_list, business_object_list, review_rating_list, review_text_list)
#     return big_object
#
# big_object = create_big_dict(raw_review_data)




















#
