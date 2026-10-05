import random
import time
from datetime import timedelta, date, datetime
def fonk1(start, end):
    b1 = time.mktime(time.strptime(start, '%Y-%m-%d'))
    b2 = time.mktime(time.strptime(end, '%Y-%m-%d'))
    b3 = b1 + random.random() * (b2 - b1)
    return time.strftime('%Y-%m-%d', time.localtime(b3))
def fonk2():
    return fonk1("2018-01-01", "2018-06-30")
def fonk3():
    return fonk1("2018-07-01", "2018-12-31")
def fonk4(start, delta):
    b4 = datetime.strptime(start, '%Y-%m-%d').date()
    b5 = b4 + timedelta(days=delta)
    return fonk1(start, str(b5))
