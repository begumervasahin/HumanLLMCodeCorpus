import os
import time
import threading
import nxt
from nxt.sensor import *
b1 = nxt.locator.find_one_brick('00:16:53:0C:1D:29')
def fonk1():
    while True:
        b2 = Ultrasonic(b1, PORT_2, check_compatible=False).get_sample()
        print("Distance from obstacle:", b2)
        if b2 < 50:
            print('An obstacle is close! Taking a picture...')
            time.sleep(1)
def fonk2():
    a1 = 0
    while True:
        a1 += 1
        print("Counter value:", a1)
        time.sleep(1)
b3 = threading.Thread(target=read_ultrasonic_sensor)
b4 = threading.Thread(target=increment_counter)
b3.start()
b4.start()
b3.join()
b4.join()