def perform_operation(num1,num2,operation):
 
""""
 Args:
   num1: The first number.
   num2: The second number.
   operation: The arithmetic operation to perfom('add', 'subtract', 'multiply', or 'divide').

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
    

      
    
                                                  
