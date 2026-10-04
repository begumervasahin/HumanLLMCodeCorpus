import time
import logging
import threading
from queue import Queue
from pyaltt import background_worker, background_task, task_supervisor, TASK_HIGH
logging.basicConfig(level=logging.DEBUG)
myevent = threading.Event()
task_queue = Queue()
@background_worker(interval=2)
def worker(**kwargs):
    print('Worker running')
    time.sleep(2.1)
@background_worker(queue=task_queue, priority=TASK_HIGH)
def my_queued_worker(task, **kwargs):
    print(f'Queued worker running, task: {task}')
@background_worker(event=myevent)
def my_event_worker(**kwargs):
    print('Event worker running')
    time.sleep(1)
task_supervisor.set_config(pool_size=2, reserve_normal=0)
task_supervisor.poll_delay = 0.01
task_supervisor.start()
def test():
    print('Test function running')
worker.start()
my_queued_worker.start()
my_event_worker.start()
task_queue.put('task1')
myevent.set()
task_queue.put('task2')
task_queue.put('task3')
task_queue.put('task4')
print('ALL SET')
background_task(test, name='ttt', wait_start=True)()
print('Job ttt started')
time.sleep(5)
my_queued_worker.stop()
my_event_worker.stop()
worker.stop()