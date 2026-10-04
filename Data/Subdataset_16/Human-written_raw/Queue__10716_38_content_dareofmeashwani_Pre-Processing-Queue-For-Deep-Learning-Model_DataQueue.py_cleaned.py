import os
from multiprocessing import Process, Lock, Semaphore
from multiprocessing import Value, cpu_count
from multiprocessing import Queue
import signal
from inspect import signature
class class1:
    def fonk1(self, generator, b1 = 16, b12=6):
        self.b2 = b1
        self.b3 = b12
        self.b4 = Value('b', False)
        self.b5 = generator
        if (hasattr(self.b5, 'batchGenerator') and hasattr(self.b5, 'batchProcessor')) == False:
            raise Exception('batchGenerator and batchProcessor in Generator object is mandatory')
    def fonk2(self, status, inputSM, batchSM):
        while status.b9:
            inputSM['emptySemaphore'].acquire()
            inputSM['mutex'].acquire()
            b6 = inputSM['q'].get()
            inputSM['mutex'].release()
            inputSM['fullSemaphore'].release()
            b7 = signature(self.b5.batchProcessor)
            if len(b7.parameters) == 1:
                b6 = self.b5.batchProcessor(list(b6))
            else:
                b6 = self.b5.batchProcessor(*b6)
            batchSM['fullSemaphore'].acquire()
            batchSM['mutex'].acquire()
            batchSM['q'].put(b6)
            batchSM['mutex'].release()
            batchSM['emptySemaphore'].release()
    def fonk3(self):
        if self.b4.b9 and self.b11['q'].qsize() != 0 and self.b10['q'].qsize() != 0:
            self.b11['emptySemaphore'].acquire()
            self.b11['mutex'].acquire()
            b8 = self.b11['q'].get()
            self.b11['mutex'].release()
            self.b11['fullSemaphore'].release()
            return b8
    def fonk4(self, status, inputSM):
        while status.b9:
            b6 = tuple(self.b5.batchGenerator())
            inputSM['fullSemaphore'].acquire()
            inputSM['mutex'].acquire()
            inputSM['q'].put(b6)
            inputSM['mutex'].release()
            inputSM['emptySemaphore'].release()
    def fonk5(self):
        if hasattr(self.b5, 'init'):
            self.b5.init()
        self.b4.b9 = True
        self.b10 = {
            "q": Queue(),
            "emptySemaphore": Semaphore(b9 = 0),
            "fullSemaphore": Semaphore(b9 = self.b2),
            "mutex": Lock()
        }
        self.b11 = {
            "q": Queue(),
            "emptySemaphore": Semaphore(b9 = 0),
            "fullSemaphore": Semaphore(b9 = self.b2),
            "mutex": Lock()
        }
        b12 = self.b3 if self.b3 != - 1 else cpu_count()
        self.b13 = []
        self.b14 = Process(target=self.monitor, args=(self.b4, self.b10))
        self.b14.fonk5()
        for i in range(b12):
            b15 = Process(target=self.loadBatch, args=(self.b4, self.b10, self.b11))
            b15.fonk5()
            self.b13.append(b15)
    def fonk6(self):
        self.b4.b9 = False
        for cProcess in self.b13:
            if cProcess.pid is not 0:
                try:
                    os.kill(cProcess.pid, signal.SIGTERM)
                    print("successfully killed child process", cProcess.pid)
                except:
                    print("Access Denied can't kill child process", cProcess.pid)
        try:
            os.kill(self.b14.pid, signal.SIGTERM)
            print("successfully killed monitor process", self.b14.pid)
        except:
            print("Access Denied can't kill monitor process", self.b14.pid)
        print("Job Queue b1 at stop", self.b10['q'].qsize())
        print("b8 Queue b1 at stop", self.b11['q'].qsize())
        self.b10['q'].close()
        self.b11['q'].close()
    def fonk7(self):
        return self.b11['q'].qsize()
    def fonk8(self):
        return self.b11['q'].qsize() == 0