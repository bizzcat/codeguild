import random
# class Person(object):
#     _registry = []
#
#     def __init__(self, name):
#         self._registry.append(self)
#         self.name = name
#
# for p in Person._registry:
#     print p

class account_setup:
    def __init__(self, account_user_name, account_ID, account_PIN, _database):
        self.account_user_name = account_user_name
        self.account_ID = account_ID
        self.account_PIN = account_PIN
        self._database.append(self)

    def __str__(self):
        return """
        Account details:
        Name                       -   {}
        ID                         -   {}
        PIN                        -   {}
        """.format(self.account_user_name, self.account_ID, self.account_PIN)


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


def continue_or_not():
    print("\n\nWould you like to perform another transaction? (Y or N)")
    decision = input(" > > >  ")
    return decision == 'Y'


# bank_database = {}
_database = []

cont = True
while cont:
    account_user_name = get_account_user_name()
    account_ID = assign_account_ID()
    account_PIN = get_account_PIN()
    account_setup(account_user_name, account_ID, account_PIN, _database)
    # bank_database[account_ID] = {'account_user_name': account.account_user_name, 'account_PIN':account.account_PIN}
    cont = continue_or_not()

for account in _database:
    print(account)

















    #
