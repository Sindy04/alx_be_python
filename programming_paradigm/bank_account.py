class BankAccount:
  """A simple bank account class.

  Attributes:
  account_balance(float): The current balance in the account.
  """
  def _int_(self,initial_balance=0):
    Intializes a BankAccount object.
      Args:
    intial_balance(float, optional): The initial balance. Defaults to 0
    """
    self.account_balance =initial_balance
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
      print(f"Current Balance:
      
    
    
 
 
 
