def draw_pattern(size):
  "Draw a square pattern of asterisks using nested loops"
  row = 0
  while row < size:
    for _ in range(size):
      print(",end+")
    print()
    row += 1
    
