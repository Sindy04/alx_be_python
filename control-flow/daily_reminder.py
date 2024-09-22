# Prompt 
task = input("Enter your task:")
priority = input("priority (high/medium/low):").lower()
time_bound = input("is time_bound (yes/no):").lower()

#Intialize
if time_bound == "yes":
  reminder = f"Reminder: '{task}' is a"
else:
  reminder =f"Note: '{task} is a'

#Process the task based on priority
match priority:
    case "high":
      reminder += "high priority task"
    case "medium"
      reminder += "medium priority task"
  
  

