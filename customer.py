import random

class Customer:
    
    seed = random.getrandbits(20)
    
    def __init__(self, name, customer_id):
        self.name = name
        if customer_id == 0:
            self.id = self.create_id(Customer.seed)
        else:
            self.id = customer_id
        self.accounts = []
        
    def create_id(self, seed):
        Customer.seed += 47
        return seed
        