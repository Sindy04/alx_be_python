import sys
from robust_division_calculator import safe_divide

def main():
  calculator = RobustDivisionCalculator()
  result = calculator.safe_divide(12,2)
  print(result) # Output: 6.0

  result = calculator.safe_divide(12,0)
  print(result) #Output: None
print("Usage: python(programming_paradigm/robust_division_calculator.py)")
sys.exit(1)
numerator = sys.argv[1]
denominator = sys.argv[2]
result = safe_divide(numerator, denominator)
print(result)
if _name_ =="_main_"
main()
