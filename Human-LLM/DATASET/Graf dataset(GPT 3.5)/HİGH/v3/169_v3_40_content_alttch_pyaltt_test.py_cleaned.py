import time
import logging
import threading
from b5 import Queue
from pyaltt import background_worker, background_task, task_supervisor
logging.basicConfig(b1 = logging.DEBUG)
b2 = threading.Event()
b3 = Queue()
@background_worker(b4 = 2)
def fonk1(**kwargs):
    print('Regular worker running')
    time.sleep(2.1)
@background_worker(b5 = b3, priority='high')
def fonk2(task, **kwargs):
    print(f'Queued worker running, task: {task}')
@background_worker(b2 = b2)
def fonk3(**kwargs):
    print('Event worker running')
    time.sleep(1)
task_supervisor.set_config(b6 = 2, reserve_normal=0)
task_supervisor.a1 = 0.01
task_supervisor.start()
def fonk4():
    print('Test')
regular_worker.start()
queued_worker.start()
event_worker.start()
b3.put('Task 1')
b2.set()
b3.put('Task 2')
b3.put('Task 3')
b3.put('Task 4')
print('All tasks and b2 set')
time.sleep(0.1)
background_task(test_function, b7 = 'test_task', wait_start=True)()
print('Test task started')
time.sleep(5)
queued_worker.stop()
event_worker.stop()
regular_worker.stop()