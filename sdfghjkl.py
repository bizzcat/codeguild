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


class Review:
    def __init__(self, rating, review_text):
        self.rating = rating
        self.review_text = review_text


class Business:
    def __init__(self, business_name, reviews):
        self.business_name = business_name
        self.reviews = reviews

list_of_reviews = []

for dicts in raw_business_review_data:
    for review in dicts['reviews']:
        rating = review['rating']
        text = review['text']
        list_of_reviews.append([rating, text])

print(list_of_reviews)

#
#
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
