task = input("Enter a task description: ")
priority = input("What's the task priority? (high/medium/low): ")
time_bound = input("Is the task time bound? (yes/no): ")
match priority, time_bound:
    case "high", "yes":
        print(f"'{task}' is a high priority task that requires immediate attention today!")
    case "high" "no":
        print(f"'{task}' is a high priority task.")
    case "low", "no":
        print(f"'{task}' is a low priority task. Consider completing it when you have free time.")
    case "low", "yes":
        print(f"'{task}' is a low priority task, though it's ought to be completed by weekend.")
