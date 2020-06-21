from django.test import TestCase

from app.calc import add, subtract


class CalcTests(TestCase):

    def test_add_two_numbers(self):
        """Test that addition of two numbers calculated correctly"""
        self.assertEqual(add(3, 8), 11)

    def test_subtract_two_numbers(self):
        """Test that subtraction of two numbers calculated correctly"""
        self.assertEqual(subtract(8, 3), 5)
