import sys
from bank_account import BankAcount

def main():
  account = BankAccount(100) #Example starting balance
  if len(sys.argv) < 2:
    print("usage: python
