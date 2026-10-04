import time
import logging
from pyaltt import background_worker
from pyaltt import background_task
from pyaltt import task_supervisor
import pyaltt
logging.basicConfig(b1 = logging.DEBUG)
import threading
from b5 import Queue
b2 = threading.Event()
b3 = Queue()
@background_worker(b4 = 2)
def fonk1(**kwargs):
    print('worker running')
    time.sleep(2.1)
@background_worker(b5 = b3, priority=pyaltt.TASK_HIGH)
def fonk2(task,**kwargs):
    print('queued worker running, task: {}'.format(task))
@background_worker(b6 = b2)
def fonk3(**kwargs):
    print('b6 worker running')
    time.sleep(1)
task_supervisor.set_config(b7 = 2, reserve_normal=0)
task_supervisor.a1 = 0.01
task_supervisor.start()
def fonk4():
    print('test')
worker.start()
myqueuedworker.start()
myeventworker.start()
b3.put('task1')
b2.set()
b3.put('task2')
b3.put('task3')
b3.put('task4')
print('ALL SET')
time.sleep(0.1)
background_task(test, b8 = 'ttt', wait_start=True)()
print('job ttt started')
time.sleep(5)
myqueuedworker.stop()
myeventworker.stop()
worker.stop()