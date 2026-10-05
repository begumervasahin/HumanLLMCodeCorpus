import os
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
            raise Exception('batchGenerator and batchProcessor in Generator object are mandatory')
    def load_batch(self, status, input_sm, batch_sm):
        while status.value:
            input_sm['emptySemaphore'].acquire()
            input_sm['mutex'].acquire()
            data = input_sm['q'].get()
            input_sm['mutex'].release()
            input_sm['fullSemaphore'].release()
            sig = signature(self.generator.batchProcessor)
            if len(sig.parameters) == 1:
                data = self.generator.batchProcessor(list(data))
            else:
                data = self.generator.batchProcessor(*data)
            batch_sm['fullSemaphore'].acquire()
            batch_sm['mutex'].acquire()
            batch_sm['q'].put(data)
            batch_sm['mutex'].release()
            batch_sm['emptySemaphore'].release()
    def get_batch(self):
        if self.status.value and self.batch_sm['q'].qsize() != 0 and self.input_sm['q'].qsize() != 0:
            self.batch_sm['emptySemaphore'].acquire()
            self.batch_sm['mutex'].acquire()
            batch = self.batch_sm['q'].get()
            self.batch_sm['mutex'].release()
            self.batch_sm['fullSemaphore'].release()
            return batch
    def monitor(self, status, input_sm):
        while status.value:
            data = tuple(self.generator.batchGenerator())
            input_sm['fullSemaphore'].acquire()
            input_sm['mutex'].acquire()
            input_sm['q'].put(data)
            input_sm['mutex'].release()
            input_sm['emptySemaphore'].release()
    def start(self):
        if hasattr(self.generator, 'init'):
            self.generator.init()
        self.status.value = True
        self.input_sm = {
            "q": Queue(),
            "emptySemaphore": Semaphore(value=0),
            "fullSemaphore": Semaphore(value=self.size),
            "mutex": Lock()
        }
        self.batch_sm = {
            "q": Queue(),
            "emptySemaphore": Semaphore(value=0),
            "fullSemaphore": Semaphore(value=self.size),
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
        for c_process in self.child_processes:
            if c_process.pid != 0:
                try:
                    os.kill(c_process.pid, signal.SIGTERM)
                    print("Successfully killed child process", c_process.pid)
                except Exception as e:
                    print("Access Denied: Can't kill child process", c_process.pid, e)
        try:
            os.kill(self.monitor_process.pid, signal.SIGTERM)
            print("Successfully killed monitor process", self.monitor_process.pid)
        except Exception as e:
            print("Access Denied: Can't kill monitor process", self.monitor_process.pid, e)
        print("Job Queue size at stop", self.input_sm['q'].qsize())
        print("Batch Queue size at stop", self.batch_sm['q'].qsize())
        self.input_sm['q'].close()
        self.batch_sm['q'].close()
    def get_size(self):
        return self.batch_sm['q'].qsize()
    def is_empty(self):
        return self.batch_sm['q'].qsize() == 0