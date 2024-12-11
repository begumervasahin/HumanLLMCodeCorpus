import queue
import threading
import time
class class1:
    def fonk1(self, b1, b2, b3, b4):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        print(f'Created b15: {self}')
    def fonk2(self):
        return f'class1 {self.b1}-{self.b2} - {self.b3}-{self.b4}'
    def fonk3(self):
        for (node_a, intf_a, node_b, intf_b) in [(self.b1, self.b2, self.b3, self.b4), (self.b3, self.b4, self.b1, self.b2)]:
            b5 = intf_a.get('out')
            if b5 is None:
                continue
            try:
                intf_b.put(b5, 'in')
                print(f'{self}: transmitting packet "{b5}" from {node_a} {intf_a} to {node_b} {intf_b}')
            except queue.Full:
                print(f'{self}: packet lost')
                pass
class class2:
    def fonk4(self):
        self.b6 = []
        self.b7 = False
    def fonk5(self):
        return 'class1 Layer'
    def fonk6(self, b15):
        self.b6.append(b15)
    def fonk7(self):
        for b15 in self.b6:
            b15.fonk3()
    def fonk8(self):
        print(f'{threading.currentThread().getName()}: class1 layer started')
        while not self.b7:
            self.fonk7()
            time.sleep(0.1)
        print(f'{threading.currentThread().getName()}: class1 layer stopped')
if b8 = = '__main__':
    b9 = object()
    b10 = object()
    b11 = {'out': 'packet1'}
    b12 = queue.Queue(maxsize=1)
    b9.b13 = {0: b11}
    b10.b13 = {0: b12}
    b14 = class2()
    b15 = class1(b9, 0, b10, 0)
    b14.fonk6(b15)
    b16 = threading.Thread(target=b14.run)
    b16.start()
    time.sleep(1)
    b11['out'] = 'packet2'
    time.sleep(2)
    b14.b7 = True
    b16.join()