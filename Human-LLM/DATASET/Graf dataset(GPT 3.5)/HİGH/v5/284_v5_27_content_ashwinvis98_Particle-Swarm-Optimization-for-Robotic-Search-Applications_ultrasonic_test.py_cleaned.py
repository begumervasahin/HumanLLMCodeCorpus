import os
import time
import threading
import nxt
from nxt.sensor import *
b1 = '00:16:53:0C:1D:29'
b2 = nxt.locator.find_one_brick(b1)
def fonk1():
    while True:
        b3 = Ultrasonic(b2, PORT_2, check_compatible=False).get_sample()
        print("Distance to obstacle:", b3)
        ''' Uncomment this section if you want to take a picture when an obstacle is close
        if b3 < 50:
            print('You are close. I am going to take your picture.')
            b4 = b4 + 1
            b5 = str(b4) + '.jpg'
            os.system('fswebcam -r 352x288 ' + b5)
            time.sleep(1)
        '''
def fonk2(start_value):
    b6 = start_value
    while True:
        b6 += 1
        print("Counter:", b6)
b7 = threading.Thread(target=read_ultrasonic_sensor)
b8 = threading.Thread(target=increment_counter, args=(1,))
b7.start()
b8.start()
b7.join()
b8.join()