import rainfall3.py

# ********************************************* USER INTERACTION FUNCTIONS *********************************************
# print (specific_monthly_totals)
# time.sleep(30)

print_welcome_display()

cont = True
while cont:
    print_user_options()
    choice = get_user_choice()
    call_functions_off_choice(choice)

print_outgoing_display()
