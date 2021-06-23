class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drink = []
        
    def sell_drink(self, customer, drink):
        self.till += drink.price
        customer.pay_drink(drink)
    
    def age_check(self, customer):
        return customer.age >= 18
                           
            
