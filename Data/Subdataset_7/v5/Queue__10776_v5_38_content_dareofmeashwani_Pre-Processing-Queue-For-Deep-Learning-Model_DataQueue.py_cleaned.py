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
            b9['emptySemaphore'].acquire()
            b9['mutex'].acquire()
            b5 = b9['q'].get()
            b9['mutex'].release()
            b9['fullSemaphore'].release()
            b6 = signature(self.b4.batchProcessor)
            if len(b6.parameters) == 1:
                b5 = self.b4.batchProcessor(list(b5))
            else:
                b5 = self.b4.batchProcessor(*b5)
            b10['fullSemaphore'].acquire()
            b10['mutex'].acquire()
            b10['q'].put(b5)
            b10['mutex'].release()
            b10['emptySemaphore'].release()
    def fonk3(self):
        if self.b3.b8 and self.b10['q'].qsize() != 0 and self.b9['q'].qsize() != 0:
            self.b10['emptySemaphore'].acquire()
            self.b10['mutex'].acquire()
            b7 = self.b10['q'].get()
            self.b10['mutex'].release()
            self.b10['fullSemaphore'].release()
            return b7
    def fonk4(self, b3, b9):
        while b3.b8:
            b5 = tuple(self.b4.batchGenerator())
            b9['fullSemaphore'].acquire()
            b9['mutex'].acquire()
            b9['q'].put(b5)
            b9['mutex'].release()
            b9['emptySemaphore'].release()
    def fonk5(self):
        if hasattr(self.b4, 'init'):
            self.b4.init()
        self.b3.b8 = True
        self.b9 = {
            "q": Queue(),
            "emptySemaphore": Semaphore(b8 = 0),
            "fullSemaphore": Semaphore(b8 = self.b1),
            "mutex": Lock()
        }
        self.b10 = {
            "q": Queue(),
            "emptySemaphore": Semaphore(b8 = 0),
            "fullSemaphore": Semaphore(b8 = self.b1),
            "mutex": Lock()
        }
        b2 = self.b2 if self.b2 != -1 else cpu_count()
        self.b11 = []
        self.b12 = Process(target=self.monitor, args=(self.b3, self.b9))
        self.b12.fonk5()
        for _ in range(b2):
            b13 = Process(target=self.load_batch, args=(self.b3, self.b9, self.b10))
            b13.fonk5()
            self.b11.append(b13)
    def fonk6(self):
        self.b3.b8 = False
        for c_process in self.b11:
            if c_process.pid != 0:
                try:
                    os.kill(c_process.pid, signal.SIGTERM)
                    print("Successfully killed child process", c_process.pid)
                except:
                    print("Access Denied: Can't kill child process", c_process.pid)
        try:
            os.kill(self.b12.pid, signal.SIGTERM)
            print("Successfully killed monitor process", self.b12.pid)
        except:
            print("Access Denied: Can't kill monitor process", self.b12.pid)
        print("Job Queue b1 at stop:", self.b9['q'].qsize())
        print("Batch Queue b1 at stop:", self.b10['q'].qsize())
        self.b9['q'].close()
        self.b10['q'].close()
    def fonk7(self):
        return self.b10['q'].qsize()
    def fonk8(self):
        return self.b10['q'].qsize() == 0