#!/usr/bin/env python
import unittest
from acme import Product
from acme_report import generate_products, adjectives, nouns


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)
        self.assertEqual(prod.explode(), '...BABOOM!!')
        self.assertTrue(prod.stealability() == 'Kind stealable')


class AcmeReportTests(unittest.TestCase):
    """Making sure counts and names are right"""
    def test_default_num_products(self):
        prod = generate_products()
        self.assertEqual(len(prod), 30)

    def test_legal_names(self):
        prod = generate_products()
        for p in prod:
            adj, noun = p.name.split()
            self.assertIn(adj, adjectives)
            self.assertIn(noun, nouns)


if __name__ == '__main__':
      unittest.main()