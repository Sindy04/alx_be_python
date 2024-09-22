# Prompt the user for a task description
task = input("Enter your task: ")
# Prompt for the task’s priority
priority = input("priority (high/medium/low): ").lower()
# Ask if the task is time-bound
time-bound = input("is time-bound (yes/no):").lower()

#Intialize
if time-bound == "yes":
  reminder = f"Reminder: '{task}' is a"
else:
  reminder =f"Note: '{task} is a'

#Process the task based on priority
match priority:
    case "high":
      reminder += "high priority task"
    case "medium"
      reminder += "medium priority task"
  
  

