from datetime import datetime, timedelta

def display_current_datetime ():
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", current_date)

display_current_datetime()