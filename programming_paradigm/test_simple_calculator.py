import unittest
from simple_calculator import SimpleCalculator

Class
TestSimpleCalculator(unittest.TestCase):
def setUp(self):
  self.calculator = SimpleCalculator()

#Test addition
def test_add_positive_number(self):
  self.assertEquall(self.calculator.add(2, 3), 5)
  
