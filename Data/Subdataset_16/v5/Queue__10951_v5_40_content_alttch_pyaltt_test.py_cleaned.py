import time
import logging
import threading
from b5 import Queue
from pyaltt import background_worker, background_task, task_supervisor, TASK_HIGH
logging.basicConfig(b1 = logging.DEBUG)
b2 = threading.Event()
b3 = Queue()
@background_worker(b4 = 2)
def fonk1(**kwargs):
    logging.info('Interval Worker running')
    time.sleep(2.1)
@background_worker(b5 = b3, priority=TASK_HIGH)
def fonk2(task, **kwargs):
    logging.info(f'Queued Worker running, task: {task}')
@background_worker(b6 = b2)
def fonk3(**kwargs):
    logging.info('Event Worker running')
    time.sleep(1)
def fonk4():
    logging.info('Test function running')
def fonk5():
    task_supervisor.set_config(b7 = 2, reserve_normal=0)
    task_supervisor.a1 = 0.01
    task_supervisor.start()
    interval_worker.start()
    queued_worker.start()
    event_worker.start()
    b3.put('task1')
    b2.set()
    b3.put('task2')
    b3.put('task3')
    b3.put('task4')
    logging.info('All set')
    background_task(test_function, b8 = 'test_task', wait_start=True)()
    logging.info('Test task started')
    time.sleep(5)
    interval_worker.stop()
    queued_worker.stop()
    event_worker.stop()
if b9 = = '__main__':
    fonk5()