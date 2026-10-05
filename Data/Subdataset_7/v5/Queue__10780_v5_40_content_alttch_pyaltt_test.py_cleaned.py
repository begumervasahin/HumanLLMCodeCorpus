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
    print('Periodic worker running')
    time.sleep(2.1)
@background_worker(b5 = b2, priority=task_supervisor.TASK_HIGH)
def fonk2(task, **kwargs):
    print('Queued worker running, task: {}'.format(task))
@background_worker(b3 = b3)
def fonk3(**kwargs):
    print('Event worker running')
    time.sleep(1)
task_supervisor.set_config(b6 = 2, reserve_normal=0)
task_supervisor.a1 = 0.01
task_supervisor.start()
def fonk4():
    print('Test function executed')
periodic_worker.start()
queued_worker.start()
event_worker.start()
b2.put('task1')
b3.set()
b2.put('task2')
b2.put('task3')
b2.put('task4')
print('All tasks enqueued and b3 set')
time.sleep(0.1)
background_task(test_function, b7 = 'test_task', wait_start=True)()
print('Background task "test_task" started')
time.sleep(5)
queued_worker.stop()
event_worker.stop()
periodic_worker.stop()