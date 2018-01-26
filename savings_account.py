import random
from account import Account

class SavingsAccount(Account):
    
    def __init__(self, customer, balance, account_number):
        super().__init__(customer, balance, account_number)
        
    def create_account_number(self, customer, account_number):
        if account_number == 0:
            self.account_number = "FI " + str(customer.id) + " " + str(random.getrandbits(15)) + " 20"
        else:
            self.account_number = account_number
        return self.account_number
    
    def transfer_to(self, account, transfer_sum):
        if self.owner == account.owner:
            if self.balance >= transfer_sum:
                self.balance -= transfer_sum
                account.balance += transfer_sum
                return 1
            else:
                return -1
        else:
            return 0