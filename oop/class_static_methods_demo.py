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
    

from class_static_methods_demo import Calculator

def main():
    # Using the static method
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")

    # Using the class method
    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")

if __name__ == "__main__":
    main()
