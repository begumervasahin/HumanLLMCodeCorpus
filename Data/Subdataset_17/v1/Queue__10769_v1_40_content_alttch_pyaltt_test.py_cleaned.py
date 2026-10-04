import time
import logging
import threading
from queue import Queue
logging.basicConfig(level=logging.DEBUG)
myevent = threading.Event()
Q = Queue()
def worker():
    while not worker_stop_event.is_set():
        logging.debug('Worker running')
        time.sleep(2.1)
def myqueuedworker():
    while not myqueuedworker_stop_event.is_set():
        task = Q.get()
        if task is None:
            break
        logging.debug(f'Queued worker running, task: {task}')
def myeventworker():
    while not myeventworker_stop_event.is_set():
        myevent.wait()
        logging.debug('Event worker running')
        time.sleep(1)
worker_stop_event = threading.Event()
myqueuedworker_stop_event = threading.Event()
myeventworker_stop_event = threading.Event()
worker_thread = threading.Thread(target=worker)
myqueuedworker_thread = threading.Thread(target=myqueuedworker)
myeventworker_thread = threading.Thread(target=myeventworker)
worker_thread.start()
myqueuedworker_thread.start()
myeventworker_thread.start()
def test():
    logging.debug('Test function running')
Q.put('task1')
myevent.set()
Q.put('task2')
Q.put('task3')
Q.put('task4')
logging.debug('ALL SET')
test_thread = threading.Thread(target=test)
test_thread.start()
test_thread.join()
logging.debug('Job test started')
time.sleep(5)
worker_stop_event.set()
myqueuedworker_stop_event.set()
myeventworker_stop_event.set()
Q.put(None)
worker_thread.join()
myqueuedworker_thread.join()
myeventworker_thread.join()
logging.debug('All workers stopped')