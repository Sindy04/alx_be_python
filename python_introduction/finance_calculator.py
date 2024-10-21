            
def calculate_monthly_savings(monthly_income, monthly_expenses):
  return monthly_income - monthly_expenses

def calculate_projected_annual_savings(monthly_savings):
  annual_interest_rate = 0.05 #5% annual interest rate
 return monthly_savings * 12 + (monthly_savings *12 *annual_ interest_rate)

def main():
  #User input for financial details
            
  monthly_income = float(input("Enter your monthly income: "))
  monthly_expenses = float(input("Enter your total monthly expenses: "))

#Calculate monthly savings
monthly_savings = (monthly_income- monthly_expenses|float(monthly_income)-float( monthly_expenses))

#Calculate projected annual savings
projected_annual_savings = calculate_projected_annual_savings(monthly_savings)

#output results
print(f"Your monthly savings are: $ {monthly_savings:.2f}")
print(f"Projected savings after one year, with interest, is: ${projected_annual_savings:.2f}")

if _name_ == "_main_":
  main()

