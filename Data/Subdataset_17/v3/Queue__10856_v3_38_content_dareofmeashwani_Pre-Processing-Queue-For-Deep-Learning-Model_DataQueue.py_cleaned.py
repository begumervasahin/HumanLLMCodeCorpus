import os
import random
import time
import signal
from multiprocessing import Process, Lock, Semaphore, Value, Queue, cpu_count
from inspect import signature
class DataQueue:
    def __init__(self, generator, size=16, child_count=6):
        self.size = size
        self.child_count = child_count
        self.status = Value('b', False)
        self.generator = generator
        self._validate_generator()
        self._init_shared_memory()
    def _validate_generator(self):
        if not (hasattr(self.generator, 'batchGenerator') and hasattr(self.generator, 'batchProcessor')):
            raise Exception('The generator object must have batchGenerator and batchProcessor methods')
    def _init_shared_memory(self):
        self.input_sm = {
            "q": Queue(),
            "empty_semaphore": Semaphore(0),
            "full_semaphore": Semaphore(self.size),
            "mutex": Lock()
        }
        self.batch_sm = {
            "q": Queue(),
            "empty_semaphore": Semaphore(0),
            "full_semaphore": Semaphore(self.size),
            "mutex": Lock()
        }
    def load_batch(self, status, input_sm, batch_sm):
        while status.value:
            self._process_input_batch(input_sm, batch_sm)
    def _process_input_batch(self, input_sm, batch_sm):
        input_sm['empty_semaphore'].acquire()
        input_sm['mutex'].acquire()
        data = input_sm['q'].get()
        input_sm['mutex'].release()
        input_sm['full_semaphore'].release()
        processed_data = self._process_data(data)
        batch_sm['full_semaphore'].acquire()
        batch_sm['mutex'].acquire()
        batch_sm['q'].put(processed_data)
        batch_sm['mutex'].release()
        batch_sm['empty_semaphore'].release()
    def _process_data(self, data):
        sig = signature(self.generator.batchProcessor)
        if len(sig.parameters) == 1:
            return self.generator.batchProcessor(list(data))
        return self.generator.batchProcessor(*data)
    def get_batch(self):
        if self.status.value and not self.batch_sm['q'].empty():
            return self._retrieve_batch()
    def _retrieve_batch(self):
        self.batch_sm['empty_semaphore'].acquire()
        self.batch_sm['mutex'].acquire()
        batch = self.batch_sm['q'].get()
        self.batch_sm['mutex'].release()
        self.batch_sm['full_semaphore'].release()
        return batch
    def monitor(self, status, input_sm):
        while status.value:
            self._generate_batch(input_sm)
    def _generate_batch(self, input_sm):
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
        self.monitor_process = Process(target=self.monitor, args=(self.status, self.input_sm))
        self.monitor_process.start()
        self.child_processes = [
            Process(target=self.load_batch, args=(self.status, self.input_sm, self.batch_sm))
            for _ in range(self._get_child_count())
        ]
        for process in self.child_processes:
            process.start()
    def _get_child_count(self):
        return self.child_count if self.child_count != -1 else cpu_count()
    def stop(self):
        self.status.value = False
        self._terminate_processes(self.child_processes)
        self._terminate_process(self.monitor_process)
        print(f"Job Queue size at stop: {self.input_sm['q'].qsize()}")
        print(f"Batch Queue size at stop: {self.batch_sm['q'].qsize()}")
        self._close_queues()
    def _terminate_processes(self, processes):
        for process in processes:
            self._terminate_process(process)
    def _terminate_process(self, process):
        if process.pid:
            try:
                os.kill(process.pid, signal.SIGTERM)
                print(f"Successfully killed process {process.pid}")
            except PermissionError:
                print(f"Access Denied: can't kill process {process.pid}")
    def _close_queues(self):
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