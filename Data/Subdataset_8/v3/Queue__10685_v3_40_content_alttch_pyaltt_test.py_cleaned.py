import time
import logging
import threading
from queue import Queue
from pyaltt import background_worker, background_task, task_supervisor
logging.basicConfig(level=logging.DEBUG)
event = threading.Event()
task_queue = Queue()
@background_worker(interval=2)
def regular_worker(**kwargs):
    print('Regular worker running')
    time.sleep(2.1)
@background_worker(queue=task_queue, priority='high')
def queued_worker(task, **kwargs):
    print(f'Queued worker running, task: {task}')
@background_worker(event=event)
def event_worker(**kwargs):
    print('Event worker running')
    time.sleep(1)
task_supervisor.set_config(pool_size=2, reserve_normal=0)
task_supervisor.poll_delay = 0.01
task_supervisor.start()
def test_function():
    print('Test')
regular_worker.start()
queued_worker.start()
event_worker.start()
task_queue.put('Task 1')
event.set()
task_queue.put('Task 2')
task_queue.put('Task 3')
task_queue.put('Task 4')
print('All tasks and event set')
time.sleep(0.1)
background_task(test_function, name='test_task', wait_start=True)()
print('Test task started')
time.sleep(5)
queued_worker.stop()
event_worker.stop()
regular_worker.stop()