import os
import signal
from multiprocessing import Process, Lock, Semaphore, Value, Queue, cpu_count
from inspect import signature
class DataQueue:
    def __init__(self, generator, size=16, child_count=6):
        self.size = size
        self.child_count = child_count
        self.status = Value('b', False)
        self.generator = generator
        if not (hasattr(self.generator, 'batchGenerator') and hasattr(self.generator, 'batchProcessor')):
            raise Exception('batchGenerator and batchProcessor in Generator object are mandatory')
    def load_batch(self, status, input_sm, batch_sm):
        while status.value:
            self._acquire_semaphore(input_sm['empty_semaphore'], input_sm['mutex'], input_sm['q'])
            data = input_sm['q'].get()
            self._release_semaphore(input_sm['mutex'], input_sm['full_semaphore'])
            data = self._process_data(data)
            self._acquire_semaphore(batch_sm['full_semaphore'], batch_sm['mutex'], batch_sm['q'])
            batch_sm['q'].put(data)
            self._release_semaphore(batch_sm['mutex'], batch_sm['empty_semaphore'])
    def _process_data(self, data):
        sig = signature(self.generator.batchProcessor)
        if len(sig.parameters) == 1:
            return self.generator.batchProcessor(list(data))
        else:
            return self.generator.batchProcessor(*data)
    def _acquire_semaphore(self, semaphore, mutex, queue):
        semaphore.acquire()
        mutex.acquire()
    def _release_semaphore(self, mutex, semaphore):
        mutex.release()
        semaphore.release()
    def get_batch(self):
        if self.status.value and not self._is_queue_empty(self.batch_sm['q']) and not self._is_queue_empty(self.input_sm['q']):
            self._acquire_semaphore(self.batch_sm['empty_semaphore'], self.batch_sm['mutex'], self.batch_sm['q'])
            batch = self.batch_sm['q'].get()
            self._release_semaphore(self.batch_sm['mutex'], self.batch_sm['full_semaphore'])
            return batch
    def _is_queue_empty(self, queue):
        return queue.qsize() == 0
    def monitor(self, status, input_sm):
        while status.value:
            data = tuple(self.generator.batchGenerator())
            self._acquire_semaphore(input_sm['full_semaphore'], input_sm['mutex'], input_sm['q'])
            input_sm['q'].put(data)
            self._release_semaphore(input_sm['mutex'], input_sm['empty_semaphore'])
    def start(self):
        if hasattr(self.generator, 'init'):
            self.generator.init()
        self.status.value = True
        self.input_sm = self._create_shared_memory()
        self.batch_sm = self._create_shared_memory()
        child_count = self.child_count if self.child_count != -1 else cpu_count()
        self.child_processes = []
        self.monitor_process = Process(target=self.monitor, args=(self.status, self.input_sm))
        self.monitor_process.start()
        for _ in range(child_count):
            p = Process(target=self.load_batch, args=(self.status, self.input_sm, self.batch_sm))
            p.start()
            self.child_processes.append(p)
    def _create_shared_memory(self):
        return {
            "q": Queue(),
            "empty_semaphore": Semaphore(value=0),
            "full_semaphore": Semaphore(value=self.size),
            "mutex": Lock()
        }
    def stop(self):
        self.status.value = False
        self._terminate_processes(self.child_processes)
        self._terminate_processes([self.monitor_process])
        print(f"Job Queue size at stop: {self.input_sm['q'].qsize()}")
        print(f"Batch Queue size at stop: {self.batch_sm['q'].qsize()}")
        self._close_queues()
    def _terminate_processes(self, processes):
        for process in processes:
            if process.pid != 0:
                try:
                    os.kill(process.pid, signal.SIGTERM)
                    print(f"Successfully killed process {process.pid}")
                except Exception as e:
                    print(f"Access denied: can't kill process {process.pid}. Error: {e}")
    def _close_queues(self):
        self.input_sm['q'].close()
        self.batch_sm['q'].close()
    def get_size(self):
        return self.batch_sm['q'].qsize()
    def is_empty(self):
        return self._is_queue_empty(self.batch_sm['q'])