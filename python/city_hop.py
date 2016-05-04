# ********************************************* INSTRUCTIONS *********************************************
# Traveling from one city to an adjacent one is called a **hop**.
#
# For this sort of problem, you'll want to iteratively visit cities you know you can access while updating:
# 1. Cities you can access.
# 1. Cities you've been to.
# 1. Cities you haven't been to.
#
# * Let the user enter a city.
# Print out all the cities connected to that city.
# * Let the user enter a city.
# Print out all cities that could be reached through two hops.
#
# ## Advanced
# * Let the user enter a city and a number of hops.
# Print out all cities that could be reached through that number of hops.
# * We've also mapped the travel time of each hop:
# ```python
# city_to_accessible_cities_with_travel_time = {
#   'Boston': {('New York', 4), ('Albany', 6), ('Portland', 3)},
#   'New York': {('Boston', 4), ('Albany', 5), ('Philadelphia', 9)},
#   'Albany': {('Boston', 6), ('New York',5), ('Portland', 7)},
#   'Portland': {('Boston', 3), ('Albany', 7)},
#   'Philadelphia': {('New York', 9)}
# }
# ```
# When the user enters a city and a number of hops, print out the shortest travel times to each city.
# Paths with fewer hops are not necessarily those with the shorter travel times.

# ********************************************* IMPORTS, INDICES, VARIABLES *********************************************
city_to_accessible_cities = {
  'Boston': {'New York', 'Albany', 'Portland'},
  'New York': {'Boston', 'Albany', 'Philadelphia'},
  'Albany': {'Boston', 'New York', 'Portland'},
  'Portland': {'Boston', 'Albany'},
  'Philadelphia': {'New York'}
}
cities_visited = []

# ********************************************* DEFINING FUNCTIONS *********************************************
def take_user_city():
    print("Select your city:")
    user_city = input(' > > >  ').capitalize()
    return user_city

def display_city_and_possible_cities(user_city, city_to_accessible_cities):
    print("From {} you can reach {}".format(user_city, str(city_to_accessible_cities[user_city])))

# ********************************************* CALLING FUNCTIONS *********************************************
user_city = take_user_city()
display_city_and_possible_cities(user_city, city_to_accessible_cities)







#
# cities_visited = []
# accessible_cities[city].update(city_to_accessible_cities[NEW_CITY])
# for city in city_to_accessible_cities
#
#     cities_visited.append(city_to_accessible_cities[CITY])
#     city_to_accessible_cities[NEW_CITY]
# current_location = city_to_accessible_cities[CITY]





































#
