from savings_account import SavingsAccount
from personal_account import PersonalAccount

class Bank:
    
    
    
    def __init__(self, name):
        self.name = name
        self.customers = []
        
        
    def get_customer_by_id(self, customer_id):
        for i in self.customers:
            if i.id == customer_id:
                return i
        return None
        
    def add_customer(self, customer):
        self.customers.append(customer)
        
    def remove_customer(self, customer):
        if customer in self.customers:
            self.customers.remove(customer)
        return
        
    def add_savings_account(self, customer, balance, account_number):
        if customer in self.customers:
            s_account = SavingsAccount(customer, balance, account_number)
            customer.accounts.append(s_account)
            return s_account
        return False
        
    def add_personal_account(self, customer, balance, account_number):
        if customer in self.customers:
            p_account = PersonalAccount(customer, balance, account_number)
            customer.accounts.append(p_account)
            return p_account
        return False
        
    def get_accounts(self, customer):
        return customer.accounts
        