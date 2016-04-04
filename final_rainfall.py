# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ INITIAL SETUP ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ********************************************* IMPORTS, VARIABLES *********************************************
import os
import time
import random
import urllib.request
import statistics

site = 'https://raw.githubusercontent.com/selassid/codeguild/master/sunnyside.rain'


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ DEFINING FUNCTIONS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ********************************************* CORE FUNCTIONS *********************************************
def break_site_into_line_list(site):
    with urllib.request.urlopen(site) as oregon_rainfall:
        line_list = [byte_line.decode('utf-8') for byte_line in oregon_rainfall]
    return line_list
def clean_the_data(line_list):
    top_skimmed = line_list[11:-1]
    clean_data_list = []
    for line in top_skimmed:
        new_line = line[0:18]
        clean_data_list.append(new_line)
    return clean_data_list

def assign_day_totals(clean_data_list):
    day_totals = []
    for line in clean_data_list:
        new_line = line[-4: -1].lstrip()
        if '-' in new_line:
            new_line = '0'
        the_line = int(new_line)
        day_totals.append(the_line)
    return day_totals
def create_dict_from_list(clean_data_list, day_totals):
    clean_data_dict = {}
    x = 0
    for line in clean_data_list:
        clean_data_dict[line[0: 11]] = day_totals[x]
        x += 1
    return clean_data_dict

def get_record_rainfall(clean_data_dict):
    record_rainfall = max(clean_data_dict.values())
    return record_rainfall
def identify_day_with_record_rainfall(record_rainfall, clean_data_dict):
    for k in clean_data_dict:
        if clean_data_dict[k] == record_rainfall:
            day_with_with_record_rainfall = k
    return day_with_with_record_rainfall

def assign_days_to_keys(clean_data_list):
    days_empty_values = {}
    for line in clean_data_list:
        date = line[0: 6]
        days_empty_values[date] = []
    return days_empty_values
def assign_day_averages(days_empty_values, clean_data_dict):
    day_averages = {}
    for line in clean_data_list:
        date = line[0: 6]
        (days_empty_values[date]).append(clean_data_dict.get(line[0:11]))
        day_averages[date] = statistics.mean(days_empty_values[date])                #(sum(days_empty_values[date]) / len(days_empty_values[date]))
    return day_averages

def assign_months_to_keys(clean_data_list):
    months_empty_values = {}
    for line in clean_data_list:
        month = line[3: 6]
        months_empty_values[month] = []
    return months_empty_values
def assign_monthly_averages(months_empty_values, clean_data_list, clean_data_dict):
    monthly_averages = {}
    year_list = []
    for line in clean_data_list:
        year = line[7: 11]
        if year not in year_list:
            year_list.append(year)
    for line in clean_data_list:
        number_of_years = len(year_list)
        month = line[3: 6]
        (months_empty_values[month]).append(clean_data_dict.get(line[0:11]))
        monthly_averages[month] = statistics.mean(months_empty_values[month])
    return monthly_averages

def assign_specific_months_to_keys(clean_data_list):
    specific_months_empty_values = {}
    for line in clean_data_list:
        month_year = line[3: 11]
        specific_months_empty_values[month_year] = []
    return specific_months_empty_values
def assign_specific_monthly_totals(specific_months_empty_values, clean_data_list, clean_data_dict):
    specific_monthly_totals = {}
    for line in clean_data_list:
        month_year = line[3: 11]
        (specific_months_empty_values[month_year]).append(clean_data_dict.get(line[0:11]))
        specific_monthly_totals[month_year] = (sum(specific_months_empty_values[month_year]))
    return specific_monthly_totals
def assign_daily_averages_for_specific_month(specific_months_empty_values, clean_data_list, clean_data_dict):
    specific_monthly_averages = {}
    for line in clean_data_list:
        month_year = line[3: 11]
        (specific_months_empty_values[month_year]).append(clean_data_dict.get(line[0:11]))
        specific_monthly_averages[month_year] = statistics.mean(specific_months_empty_values[month_year])
    return specific_monthly_averages

