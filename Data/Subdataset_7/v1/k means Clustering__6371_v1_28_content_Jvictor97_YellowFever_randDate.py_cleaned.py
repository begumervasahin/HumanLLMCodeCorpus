import random
import time
from datetime import timedelta, datetime
def fonk1(start, end, prop):
    b1 = time.mktime(time.strptime(start, '%Y-%m-%d'))
    b2 = time.mktime(time.strptime(end, '%Y-%m-%d'))
    b3 = b1 + prop * (b2 - b1)
    return time.strftime('%Y-%m-%d', time.localtime(b3))
def fonk2():
    return fonk1("2018-01-01", "2018-06-30", random.random())
def fonk3():
    return fonk1("2018-07-01", "2018-12-31", random.random())
def fonk4(start, delta):
    b4 = datetime.strptime(start, '%Y-%m-%d').date()
    return fonk1(start, str(b4 + timedelta(b5 = delta)), random.random())
print("Random hot date:", fonk2())
print("Random cold date:", fonk3())
print("Random date with custom range and delta:", fonk4("2023-01-01", 365))