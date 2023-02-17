#1////////////////////////////////////////////////
from datetime import timedelta, date

d = timedelta(5)
print(date.today() - d)


#2////////////////////////////////////////////////
from datetime import datetime, timedelta, date
today = date.today()
tomorrow = date.today() + timedelta(1)
yesterday = date.today() - timedelta(1)
print(f"Today's date: {today}\nYesterday's date: {yesterday}\nTomorrow's date: {tomorrow}")

d = datetime.today().replace(microsecond = 0)
print(d)


#3////////////////////////////////////////////////
from datetime import datetime
def date_diff_in_Seconds(dt2, dt1):
  timedelta = dt2 - dt1
  return timedelta.days * 24 * 3600 + timedelta.seconds


#4////////////////////////////////////////////////
from datetime import datetime
fd = datetime.strptime(input("Enter first date: "), "%d/%m/%Y")
sd = datetime.strptime(input("Enter second date: "), "%d/%m/%Y")
print((fd-sd).days * 24 * 3600)

