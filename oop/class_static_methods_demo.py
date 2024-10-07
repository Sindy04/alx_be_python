class Calculator:
  """
  A class for performing arithmetic operations.
  """
  calculation_type = "Arithmetic Operations"

@staticmethod
def add(a,b):
  """
  Returns the sum of two numbers.

Args:
a (int or float): The first number.
b (int or float): The second number.

Returns:
int or float: The sum of a and b.
"""
  return a + b
  @classmethod
  def multiply(cls, a, b):
    """
    Returns the product of two numbers.

    Args:
    a (int or float): The first number
    b (int or float): The second number

    Returns:
    int or float: The product of a and b.
    """
    print(f"Calculation type: {cls.calculation_type}")
    return a * b
