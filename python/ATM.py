import random

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def print_user_options():
    print("""
    Please choose from the following options:
    A  -  Create a new account
    B  -  Deposit into savings
    C  -  Deposit into checking
    D  -  Withdraw from savings
    E  -  Withdraw from checking
    F  -  Check account balances
    G  -  Open up savings in existing account
    H  -  Open up checking in existing account
    Q  -  Exit
    """)
    user_choice = input('  > > >  ').upper()
    return user_choice

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ACCOUNT FUNCTIONS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class account_setup:
    def __init__(self, account_user_name, account_ID, account_PIN):
        self.account_user_name = account_user_name
        self.account_ID = account_ID
        self.account_PIN = account_PIN
    def __str__(self):
        return """\n
        Account details:
        Name                       -   {}
        ID                         -   {}
        PIN                        -   {}
        \n""".format(self.account_user_name, self.account_ID, self.account_PIN)

def get_account_user_name():
    print("What name would you like under this new account?")
    account_user_name = input('  > > >  ')
    return account_user_name
def assign_account_ID():
    random_num = random.randint(1, 10000)
    account_ID = '{:0>7}'.format(random_num)
    return account_ID
def get_account_PIN():
    print("Please select a 4 digit numerical PIN for your account.")
    account_PIN = int(input('  > > >  '))
    while len(str(account_PIN)) < 4 or len(str(account_PIN)) > 4:
        print("ERROR: Must use 4 digit numerical PIN.   ex: 5643 ")
        account_PIN = input('  > > >  ')
    return account_PIN

def checking_or_savings_choice():
    print("""
    Would you like to open a checking or savings account; or both?
    A  -  Checking
    B  -  Savings
    C  -  Both
    """)
    choice = input('  > > >  ')

# def create_new_checking_or_savings_off_choice(choice, bank_database, account_user_name):
#     if choice == 'A':
#         bank_database[account_user_name] = create_checking(bank_database, account_user_name)
#         print(bank_database[account_user_name])
#     if choice == 'B':
#         bank_database[account_user_name] = create_savings(bank_database, account_user_name)
#     if choice == 'C':
#         bank_database[account_user_name] = create_checking(bank_database, account_user_name)
#         bank_database[account_user_name] = create_savings(bank_database, account_user_name)
#     # else:
#     #     print("Please select a valid option, A or B or C")
#     return bank_database

def create_checking(bank_database, account_user_name):
    if 'checking_balance' not in bank_database[account_user_name]:
        bank_database[account_user_name]['checking_balance'] = 0
    else:
        print("Sorry, only one checking allowed per account.")
    return bank_database
def create_savings(bank_database, account_user_name):
    if 'savings_balance' not in bank_database[account_user_name]:
        bank_database[account_user_name]['savings_balance'] = 0
    else:
        print("Sorry, only one savings allowed per account.")
    return bank_database

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ATM FUNCTIONS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def get_user_name_input():
    print("Please enter your name")
    user_name_input = input('Name  > > >  ')
    return user_name_input
def get_user_PIN_input():
    user_PIN_input = input('PIN   > > >  ')
    return user_PIN_input
def grant_or_deny_ATM_access(user_name_input, user_PIN_input):
    if user_name_input in bank_database:
        if user_PIN_input in bank_database[user_name_input][account_PIN]:
            return True
    if user_name_input not in bank_database:
        return False
    if user_PIN_input not in bank_database[user_name_input][account_PIN]:
        return False
