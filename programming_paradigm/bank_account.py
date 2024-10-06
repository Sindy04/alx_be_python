class BankAccount:
  
  """
  A simple bank account class.
  Attributes:
  account_balance (): The current balance in the account.
  """
 
    Intializes a BankAccount object.
    
    def __init__(self.account_balance): The initial balance. Defaults to 0
    
    self.account_balance = initial_balance

   #Deposit
  def deposit(self, amount):
#while True:
     """Deposits a specific amount into the account."""
       try:
         if amount > 0:
           self.account_balance += amount
           return True
           
       except ValueError as e:
         print(f"Invalid Input {e}")
         return False
       
      
    #Withdrawal
    def withdraw(self, amount):
      """Withdraws a specified amount from the account if sufficient funds exits."""
      
     Args:
     amount(float): The amount to withdraw.

     Returns:
     bool: True if withdrawal is successful, False otherwise.
     
      if amount>self.account_balance:
        return False
        self.account_balance -= amount
        return True
#Display_balance
    def display_balance(self):
      
      """Prints the current account balance."""
    
      print(f"Current Balance: ${self.acount_balance: 2f}")
      #Example usage:
    if _name_ == "_main_":
      account = BankAccount(100)
      acount.display_balance()

main-0.py
import sys
from bank_account import BankAcount

def main():
  account = BankAccount(100) #Example starting balance
  if len(sys.argv) < 2:
    print("usage: python(programming_paradigm/bank_account.py)<command>:<amount>")
    print("Command: deposit, withdaw, display")
    sys.exit(1)

command, params = sys.argv[1].split(':')
amount = float(paramas[0]) if params else None
if command == "deposit" and amount is not None:
  account.depoit(amount)
  print(f"Deposited: ${amount:.2f}")
elif command == "withdraw" and amount is not None:
  if account.withdraw(amount):
    print(f"Withdraw:${amount:.2f}")
  else:
    print("Insufficient funds.")
  elif command == "display":
    account.display_balance()
else:
print("Invalid command.")
if _name_ == "-main_"
main()
      
    
    
 
 
 
