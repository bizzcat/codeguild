# class AddressBookEntry:
#     def __init__(self, name, phone_number, city):
#         self.name = name
#         self.phone_number = phone_number
#         self.city = city
#
#     def __str__(self):
#         return "\nAddressBookEntry({}, {}, {})\n".format(self.name, self.phone_number, self.city)
#
# female1 = AddressBookEntry('Allison', '503 784 2617', 'Portland')
#
# print(female1)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ATM PRACTICE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class ATM:
    def __init__(self, name, balance, database):
        self.name = name
        self.balance = balance
        self.database_total = database[name]
    def deposit_money(self, deposit):
        self.balance = self.balance + deposit
    def withdraw_money(self, withdrawal):
        if self.balance >= withdrawal:
            self.balance = self.balance - withdrawal
        else:
            print("\nError, insufficient funds")
    # def calculate_interest(self):
    #     account_interest = (sum(self.database_total) * 1.05)
    #     print("Account interest of 0.05%  would increase total account balance from ${:,} to ${:,}".format(sum(self.database_total), (account_interest)))
    def __str__(self):
        return "\nAccount balance for {} has been updated by ${:,} for a total account balance of ${:,}".format(self.name, (self.balance - self.withdrawal), sum(self.database_total))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def take_name():
    print("\n\nWhat is your name?")
    name = input(" > > >  ")
    return name
def create_account(name, database):
    if name in database:
        database[name] = [database[name]]
    if name not in database:
        database[name] = []
    return database
def take_deposit():
    print("\nHow much would you like to deposit?")
    deposit = int(input(" > > >  "))
    return deposit
def take_withdrawal():
    print("\nHow much would you like to withdraw?")
    withdrawal = int(input(" > > >  "))
    return withdrawal
def continue_or_not():
    print("\n\nWould you like to perform another transaction? (Y or N)")
    decision = input(" > > >  ")
    return decision == 'Y'

database = {}
balance = 0
cont = True
while cont:
    name = take_name()
    database = create_account(name, database)
    deposit = take_deposit()
    withdrawal = take_withdrawal()

    user_account = ATM(name, balance, database)
    user_account.deposit_money(deposit)
    user_account.withdraw_money(withdrawal)
    database[name].append(user_account.balance)
    database[name] = sum(database[name])

    print("\n\n", user_account, "\n\n")
    cont = continue_or_not()

print("\n\n")
for name in database.keys():
    print("{}: ${:,}".format(name, database[name]))
print("\n\n")
end = input('Finished?  ')










# Write a program that functions aas a simple ATM ffor a single account.
#
# An account will be a cclass: it will have a field ffor the balance.
#
# Write functions ffor the account cclass that:
#
# Deposit to the account.
# Check iff enough funds ffor a withdrawal.
# Withdraw an allowed amount.
# Calculate "0.5"% interest on the account.
# Implement a user interface that lets a user pick each of those actions aand updates the account. After each action it will print the balance.
