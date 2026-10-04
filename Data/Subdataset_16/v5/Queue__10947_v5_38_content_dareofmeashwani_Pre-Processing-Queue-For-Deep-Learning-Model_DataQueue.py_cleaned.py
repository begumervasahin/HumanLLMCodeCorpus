import os
import signal
from multiprocessing import Process, Lock, Semaphore, Value, Queue, cpu_count
from inspect import signature
class class1:
    def fonk1(self, b4, b1 = 16, b2=6):
        self.b1 = b1
        self.b2 = b2
        self.b3 = Value('b', False)
        self.b4 = b4
        if not (hasattr(self.b4, 'batchGenerator') and hasattr(self.b4, 'batchProcessor')):
            raise Exception('batchGenerator and batchProcessor in Generator object are mandatory')
    def fonk2(self, b3, b9, b10):
        while b3.b8:
            self.fonk4(b9['empty_semaphore'], b9['mutex'], b9['q'])
            b5 = b9['q'].get()
            self.fonk5(b9['mutex'], b9['full_semaphore'])
            b5 = self.fonk3(b5)
            self.fonk4(b10['full_semaphore'], b10['mutex'], b10['q'])
            b10['q'].put(b5)
            self.fonk5(b10['mutex'], b10['empty_semaphore'])
    def fonk3(self, b5):
        b6 = signature(self.b4.batchProcessor)
        if len(b6.parameters) == 1:
            return self.b4.batchProcessor(list(b5))
        else:
            return self.b4.batchProcessor(*b5)
    def fonk4(self, semaphore, mutex, queue):
        semaphore.acquire()
        mutex.acquire()
    def fonk5(self, mutex, semaphore):
        mutex.release()
        semaphore.release()
    def fonk6(self):
        if self.b3.b8 and not self.fonk7(self.b10['q']) and not self.fonk7(self.b9['q']):
            self.fonk4(self.b10['empty_semaphore'], self.b10['mutex'], self.b10['q'])
            b7 = self.b10['q'].get()
            self.fonk5(self.b10['mutex'], self.b10['full_semaphore'])
            return b7
    def fonk7(self, queue):
        return queue.qsize() == 0
    def fonk8(self, b3, b9):
        while b3.b8:
            b5 = tuple(self.b4.batchGenerator())
            self.fonk4(b9['full_semaphore'], b9['mutex'], b9['q'])
            b9['q'].put(b5)
            self.fonk5(b9['mutex'], b9['empty_semaphore'])
    def fonk9(self):
        if hasattr(self.b4, 'init'):
            self.b4.init()
        self.b3.b8 = True
        self.b9 = self.fonk10()
        self.b10 = self.fonk10()
        b2 = self.b2 if self.b2 != -1 else cpu_count()
        self.b11 = []
        self.b12 = Process(target=self.monitor, args=(self.b3, self.b9))
        self.b12.fonk9()
        for _ in range(b2):
            b13 = Process(target=self.load_batch, args=(self.b3, self.b9, self.b10))
            b13.fonk9()
            self.b11.append(b13)
    def fonk10(self):
        return {
            "q": Queue(),
            "empty_semaphore": Semaphore(b8 = 0),
            "full_semaphore": Semaphore(b8 = self.b1),
            "mutex": Lock()
        }
    def fonk11(self):
        self.b3.b8 = False
        self.fonk12(self.b11)
        self.fonk12([self.b12])
        print(f"Job Queue b1 at stop: {self.b9['q'].qsize()}")
        print(f"Batch Queue b1 at stop: {self.b10['q'].qsize()}")
        self.fonk13()
    def fonk12(self, processes):
        for process in processes:
            if process.pid != 0:
                try:
                    os.kill(process.pid, signal.SIGTERM)
                    print(f"Successfully killed process {process.pid}")
                except Exception as e:
                    print(f"Access denied: can't kill process {process.pid}. Error: {e}")
    def fonk13(self):
        self.b9['q'].close()
        self.b10['q'].close()
    def fonk14(self):
        return self.b10['q'].qsize()
    def fonk15(self):
        return self.fonk7(self.b10['q'])