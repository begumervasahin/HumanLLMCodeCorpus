import queue
import threading
import time
class class1:
    def fonk1(self, b1, b2, b3, b4):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        print(f'Created b17: {self}')
    def fonk2(self):
        return f'class1 {self.b1}-{self.b2} - {self.b3}-{self.b4}'
    def fonk3(self):
        for src_node, src_intf, dest_node, dest_intf in [(self.b1, self.b2, self.b3, self.b4), (self.b3, self.b4, self.b1, self.b2)]:
            b5 = src_node.b15[src_intf]
            b6 = dest_node.b15[dest_intf]
            b7 = b5.get('out')
            if b7 is None:
                continue
            try:
                b6.put(b7, 'in')
                print(f'{self}: direction {src_node}-{src_intf} -> {dest_node}-{dest_intf}: transmitting b7 "{b7}"')
            except queue.Full:
                print(f'{self}: direction {src_node}-{src_intf} -> {dest_node}-{dest_intf}: b7 lost')
class class2:
    def fonk4(self):
        self.b8 = []
        self.b9 = False
    def fonk5(self):
        return 'class1 Layer'
    def fonk6(self, b17):
        self.b8.append(b17)
    def fonk7(self):
        for b17 in self.b8:
            b17.fonk3()
    def fonk8(self):
        print(f'{threading.currentThread().getName()}: class1 layer started')
        while not self.b9:
            self.fonk7()
        print(f'{threading.currentThread().getName()}: class1 layer stopped')
if b10 = = '__main__':
    b11 = object()
    b12 = object()
    b13 = {'out': 'packet1'}
    b14 = queue.Queue(maxsize=1)
    b11.b15 = {0: b13}
    b12.b15 = {0: b14}
    b16 = class2()
    b17 = class1(b11, 0, b12, 0)
    b16.fonk6(b17)
    b18 = threading.Thread(target=b16.run)
    b18.start()
    time.sleep(1)
    b13['out'] = 'packet2'
    time.sleep(2)
    b16.b9 = True
    b18.join()