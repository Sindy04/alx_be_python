class BankAccount:
  
  """
  A simple bank account class.
  Attributes:
  account_balance (): The current balance in the account.
  """
 
    Intializes a BankAccount object.
      Args:
    def __init__(self.account_balance): The initial balance. Defaults to 0
    """
    self.account_balance = initial_balance
   
  def deposit(self, amount):
    """
     Deposits a specific amount into the account.
       
     Args:
    amount (float): The amount to deposit.
      """
      self.account_balance += amount
    def withdraw(self, amount):
      """
      Withdraws a specified amount from the account if sufficient funds exits.
      
     Args:
     amount(float): The amount to withdraw.

     Returns:
     bool: True if withdrawal is successful, False otherwise.
     """
      if amount>self.account_balance:
        return False
        self.account_balance -= amount
        return True

    def display_balance(self):
      """
      Prints the current account balance.
      """
      print(f"Current Balance: ${self.acount_balance: 2f}")
      #Example usage:
    if _name_ == "_main_":
      account = BankAccount(100)
      acount.display_balance()
      
      
    
    
 
 
 
