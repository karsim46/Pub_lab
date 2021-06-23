import unittest
from unittest import runner
from src.pub import *
from src.customer import *
from src.drink import *

class TestPub(unittest.TestCase):

    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100)
        self.customer = Customer("Stephen", 100, 37)
        self.drink = Drink("cider", 5, 5)
        
    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self. pub.name)

    def test_sell_drink(self):
        self.pub.sell_drink(self.customer, self.drink) 
        self.assertEqual(95, self.customer.wallet)
        self.assertEqual(105, self.pub.till)
    
    def test_age_check(self):
        self.assertEqual(True, self.pub.age_check(self.customer))
    
        
