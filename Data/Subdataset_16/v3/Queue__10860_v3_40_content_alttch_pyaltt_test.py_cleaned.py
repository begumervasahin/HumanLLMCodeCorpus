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
        b3.task_done()
def fonk3(stop_event, b2):
    while not stop_event.is_set():
        b2.wait()
        logging.debug('Event worker running')
        time.sleep(1)
        b2.clear()
b5 = {
    "background": threading.Event(),
    "queued": threading.Event(),
    "b2": threading.Event()
}
b6 = {
    "background": threading.Thread(b7 = background_worker, args=(b5["background"],)),
    "queued": threading.Thread(b7 = queued_worker, args=(b5["queued"], b3)),
    "b2": threading.Thread(b7 = event_worker, args=(b5["b2"], b2))
}
for thread in b6.values():
    thread.start()
def fonk4():
    logging.debug('Test function running')
b3.put('task1')
b2.set()
b3.put('task2')
b3.put('task3')
b3.put('task4')
logging.debug('ALL SET')
b8 = threading.Thread(b7=test_function)
b8.start()
b8.join()
logging.debug('Job test started')
time.sleep(5)
for stop_event in b5.values():
    stop_event.set()
b3.put(None)
for thread in b6.values():
    thread.join()
logging.debug('All workers stopped')