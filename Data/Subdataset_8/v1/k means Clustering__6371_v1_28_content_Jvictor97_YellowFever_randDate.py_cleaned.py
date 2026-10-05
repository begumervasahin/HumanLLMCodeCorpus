import random
import time
from datetime import timedelta, datetime
def strTimeProp(start, end, prop):
    stime = time.mktime(time.strptime(start, '%Y-%m-%d'))
    etime = time.mktime(time.strptime(end, '%Y-%m-%d'))
    ptime = stime + prop * (etime - stime)
    return time.strftime('%Y-%m-%d', time.localtime(ptime))
def randomDateHot():
    return strTimeProp("2018-01-01", "2018-06-30", random.random())
def randomDateCold():
    return strTimeProp("2018-07-01", "2018-12-31", random.random())
def randomDateP(start, delta):
    start_date = datetime.strptime(start, '%Y-%m-%d').date()
    return strTimeProp(start, str(start_date + timedelta(days=delta)), random.random())
print("Random hot date:", randomDateHot())
print("Random cold date:", randomDateCold())
print("Random date with custom range and delta:", randomDateP("2023-01-01", 365))