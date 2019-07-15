#!/usr/bin/env python

import random
from acme import Product

# Useful to use with random.sample to generate names
adjectives = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
nouns = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=31):
    products = []

    for i in range(num_products):

        name = '{} {}'.format(random.sample(adjectives, 1)[0], random.sample(nouns, 1)[0])
        price = random.randint(5, 101)
        weight = random.randint(5, 101)
        flammability = random.uniform(0, 2.5)
        products.append(Product(name, price, weight, flammability))

    return products


def inventory_report(products):
    def ave(lst):
        aver = sum(lst) / len(lst)
        return aver

    names = set([p.name for p in products])
    len_prod = len(names)

    average_price = ave([p.price for p in products])
    average_weight = ave([p.weight for p in products])
    average_flammability = ave([p.flammability for p in products])

    return 'ACME CORPORATION OFFICIAL INVENTORY REPORT', 'Unique product names:', len_prod, 'Average price:', average_price, 'Average weight:', average_weight, 'Average flammability:', average_flammability


if __name__ == '__main__':
    inventory_report(generate_products())

print(inventory_report(generate_products()))
