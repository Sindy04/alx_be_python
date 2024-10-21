monthly income = 5000
monthly expenses = 4000
monthly savings = 1000
interest rate = 0.05

#calculate projected savings
Projected Savings = (monthly savings * 12 +(monthly savings * 12 *0.05))
print(Projected Savings)
                     
def calculate_monthly_savings(monthly_income, monthly_expenses):
  return monthly_income - monthly_expenses

def calculate_projected_annual_savings(monthly_savings):
  annual_interest_rate = 0.05 #5% annual interest rate
 return monthly_savings * 12 + (monthly_savings *12 *annual_ interest_rate)

def main():
  #User input for financial details
  monthly_income = float(input("Enter your monthly_income:$"))
  monthly_expenses = float(input("Enter your total monthly expenses: $"))

#Calculate monthly savings
monthly_savings = calculate_monthly_saving(monthly_income, monthly_expenses)
