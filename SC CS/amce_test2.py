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
        self.assertEqual(prod.explode(), ('...fizzle') | ('...boom!') | ('...BABOOM!!'))
        self.assertEqual(prod.stealability(), ('Not stealable') | ('Kind stealable') | ('Not so stealable'))

class AcmeReportTests(unittest.TestCase):
    """Making sure counts and names are right"""
    def test_default_num_products(self):
      prod = generate_products()
      self.assertCountEqual(prod.names, 30)
    def test_legal_names(self):
      prod = generate_products()
      self.assertIn(prod.names,adjectives.append(nouns))

if __name__ == '__main__':
    unittest.main()