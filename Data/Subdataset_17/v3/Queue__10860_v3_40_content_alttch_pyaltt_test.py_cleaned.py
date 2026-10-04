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
        task_queue.task_done()
def event_worker(stop_event, event):
    while not stop_event.is_set():
        event.wait()
        logging.debug('Event worker running')
        time.sleep(1)
        event.clear()
stop_events = {
    "background": threading.Event(),
    "queued": threading.Event(),
    "event": threading.Event()
}
threads = {
    "background": threading.Thread(target=background_worker, args=(stop_events["background"],)),
    "queued": threading.Thread(target=queued_worker, args=(stop_events["queued"], task_queue)),
    "event": threading.Thread(target=event_worker, args=(stop_events["event"], event))
}
for thread in threads.values():
    thread.start()
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
for stop_event in stop_events.values():
    stop_event.set()
task_queue.put(None)
for thread in threads.values():
    thread.join()
logging.debug('All workers stopped')