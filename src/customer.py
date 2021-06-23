class Customer:
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age

    def pay_drink(self, drink):
        self.wallet -= drink.price
