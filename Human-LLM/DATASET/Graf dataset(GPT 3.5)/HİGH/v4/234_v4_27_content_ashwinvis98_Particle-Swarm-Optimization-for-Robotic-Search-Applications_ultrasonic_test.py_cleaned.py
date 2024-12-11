import os
import time
import threading
import nxt
from nxt.sensor import *
b1 = nxt.locator.find_one_brick('00:16:53:0C:1D:29')
def fonk1():
    while True:
        b2 = Ultrasonic(b1, PORT_2, check_compatible=False).get_sample()
        print("Distance to obstacle:", b2)
        ''' Uncomment this section if you want to take a picture when an obstacle is close
        if b2 < 50:
            print('You are close. I am going to take your picture.')
            b3 = b3 + 1
            b4 = str(b3) + '.jpg'
            os.system('fswebcam -r 352x288 ' + b4)
            time.sleep(1)
        '''
def fonk2(a1):
    a1 = 0
    while True:
        a1 = a1 + 1
        print("Counter:", a1)
b5 = threading.Thread(target=ultrasonic_sensor)
b6 = threading.Thread(target=counter, args=(1,))
b5.start()
b6.start()
b5.join()
b6.join()