def assign_years_to_keys(clean_data_list):
    years_empty_values = {}
    for line in clean_data_list:
        year = line[7: 11]
        years_empty_values[year] = []
    return years_empty_values
def assign_values_to_year(years_empty_values, clean_data_list, clean_data_dict):
    for line in clean_data_list:
        year = line[7: 11]
        (years_empty_values[year]).append(clean_data_dict.get(line[0:11]))
    years_dict = years_empty_values
    return years_dict
def assign_year_totals(years_dict, clean_data_list):
    year_totals = {}
    for line in clean_data_list:
        year = line[7: 11]
        year_totals[year] = (sum(years_dict[year]))
    return year_totals
def assign_year_daily_averages(years_empty_values, clean_data_dict, clean_data_list):
    year_daily_averages = {}
    for line in clean_data_list:
        year = line[7: 11]
        (years_empty_values[year]).append(clean_data_dict.get(line[0:11]))
        year_daily_averages[year] = statistics.mean(years_empty_values[year])
    return year_daily_averages

# ********************************************* PRINTING FUNCTIONS *********************************************
def print_day_with_record_rainfall(day_with_with_record_rainfall, record_rainfall):
    print_buffer_header_and_clear_terminal()
    print ("\nThe day with record rainfall was {} with {:.2f} inches\n".format(day_with_with_record_rainfall, record_rainfall * 0.01))
    print_continue_or_not()
def print_average_rainfall_for_day(day_averages):
    print_buffer_header_and_clear_terminal()
    print ("Please select the month:  MMM")
    month = input('Month  > > >  ').upper()

    print_buffer_header_and_clear_terminal()
    print ("Please select day of month:  DD")
    day = input('Day  > > >  ')

    print_buffer_header_and_clear_terminal()
    date = str(day + '-' + month)
    if date in day_averages:
        day_averages_in_inches = {}
        day_averages_in_inches[date] = day_averages[date] * 0.01
        print ("The average rainfall for {} is {:.2f} inches\n".format(date, day_averages_in_inches[date]))

    print_continue_or_not()
def print_average_rainfall_for_month(monthly_averages):
    print_buffer_header_and_clear_terminal()
    print("Please select the month:  MMM")
    month = input('Month  > > >  ').upper()

    month = str(month)
    print_buffer_header_and_clear_terminal()
    if month in monthly_averages:
        monthly_averages_in_inches = {}
        monthly_averages_in_inches[month] = monthly_averages[month] * 0.01
        print("The average rainfall for {} is {:.2f} inches\n".format(month, monthly_averages_in_inches[month]))

    print_continue_or_not()
def print_rainfall_for_specific_day_and_year(clean_data_dict):
    print_buffer_header_and_clear_terminal()
    print ("Please select the year:  YYYY")
    year = input('Year  > > >  ')

    print_buffer_header_and_clear_terminal()
    print ("Please select the month:  MMM")
    month = input('Month  > > >  ').upper()

    print_buffer_header_and_clear_terminal()
    print ("Please select day of month:  DD")
    day = input('Day  > > >  ')

    print_buffer_header_and_clear_terminal()
    date = str(day + '-' + month + '-' + year)
    if date in clean_data_dict:
        date_in_inches = {}
        date_in_inches[date] = clean_data_dict[date] * 0.01
        print("The total rainfall on {} was {:.2f} inches\n".format(date, date_in_inches[date]))

    print_continue_or_not()
def print_total_and_average_daily_rainfall_for_month_of_year(specific_monthly_averages, specific_monthly_totals):
    print_buffer_header_and_clear_terminal()
    print ("Please select the year:  YYYY")
    year = input('Year  > > >  ')

    print_buffer_header_and_clear_terminal()
    print ("Please select the month:  MMM")
    month = input('Month  > > >  ').upper()

    print_buffer_header_and_clear_terminal()
    month_of_year = str(month + '-' + year)
    if month_of_year in specific_monthly_totals:
        specific_monthly_totals_in_inches = {}
        specific_monthly_totals_in_inches[month_of_year] = specific_monthly_totals[month_of_year] * 0.01
        specific_monthly_averages_in_inches = {}
        specific_monthly_averages_in_inches[month_of_year] = specific_monthly_averages[month_of_year] * 0.01
        print ("The total rainfall in {} of {} was {:.2f} inches\n".format(month, year, specific_monthly_totals_in_inches[month_of_year]))
        print ("The average daily rainfall in {} of {} was {:.2f} inches\n".format(month, year, specific_monthly_averages_in_inches[month_of_year]))

    print_continue_or_not()
