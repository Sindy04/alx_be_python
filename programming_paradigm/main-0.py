import sys
from bank_account import BankAcount

def main():
  account = BankAccount(100) #Example starting balance
  if len(sys.argv) < 2:
    print("usage: python main.py<command>:<amount>")
    print("Command: deposit, withdaw, display")
    sys.exit(1)

command, params = sys.argv[1].split(':')
amount = float(paramas[0]) if params else None
if command == "deposit" and amount is not None:
  account.depoit(amount)
  print(f"Deposited: {amount:.2f}")
elif command == "withdraw" and amount is not None:
  if account.withdraw(amount):
    print(f"Withdraw: {amount:.2f}")
  else:
    print("Insufficient funds.")
  elif command == "display":
    account.display_balance()
else:
print("Invalid command.")
if _name_ == "-main_"
main()
