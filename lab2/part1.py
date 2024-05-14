from datetime import datetime, timedelta

# 1
print("\n#1")
basic_delta = timedelta(days=365, hours=5, minutes=1, seconds=0)
print("Basic timedelta:", basic_delta)

# 2
print("\n#2")
today = datetime.now()
print("Today is:", today)

# 3
print("\n#3")
print("Two years + NOW :", today + timedelta(days=365 * 2))

# 4
print("\n#4")
print("2 weeks, 3 days + NOW:", today + timedelta(weeks=2, days=3))

# 5
print("\n#5")
three_weeks_ago = today - timedelta(weeks=3)
print("Three weeks ago it was", three_weeks_ago.strftime("%A %B %d, %Y"))

# 6
print("\n#6")
current_year = today.year
next_christmas = datetime(year=current_year, month=12, day=25)

if next_christmas < today:
    next_christmas = datetime(year=current_year + 1, month=12, day=25)

days_till_christmas = next_christmas - today

print(days_till_christmas.days, "days left till next Christmas.")