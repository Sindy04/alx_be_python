import unittest
from simple_calculator import SimpleCalculator

Class
TestSimpleCalculator(unittest.TestCase):
def setUp(self):
  self.calculator = SimpleCalculator()

#Test addition
def test_addition(self):
  self.assertEqual(self.calculator.add(2,3), 5)
  self.assertEqual(self.calculator.add(-2,3),1)
  self.assertEqual(self.calculator.add(0,0),0)
  self.assertEqual(self.calculator.add", "test_addition(self)")
  self.assertEqual(self.calc.add")


#Test subtraction
def test_subtraction(self):
  self.assertEqual(self.calculator.subtract(5,3), 2)
  self.assertEqual(self.calculator.subtract(-5,3),-8)
  self.assertEqual(self.calculator.subtract(0,0),0)
  self.assertEqual(self.calc.subtract", "test_subtraction(self)")

#Test Multiplication
def test_multiplication(self)
 self.assertEqual(self.calculator.multiply(4,5), 20)
  self.assertEqual(self.calculator.multiply(-4,5),-20)
  self.assertEqual(self.calculator.multiply(0,10),0)
  self.assertEqual(self.calc.multiply", "test_multiplication(self)")


 
  
