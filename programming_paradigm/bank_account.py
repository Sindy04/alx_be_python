class BankAccount:
  def __init__(self, initial_balance=0):
    self._account_balance = initial_balance

#Depositing Method
def deposit(self, ammount):
 if amount > 0:
   self._account_balance += amount

#Withdrawal Method
def withdraw(self, amount):
  if amount > 0 and self._account_balance >= amount:
    self._account_balance -= amount
    return True #withdrawal successful
  elif amount > self._account_balance:
    return False #withdrawal failed

def display_balance(self):
  print(f"Current Balance: {self._amount_balance}")
    
 
 
 
