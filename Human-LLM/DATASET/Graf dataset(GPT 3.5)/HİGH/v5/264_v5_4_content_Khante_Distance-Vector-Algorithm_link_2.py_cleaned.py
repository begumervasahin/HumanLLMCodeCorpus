import queue
import threading
class class1:
    def fonk1(self, b1, b2, b3, b4):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        print(f'Created b18: {self}')
    def fonk2(self):
        return f'class1 {self.b1}-{self.b2} - {self.b3}-{self.b4}'
    def fonk3(self):
        src_node, src_intf, dest_node, b5 = self.b1, self.b2, self.b3, self.b4
        b6 = src_node.b16[src_intf]
        b7 = dest_node.b16[b5]
        b8 = b6.get('out')
        if b8 is None:
            return
        try:
            b7.put(b8, 'in')
            print(f'{self}: {src_node}-{src_intf} -> {dest_node}-{b5}: transmitting b8 "{b8}"')
        except queue.Full:
            print(f'{self}: {src_node}-{src_intf} -> {dest_node}-{b5}: b8 lost')
class class2:
    def fonk4(self):
        self.b9 = []
        self.b10 = False
    def fonk5(self):
        return 'class1 Layer'
    def fonk6(self, b18):
        self.b9.append(b18)
    def fonk7(self):
        for b18 in self.b9:
            b18.fonk3()
    def fonk8(self):
        print(f'{threading.currentThread().getName()}: class1 layer started')
        while not self.b10:
            self.fonk7()
        print(f'{threading.currentThread().getName()}: class1 layer stopped')
if b11 = = '__main__':
    b12 = object()
    b13 = object()
    b14 = {'out': 'packet1'}
    b15 = queue.Queue(maxsize=1)
    b12.b16 = {0: b14}
    b13.b16 = {0: b15}
    b17 = class2()
    b18 = class1(b12, 0, b13, 0)
    b17.fonk6(b18)
    b19 = threading.Thread(target=b17.run)
    b19.start()
    b14['out'] = 'packet2'
    b17.b10 = True
    b19.join()