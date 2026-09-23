#Date Functions and Manipulations
from datetime import datetime, timedelta

# 1. Current Date and Current Time
now = datetime.now()
print(f" Current Timestamp: {now}")
print(f" Just Current Date: {now.date()}")
print(f" Just Current Time: {now.time()}")

# 2. Extracting Components (Year, Month, Day, Week)
print(f" Year:  {now.year}")
print(f" Month: {now.month}")
print(f" Day:   {now.day}")

# isocalendar() returns (year, week_number, weekday)
print(f" Week Number of the Year: {now.isocalendar()[1]}") 

# 3. DateAdd (Adding Intervals)
# In Python, we use 'timedelta' to add or subtract days, hours, or weeks.
three_days_later = now + timedelta(days=3)
two_weeks_ago = now - timedelta(weeks=2)
print(f" Date Interval Addition/Subtraction:")
print(f" 3 Days from Now: {three_days_later.date()}")
print(f" 2 Weeks Ago:     {two_weeks_ago.date()}")

# 4. DateDiff (Difference between two dates)
# Let's calculate the time remaining until Next New Year
next_new_year = datetime(year=now.year + 1, month=1, day=1)
time_difference = next_new_year - now

print(f" Date Difference (DateDiff):")
print(f" Time until next New Year: {time_difference.days} days")

# 5. Advanced Formatting (Converting Date to clean text)
# %A = Full Weekday name, %B = Full Month name, %d = Day, %Y = Year
formatted_date = now.strftime("%A, %B %d, %Y")
print(f" Formatted Date String: {formatted_date}")
