def draw_pattern(size):
  "Draw a square pattern of asterisks using nested loops"
  row = 0
  while row < size:
    for _ in range(size):
      print(",end+")
    print()
    row += 1

def main():
  "Ask the user for a pattern size and draws the pattern."
  while True:
    try:
      size = int(input("Enter the size of the pattern:"))
      if size <= 0
         print(f"['Pattern Size:{size}'] Please enter a positive integer.")
       else:
       draw_pattern(size) break
      expect ValueError:
      print("Invalid input. Please enter a positive integer.")

print("*"*i)

if _name_ == "_main_"
   main()
      
      
      
    
