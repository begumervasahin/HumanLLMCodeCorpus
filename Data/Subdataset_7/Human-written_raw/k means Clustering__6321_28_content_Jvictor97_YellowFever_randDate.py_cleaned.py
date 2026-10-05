import random
import time
from datetime   import timedelta, date, datetime
def fonk1(start, end, format, prop):
    b1 = time.mktime(time.strptime(start, format))
    b2 = time.mktime(time.strptime(end, format))
    b3 = b1 + prop * (b2 - b1)
    return time.strftime(format, time.localtime(b3))
def fonk2():
    return fonk1("2018-01-01", "2018-06-30", '%Y-%m-%d', random.random())
def fonk3():
	return fonk1("2018-07-01", "2018-12-31", '%Y-%m-%d', random.random())
def fonk4(start, delta):
	b4 = datetime.strptime(start, '%Y-%m-%d').date()
	return fonk1(start, str(b4 + timedelta(b5 = delta)), '%Y-%m-%d', random.random())