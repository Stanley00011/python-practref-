# Get the current day, month, year, hour, minute and timestamp from datetime module
from datetime import datetime
now = datetime.now()
print(now)
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
timestampp = now.timestamp()

print(f"the current time fram: {day}, {month},{year},{hour},{minute},{timestampp} ")

# Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
t = now.strftime("%m/%d/%Y, %H:%M:%S")
print("time:", t)

# Today is 5 December, 2019. Change this time string to time.
today = ('5 December, 2019') 
date_object = datetime.strptime(today, "%d %B, %Y")

# Calculate the time difference between now and new year.
from datetime import date
today = date(year=2026, month=1, day=7)
new_year = date(year=2027, month=1, day=1)
time_left_for_newyear = new_year - today
# Time left for new year:  27 days, 0:00:00
print('Time left for new year: ', time_left_for_newyear)

# Calculate the time difference between 1 January 1970 and now.
seventies = date(year=1970, month=1, day=1)
todayd = date(year=2026, month=1, day=7)

time_from_sevt = todayd - seventies 
print(f" sventes: {time_from_sevt}")

# Think, what can you use the datetime module for? Examples:
# Time series analysis
# To get a timestamp of any activities in an application
# Adding posts on a blog
