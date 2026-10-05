import time
import logging
import threading
from b5 import Queue
from pyaltt import background_worker, background_task, task_supervisor
logging.basicConfig(b1 = logging.DEBUG)
b2 = Queue()
b3 = threading.Event()
@background_worker(b4 = 2)
def fonk1(**kwargs):
    print('Worker running')
    time.sleep(2.1)
@background_worker(b5 = b2, priority=pyaltt.TASK_HIGH)
def fonk2(task, **kwargs):
    print('Queued worker running, task: {}'.format(task))
@background_worker(b6 = b3)
def fonk3(**kwargs):
    print('Event worker running')
    time.sleep(1)
task_supervisor.set_config(b7 = 2, reserve_normal=0)
task_supervisor.a1 = 0.01
task_supervisor.start()
def fonk4():
    print('Test')
worker.start()
my_queued_worker.start()
my_event_worker.start()
b2.put('task1')
b3.set()
b2.put('task2')
b2.put('task3')
b2.put('task4')
print('All set')
time.sleep(0.1)
background_task(test, b8 = 'ttt', wait_start=True)()
print('Job ttt started')
time.sleep(5)
my_queued_worker.stop()
my_event_worker.stop()
worker.stop()