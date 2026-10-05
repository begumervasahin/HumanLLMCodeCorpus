import time
import logging
import threading
from queue import Queue
from pyaltt import background_worker, background_task, task_supervisor
logging.basicConfig(level=logging.DEBUG)
task_queue = Queue()
event = threading.Event()
@background_worker(interval=2)
def periodic_worker(**kwargs):
    print('Periodic worker running')
    time.sleep(2.1)
@background_worker(queue=task_queue, priority=task_supervisor.TASK_HIGH)
def queued_worker(task, **kwargs):
    print('Queued worker running, task: {}'.format(task))
@background_worker(event=event)
def event_worker(**kwargs):
    print('Event worker running')
    time.sleep(1)
task_supervisor.set_config(pool_size=2, reserve_normal=0)
task_supervisor.poll_delay = 0.01
task_supervisor.start()
def test_function():
    print('Test function executed')
periodic_worker.start()
queued_worker.start()
event_worker.start()
task_queue.put('task1')
event.set()
task_queue.put('task2')
task_queue.put('task3')
task_queue.put('task4')
print('All tasks enqueued and event set')
time.sleep(0.1)
background_task(test_function, name='test_task', wait_start=True)()
print('Background task "test_task" started')
time.sleep(5)
queued_worker.stop()
event_worker.stop()
periodic_worker.stop()