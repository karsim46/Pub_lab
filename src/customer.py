class Customer:
    def __init__(self, name, wallet, age, drunkeness_level):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkeness_level = drunkeness_level

    def pay_drink(self, drink):
        self.wallet -= drink.price

    def is_customer_pissed(self, drink):
        drunkeness_level = 0

