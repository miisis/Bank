class Account:
    
    def __init__(self, customer, balance, account_number):
        self.owner = customer
        self.balance = balance
        self.account_number = self.create_account_number(customer, account_number)
        
    def create_account_number(self, custsomer, account_number):
        return
        
    def get_customer(self):
        return self.owner
    
    def get_balance(self):
        return self.balance
    
    def get_number(self):
        return self.account_number
    
    def deposit(self, deposit_sum):
        self.balance += deposit_sum
        
    def withdraw(self, withdraw_sum):
        if self.balance >= withdraw_sum:
            self.balance -= withdraw_sum
            return True
        else:
            return False
        
    def transfer_to(self, account, transfer_sum):
        return 