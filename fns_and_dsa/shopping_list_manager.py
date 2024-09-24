def display_menu():
  """Displays the shopping list manager menu.""""
  print("\nShopping List Manager")
  print("1.Add Item")
  print("2.Remove Item")
  print("3.View List")
  print("4.Exit")


def main():
  """Manages the shopping list."""
  shopping_list =[]
  while True:
    display_menu()
    choice = input("Enter your choice:")

