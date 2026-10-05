import time
import logging
import threading
from queue import Queue
from pyaltt import background_worker, background_task, task_supervisor
logging.basicConfig(level=logging.DEBUG)
Q = Queue()
my_event = threading.Event()
@background_worker(interval=2)
def worker(**kwargs):
    print('Worker running')
    time.sleep(2.1)
@background_worker(queue=Q, priority=pyaltt.TASK_HIGH)
def my_queued_worker(task, **kwargs):
    print('Queued worker running, task: {}'.format(task))
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
Q.put('task1')
my_event.set()
Q.put('task2')
Q.put('task3')
Q.put('task4')
print('All set')
time.sleep(0.1)
background_task(test, name='ttt', wait_start=True)()
print('Job ttt started')
time.sleep(5)
my_queued_worker.stop()
my_event_worker.stop()
worker.stop()