import os
import time
import threading
import nxt
from nxt.sensor import *
b = nxt.locator.find_one_brick('00:16:53:0C:1D:29')
def ultra():
    while True:
        distance = Ultrasonic(b, PORT_2, check_compatible=False).get_sample()
        print("Obstacle at", distance)
        if distance < 50:
            print('You are close, I am going to take your picture')
            time.sleep(1)
def cal():
    i = 0
    while True:
        i += 1
        print("i =", i)
        time.sleep(1)
t1 = threading.Thread(target=ultra)
t2 = threading.Thread(target=cal)
t1.start()
t2.start()
t1.join()
t2.join()