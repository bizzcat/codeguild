city_dict = {
  'Boston': ['New York', 'Albany', 'Portland'],
  'New York': ['Boston', 'Albany', 'Philly'],
  'Albany': ['Boston', 'New York', 'Portland'],
  'Portland': ['Boston', 'Albany', '      '],
  'Philly': ['New York', '      ', '      '],
  '      ': ['      ', '      ', '      ']
}
current_city = 'Boston'

print("""
\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n

   {0:^10} --->---->--- * --->----->----->----->----->---- * --->----->----->----->----->---- *
                           |                                  |                                  |
                           |                                  |                                  |
                           |                                  |                                  |
                      {1:^10}                         {5:^10}                         {9:^10}
                          /|\                                /|\                                /|\\
                         / | \                              / | \                              / | \\
                 *-<-<--   |   -->->-*              *-<-<--   |   -->->-*              *-<-<--   |   -->->-*
                /          |          \            /          |          \            /          |          \\
               /           |           \          /           |           \          /           |           \\
         {2:^10}    {3:^10} {4:^10}  {6:^10} {7:^10} {8:^10}  {10:^10} {11:^10} {11:^10}




 \n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n
""".format(
    current_city,
    city_dict[current_city][0], city_dict[city_dict[current_city][0]][0], city_dict[city_dict[current_city][0]][1], city_dict[city_dict[current_city][0]][2],
    city_dict[current_city][1], city_dict[city_dict[current_city][1]][0], city_dict[city_dict[current_city][1]][1], city_dict[city_dict[current_city][1]][2],
    city_dict[current_city][2], city_dict[city_dict[current_city][2]][0], city_dict[city_dict[current_city][2]][1], city_dict[city_dict[current_city][2]][2]
    ))




def display_immediately_accessible_cities(current_city, city_to_accessible_cities):
    city_dict = city_to_accessible_cities
    print("""
    \n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n

       {0:^10} --->---->--- * --->----->----->----->----->---- * --->----->----->----->----->---- *
                               |                                  |                                  |
                               |                                  |                                  |
                               |                                  |                                  |
                          {1:^10}                         {5:^10}                         {9:^10}
                              /|\                                /|\                                /|\\
                             / | \                              / | \                              / | \\
                     *-<-<--   |   -->->-*              *-<-<--   |   -->->-*              *-<-<--   |   -->->-*
                    /          |          \            /          |          \            /          |          \\
                   /           |           \          /           |           \          /           |           \\
             {2:^10}    {3:^10} {4:^10}  {6:^10} {7:^10} {8:^10}  {10:^10} {11:^10} {11:^10}




     \n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n
    """.format(
        current_city,
        city_dict[current_city][0], city_dict[city_dict[current_city][0]][0], city_dict[city_dict[current_city][0]][1], city_dict[city_dict[current_city][0]][2],
        city_dict[current_city][1], city_dict[city_dict[current_city][1]][0], city_dict[city_dict[current_city][1]][1], city_dict[city_dict[current_city][1]][2],
        city_dict[current_city][2], city_dict[city_dict[current_city][2]][0], city_dict[city_dict[current_city][2]][1], city_dict[city_dict[current_city][2]][2]
        ))


# display_immediately_accessible_cities(current_city, city_to_accessible_cities)






# word = 'Philadelphia'
# print("{0:^14}.".format(word))
#















#
