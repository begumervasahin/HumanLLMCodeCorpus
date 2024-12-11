import queue
import threading
import time
class class1:
    def fonk1(self, b1, b2, b3, b4):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        print(f'Created b13: {self}')
    def fonk2(self):
        return f'class1 {self.b1}-{self.b2} - {self.b3}-{self.b4}'
    def fonk3(self):
        for src_node, src_intf, dest_node, dest_intf in [(self.b1, self.b2, self.b3, self.b4), (self.b3, self.b4, self.b1, self.b2)]:
            b5 = src_node.b11[src_intf]
            b6 = dest_node.b11[dest_intf]
            b7 = b5.get('out')
            if b7 is None:
                continue
            try:
                b6.put(b7, 'in')
                print(f'{self}: transmitting b7 "{b7}" from {src_node}-{src_intf} to {dest_node}-{dest_intf}')
            except queue.Full:
                print(f'{self}: b7 lost in transmission')
class class2:
    def fonk4(self):
        self.b8 = []
        self.b9 = False
    def fonk5(self):
        return 'class1 Layer'
    def fonk6(self, b13):
        self.b8.append(b13)
    def fonk7(self):
        for b13 in self.b8:
            b13.fonk3()
    def fonk8(self):
        print(f'{threading.currentThread().getName()}: class1 layer started')
        while not self.b9:
            self.fonk7()
        print(f'{threading.currentThread().getName()}: class1 layer stopped')
if b10 = = '__main__':
    b1 = object()
    b3 = object()
    b2 = {'out': 'packet1'}
    b4 = queue.Queue(maxsize=1)
    b1.b11 = {0: b2}
    b3.b11 = {0: b4}
    b12 = class2()
    b13 = class1(b1, 0, b3, 0)
    b12.fonk6(b13)
    b14 = threading.Thread(target=b12.run)
    b14.start()
    time.sleep(1)
    b2['out'] = 'packet2'
    time.sleep(2)
    b12.b9 = True
    b14.join()