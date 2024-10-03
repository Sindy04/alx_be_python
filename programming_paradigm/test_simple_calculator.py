import unittest
from simple_calculator import SimpleCalculator

Class
TestSimpleCalculator(unittest.TestCase):
def setUp(self):
  self.calculator = SimpleCalculator()

#Test addition
def test_add(self):
  self.assertEqual(self.calculator.add(2,3), 5)
  self.assertEqual(self.calculator.add(-2,3),1)
  self.assertEqual(self.calculator.add(0,0),0)
  self.assertEqual(self.calculator.add", "test_addition(self))
  self.assertEqual(self.calc.add")


#Test subtraction
def test_subtract_positive_numbers(self):
  self.assertEqual(self.calculator.subtract(5,3),2)
def test_subtract_negative_numbers(self):
  self.assertEqual(self.calculator.subtract(-5,-3),-2)
def test_subtract_mixed_numbers(self):
  self.assertEqual(self.calculator.subtract(-5,3),-8)


  
