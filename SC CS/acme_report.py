#!/usr/bin/env python

import random
from acme import Product

# Useful to use with random.sample to generate names
adjectives = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
nouns = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

def generate_products(num_products=30):
  names = []
  prices = []
  flammabilities = []
  weights = []
  products = []
  for i in range(num_products):
    name = '{} {}'.format(random.sample(adjectives,1)[0], random.sample(nouns,1)[0])
    names.append(name)

    price = random.randint(5,101)
    prices.append(price)

    weight = random.randint(5,101)
    weights.append(weight)

    flammability = random.uniform(0, 2.5)
    flammabilities.append(flammability)
  products.append(names)
  products.append(prices)
  products.append(weights)
  products.append(flammabilities)
  return products


def inventory_report(products):
  def ave(lst):
    average = sum(lst) / len(lst)
    return average
  averages=[]
  names = set(products[0])
  
  for i in range(1,len(products)):
    average = ave(products[i])
    averages.append(average)
  print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
  print('Unique product names:', len(names))
  print('Average price:', averages[0])
  print('Average weight:', averages[1])
  print('Average flammability:', averages[2])


if __name__ == '__main__':
    inventory_report(generate_products())
  