def print_total_and_average_daily_rainfall_for_year(year_totals, year_daily_averages):
    print_buffer_header_and_clear_terminal()
    print ("Please select the year:  YYYY")
    year = input('Year  > > >  ')

    print_buffer_header_and_clear_terminal()
    year = str(year)
    if year in year_totals:
        year_totals_in_inches = {}
        year_totals_in_inches[year] = year_totals[year] * 0.01
        year_daily_averages_in_inches = {}
        year_daily_averages_in_inches[year] = year_daily_averages[year] * 0.01
        print ("The total rainfall in {} was {:.2f} inches\n".format(year, year_totals_in_inches[year]))
        print ("The average daily rainfall in {} was {:.2f} inches\n".format(year, year_daily_averages_in_inches[year]))
    print_continue_or_not()
def print_total_and_average_rainfall_for_every_year(years_dict, year_totals, year_daily_averages):
    print_buffer_header_and_clear_terminal()
    for year in years_dict:
        year_totals_in_inches = {}
        year_totals_in_inches[year] = year_totals[year] * 0.01
        year_daily_averages_in_inches = {}
        year_daily_averages_in_inches[year] = year_daily_averages[year] * 0.01
        print ("\n\n\t\t~~~ {} ~~~\n".format(year))
        print ("Total rainfall:   {:.2f} inches".format(year_totals_in_inches[year]))
        print ("Average daily:    {:.2f} inches\n".format(year_daily_averages_in_inches[year]))

    print_continue_or_not()

