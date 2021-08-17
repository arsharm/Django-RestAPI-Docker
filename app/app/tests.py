from django.test import TestCase

from app.calc import add, subtract


class CalcTests(TestCase):

    def test_add_numbers(self):
        """Test the two numbers are added together"""
        self.assertEqual(add(3, 8), 11)

    def test_sub_number(self):
        """Subtract Two numbers"""
        self.assertEqual(subtract(6, 11), 5)
