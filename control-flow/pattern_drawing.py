def draw_pattern(n):
  pattern=""
  for i in range(1,n+1):
    pattern += "*"*i+"\n"
    for i in range(n-1, 0,-1):
      pattern += "*"*i+"\n"
      return pattern
  result = draw_pattern(4)
  print(result)
  
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


if _name_ == "_main_"
   main()
      
      
      
    