# ********************************************* USER INTERACTION FUNCTIONS *********************************************
def print_welcome_display():
    os.system('clear')
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print ("""
     . \t | \t | \t | \t | \t   \t . \t | \t |
       \t . \t | \t | \t | \t | \t   \t . \t |
     | \t   \t . \t | \t | \t | \t | \t   \t .
     | \t | \t   \t . \t | \t | \t | \t | \t
     | \t | \t | \t   \t . \t | \t | \t | \t |
     | \t | \t | \t | \t   \t . \t | \t | \t |
     . \t | \t | \t | \t | \t   \t . \t | \t |
       \t\./\t\ /\t   \t   \t   \t   \t\./\t\ /\t 0.1 in
    """)
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n")
    print("Welcome to rain data tracker 2.0!")
    time.sleep(0.3)

    os.system('clear')
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print ("""
     | \t | \t | \t | \t   \t . \t | \t | \t |
     . \t | \t | \t | \t | \t   \t . \t | \t |
       \t . \t | \t | \t | \t | \t   \t . \t |
     | \t   \t . \t | \t | \t | \t | \t   \t .
     | \t | \t   \t . \t | \t | \t | \t | \t
     | \t | \t | \t   \t . \t | \t | \t | \t |
     | \t | \t | \t | \t   \t . \t | \t | \t |
    \./\t\ /\t   \t   \t   \t   \t\./\t\ /\t   \t 0.2 in
    """)
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n")
    print("Welcome to rain data tracker 2.0!")
    time.sleep(0.3)

    os.system('clear')
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print ("""
     | \t | \t | \t   \t . \t | \t | \t | \t |
     | \t | \t | \t | \t   \t . \t | \t | \t |
     . \t | \t | \t | \t | \t   \t . \t | \t |
       \t . \t | \t | \t | \t | \t   \t . \t |
     | \t   \t . \t | \t | \t | \t | \t   \t .
     | \t | \t   \t . \t | \t | \t | \t | \t
     | \t | \t | \t   \t . \t | \t | \t | \t |
    \ /\t   \t   \t   \t   \t\./\t\ /\t   \t   \t 0.3 in
    """)
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n")
    print("Welcome to rain data tracker 2.0!")
    time.sleep(0.3)

    os.system('clear')
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print ("""
     | \t | \t   \t . \t | \t | \t | \t | \t |
     | \t | \t | \t   \t . \t | \t | \t | \t |
     | \t | \t | \t | \t   \t . \t | \t | \t |
     . \t | \t | \t | \t | \t   \t . \t | \t |
       \t . \t | \t | \t | \t | \t   \t . \t |
     | \t   \t . \t | \t | \t | \t | \t   \t .
     | \t | \t   \t . \t | \t | \t | \t | \t
       \t   \t   \t   \t\./\t\ /\t   \t   \t   \t 0.4 in
    """)
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n")
    print("Welcome to rain data tracker 2.0!")
    time.sleep(0.3)

    os.system('clear')
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print ("""
     | \t   \t . \t | \t | \t | \t | \t   \t .
     | \t | \t   \t . \t | \t | \t | \t | \t
     | \t | \t | \t   \t . \t | \t | \t | \t |
     | \t | \t | \t | \t   \t . \t | \t | \t |
     . \t | \t | \t | \t | \t   \t . \t | \t |
       \t . \t | \t | \t | \t | \t   \t . \t |
     | \t   \t . \t | \t | \t | \t | \t   \t .
       \t   \t   \t\./\t\ /\t   \t   \t   \t   \t 0.5 in
    """)
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n")
    print("Welcome to rain data tracker 2.0!")
    time.sleep(0.3)

    os.system('clear')
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print ("""
       \t . \t | \t | \t | \t | \t   \t . \t |
     | \t   \t . \t | \t | \t | \t | \t   \t .
     | \t | \t   \t . \t | \t | \t | \t | \t
     | \t | \t | \t   \t . \t | \t | \t | \t |
     | \t | \t | \t | \t   \t . \t | \t | \t |
     . \t | \t | \t | \t | \t   \t . \t | \t |
       \t . \t | \t | \t | \t | \t   \t . \t |
       \t   \t\./\t\ /\t   \t   \t   \t   \t\./\t 0.4 in
    """)
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n")
    print("Welcome to rain data tracker 2.0!")
    time.sleep(0.3)

    os.system('clear')
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print ("""
     . \t | \t | \t | \t | \t   \t . \t | \t |
       \t . \t | \t | \t | \t | \t   \t . \t |
     | \t   \t . \t | \t | \t | \t | \t   \t .
     | \t | \t   \t . \t | \t | \t | \t | \t
     | \t | \t | \t   \t . \t | \t | \t | \t |
     | \t | \t | \t | \t   \t . \t | \t | \t |
     . \t | \t | \t | \t | \t   \t . \t | \t |
       \t\./\t\ /\t   \t   \t   \t   \t\./\t\ /\t 0.7 in
    """)
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n")
    print("Welcome to rain data tracker 2.0!")
    time.sleep(0.3)

    os.system('clear')
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print ("""
     | \t | \t | \t | \t   \t . \t | \t | \t |
     . \t | \t | \t | \t | \t   \t . \t | \t |
       \t . \t | \t | \t | \t | \t   \t . \t |
     | \t   \t . \t | \t | \t | \t | \t   \t .
     | \t | \t   \t . \t | \t | \t | \t | \t
     | \t | \t | \t   \t . \t | \t | \t | \t |
     | \t | \t | \t | \t   \t . \t | \t | \t |
    \./\t\ /\t   \t   \t   \t   \t\./\t\ /\t   \t 0.8 in
    """)
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n")
    print("Welcome to rain data tracker 2.0!")
    time.sleep(0.3)

    os.system('clear')
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print ("""
     | \t | \t | \t   \t . \t | \t | \t | \t |
     | \t | \t | \t | \t   \t . \t | \t | \t |
     . \t | \t | \t | \t | \t   \t . \t | \t |
       \t . \t | \t | \t | \t | \t   \t . \t |
     | \t   \t . \t | \t | \t | \t | \t   \t .
     | \t | \t   \t . \t | \t | \t | \t | \t
     | \t | \t | \t   \t . \t | \t | \t | \t |
    \ /\t   \t   \t   \t   \t\./\t\ /\t   \t   \t 0.9 in
    """)
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n")
    print("Welcome to rain data tracker 2.0!")
    time.sleep(0.3)

    os.system('clear')
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print ("""
     | \t | \t | \t . \t | \t | \t | \t | \t
     | \t | \t | \t   \t . \t | \t | \t | \t |
     | \t | \t | \t | \t   \t . \t | \t | \t |
     . \t | \t | \t | \t | \t   \t . \t | \t |
       \t . \t | \t | \t | \t | \t   \t . \t |
     | \t   \t . \t | \t | \t | \t | \t   \t .
     | \t | \t   \t . \t | \t | \t | \t | \t
       \t   \t   \t   \t\./\t\ /\t   \t   \t   \t 1.0 in
    """)
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n")
    print("Welcome to rain data tracker 2.0!")
    time.sleep(0.3)


    os.system('clear')
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print ("""
     | \t   \t . \t | \t | \t | \t | \t   \t .
     | \t | \t   \t . \t | \t | \t | \t | \t
     | \t | \t | \t   \t . \t | \t | \t | \t |
     | \t | \t | \t | \t   \t . \t | \t | \t |
     . \t | \t | \t | \t | \t   \t . \t | \t |
       \t . \t | \t | \t | \t | \t   \t . \t |
     | \t   \t . \t | \t | \t | \t | \t   \t .
       \t   \t   \t\./\t\ /\t   \t   \t   \t   \t 1.0 in!!!
    """)
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n")
    print("Welcome to rain data tracker 2.0!")
    time.sleep(0.3)

    os.system('clear')
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print ("""
       \t . \t | \t | \t | \t | \t   \t . \t |
     | \t   \t . \t | \t | \t | \t | \t   \t .
     | \t | \t   \t . \t | \t | \t | \t | \t
     | \t | \t | \t   \t . \t | \t | \t | \t |
     | \t | \t | \t | \t   \t . \t | \t | \t |
     . \t | \t | \t | \t | \t   \t . \t | \t |
       \t . \t | \t | \t | \t | \t   \t . \t |
       \t   \t\./\t\ /\t   \t   \t   \t   \t\./\t 1.0 in!!!!!!
    """)
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n")
    print("Welcome to rain data tracker 2.0!")
    time.sleep(0.3)

    os.system('clear')
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print ("""
     . \t | \t | \t | \t | \t   \t . \t | \t |
       \t . \t | \t | \t | \t | \t   \t . \t |
     | \t   \t . \t | \t | \t | \t | \t   \t .
     | \t | \t   \t . \t | \t | \t | \t | \t
     | \t | \t | \t   \t . \t | \t | \t | \t |
     | \t | \t | \t | \t   \t . \t | \t | \t |
     . \t | \t | \t | \t | \t   \t . \t | \t |
       \t\./\t\ /\t   \t   \t   \t   \t\./\t\ /\t 1.0 in!!!!!!!!!
    """)
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n")
    print("Welcome to rain data tracker 2.0!")
    time.sleep(1.2)
