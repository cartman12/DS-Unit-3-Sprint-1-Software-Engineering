"""ACME
"""
import random


class Product:
    """ init """

    def __init__(self, name, price=10, weight=20,
                 flammability=0.5,
                 identifier=random.randint(1000000, 10000000)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        """ Price by weight """

        if (self.price / self.weight) < 0.5:
            print('Not stealable')
        elif 0.5 <= (self.price / self.weight) < 1 :
            print('Kind stealable')
        else:
            print('Not so stealable')

    def explode(self):
        """ Explodibility """

        if (self.flammability * self.weight) < 10:
            print('...fizzle')
        elif ((self.flammability * self.weight) >= 50) and ((self.flammability * self.weight) < 50):
            print('...boom!')
        else:
            print('...BABOOM!!')


""" Subclass """


class BoxingGlove(Product):
    """ Boxing gloves specs """
    def __init__(self, name, price=10,
                 flammability=0.5, identifier=random.randint(1000000, 10000000)):
        super().__init__(name, price,flammability,identifier)
        self.weight = 10
    
    def explode(self):
        """ Override explode """
        print("It's a boxing glove")

    def punch(self):
        """ punch """

        if self.weight < 5:
            print("That tickles")
        
        elif 5 <= self.weight < 15:
            print('Hey that hurts')

        else:
            print('OUCH!')
