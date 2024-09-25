def display_current_datetime():
  """Displays the current date and time."""
  current_date = datetime.now()
  print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")

def calculate_future_date(days):
  """Calculates a future date based on the current date and added days."""
  current_date = datetime.now()
  future_date = current_date + timedelta(days=days)
  return future_date

def main():
  """Demonstrates datetime module usage."""
  display_current_datetime()

  while True:
    try:
      days = int(input("Enter the number of days to add to the current date:"))
      break
      expect ValueError:
        print("Invalid input. Please enter an integer.")

      future_date = calculate_future_date(days)
      print(f"Future date: {future_date.strftime('%Y-%m-%d')}")

if _name_ == "_main_":
  main()
