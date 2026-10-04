import time
import logging
import threading
from queue import Queue
logging.basicConfig(b1 = logging.DEBUG)
b2 = threading.Event()
b3 = Queue()
def fonk1(stop_event):
    while not stop_event.is_set():
        logging.debug('Background worker running')
        time.sleep(2.1)
def fonk2(stop_event, b3):
    while not stop_event.is_set():
        b4 = b3.get()
        if b4 is None:
            break
        logging.debug(f'Queued worker running, b4: {b4}')
def fonk3(stop_event, b2):
    while not stop_event.is_set():
        b2.wait()
        logging.debug('Event worker running')
        time.sleep(1)
b5 = threading.Event()
b6 = threading.Event()
b7 = threading.Event()
b8 = threading.Thread(target=background_worker, args=(b5,))
b9 = threading.Thread(target=queued_worker, args=(b6, b3))
b10 = threading.Thread(target=event_worker, args=(b7, b2))
b8.start()
b9.start()
b10.start()
def fonk4():
    logging.debug('Test function running')
b3.put('task1')
b2.set()
b3.put('task2')
b3.put('task3')
b3.put('task4')
logging.debug('ALL SET')
b11 = threading.Thread(target=test_function)
b11.start()
b11.join()
logging.debug('Job test started')
time.sleep(5)
b5.set()
b6.set()
b7.set()
b3.put(None)
b8.join()
b9.join()
b10.join()
logging.debug('All workers stopped')