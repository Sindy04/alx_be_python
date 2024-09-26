
task = input("Enter your task: ")
priority = input("priority (high/medium/low): ").strip().lower()
time_bound = input(" is it time-bound? (yes/no):").strip().lower()
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

def main():
  "Gets task details and provides a customized reminder."
  task, priority, time_bound = get_task_details()
  Provide_reminder(task,priority,time_bound)



  

