# Code to know the days, months and year till now from your birthday

import datetime

current_date = datetime.date.today()
print(f"Current date: {current_date}")

birthday = datetime.date(2003, 4, 5)
print(f"My birthday: {birthday}")

days_passed = (current_date - birthday).days
years_passed = current_date.year - birthday.year
months_passed = (years_passed * 12) + current_date.month - birthday.month

# Adjust year count if current month/day is before Birthday
if current_date.month < 4 or (current_date.month == 4 and current_date.day < 5):
    years_passed -= 1

print(f"Days passed: {days_passed}")
print(f"Months passed (approx): {months_passed}")
print(f"Years passed (approx): {years_passed}")