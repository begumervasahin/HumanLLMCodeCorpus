import time
import logging
import threading
from queue import Queue
logging.basicConfig(level=logging.DEBUG)
event = threading.Event()
task_queue = Queue()
def background_worker(stop_event):
    while not stop_event.is_set():
        logging.debug('Background worker running')
        time.sleep(2.1)
def queued_worker(stop_event, task_queue):
    while not stop_event.is_set():
        task = task_queue.get()
        if task is None:
            break
        logging.debug(f'Queued worker running, task: {task}')
def event_worker(stop_event, event):
    while not stop_event.is_set():
        event.wait()
        logging.debug('Event worker running')
        time.sleep(1)
background_worker_stop_event = threading.Event()
queued_worker_stop_event = threading.Event()
event_worker_stop_event = threading.Event()
background_worker_thread = threading.Thread(target=background_worker, args=(background_worker_stop_event,))
queued_worker_thread = threading.Thread(target=queued_worker, args=(queued_worker_stop_event, task_queue))
event_worker_thread = threading.Thread(target=event_worker, args=(event_worker_stop_event, event))
background_worker_thread.start()
queued_worker_thread.start()
event_worker_thread.start()
def test_function():
    logging.debug('Test function running')
task_queue.put('task1')
event.set()
task_queue.put('task2')
task_queue.put('task3')
task_queue.put('task4')
logging.debug('ALL SET')
test_thread = threading.Thread(target=test_function)
test_thread.start()
test_thread.join()
logging.debug('Job test started')
time.sleep(5)
background_worker_stop_event.set()
queued_worker_stop_event.set()
event_worker_stop_event.set()
task_queue.put(None)
background_worker_thread.join()
queued_worker_thread.join()
event_worker_thread.join()
logging.debug('All workers stopped')