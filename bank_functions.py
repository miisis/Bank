from customer import Customer

'''Function add_customer_to_the_bank adds a new customer to the bank and 
    creates a new id for them.''' 

def add_customer_to_the_bank(bank):
    name = input("Please enter the name of the customer you want to add to the bank. The first character of the name can't be a space. "
                "If you don't want to add a new customer you can cancel your choice by entering 0.\n")
    if name != '0':
        while name == "" or name[0] == " ":
            name = input("Please name the customer correctly.\n")
        customer = Customer(name, 0) 
        bank.add_customer(customer)
        print("{} is now a customer of {}. Their id is {}.".format(name, bank.name, customer.id))
    return

'''Function remove_customer_from_the_bank removes the given customer from the bank.'''    
    
def remove_customer_from_the_bank(bank):
    customer_id = input("Please enter the id of the customer you want to remove from the bank. " 
                    "If you don't want to remove any customer you can cancel your choice by entering 0.\n")
    if customer_id != '0':
        customer = check_customer(bank, customer_id)
        if customer == None:
            return
        bank.remove_customer(customer)
        print("{} has been removed and isn't the customer of {} anymore.".format(customer.name, bank.name))
    return

'''Function add_an_account_for_a_customer adds either a personal account or a savings account
    for them. It also creates an account number for the new account.'''
    
def add_an_account_for_a_customer(bank):
    customer_id = input("Please enter the id of the customer you want to add the account for. "    
                    "If you don't want to add an account to any customer you can cancel your choice by entering 0.\n")
    if customer_id != '0':
        customer = check_customer(bank, customer_id)
        if customer == None:
            return
        account = input("Please enter 1 if you want to add a personal account and 2 if you want to add a savings account.\n")
        while account != '1' and account != '2':
            account = input("Please enter either 1 or 2.\n")
        if account == '1':
            success = bank.add_personal_account(customer, 0, 0)
        else:
            success = bank.add_savings_account(customer, 0, 0)
            
        print("The account was succesfully added to the customer {}. The account number is {}".format(customer.name, success.account_number))
    return

'''Function withdraw_money decreases the given sum from the given account.
    If there isn't enough money on the account the function does nothing.'''
    
def withdraw_money(bank):
    customer_id = input("Please enter the id of the customer whose money will be withdrawed. "
                        "If you don't want to withdraw any money you can cancel your choice by entering 0.\n")
    if customer_id != '0':
        customer = check_customer(bank, customer_id)
        if customer == None:
            return
        number = input("Please enter the account number of the account that the money will be withdrawed from " 
                    "in the correct format ('FI xxxxxx xxxxxxx xx')\n")
        account = check_account(bank, customer, number)
        if account == None:
            return
        while True:
            try:
                withdraw = input("Please enter the sum which will be withdrawed from the account.\n")
                withdraw = float(withdraw)
                if withdraw < 0:
                    raise ValueError
                break
            except ValueError:
                print("Please enter only positive numbers!")

        success = account.withdraw(withdraw)
        if success == False:
            print("There isn't enough money on this account so we weren't able to withdraw the sum from the account. "
                  "The balance on this account is {}.".format(account.balance))
        else:
            print("The sum was withdrawed from the account.")
    return

'''Function deposit_money increases the balance on the given account with the given sum.'''

def deposit_money(bank):
    customer_id = input("Please enter the id of the customer whose account the money will be deposited to. "
                        "If you don't want to deposit any money you can cancel your choice by entering 0.\n")
    if customer_id != '0':
        customer = check_customer(bank, customer_id)
        if customer == None:
            return
        number = input("Please enter the account number of the account that the money will be deposited to " 
                    "in the correct format ('FI xxxxxx xxxxxxx xx')\n")
        account = check_account(bank, customer, number)
        if account == None:
            return
        while True:
            try:
                deposit = input("Please enter the sum which will be deposited to the account.\n")
                deposit = float(deposit)
                if deposit < 0:
                    raise ValueError
                break
            except ValueError:
                print("Please enter only positive numbers!")

        account.deposit(deposit)
        print("The sum was deposited to the account.")
    return

'''Function transfer_money transfers money from an account to another.'''

