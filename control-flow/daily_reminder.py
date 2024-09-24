def get_task_details():
  "Gets task description, priority and time sensitivity from the user."
  
task = input("Enter your task: ")
priority = input("priority (high/medium/low): ").lower()
time_bound = input(" is it time-bound? (yes/no):").lower()
return task, priority, time_bound

def provide_reminder(task, priority,time_bound):
  "Provides a customizes reminder based on priority and time sensitivity."
  match priority:
    case "high":
      reminder = f"'{task}' is a high priority task"
    case "medium":
      reminder = f"'{task}' is a medium priority task"
    case "low":
      reminder = f"Note:'{task}' is a low priority task"
    case:
      reminder = f"Unknown priority task: '{task}'"

if time_bound == "yes":
      reminder += " then requires immediate attention today!"
 elif priority == "low" and time_bound == "no":
      reminder += ".Consider completing it when you have free time."
 else:
      reminder +=" .Complete it as soon as possible."
   print("Reminder:",reminder)



  

