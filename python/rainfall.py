import urllib.request

site = 'http://or.water.usgs.gov/non-usgs/bes/sunnyside.rain'

def site_into_line_list(site):
    with urllib.request.urlopen(site) as oregon_rainfall:
        line_list = [byte_line.decode('utf-8') for byte_line in oregon_rainfall]
    return line_list

def clean_data_list(line_list):
    top_skimmed = line_list[11:-1]
    clean_data_list = []
    for line in top_skimmed:
        new_line = line[0:18]
        clean_data_list.append(new_line)
    return clean_data_list

def get_day_totals_list(clean_data_list):
    day_totals = []
    for line in clean_data_list:
        new_line = line[-4: -1].lstrip()
        if '-' in new_line:
            new_line = '0'
        the_line = int(new_line)
        day_totals.append(the_line)
    return day_totals

def list_into_dict(clean_data_list, day_totals):
    data_dict = {}
    x = 0
    for line in clean_data_list:
        data_dict[line[0: 11]] = day_totals[x]
        x += 1
    return data_dict

def highest_value(data_dict):
    highest_value = max(data_dict.values())
    return highest_value

def find_day_with_highest_value(highest_value, data_dict):
    for k in data_dict:
        if data_dict[k] == highest_value:
            day_with_with_highest_value = k
    return day_with_with_highest_value

def print_day_with_highest_value(day_with_with_highest_value):
    print ("\nThe day with record rainfall is:  " + day_with_with_highest_value + "  with " + str(highest_value * 0.01) + " inches of rain.\n")

def years_into_dict(clean_data_list):
    d_years_empty = {}
    for line in clean_data_list:
        year = line[7: 11]
        d_years_empty[year] = []
    return d_years_empty

def get_year_values(d_years_empty, clean_data_list, data_dict):
    for line in clean_data_list:
        year = line[7: 11]
        (d_years_empty[year]).append(data_dict.get(line[0:11]))
    year_values = d_years_empty
    return year_values

def get_year_totals(year_values, clean_data_list):
    year_totals = {}
    for line in clean_data_list:
        year = line[7: 11]
        year_totals[year] = (sum(year_values[year]))
    return year_totals

def get_day_average_empty(data_dict):
    day_average_empty = {}
    for line in clean_data_list:
        date = line[0: 6]
        day_average_empty[date] = []
    return day_average_empty

def get_day_average(day_average_empty, data_dict):
    day_averages = {}
    for line in clean_data_list:
        date = line[0: 6]
        (day_average_empty[date]).append(data_dict.get(line[0:11]))
        day_averages[date] = (sum(day_average_empty[date]) / len(day_average_empty[date]))
    return day_averages

def print_day_averages(day_averages):
    for day in day_averages:
        print (day, "had an average of", day_averages[day],  "inches.")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ USER INTERACTION ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def list_user_options():
    os.system('clear')
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print ("""
    \tA - Average rainfall for a day of the year
    \tB - Total rainfall for a specific date of a specific year
    \tC - Average daily rainfall for a month
    \tD - Total rainfall for a specific month of a specific year
    \tE - Total rainfall for a specific month of a every year
    \tF - Total and average daily rainfall for a specific year
    \tG - Total rainfall for a specific year
    \tH - Total rainfall for every year
    """)
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n")
    choice = input("\t    Your choice  > > >  ").upper()

# PUT IN CHOICE
def get_user_year(choice):
    if choice == 'A':

    if choice == 'B':

    if choice == 'C':

    if choice == 'D':

    if choice == 'E':

    if choice == 'F':

    if choice == 'G':

    if choice == 'H':

    else:
        print ("Please select a valid option.")
        get_user_year(choice)






# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ CALLING FUNCTIONS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
line_list = site_into_line_list(site)
clean_data_list = clean_data_list(line_list)
day_totals = get_day_totals_list(clean_data_list)
data_dict = list_into_dict(clean_data_list, day_totals)
d_years_empty = years_into_dict(clean_data_list)
year_values = get_year_values(d_years_empty, clean_data_list, data_dict)
year_totals = get_year_totals(year_values, clean_data_list)
highest_value = highest_value(data_dict)
day_with_with_highest_value = find_day_with_highest_value(highest_value, data_dict)
print_day_with_highest_value(day_with_with_highest_value)

day_average_empty = get_day_average_empty(data_dict)
day_averages = get_day_average(day_average_empty, data_dict)
# print_day_averages(day_averages)










# print (d, '\n\n\n\n', clean_data_list[0:10])



#### def list_into_data(clean_data_list):
####     clean_data_string = '\n'.join(clean_data_list)
####     return clean_data_string
#### d_years = break_into_years(d, clean_data_list)
#### clean_data_string = list_into_data(clean_data_list)





    # years_total = sum(d_years_empty[year].values())



# def add_values_years_dict(d_years_empty, clean_data_list):
#     for line in clean_data_list:
#         (d_years_empty[line[7: 11]]).append(line[0:6] + ': ' + str(d.get(line[0:11])))
#     d_years = d_years_empty
#     return d_years


    #
    #
    #     l_temp.append(dict({str(line[0:6]): d.get(line[0:11])}))
    #     for date in l_temp:
    #         d_years[line[7: 11]].update(l_temp[str(line)])
    # print (d_years)
    # return d_years
    #









#FOR TOTAL RAIN IN A YEAR OR MONTH USE
# # iteration
# >>> n = 0
# >>> for val in values:
# ...     n += val
# >>> print(n)
# 504


# clean_data = clean_data(rainfall_doc)
# print (rainfall_doc)
# line_list = doc_into_line_list(rainfall_doc)





# def site_into_doc(site):
#     with urllib.request.urlopen(site) as oregon_rainfall:
#         rainfall_doc = [byte_line.decode('utf-8') for byte_line in oregon_rainfall]
#
#     return rainfall_doc

# def doc_into_line_list(rainfall_doc):
#     line_list = []
#     for line in rainfall_doc:
#         line_list.append(line)
#     return line_list
#
# def list_into_data(line_list):
#     rainfall_data = ''.join(line_list)
#     return rainfall_data
#
# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ CALLING FUNCTIONS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# rainfall_doc = site_into_doc(site)
# line_list = doc_into_line_list(rainfall_doc)
# print (line_list)
# # rainfall_data = list_into_data(line_list)
#
#
#
#
#
#
#
#
# # def get_user_site():
# #     site = input('')
# #     return site
#
#
#
# #     line_list = []
# #     with urllib.request.urlopen(site) as oregon_rainfall:
# #         lines = [byte_line.decode('utf-8') for byte_line in oregon_rainfall]
# #         line_list.append(lines)
# #         rainfall_data = ''.join(lines)
# #     return rainfall_data
# #     return line_list
#
# # def site_into_lines(site):
# #     line_list = []
# #
# #
# #
# #
# # print(rainfall_data[2])
