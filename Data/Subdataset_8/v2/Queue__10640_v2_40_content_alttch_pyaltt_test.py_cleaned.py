import time
import logging
import threading
from queue import Queue
from pyaltt import background_worker, background_task, task_supervisor
logging.basicConfig(level=logging.DEBUG)
my_event = threading.Event()
Q = Queue()
@background_worker(interval=2)
def worker(**kwargs):
    print('Worker running')
    time.sleep(2.1)
@background_worker(queue=Q, priority='high')
def my_queued_worker(task, **kwargs):
    print(f'Queued worker running, task: {task}')
@background_worker(event=my_event)
def my_event_worker(**kwargs):
    print('Event worker running')
    time.sleep(1)
task_supervisor.set_config(pool_size=2, reserve_normal=0)
task_supervisor.poll_delay = 0.01
task_supervisor.start()
def test():
    print('Test')
worker.start()
my_queued_worker.start()
my_event_worker.start()
Q.put('Task 1')
my_event.set()
Q.put('Task 2')
Q.put('Task 3')
Q.put('Task 4')
print('All set')
time.sleep(0.1)
background_task(test, name='ttt', wait_start=True)()
print('Job ttt started')
time.sleep(5)
my_queued_worker.stop()
my_event_worker.stop()
worker.stop()