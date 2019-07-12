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
            return 'Not stealable'
        elif 0.5 <= (self.price / self.weight) < 1 :
            return 'Kind stealable'
        else:
            return 'Not so stealable'

    def explode(self):
        """ Explodibility """

        if (self.flammability * self.weight) < 10:
            return '...fizzle'
        elif ((self.flammability * self.weight) >= 50) and ((self.flammability * self.weight) < 50):
            return '...boom!'
        else:
            return '...BABOOM!!'


""" Subclass """


class BoxingGlove(Product):
    """ Boxing gloves specs """
    def __init__(self, name,weight = 10, price=10,
                 flammability=0.5, identifier=random.randint(1000000, 10000000)):
        super().__init__(name, price,flammability,identifier)
        self.weight = weight
    
    def explode(self):
        """ Override explode """
        return "It's a boxing glove"

    def punch(self):
        """ punch """

        if self.weight < 5:
            return "That tickles"
        
        elif 5 <= self.weight < 15:
            return 'Hey that hurts'

        else:
            return 'OUCH!'
