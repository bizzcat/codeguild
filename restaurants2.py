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
        return statistics.mean(avg_list)

def get_biz_name_to_biz_object():
    dict_of_biz_objects = {}
    for dicts in raw_business_review_data:
        business_name = dicts['business_name']
        review_objects_to_biz_list = []
        for review in dicts['reviews']:
            rating = review['rating']
            review_text = review['text']
            review_objects_to_biz_list.append(Review(rating, review_text))
        dict_of_biz_objects[business_name] = Business(business_name, review_objects_to_biz_list)
    return dict_of_biz_objects

def get_user_restaurant_search():
    print("Restaurants: \nVoodoo Donuts \nSalt & Straw")
    user_restaurant_search = input('What restaurant would you like to see reviews of?  ')
    return user_restaurant_search




dict_of_biz_objects = get_biz_name_to_biz_object()

user_restaurant_search = get_user_restaurant_search()
user_restaurant_selection = dict_of_biz_objects[user_restaurant_search]
user_restaurant_avg_rating = user_restaurant_selection.get_avg_rating()

print(user_restaurant_avg_rating)













































#
