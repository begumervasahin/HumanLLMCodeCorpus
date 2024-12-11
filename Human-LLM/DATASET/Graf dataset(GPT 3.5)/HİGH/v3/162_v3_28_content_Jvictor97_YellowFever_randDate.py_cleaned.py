import random
import time
from datetime import timedelta, datetime
def fonk1(start_date, b5, proportion):
    b1 = time.mktime(time.strptime(start_date, '%Y-%m-%d'))
    b2 = time.mktime(time.strptime(b5, '%Y-%m-%d'))
    b3 = b1 + proportion * (b2 - b1)
    return time.strftime('%Y-%m-%d', time.localtime(b3))
def fonk2():
    return fonk1("2018-01-01", "2018-06-30", random.random())
def fonk3():
    return fonk1("2018-07-01", "2018-12-31", random.random())
def fonk4(start_date, delta_days):
    b4 = datetime.strptime(start_date, '%Y-%m-%d').date()
    b5 = str(b4 + timedelta(days=delta_days))
    return fonk1(start_date, b5, random.random())
print("Random hot date:", fonk2())
print("Random cold date:", fonk3())
print("Random date with custom range and delta:", fonk4("2023-01-01", 365))