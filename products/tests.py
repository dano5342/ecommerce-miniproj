from django.test import TestCase
from .models import Product


class ProductTests(TestCase):
    """ Test the product model
    and define the tests here"""
    
    def test_str(self):
        test_name = Product(name="A Product")
        self.assertEqual(str(test_name), "A Product")
        
        