class ATM:
    def __init__(self, account_user_name, account_checking, account_savings, bank_database):
        self.account = bank_database[account_user_name]
        self.account_user_name = bank_database[account_user_name][account_user_name]
        self.account_checking = bank_database[account_user_name][checking_balance]
        self.account_savings = bank_database[account_user_name][savings_balance]

    def deposit_into_savings(self, account_savings):
        self.account_checking = self.account_savings + savings_deposit
        bank_database[account_user_name][savings_balance] = self.account_savings
        return bank_database
    def deposit_into_checking(self, bank_database, checking_deposit):
        self.account_checking = self.account_checking + checking_deposit
        bank_database[account_user_name][checking_balance] = self.account_checking
        return bank_database

    def check_for_insufficient_savings(self, savings_withdrawal):
        if savings_withdrawal > self.account_savings:
            cont = False
        else:
            cont = True
        return cont
    def check_for_insufficient_checking(self, checking_withdrawal):
        if checking_withdrawal > self.account_checking:
            cont = False
        else:
            cont = True
        return cont

    def withdraw_from_savings(self, savings_withdrawal):
        self.account_savings = self.account_savings + savings_withdrawal
        bank_database[account_user_name][savings_balance] = self.account_savings
        return bank_database
    def withdraw_from_checking(self, checking_withdrawal):
        self.account_checking = self.account_checking - checking_withdrawal
        bank_database[account_user_name][checking_balance] = self.account_checking
        return bank_database

    def calculate_interest_on_savings(self):
        interest_accrued = self.account_savings * 0.05
        account_savings_with_interest = self.account_savings + interest_accrued
        return account_savings_with_interest

    def __str__(self, account_savings_with_interest):
        return """
        \nAccount overview:
        Name                       -   {}
        Checking balance           -   ${:,}
        Savings balance            -   ${:,}
        Savings after interest     -   ${:,}
        """.format(self.account_user_name, self.account_checking, self.account_savings, account_savings_with_interest)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

bank_database = {}

cont = True
while cont:
    user_choice = print_user_options()
    if user_choice == 'A': #Create account
        account_user_name = get_account_user_name()
        account_ID = assign_account_ID()
        account_PIN = get_account_PIN()
        account = account_setup(account_user_name, account_ID, account_PIN)
        print(account)
        bank_database[account_user_name] = {'account_ID': account.account_ID, 'account_PIN':account.account_PIN}
        choice = checking_or_savings_choice()
        if choice == 'A':
            bank_database[account_user_name] = create_checking(bank_database, account_user_name)
            print(bank_database[account_user_name])
        if choice == 'B':
            bank_database[account_user_name] = create_savings(bank_database, account_user_name)
        if choice == 'C':
            bank_database[account_user_name] = create_checking(bank_database, account_user_name)
            bank_database[account_user_name] = create_savings(bank_database, account_user_name)

    if user_choice == 'Q': #QUIT
        cont = False

    else:
        user_name_input = get_user_name_input()
        user_PIN_input = get_user_PIN_input()
        access = grant_or_deny_ATM_access(user_name_input, user_PIN_input)
        while access:
            if user_choice == 'B': #Deposit into savings
                print("How much would you like to deposit into savings?")
                savings_deposit = input("  > > >  ")
                bank_database = deposit_into_savings(account_savings)
            if user_choice == 'C': #Deposit into checking
                print("How much would you like to deposit into checking?")
                checking_deposit = input("  > > >  ")
                bank_database = deposit_into_checking(account_checking, checking_deposit)

            if user_choice == 'D': #Withdraw from savings
                cont = check_for_insufficient_savings(account_savings)
                bank_database = withdraw_from_savings(account_savings)

            if user_choice == 'E': #Withdraw from checking
                cont = check_for_insufficient_checking(account_checking)
                bank_database = withdraw_from_checking(account_checking)

            if user_choice == 'F': #Check account balances
                account_savings_with_interest = calculate_interest_on_savings(account_savings)
                account_overview = ATM(account_user_name, account_checking, account_savings)
            # if user_choice == 'G': #Open up savings in existing account
            #
            # if user_choice == 'H': #Open up checking in existing account
    print(bank_database)

print(bank_database)
input('Present Enter to close. ')
quit()




#~~~~~~~~~~~~~~~~~~~~~~ NOTES
print("\n\n")
print(account_user_name)
print("\n\n")
print(account)
print("\n\n")
print(bank_database)
print("\n\n")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ATM FUNCTIONS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# def get_user_name():
#
# def get_savings_deposit():
# def get_checkings_deposit():
#
# def get_savings_withdrawal():
# def get_checkings_withdrawal():
#
# def call_functions_off_user_choice():
#
# bank_database = {}


















#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




























    #
