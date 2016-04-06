import os
import time

city_to_accessible_cities = {
  'Boston': {'New York', 'Albany', 'Portland'},
  'New York': {'Boston', 'Albany', 'Philly'},
  'Albany': {'Boston', 'New York', 'Portland'},
  'Portland': {'Boston', 'Albany', '      '},
  'Philly': {'New York', '      ', '      '},
  '      ': {'      ', '      ', '      '}
}
city_to_accessible_cities_lists = {
  'Boston': ['New York', 'Albany', 'Portland'],
  'New York': ['Boston', 'Albany', 'Philly'],
  'Albany': ['Boston', 'New York', 'Portland'],
  'Portland': ['Boston', 'Albany', '      '],
  'Philly': ['New York', '      ', '      '],
  '      ': ['      ', '      ', '      ']
}

city_list = [
    'Boston', 'New York', 'Albany', 'Portland', 'Philly'
    ]
cities_visited = []



# ********************************************* INITIATIVE FUNCTIONS *********************************************
def take_user_city(city_list):
    os.system('clear')
    print(
"""
\n
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
\n\n\n\n\n\n\n\n
\t\t\t\t\tYou may chose to start from one of these five cities:



\t\t\t~{0:^16}~{1:^16}~{2:^16}~{3:^16}~{4:^16}~

\n\n\n\n\n\n\n\n
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
\n\n\n
Select your city:""".format(city_list[0], city_list[1], city_list[2], city_list[3], city_list[4]))
    current_city = input(' > > >  ')
    return current_city
def take_user_hops():
    print("\nSelect number of hops:")
    hops_left = int(input(' > > >  '))
    return hops_left

# ********************************************* DISPLAY FUNCTIONS *********************************************
def display_roadtrip_status(current_city, cities_visited, city_to_accessible_cities_lists, hops_left):
    os.system('clear')
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    display_map(current_city, city_to_accessible_cities_lists)
    display_cities_visited(cities_visited)
    display_number_of_hops(hops_left)
    print("\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

def display_map(current_city, city_to_accessible_cities_lists):
    city_dict = city_to_accessible_cities_lists
    print("""
                                        ~~*~~    Possible routes from {0}    ~~*~~


   {0:^10}  ---->->---- * --------------->->->---------------- * --------------->->->---------------- *
                           |                                      |                                      |
                           |                                      |                                      |

                      {1:^10}                             {5:^10}                             {9:^10}

                        /  |  \                                /  |  \                                /  |  \\
                 *-----*   |   *-----*                  *-----*   |   *-----*                  *-----*   |   *-----*
                /          |          \                /          |          \                /          |          \\

         {2:^10}   {3:^10}   {4:^10}     {6:^10}  {7:^10}  {8:^10}     {10:^10}  {11:^10}  {12:^10}

    """.format(
        current_city,
        city_dict[current_city][0], city_dict[city_dict[current_city][0]][0], city_dict[city_dict[current_city][0]][1], city_dict[city_dict[current_city][0]][2],
        city_dict[current_city][1], city_dict[city_dict[current_city][1]][0], city_dict[city_dict[current_city][1]][1], city_dict[city_dict[current_city][1]][2],
        city_dict[current_city][2], city_dict[city_dict[current_city][2]][0], city_dict[city_dict[current_city][2]][1], city_dict[city_dict[current_city][2]][2],

        ))
def display_cities_visited(cities_visited):
    print("\n\tYou have already visited: {}".format(str(cities_visited)))
def display_number_of_hops(hops_left):
    print("\n\tYou have {} hops left\n".format(hops_left))
def display_end_of_trip():
    os.system('clear')
    print("""
    \n
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    \n\n\n\n\n\n\n\n\n\n
    Congratulations! You have vistied {} cities!

    {} will all miss you very, very deeply... Au revoir!

    \n\n\n\n\n\n\n\n\n\n
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    \n\n\n

    """.format(len(cities_visited), str(cities_visited)))
    time.sleep(10)
    quit()


# ********************************************* DECISIVE FUNCTIONS *********************************************
def take_user_next_city():
    print("\n\nWhich city would you like to go next?")
    next_city = input(' > > >  ')
    return next_city
    next_city = take_user_next_city()
def scan_for_end_of_trip(hops_left):
    if hops_left == 0:
        display_end_of_trip()


# ********************************************* UPDATING INDICES AND VARIABLES *********************************************
def update_cities_visited(cities_visited, current_city):
    cities_visited.append(current_city)
    return cities_visited
def update_current_city(next_city, city_to_accessible_cities, current_city):
    if next_city in city_to_accessible_cities[current_city]:
        current_city = next_city
    if next_city not in city_to_accessible_cities[current_city]:
        print("{} is not a possible destination after {}.".format(next_city, current_city))
    return current_city
def update_number_of_hops(hops_left):
    hops_left = (hops_left - 1)
    # if hops_left = 0:
        # a function displaying final message, closes loop, prompts user to play again
    return hops_left



    cities_visited = update_cities_visited(current_city)
    current_city = update_current_city(next_city, city_to_accessible_cities, current_city)

# ********************************************* CALLING FUNCTIONS *********************************************
current_city = take_user_city(city_list)
hops_left = take_user_hops()

cont = True
while cont:
    display_roadtrip_status(current_city, cities_visited, city_to_accessible_cities_lists, hops_left)
    next_city = take_user_next_city()
    cities_visited = update_cities_visited(cities_visited, current_city)
    current_city = update_current_city(next_city, city_to_accessible_cities, current_city)
    hops_left = update_number_of_hops(hops_left)
    scan_for_end_of_trip(hops_left)




    # update_everything(current_city, cities_visited, city_to_accessible_cities, hops_left, next_city)
    # # def update_everything(current_city, cities_visited, city_to_accessible_cities, hops_left, next_city):
    #     cities_visited = update_cities_visited(cities_visited, current_city)
    #     current_city = update_current_city(next_city, city_to_accessible_cities, current_city)
    #     hops_left = update_number_of_hops(hops_left)









# # def display_immediately_accessible_cities(current_city, city_to_accessible_cities):
#     print("\n\n~~~~~~~~\n\nFrom {} you can reach:".format(current_city))
#     for adj_city in city_to_accessible_cities[current_city]:
#         print("\n{}, from which you can then reach {}".format(adj_city, city_to_accessible_cities[adj_city]))



    # def update_cities_accessible_by_hops():

# Use the below if it is better to print out adjacent cities and distant cities separately rather than simultaneously in one function
    # def display_immediately_accessible_cities(current_city, city_to_accessible_cities):
    #     print("~~~~~~~~\n\nFrom {} you can reach:".format(current_city))
    #     for city in city_to_accessible_cities[current_city]:
    #         print(city)
    # def display_cities_accessible_by_hops():
    #
    #     print("~~~~~~~~\n\nFrom {} you can reach:")

# def scan_for_end_of_trip():
#     if hops_left == 0:
#         quit()


#
# take user city
# take user hops
# loop begin:
#     display roadtrip status
#         display current_city
#         display cities_visited
#         display accessible_cities
#         display number_of_hops
#     take user nextt city
#     update everything
#         update current_city
#         update cities_visited
#         update immediately_accessible_cities
#         update cities_accessible_by_hops
#         update number_of_hops
