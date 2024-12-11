import random
import time
from datetime import timedelta, datetime
def fonk1(b4, b5):
    b1 = time.mktime(time.strptime(b4, '%Y-%m-%d'))
    b2 = time.mktime(time.strptime(b5, '%Y-%m-%d'))
    b3 = b1 + random.random() * (b2 - b1)
    return time.strftime('%Y-%m-%d', time.localtime(b3))
def fonk2():
    return fonk1("2018-01-01", "2018-06-30")
def fonk3():
    return fonk1("2018-07-01", "2018-12-31")
def fonk4(b4, days):
    b4 = datetime.strptime(b4, '%Y-%m-%d').date()
    b5 = b4 + timedelta(days=days)
    return fonk1(b4.strftime('%Y-%m-%d'), b5.strftime('%Y-%m-%d'))
