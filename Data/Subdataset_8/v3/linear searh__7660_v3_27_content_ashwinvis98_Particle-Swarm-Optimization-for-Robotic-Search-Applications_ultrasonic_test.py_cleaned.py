import os
import time
import threading
import nxt
from nxt.sensor import *
brick = nxt.locator.find_one_brick('00:16:53:0C:1D:29')
def read_ultrasonic_sensor():
    while True:
        distance = Ultrasonic(brick, PORT_2, check_compatible=False).get_sample()
        print(f"Distance from obstacle: {distance} cm")
        if distance < 50:
            print('Warning: An obstacle is detected! Taking necessary action...')
            time.sleep(1)
def increment_counter():
    counter = 0
    while True:
        counter += 1
        print(f"Counter value: {counter}")
        time.sleep(1)
ultrasonic_thread = threading.Thread(target=read_ultrasonic_sensor)
counter_thread = threading.Thread(target=increment_counter)
ultrasonic_thread.start()
counter_thread.start()
ultrasonic_thread.join()
counter_thread.join()