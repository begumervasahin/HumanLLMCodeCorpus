import os
import time
import threading
import nxt
from nxt.sensor import *
brick = nxt.locator.find_one_brick('00:16:53:0C:1D:29')
def ultrasonic_sensor():
    while True:
        distance = Ultrasonic(brick, PORT_2, check_compatible=False).get_sample()
        print("Distance to obstacle:", distance)
        ''' Uncomment this section if you want to take a picture when an obstacle is close
        if distance < 50:
            print('You are close. I am going to take your picture.')
            file_count = file_count + 1
            filename = str(file_count) + '.jpg'
            os.system('fswebcam -r 352x288 ' + filename)
            time.sleep(1)
        '''
def counter(i):
    i = 0
    while True:
        i = i + 1
        print("Counter:", i)
thread_ultrasonic = threading.Thread(target=ultrasonic_sensor)
thread_counter = threading.Thread(target=counter, args=(1,))
thread_ultrasonic.start()
thread_counter.start()
thread_ultrasonic.join()
thread_counter.join()