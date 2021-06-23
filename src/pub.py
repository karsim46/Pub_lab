class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drink = []
        
    def buy_drink(self, customer, drink):
        self.till += drink.price
        customer.pay_drink(drink)
    
