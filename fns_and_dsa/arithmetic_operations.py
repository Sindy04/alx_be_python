def perform_operation():
def perform_operation(num1:float,num2:float,operation: str):
 
""""
 Args:
   num1 (float): The first number.
   num2 (float): The second number.
   operation (str): The arithmetic operation to perfom('add', 'subtract', multiply', or 'divide').

 Returns:
 float or str: The result of the arithmetic operation or an error message for division by zero.
""""
 match operation:
  case "add":
    return num1 + num2
  case "subtract":
    return num1 - num2
  case "multiply":
    return num1 * num2
  case "divide":
    if num2 != 0
       return num1 / num2
    else:
      return "Error: Division by zero"
   case _:
      return "Error: Invalid operation"
    

      
    
                                                  
