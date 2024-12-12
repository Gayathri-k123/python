import calendar
from datetime import date,timedelta
today=date.today()
yesterday=today-timedelta(days=1)
tomorrow=today+timedelta(days=1)
print("yesterday",calendar.day_name[yesterday.weekday()])
print("today",calendar.day_name[today.weekday()])
print("tomorrow",calendar.day_name[tomorrow.weekday()])


