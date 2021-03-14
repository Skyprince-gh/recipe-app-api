from django.test import TestCase

from app.calc import add,subtract

class CalcTests(TestCase):

  def test_add_two_numbers(self):
    """Test that two numbers are added together"""
    self.assertEqual(add(3,8), 11)


  def test_subtract_two_numbers(self):
    """Test that two values are subtracted and returned"""

    self.assertEqual(subtract(8,5), 3)