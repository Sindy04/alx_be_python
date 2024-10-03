import unittest
from simple_calculator import SimpleCalculator

Class
TestSimpleCalculator(unittest.TestCase):
def setUp(self):
  self.calculator = SimpleCalculator()

#Test addition
def test_add_positive_numbers(self):
  self.assertEqual(self.calculator.add(2, 3), 5)

def test_add_negative_numbers(self):
  self.assertEqual(self.calculator.add(-2,-3),-5)

def test_add_mixed_numbers(self):
   self.assertEqual(self.calculator.add(-2,3),1)

#Test subtraction
def test_subtract_positive_numbers(self):
  self.assertEqual(self.calculator.subtract(5,3),2)
def test_subtract_negative_numbers(self):
  self.assertEqual(self.calculator.subtract(-5,-3),-2)
def test_subtract_mixed_numbers(self):
  self.assertEqual(self.calculator.subtract(-5,3),-8)


  
