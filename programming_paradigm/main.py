import sys
from robust_division_calculator import safe_divide
def main():
print("Usage: python(programming_paradigm/robust_division_calculator.py)<numerator><denominator>")
sys.exit(1)
numerator = sys.argv[1]
denominator = sys.argv[2]
result = safe_divide(numerator, denominator)
print(result)
if _name_ =="_main_"
main()
