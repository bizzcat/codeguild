import statistics


raw_business_review_data = [
  {
    'business_name': 'Salt & Straw',
    'reviews': [
      {'rating': 5, 'text': 'Lucious ice cream!'},
      {'rating': 4, 'text': 'Super tasty, but such a long line!'},
      {'rating': 2, 'text': 'Overrated, but I like sugar.'}
    ],
  },
  {
    'business_name': 'Voodoo Donuts',
    'reviews': [
      {'rating': 1, 'text': 'I do not like bubblegum on my donuts.'},
      {'rating': 5, 'text': 'Pink building is so cute!'},
      {'rating': 2, 'text': 'Diabetes inducing.'}
    ],
  },
]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ DEFINING CLASSES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Review:
    def __init__(self, rating, review_text):
        self.rating = rating
        self.review_text = review_text

    def __repr__(self):
        return 'Review({}, {})'.format(self.rating, self.review_text)


class Business:
    def __init__(self, business_name, reviews):
        self.business_name = business_name
        self.reviews = reviews
    def __repr__(self):
        return "Business({}, {})".format(self.business_name, self.reviews)
    def get_avg_rating(self):
        avg_list = []
        for review in self.reviews:
            avg_list.append(review.rating)
        print(statistics.mean(avg_list))

        # for thing in self:
        #     print(thing)


my_review = Review(5, 'Tasty!')
my_review.rating  #> 5

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ GENERIC DICTIONARIES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



# dict_of_biz_objects = {}
# def get_biz_name_to_biz_object(dict_of_biz_objects):
#     for dicts in raw_business_review_data:
#         business_name_a = dicts['business_name']
#         review_ratings_to_biz_list = []
#         review_text_to_biz_list = []
#         review_objects_to_biz_list = []
#         for review in dicts['reviews']:
#             rating_a = review['rating']
#             review_ratings_to_biz_list.append(rating_a)
#             review_text_a = review['text']
#             review_text_to_biz_list.append(review_text_a)
#             review_objects_to_biz_list.append(Review(rating_a, review_text_a))
#         dict_of_biz_objects[business_name_a] = Business(business_name_a, review_objects_to_biz_list)
#     return dict_of_biz_objects
#
# get_biz_name_to_biz_object(dict_of_biz_objects)
# print('\n\n\n')
# print(dict_of_biz_objects)
# print('\n\n\n')


def get_biz_name_to_biz_object():
    dict_of_biz_objects = {}
    dict_of_avg_rating = {}
    for dicts in raw_business_review_data:
        business_name_a = dicts['business_name']
        review_ratings_to_biz_list = []
        review_objects_to_biz_list = []
        for review in dicts['reviews']:
            rating_a = review['rating']
            review_text_a = review['text']
            review_ratings_to_biz_list.append(rating_a)
            review_objects_to_biz_list.append(Review(rating_a, review_text_a))
        dict_of_biz_objects[business_name_a] = Business(business_name_a, review_objects_to_biz_list)
    return dict_of_biz_objects



dict_of_biz_objects = get_biz_name_to_biz_object()
some_biz_object = dict_of_biz_objects['Salt & Straw']

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def get_biz_name_to_biz_object():
    dict_of_biz_objects = {}
    dict_of_avg_rating = {}
    for dicts in raw_business_review_data:
        business_name_a = dicts['business_name']
        review_ratings_to_biz_list = []
        review_objects_to_biz_list = []
        for review in dicts['reviews']:
            rating_a = review['rating']
            review_text_a = review['text']
            review_ratings_to_biz_list.append(rating_a)
            review_objects_to_biz_list.append(Review(rating_a, review_text_a))
        dict_of_biz_objects[business_name_a] = Business(business_name_a, review_objects_to_biz_list)
    return dict_of_biz_objects



dict_of_biz_objects = get_biz_name_to_biz_object()
some_biz_object = dict_of_biz_objects['Salt & Straw']
some_biz_object.get_avg_rating()











# print('\n\n\n')
# print(dict_of_avg_rating)
# print('\n\n\n')



#
#
# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ SPECIFIC DICTIONARIES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# print("\n\n\nSPECIFIC DICTIONARIES\n")
# def get_list_of_all_review_objects(list_of_review_objects):
#     for dicts in raw_business_review_data:
#         for review in dicts['reviews']:
#             rating_a = review['rating']
#             review_text_a = review['text']
#             list_of_review_objects.append(Review(rating_a, review_text_a))
#             print('\n')
#     return list_of_review_objects
#
# def get_biz_name_to_biz_object_with_avg_rating(dict_of_biz_objects):
#     for dicts in raw_business_review_data:
#         business_name_a = dicts['business_name']
#         reviews_to_biz_list = []
#         for review in dicts['reviews']:
#             reviews_to_biz_list.append(review)
#         # print(business_name_a, reviews_to_biz_list)
#         # print (Business(business_name_a, reviews_to_biz_list))
#         dict_of_biz_objects[business_name_a] = Business(business_name_a, reviews_to_biz_list)
#     return dict_of_biz_objects
#
#
# dict_of_biz_objects = {}
# list_of_review_objects = []
#
#
#
# list_of_review_objects = get_list_of_all_review_objects(list_of_review_objects)
# dict_of_biz_objects = get_biz_name_to_biz_object(dict_of_biz_objects)
#
#












# dict where biz name is key, and reviews is value
#
# user_business = 'Voodoo Donuts'
# print('\n\n\n')
# Business.get_reviews_for_business(user_business)
# print('\n\n\n')

#
# reviews_to_biz_list = []
# for review in dicts['reviews']:
#     rating_a = review['rating']
#     review_text_a = review['text']
#     reviews_to_biz_list.append([rating_a, review_text_a])





# def convert_dict_to_review(d_review):
#     return Review(d_review['rating'], d_review['review_text'])
#
#
# def convert_list_of_dict_to_reviews(l_d_reviews):
#     l_reviews = []
#     for d_review in l_d_reviews:
#         l_reviews.append(convert_dict_to_review(d_review))
#     return l_reviews
#
# def convert_biz_dict_to_biz(l_reviews):
#     biz_list_of_reviews = []
#     for review in l_reviews:
#         biz_list_of_reviews.append(convert_list_of_dict_to_reviews(l_d_reviews))
#     return biz_list_of_reviews
#
# def convert_big_dict_to_businesses(raw_business_review_data):
#     biz_list = []
#     for business in raw_business_review_data:
#         biz_list.append(business['business_name'])
#     return biz_list
#
# def assign_reviews_to_business(biz_list, biz_list_of_reviews):
#     biz_to_reviews = {}
#     for business in biz_list:
#         biz_to_reviews[business] = convert_biz_dict_to_biz(l_reviews)
#     return biz_to_reviews
#
# # What I did here was to break down the bits of data into lists that can be assigned to *some key in some dict*, what we need to do
#
#
# biz_list = convert_big_dict_to_businesses(biz_list_of_reviews)
# biz_to_reviews = assign_reviews_to_business(biz_list, biz_list_of_reviews)
#
# print("biz_to_reviews", biz_to_reviews)
# print("biz_list", biz_list)
# print("biz_list_of_reviews", biz_list_of_reviews)
# print("l_reviews", l_reviews)
# print("l_d_reviews", l_d_reviews)
