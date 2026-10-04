import os
import random
import time
import signal
from multiprocessing import Process, Lock, Semaphore, Value, cpu_count, Queue
from inspect import signature
class DataQueue:
    def __init__(self, generator, size=16, child_count=6):
        self.size = size
        self.child_count = child_count
        self.status = Value('b', False)
        self.generator = generator
        if not (hasattr(self.generator, 'batchGenerator') and hasattr(self.generator, 'batchProcessor')):
            raise Exception('The generator object must have batchGenerator and batchProcessor methods')
    def load_batch(self, status, input_sm, batch_sm):
        while status.value:
            input_sm['empty_semaphore'].acquire()
            input_sm['mutex'].acquire()
            data = input_sm['q'].get()
            input_sm['mutex'].release()
            input_sm['full_semaphore'].release()
            sig = signature(self.generator.batchProcessor)
            if len(sig.parameters) == 1:
                data = self.generator.batchProcessor(list(data))
            else:
                data = self.generator.batchProcessor(*data)
            batch_sm['full_semaphore'].acquire()
            batch_sm['mutex'].acquire()
            batch_sm['q'].put(data)
            batch_sm['mutex'].release()
            batch_sm['empty_semaphore'].release()
    def get_batch(self):
        if self.status.value and not self.batch_sm['q'].empty() and not self.input_sm['q'].empty():
            self.batch_sm['empty_semaphore'].acquire()
            self.batch_sm['mutex'].acquire()
            batch = self.batch_sm['q'].get()
            self.batch_sm['mutex'].release()
            self.batch_sm['full_semaphore'].release()
            return batch
    def monitor(self, status, input_sm):
        while status.value:
            data = tuple(self.generator.batchGenerator())
            input_sm['full_semaphore'].acquire()
            input_sm['mutex'].acquire()
            input_sm['q'].put(data)
            input_sm['mutex'].release()
            input_sm['empty_semaphore'].release()
    def start(self):
        if hasattr(self.generator, 'init'):
            self.generator.init()
        self.status.value = True
        self.input_sm = {
            "q": Queue(),
            "empty_semaphore": Semaphore(value=0),
            "full_semaphore": Semaphore(value=self.size),
            "mutex": Lock()
        }
        self.batch_sm = {
            "q": Queue(),
            "empty_semaphore": Semaphore(value=0),
            "full_semaphore": Semaphore(value=self.size),
            "mutex": Lock()
        }
        child_count = self.child_count if self.child_count != -1 else cpu_count()
        self.child_processes = []
        self.monitor_process = Process(target=self.monitor, args=(self.status, self.input_sm))
        self.monitor_process.start()
        for i in range(child_count):
            p = Process(target=self.load_batch, args=(self.status, self.input_sm, self.batch_sm))
            p.start()
            self.child_processes.append(p)
    def stop(self):
        self.status.value = False
        for child_process in self.child_processes:
            if child_process.pid:
                try:
                    os.kill(child_process.pid, signal.SIGTERM)
                    print(f"Successfully killed child process {child_process.pid}")
                except PermissionError:
                    print(f"Access Denied: can't kill child process {child_process.pid}")
        if self.monitor_process.pid:
            try:
                os.kill(self.monitor_process.pid, signal.SIGTERM)
                print(f"Successfully killed monitor process {self.monitor_process.pid}")
            except PermissionError:
                print(f"Access Denied: can't kill monitor process {self.monitor_process.pid}")
        print(f"Job Queue size at stop: {self.input_sm['q'].qsize()}")
        print(f"Batch Queue size at stop: {self.batch_sm['q'].qsize()}")
        self.input_sm['q'].close()
        self.batch_sm['q'].close()
    def get_size(self):
        return self.batch_sm['q'].qsize()
    def is_empty(self):
        return self.batch_sm['q'].empty()
class ExampleGenerator:
    def batchGenerator(self):
        return [random.randint(1, 100) for _ in range(10)]
    def batchProcessor(self, data):
        return sum(data)
if __name__ == "__main__":
    gen = ExampleGenerator()
    dq = DataQueue(gen)
    dq.start()
    time.sleep(10)
    dq.stop()
    print(f"Final batch size: {dq.get_size()}")
    print(f"Is batch empty? {dq.is_empty()}")