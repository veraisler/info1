from vehicle import *
import random


class Customer(object):
    
    def __init__(self,name):
        self.__name = name
        self.__score = self.credit_score()

    def __str__(self):
        return "Customer: {0:s}".format(self.__name)

    def credit_score(self):
        i = random.randint(0,100)
        self.valid = False
        if i > 60:
            self.valid = True

    def get_score(self):
        return self.valid


class VIP_Customer(Customer):

    def credit_score(self):
        self.valid = True
        return self.valid

### test cases ###

# initialising customer instances

Wendy = Customer("Wendy")
Heidi = VIP_Customer("Heidi")

print(Wendy) # expected output: Customer: Wendy
print(Heidi) # expected output: Customer: Heidi

print(Wendy.get_score()) # expected output: True
print(Heidi.get_score()) # expected output: True