def transfer_money(bank):
    id1 = input("Please enter the id of the customer whose account the money will be transfered from. " 
                "If you don't want to transfer any money you can cancel your choice by entering 0.\n")
    if id1 != '0':
        customer1 = check_customer(bank, id1)
        if customer1 == None:
            return
        number1 = input("Please enter the account number of the account that the money will be " 
                        "transfered from in the correct format ('FI xxxxxx xxxxxxx xx')\n")
        account1 = check_account(bank, customer1, number1)   
        if account1 == None:
            return
        id2 = input("Please enter the id of the customer whose account the money will be transfered to.\n")
        customer2 = check_customer(bank, id2)
        if customer2 == None:
            return
        number2 = input("Please enter the account number of the account that the money will be " 
                        "transfered to in the correct format ('FI xxxxxx xxxxxxx xx')\n")
        account2 = check_account(bank, customer2, number2)
        if account2 == None:
            return
        while True:
            try:
                transfer = input("Please enter the sum that will be transfered.\n")
                transfer = float(transfer)
                if transfer < 0:
                    raise ValueError
                break
            except ValueError:
                print("Please enter only positive numbers!")
        success = account1.transfer_to(account2, transfer)
        if success == 1:
            print("The money was transfered succesfully.")
        elif success == -1:
            print("There isn't enough money on the account {} so the transfer coulnd't be done. The balance on this account is {}.".format(number1, account1.balance))
        else:
            print("The transfer failed. You can transfer money from a savings account only to an account which has the same owner.")
    return 

'''Function check_balance checks the balance on the given account.'''

def check_balance(bank):
    customer_id = input("Please enter the id of the customer whose balance you want to check. " 
                        "If you don't want to check anyone's balance you can cancel your choice by entering 0.\n")
    customer = check_customer(bank, customer_id)
    if customer == None:
        return
    number = input("Please enter the account number of the account that you want to check the balance " 
                "from in the correct format ('FI xxxxxx xxxxxxx')\n")
    account = check_account(bank, customer, number)
    if account == None:
        return
    print_balance(account, customer.name)
    return

'''Function print_information prints out all the names and ids of the customers 
    and also all their account numbers and the balances on the accounts.'''


def print_information(bank):
    for customer in bank.customers:
        print("{}, {}:".format(customer.name, customer.id))
        for account in customer.accounts:
            print("{}: {}".format(account.account_number, account.balance))
        print("\n")
    if bank.customers == []:
        print("There's no customers in this bank.")
    return
        
'''Function save_information saves all the existing information (names and ids of all
    customers and all their account numbers including the balances on the accounts).'''

def save_information(bank):
    name = input("Please enter how you want this file to be named. If you don't want to save "
                 "the existing information you can cancel your choice by entering 0.\n")
    if name != '0':
        name = name + ".txt"
        try:
            file = open(name, "w")
            for customer in bank.customers:
                file.write("{},{}".format(customer.name, customer.id))
                for account in customer.accounts:
                    file.write(",{},{}".format(account.account_number, account.balance))
                file.write("\n")
            file.close()
            print("All information has been saved.")
        except OSError:
            print("Something went wrong. Please try again.")
    return

'''Function load_information loads informations from a file and saves it to the bank.'''

def load_information(bank):
    name = input("Please give the name of the file from which you want to load the information. "
                 "If you don't want to load information you can cancel your choice by entering 0.\n")
    if name != '0':
        try:
            file = open(name, "r")
            for line in file:
                l = line.split(',')
                c_name = l[0]
                c_id = l[1].strip('\n')
                customer = Customer(c_name, int(c_id))
                bank.add_customer(customer)
                i = 2
                while i < len(l):
                    account_number = l[i]
                    balance = l[i+1]
                    balance = str(balance)
                    balance.strip('\n')
                    l2 = account_number.split(" ")
                    if l2[3] == '10':
                        bank.add_personal_account(customer, float(balance), account_number)
                    else:
                        bank.add_savings_account(customer, float(balance), account_number)
                    i += 2
            print("The information has been loaded.")
            file.close()
        except OSError:
            print("We weren't able to open the file. Please check the name you gave is correct and try again.")
    return
             
   
'''Function check_customer checks that the given customer is a customer of the bank.'''        
        
def check_customer(bank, customer_id):
    while True:
        try:
            customer_id = int(customer_id)
            break
        except ValueError:
            print("Please enter only numbers!")
            customer_id = input("Please enter the id of the customer.\n")
    customer = bank.get_customer_by_id(customer_id)
    if customer != None:
        if customer.id == customer_id:
            return customer
        
    print("There wasn't any customer with the id you provided. Please check the information",
                "is correct and try again.")
    return None  

'''Function check_account checks that the given customer and the given account number match.'''

def check_account(bank, customer, number):
    accountlist = bank.get_accounts(customer)
    if accountlist == []:
        print("Customer {} doesn't have any accounts in this bank.".format(customer.name))
        return None
    account = None
    for i in accountlist:
        if i.account_number == number:
            account = i
            break
    if account == None:
        print("Customer {} doesn't have an account with the account number you provided. " 
              "Please check all the information is correct and the account number has been given in the correct format.".format(customer.name))
    return account

'''Function print_balance prints the information in the right format.'''

def print_balance(account, name):
    print("{} has a balance of {} on the account {}.".format(name, account.get_balance(), account.get_number()))