import os
import time

city_list = ['Boston', 'New York', 'Albany', 'Portland', 'Philly']
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

city_to_accessible_cities_with_travel_time = {
  'Boston': {'New York': 4, 'Albany': 6, 'Portland': 3},
  'New York': {'Boston': 4, 'Albany': 5, 'Philly': 9},
  'Albany': {'Boston': 6, 'New York': 5, 'Portland': 7},
  'Portland': {'Boston': 3, 'Albany': 7, '      ': 0},
  'Philly': {'New York': 9, '      ': 0, '      ': 0},
  '      ': {'      ': 0, '      ': 0, '      ': 0}
  }

cities_visited = []
time_traveling = []
time_traveling_total = 0

# ********************************************* INITIATIVE FUNCTIONS *********************************************
def take_user_city(city_list):
    os.system('clear')
    print(
    """
    \n
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    \n\n\n\n\n\n\n
    \t\t\t\t\tYou may chose to start from one of these five cities:



    \t\t\t {0:^16}~{1:^16}~{2:^16}~{3:^16}~{4:^16}

    \n\n\n\n\n\n\n\n\n
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
def display_roadtrip_status(current_city, cities_visited, city_to_accessible_cities_lists, hops_left, time_traveling_total):
    os.system('clear')
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    display_map(current_city, city_to_accessible_cities_lists)
    display_cities_visited(cities_visited)
    display_number_of_hops(hops_left)
    display_time_traveling(time_traveling_total)
    print("\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

def display_map(current_city, city_to_accessible_cities_lists):
    city_dict = city_to_accessible_cities_lists
    city_dict_times = city_to_accessible_cities_with_travel_time
    adj_city_times = []
    adj_city_times_display = []
    adj_city_names = []
    far_city_times = []
    # far_city_times1 = []
    # far_city_times2 = []
    x = -1
    for adj_city in city_dict_times[current_city]:
        adj_city_times.insert(x, city_dict_times[current_city][adj_city])
        adj_city_names.insert(x, adj_city)
        adj_city_times_display.insert(x, '(' + str(int(city_dict_times[current_city][adj_city])) + ' hrs)')
        for far_city in city_dict_times[adj_city]:
            far_city_times.insert(x, '(' + str(int(city_dict_times[adj_city][far_city]) + int(city_dict_times[current_city][adj_city])) + ' hrs)')
            # adj_city0 = far_city0, 1, 2 ------- adj_city1 = far_city3, 4, 5
            # far_city_times2.insert(x, '(' + str(int(city_dict_times[adj_city_names[2]][far_city]) + int(adj_city_times[2])) + ' hrs)')
    #
    # for adj_city, far_city in city_dict_times[current_city]:
    #     adj_city_times.insert(x, city_dict_times[current_city][adj_city])
    #     adj_city_names.insert(x, adj_city)
    #     adj_city_times_display.insert(x, '(' + str(int(city_dict_times[current_city][adj_city])) + ' hrs)')
    #     far_city_times0.insert(x, '(' + str(int(city_dict_times[adj_city][far_city]) + int(city_dict_times[current_city][adj_city]) + ' hrs)')
    #     far_city_times1.insert(x, '(' + str(int(city_dict_times[adj_city_names[1]][far_city]) + int(adj_city_times[1])) + ' hrs)')
    #
    # for adj_city in city_dict_times[current_city]:
    #     adj_city_times.insert(x, city_dict_times[current_city][adj_city])
    #     x += 1
    # x=0
    # for adj_city in city_dict_times[current_city]:
    #     adj_city_names.insert(x, adj_city)
    #     x += 1
    # x=0
    # for time in adj_city_times:
    #     adj_city_times_display.insert(x, '(' + str(int(time)) + ' hrs)')
    #     x += 1
    # for far_city in city_dict_times[adj_city_names[0]]:
    #     far_city_times0.append('(' + str(int(city_dict_times[adj_city_names[0]][far_city]) + int(adj_city_times[0])) + ' hrs)')
    # for far_city in city_dict_times[adj_city_names[1]]:
    #     far_city_times1.append('(' + str(int(city_dict_times[adj_city_names[1]][far_city]) + int(adj_city_times[1])) + ' hrs)')
    # for far_city in city_dict_times[adj_city_names[2]]:
    #     far_city_times2.append('(' + str(int(city_dict_times[adj_city_names[2]][far_city]) + int(adj_city_times[2])) + ' hrs)')

    print(
    '\n\t\t\t\t\t\t', adj_city_times, '\n\t\t\t\t\t\t',
    adj_city_times_display, '\n\t\t\t\t\t\t',
    adj_city_names, '\n\t\t\t\t\t\t',
    far_city_times
    )

    print("""
                                        ~~*~~    Possible routes from {0}    ~~*~~


   {0:^10}  ---->->---- * --------------->->->---------------- * --------------->->->---------------- *
                           |                                      |                                      |
                           |                                      |                                      |

                      {1:^10}                             {5:^10}                           {9:^10}
                      {13:^10}                             {17:^10}                             {21:^10}

                         / | \                                  / | \                                  / | \\
                 *------   |   ------*                  *------   |   ------*                  *------   |   ------*
                /          |          \                /          |          \                /          |          \\
               /           |           \              /           |           \              /           |           \\

         {2:^10}   {3:^10}   {4:^10}     {6:^10}  {7:^10}  {8:^10}     {10:^10}  {11:^10}  {12:^10}
         {14:^10}   {15:^10}   {16:^10}     {18:^10}  {19:^10}  {20:^10}     {22:^10}  {23:^10}  {24:^10}
    """.format(
        current_city,
        city_dict[current_city][0], city_dict[city_dict[current_city][0]][0], city_dict[city_dict[current_city][0]][1], city_dict[city_dict[current_city][0]][2],
        city_dict[current_city][1], city_dict[city_dict[current_city][1]][0], city_dict[city_dict[current_city][1]][1], city_dict[city_dict[current_city][1]][2],
        city_dict[current_city][2], city_dict[city_dict[current_city][2]][0], city_dict[city_dict[current_city][2]][1], city_dict[city_dict[current_city][2]][2],

        adj_city_times_display[0], far_city_times[0], far_city_times[1], far_city_times[2],
        adj_city_times_display[1], far_city_times[3], far_city_times[4], far_city_times[5],
        adj_city_times_display[2], far_city_times[6], far_city_times[7], far_city_times[8]
        ))
def display_cities_visited(cities_visited):
    print("\n\n\tYou have already visited: {}".format(str(cities_visited)))
def display_number_of_hops(hops_left):
    print("\n\tYou have {} hops left\n".format(hops_left))
def display_time_traveling(time_traveling_total):
    print("\tYou have been traveling for {} hours\n".format(time_traveling_total))

def display_end_of_trip():
    os.system('clear')
    print("""
    \n
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    \n\n\n\n\n\n\n\n
    \t\t\t\t\tCongratulations! You have vistied {} cities!


    \t\t\t{} will all miss you very, very deeply... Au revoir!

    \n\n\n\n\n\n\n\n
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
    return hops_left
def update_time_traveling(time_traveling, city_to_accessible_cities_with_travel_time, next_city, current_city):
    time_traveling.append(city_to_accessible_cities_with_travel_time[next_city][current_city])
    time_traveling_total = sum(time_traveling)
    return time_traveling_total

# ********************************************* CALLING FUNCTIONS *********************************************
current_city = take_user_city(city_list)
hops_left = take_user_hops()

cont = True
while cont:
    display_roadtrip_status(current_city, cities_visited, city_to_accessible_cities_lists, hops_left, time_traveling_total)

    next_city = take_user_next_city()
    
    cities_visited = update_cities_visited(cities_visited, current_city)
    current_city = update_current_city(next_city, city_to_accessible_cities, current_city)
    hops_left = update_number_of_hops(hops_left)
    time_traveling_total = update_time_traveling(time_traveling, city_to_accessible_cities_with_travel_time, next_city, current_city)

    scan_for_end_of_trip(hops_left)
