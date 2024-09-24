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

    if choice == '1':
      #Add an item to the shopping list
      item = input("Enter item name:")
      shopping_list.append(item)
      print(f"Added '{item}' to the shopping list.")

