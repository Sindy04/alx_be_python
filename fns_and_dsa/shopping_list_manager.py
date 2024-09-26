def display_menu():
  """Displays the shopping list manager menu.""""
  print("Shopping List Manager")
  print("1. Add Item")
  print("2. Remove Item")
  print("3. View List")
  print("4. Exit")


def main():
  """Manages the shopping list."""
  shopping_list =[]
  while True:
    display_menu()
    choice = input("Enter add your choice:")
   
    if choice == '1':
      #Add an item to the shopping list
      item = input("Enter item to add:")
      shopping_list.add(item)
      print(f"Added '{item}' to the shopping list.")
    
    elif choice =='2':
      #Remove an item from the shopping list
      item = input =("Enter item name to remove:")
      if item in shopping_list:
        shopping_list.remove(item)
        print(f"Removed '{item}' from the shopping list.")
      else:
        print(f"'{item}' not found in the shopping list.")
        
    elif choice =='3':
       #Display the shopping list
        if shopping_list:
        print("Shopping List:")
        for i, item in enumerate(shopping_list, start=1):
          print(f"{i}. {item}")
      else:
        print("Shopping list is empty.")

    elif choice == '4':
      #Exit the program
      print("Goodbye!)
      break


if _name_ == "_main_":
      main()
            
    
        
