from datetime import datetime, timedelta

def display_current_datetime ():
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", current_date)

display_current_datetime()
def calculate_future_date():
    current_date = datetime.now()
    numbers_of_days = int(input("Enter the number of days to add to the current date: "))
    future_date = current_date + timedelta(numbers_of_days)
    print(f"Future date: {future_date.strftime("%Y-%m-%d")}")
    
calculate_future_date()