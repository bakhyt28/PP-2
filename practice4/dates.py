#1
from datetime import datetime, timedelta

current_moment = datetime.now()   # get the current date and time
date_minus_five = current_moment - timedelta(days=5)   # calculate the date 5 days earlier

# print the result
print(date_minus_five)


#2
from datetime import datetime, timedelta

today_date = datetime.now()   # store today's date and time
day_before = today_date - timedelta(days=1)   # calculate yesterday's date
day_after = today_date + timedelta(days=1)    # calculate tomorrow's date

# display all three dates
print("Yesterday:", day_before)
print("Today:", today_date)
print("Tomorrow:", day_after)


#3
from datetime import datetime

present_time = datetime.now()   # get current time with microseconds
clean_time = present_time.replace(microsecond=0)   # remove microseconds from time

# print time without microseconds
print(clean_time)


#4
from datetime import datetime

first_datetime = datetime(2008, 4, 10, 17, 0, 0)   # define the first date and time
second_datetime = datetime(2026, 2, 22, 13, 46, 0) # define the second date and time

seconds_difference = second_datetime - first_datetime   # calculate time difference

# convert the difference to seconds and print it
print("Difference in seconds:", seconds_difference.total_seconds())