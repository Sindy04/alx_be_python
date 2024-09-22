print("Enter your task: Finish project report")

# Prompt user input
Task = input("Enter your Task: ")
Priority = input("Priority (high/medium/low): ").lower()
Time_bound = input("Time_bound (yes/no): ").lower()

#Intialize the reminder message
reminder_message= "Reminder: "
 
if Time_bound == "yes":
  reminder = f"Reminder: '{Task}' is a"
else:
  reminder =f"Note: '{Task} is a'

#Process the task based on priority
match priority:
    case "high":
      reminder += "high priority task"
    case "medium"
      reminder += "medium priority task"
  case "low":
       reminder += "low priority task"
  case _: = "Invalid priority level."

  #Modify the reminder
 if time_bound == "yes":
      reminder += " that requires immediate attention today!"
else:
reminder += " Condsider completing it when you have free time. "
#print the reminder
print("reminder")
 
  
  

