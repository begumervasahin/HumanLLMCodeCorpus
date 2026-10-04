import time
import logging
import threading
from queue import Queue
from pyaltt import background_worker, background_task, task_supervisor, TASK_HIGH
logging.basicConfig(level=logging.DEBUG)
task_event = threading.Event()
task_queue = Queue()
@background_worker(interval=2)
def interval_worker(**kwargs):
    logging.info('Interval Worker running')
    time.sleep(2.1)
@background_worker(queue=task_queue, priority=TASK_HIGH)
def queued_worker(task, **kwargs):
    logging.info(f'Queued Worker running, task: {task}')
@background_worker(event=task_event)
def event_worker(**kwargs):
    logging.info('Event Worker running')
    time.sleep(1)
def test_function():
    logging.info('Test function running')
def main():
    task_supervisor.set_config(pool_size=2, reserve_normal=0)
    task_supervisor.poll_delay = 0.01
    task_supervisor.start()
    interval_worker.start()
    queued_worker.start()
    event_worker.start()
    task_queue.put('task1')
    task_event.set()
    task_queue.put('task2')
    task_queue.put('task3')
    task_queue.put('task4')
    logging.info('All set')
    background_task(test_function, name='test_task', wait_start=True)()
    logging.info('Test task started')
    time.sleep(5)
    interval_worker.stop()
    queued_worker.stop()
    event_worker.stop()
if __name__ == '__main__':
    main()