#User input for financial details
  monthly income = input("Enter your monthly income:$")
  monthly expenses = input("Enter your total monthly expenses: $")
                
def calculate_monthly_savings(monthly_income, monthly_expenses):
  return monthly_income - monthly_expenses

def calculate_projected_annual_savings(monthly_savings):
  annual_interest_rate = 0.05 #5% annual interest rate
 return monthly_savings * 12 + (monthly_savings *12 *annual_ interest_rate)

def main():
  #User input for financial details
  monthly income = input("Enter your monthly income:$")
  monthly expenses = input("Enter your total monthly expenses: $")

#Calculate monthly savings
monthly_savings = calculate_monthly_saving(monthly_income, monthly_expenses)
