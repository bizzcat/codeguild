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
current_city = 'Boston'

def update_lists_and_dicts(city_to_accessible_cities_with_travel_time, current_city):
    city_dict = city_to_accessible_cities_lists
    city_dict_times = city_to_accessible_cities_with_travel_time
    leading_city_names = []
    adj_city_names = []

    for city in list(city_dict):
        leading_city_names.append(city)
    for city in leading_city_names:
        adj_city_names.append(list(city_dict[city].items())
    for city in adj_city_names:
        






    x = -1
    for adj_city in city_dict_times[current_city]:
        adj_city_times.insert(x, city_dict_times[current_city][adj_city])
        adj_city_names.insert(x, adj_city)
        adj_city_times_display.insert(x, '(' + str(int(city_dict_times[current_city][adj_city])) + ' hrs)')

    for adj_city in adj_city_names:
        far_cities.insert(x, city_dict_times[adj_city])
        # for far_city in far_cities:
            # far_city_times.append(city_dict_times[adj_city][far_city])
        print(city_dict_times[adj_city])
    print(far_city_times)

update_lists_and_dicts(city_to_accessible_cities_with_travel_time, current_city)
# ~~~~~~~~~~~~~~~~~~~~
# def display_map(current_city, city_to_accessible_cities_lists):
#     city_dict = city_to_accessible_cities_lists
#     city_dict_times = city_to_accessible_cities_with_travel_time
#     adj_city_times = []
#     adj_city_times_display = []
#     adj_city_names = []
#     far_city_times = []
#
#     x = -1
#     for adj_city in city_dict_times[current_city]:
#         adj_city_times.insert(x, city_dict_times[current_city][adj_city])
#         adj_city_names.insert(x, adj_city)
#         adj_city_times_display.insert(x, '(' + str(int(city_dict_times[current_city][adj_city])) + ' hrs)')
#
#     for adj_city in adj_city_names:
#         far_cities = city_dict_times[adj_city].keys()
#         for far_city in far_cities:
#             far_city_times.insert(x, city_dict_times[adj_city][far_city])
#
#
#     '\n\t\t\t\t\t\t', adj_city_times, '\n\t\t\t\t\t\t',
#     adj_city_times_display, '\n\t\t\t\t\t\t',
#     adj_city_names, '\n\t\t\t\t\t\t',
#     far_city_times
#     )
#
#     print("""
#                                         ~~*~~    Possible routes from {0}    ~~*~~
#
#
#    {0:^10}  ---->->---- * --------------->->->---------------- * --------------->->->---------------- *
#                            |                                      |                                      |
#                            |                                      |                                      |
#
#                       {1:^10}                             {5:^10}                           {9:^10}
#                       {13:^10}                             {17:^10}                             {21:^10}
#
#                          / | \                                  / | \                                  / | \\
#                  *------   |   ------*                  *------   |   ------*                  *------   |   ------*
#                 /          |          \                /          |          \                /          |          \\
#                /           |           \              /           |           \              /           |           \\
#
#          {2:^10}   {3:^10}   {4:^10}     {6:^10}  {7:^10}  {8:^10}     {10:^10}  {11:^10}  {12:^10}
#          {14:^10}   {15:^10}   {16:^10}     {18:^10}  {19:^10}  {20:^10}     {22:^10}  {23:^10}  {24:^10}
#     """.format(
#         current_city,
#         city_dict[current_city][0], city_dict[city_dict[current_city][0]][0], city_dict[city_dict[current_city][0]][1], city_dict[city_dict[current_city][0]][2],
#         city_dict[current_city][1], city_dict[city_dict[current_city][1]][0], city_dict[city_dict[current_city][1]][1], city_dict[city_dict[current_city][1]][2],
#         city_dict[current_city][2], city_dict[city_dict[current_city][2]][0], city_dict[city_dict[current_city][2]][1], city_dict[city_dict[current_city][2]][2],
#
#         adj_city_times_display[0], far_city_times[0], far_city_times[1], far_city_times[2],
#         adj_city_times_display[1], far_city_times[3], far_city_times[4], far_city_times[5],
#         adj_city_times_display[2], far_city_times[6], far_city_times[7], far_city_times[8]
#         ))