def print_buffer_header_and_clear_terminal():
    os.system('clear')
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print ("""
     . \t | \t | \t | \t | \t   \t . \t | \t |
       \t . \t | \t | \t | \t | \t   \t . \t |
     | \t   \t . \t | \t | \t | \t | \t   \t .
     | \t | \t   \t . \t | \t | \t | \t | \t
     | \t | \t | \t   \t . \t | \t | \t | \t |
     | \t | \t | \t | \t   \t . \t | \t | \t |
     . \t | \t | \t | \t | \t   \t . \t | \t |
       \t\./\t\ /\t   \t   \t   \t   \t\./\t\ /\t
    """)
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n")
    time.sleep(0.4)
def print_continue_or_not():
    print ("\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print("\n\n\n\n\n\n\nEnter:\tY = continue \tN = exit\n\n")
    cont = input("Continue?  > > >  ").upper()
    if cont == 'Y':
        cont = True
    if cont == 'N':
        print_outgoing_display()
    else:
        cont = True
    return cont
def print_user_options():
    os.system('clear')
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print ("""
    \tA - Day with most rainfall
    \tB - Average rainfall for a day of the year
    \tC - Average rainfall for a month of the year
    \tD - Total rainfall for a specific day
    \tE - Total and average daily rainfall for a specific month
    \tF - Total and average daily rainfall for a specific year
    \tG - Total rainfall for every year
    \tQ - Exit program
    """)
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n")
def get_user_choice():
    choice = input("Your choice  > > >  ").upper()
    return choice
def call_functions_off_choice(choice):
    if choice == 'A': # Day with most rainfall
        print_day_with_record_rainfall(day_with_with_record_rainfall, record_rainfall)
    if choice == 'B': # Average rainfall for a day of the year
        print_average_rainfall_for_day(day_averages)
    if choice == 'C': # Average rainfall for a month of the year
        print_average_rainfall_for_month(monthly_averages)
    if choice == 'D': # Total rainfall for a specific day
        print_rainfall_for_specific_day_and_year(clean_data_dict)
    if choice == 'E': # Total and average daily rainfall for a specific month
        print_total_and_average_daily_rainfall_for_month_of_year(specific_monthly_averages, specific_monthly_totals)
    if choice == 'F': # Total and average daily rainfall for a specific year
        print_total_and_average_daily_rainfall_for_year(year_totals, year_daily_averages)
    if choice == 'G': # Total rainfall for every year
        print_total_and_average_rainfall_for_every_year(years_dict, year_totals, year_daily_averages)
    if choice == 'Q': # Exit program
        print_outgoing_display()
        quit()

def print_outgoing_display():
    os.system('clear')
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print ("""
     . \t | \t | \t | \t | \t   \t . \t | \t |
       \t . \t | \t | \t | \t | \t   \t . \t |
     | \t   \t . \t | \t | \t | \t | \t   \t .
     | \t | \t   \t . \t | \t | \t | \t | \t
     | \t | \t | \t   \t . \t | \t | \t | \t |
     | \t | \t | \t | \t   \t . \t | \t | \t |
     . \t | \t | \t | \t | \t   \t . \t | \t |
       \t\./\t\ /\t   \t   \t   \t   \t\./\t\ /\t
    """)
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n")
    time.sleep(0.4)

    os.system('clear')
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print ("""
     | \t | \t | \t | \t   \t . \t | \t | \t |
     . \t | \t | \t | \t | \t   \t . \t | \t |
       \t . \t | \t | \t | \t | \t   \t . \t |
     | \t   \t . \t | \t | \t | \t | \t   \t .
     | \t | \t   \t . \t | \t | \t | \t | \t
     | \t | \t | \t   \t . \t | \t | \t | \t |
     | \t | \t | \t | \t   \t . \t | \t | \t |
    \./\t\ /\t   \t   \t   \t   \t\./\t\ /\t   \t Goodbye
    """)
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n")
    time.sleep(0.4)

    os.system('clear')
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print ("""
     | \t | \t | \t   \t . \t | \t | \t | \t |
     | \t | \t | \t | \t   \t . \t | \t | \t |
     . \t | \t | \t | \t | \t   \t . \t | \t |
       \t . \t | \t | \t | \t | \t   \t . \t |
     | \t   \t . \t | \t | \t | \t | \t   \t .
     | \t | \t   \t . \t | \t | \t | \t | \t
     | \t | \t | \t   \t . \t | \t | \t | \t |
    \ /\t   \t   \t   \t   \t\./\t\ /\t   \t   \t Goodbye!!!
    """)
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n")
    time.sleep(0.4)

    os.system('clear')
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print ("""
     | \t | \t   \t . \t | \t | \t | \t | \t |
     | \t | \t | \t   \t . \t | \t | \t | \t |
     | \t | \t | \t | \t   \t . \t | \t | \t |
     . \t | \t | \t | \t | \t   \t . \t | \t |
       \t . \t | \t | \t | \t | \t   \t . \t |
     | \t   \t . \t | \t | \t | \t | \t   \t .
     | \t | \t   \t . \t | \t | \t | \t | \t
       \t   \t   \t   \t\./\t\ /\t   \t   \t   \t Goodbye!!!!!!
    """)
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n")
    time.sleep(0.4)

    os.system('clear')
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print ("""
     | \t   \t . \t | \t | \t | \t | \t   \t .
     | \t | \t   \t . \t | \t | \t | \t | \t
     | \t | \t | \t   \t . \t | \t | \t | \t |
     | \t | \t | \t | \t   \t . \t | \t | \t |
     . \t | \t | \t | \t | \t   \t . \t | \t |
       \t . \t | \t | \t | \t | \t   \t . \t |
     | \t   \t . \t | \t | \t | \t | \t   \t .
       \t   \t   \t\./\t\ /\t   \t   \t   \t   \t Goodbye!!!!!!!!!
    """)
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n")
    time.sleep(0.4)

    os.system('clear')
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print ("""
       \t . \t | \t | \t | \t | \t   \t . \t |
     | \t   \t . \t | \t | \t | \t | \t   \t .
     | \t | \t   \t . \t | \t | \t | \t | \t
     | \t | \t | \t   \t . \t | \t | \t | \t |
     | \t | \t | \t | \t   \t . \t | \t | \t |
     . \t | \t | \t | \t | \t   \t . \t | \t |
       \t . \t | \t | \t | \t | \t   \t . \t |
       \t   \t\./\t\ /\t   \t   \t   \t   \t\./\t Goodbye
    """)
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n")
    time.sleep(0.4)

    os.system('clear')
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print ("""
     . \t | \t | \t | \t | \t   \t . \t | \t |
       \t . \t | \t | \t | \t | \t   \t . \t |
     | \t   \t . \t | \t | \t | \t | \t   \t .
     | \t | \t   \t . \t | \t | \t | \t | \t
     | \t | \t | \t   \t . \t | \t | \t | \t |
     | \t | \t | \t | \t   \t . \t | \t | \t |
     . \t | \t | \t | \t | \t   \t . \t | \t |
       \t\./\t\ /\t   \t   \t   \t   \t\./\t\ /\t Goodbye!!!
    """)
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n")
    time.sleep(0.4)

    os.system('clear')
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print ("""
     | \t | \t | \t | \t   \t . \t | \t | \t |
     . \t | \t | \t | \t | \t   \t . \t | \t |
       \t . \t | \t | \t | \t | \t   \t . \t |
     | \t   \t . \t | \t | \t | \t | \t   \t .
     | \t | \t   \t . \t | \t | \t | \t | \t
     | \t | \t | \t   \t . \t | \t | \t | \t |
     | \t | \t | \t | \t   \t . \t | \t | \t |
    \./\t\ /\t   \t   \t   \t   \t\./\t\ /\t   \t Goodbye!!!!!
    """)
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n")
    time.sleep(0.4)

    os.system('clear')
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print ("""
     | \t | \t | \t   \t . \t | \t | \t | \t |
     | \t | \t | \t | \t   \t . \t | \t | \t |
     . \t | \t | \t | \t | \t   \t . \t | \t |
       \t . \t | \t | \t | \t | \t   \t . \t |
     | \t   \t . \t | \t | \t | \t | \t   \t .
     | \t | \t   \t . \t | \t | \t | \t | \t
     | \t | \t | \t   \t . \t | \t | \t | \t |
    \ /\t   \t   \t   \t   \t\./\t\ /\t   \t   \t Goodbye!!!!!!!!!
    """)
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n")
    time.sleep(0.4)

    os.system('clear')
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print ("""
     | \t | \t | \t . \t | \t | \t | \t | \t
     | \t | \t | \t   \t . \t | \t | \t | \t |
     | \t | \t | \t | \t   \t . \t | \t | \t |
     . \t | \t | \t | \t | \t   \t . \t | \t |
       \t . \t | \t | \t | \t | \t   \t . \t |
     | \t   \t . \t | \t | \t | \t | \t   \t .
     | \t | \t   \t . \t | \t | \t | \t | \t
       \t   \t   \t   \t\./\t\ /\t   \t   \t   \t Goodbye
    """)
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n")
    time.sleep(0.4)


    os.system('clear')
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print ("""
     | \t   \t . \t | \t | \t | \t | \t   \t .
     | \t | \t   \t . \t | \t | \t | \t | \t
     | \t | \t | \t   \t . \t | \t | \t | \t |
     | \t | \t | \t | \t   \t . \t | \t | \t |
     . \t | \t | \t | \t | \t   \t . \t | \t |
       \t . \t | \t | \t | \t | \t   \t . \t |
     | \t   \t . \t | \t | \t | \t | \t   \t .
       \t   \t   \t\./\t\ /\t   \t   \t   \t   \t Goodbye!!!
    """)
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n")
    time.sleep(0.4)

    os.system('clear')
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print ("""
       \t . \t | \t | \t | \t | \t   \t . \t |
     | \t   \t . \t | \t | \t | \t | \t   \t .
     | \t | \t   \t . \t | \t | \t | \t | \t
     | \t | \t | \t   \t . \t | \t | \t | \t |
     | \t | \t | \t | \t   \t . \t | \t | \t |
     . \t | \t | \t | \t | \t   \t . \t | \t |
       \t . \t | \t | \t | \t | \t   \t . \t |
       \t   \t\./\t\ /\t   \t   \t   \t   \t\./\t Goodbye!!!!!!
    """)
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n")
    time.sleep(0.4)

    os.system('clear')
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print ("""
     . \t | \t | \t | \t | \t   \t . \t | \t |
       \t . \t | \t | \t | \t | \t   \t . \t |
     | \t   \t . \t | \t | \t | \t | \t   \t .
     | \t | \t   \t . \t | \t | \t | \t | \t
     | \t | \t | \t   \t . \t | \t | \t | \t |
     | \t | \t | \t | \t   \t . \t | \t | \t |
     . \t | \t | \t | \t | \t   \t . \t | \t |
       \t\./\t\ /\t   \t   \t   \t   \t\./\t\ /\t Goodbye!!!!!!!!!
    """)
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n")
    time.sleep(2)
    quit()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ CALLING FUNCTIONS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ********************************************* CORE FUNCTIONS *********************************************
line_list = break_site_into_line_list(site)
clean_data_list = clean_the_data(line_list)

day_totals = assign_day_totals(clean_data_list)
clean_data_dict = create_dict_from_list(clean_data_list, day_totals)

record_rainfall = get_record_rainfall(clean_data_dict)
day_with_with_record_rainfall = identify_day_with_record_rainfall(record_rainfall, clean_data_dict)

days_empty_values = assign_days_to_keys(clean_data_dict)
day_averages = assign_day_averages(days_empty_values, clean_data_dict)

months_empty_values = assign_months_to_keys(clean_data_dict)
monthly_averages = assign_monthly_averages(months_empty_values, clean_data_list, clean_data_dict)

specific_months_empty_values = assign_specific_months_to_keys(clean_data_list)
specific_monthly_totals = assign_specific_monthly_totals(specific_months_empty_values, clean_data_list, clean_data_dict)
specific_monthly_averages = assign_daily_averages_for_specific_month(specific_months_empty_values, clean_data_list, clean_data_dict)

years_empty_values = assign_years_to_keys(clean_data_list)
years_dict = assign_values_to_year(years_empty_values, clean_data_list, clean_data_dict)
year_totals = assign_year_totals(years_dict, clean_data_list)
year_daily_averages = assign_year_daily_averages(years_empty_values, clean_data_dict, clean_data_list)

# ********************************************* USER INTERACTION FUNCTIONS *********************************************
print_welcome_display()

cont = True
while cont:
    print_user_options()
    choice = get_user_choice()
    call_functions_off_choice(choice)

print_outgoing_display()
