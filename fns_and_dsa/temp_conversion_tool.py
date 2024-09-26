#Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
  """Converts Fahrenheit to Celsius."""
return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
  """Converts Celsius to Fahrenheit."""
 return (celsius*CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
  """Performs temperature conversion based on user input."""
  while True: 
    try:
      temperature = float(input("Enter the temperature to convert:")
      unit = input("Is this temperature in Celsius or Fahrenheit? (C/F):").strip().upper()
      if unit == 'C':
        converted_temperature = converted_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted_temperature}°F")
      elif unit == 'F':
        converted_temperature = converted_to_celsius(temperature)
        print(f"{temperature}°F is {converted_temperature}°C")
      else:
        print("Invalid unit. Please enter C for Celsius or F for Fahrenheit.")
        continue

      break

    except ValueError:
      print("Invalid temperature. Please enter a numeric value.")

if _name_ == "_main_"
   main()
      
        
 
 
