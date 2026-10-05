import queue
import threading
import time
class class1:
    def fonk1(self, b1, b2, b3, b4):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        print('Created b17 %s' % self.fonk5())
    def fonk2(self):
        return 'class1 %s-%d - %s-%d' % (self.b1, self.b2, self.b3, self.b4)
    def fonk3(self):
        for (node_a, node_a_intf, node_b, node_b_intf) in [(self.b1, self.b2, self.b3, self.b4), (self.b3, self.b4, self.b1, self.b2)]:
            b5 = node_a.b15[node_a_intf]
            b6 = node_b.b15[node_b_intf]
            b7 = b5.get('out')
            if b7 is None:
                continue
            try:
                b6.put(b7, 'in')
                print('%s: transmitting packet "%s" on %s %s -> %s, %s' % (self, b7, node_a, node_a_intf, node_b, node_b_intf))
            except queue.Full:
                print('%s: packet lost' % (self))
                pass
class class2:
    def fonk4(self):
        self.b8 = []
        self.b9 = False
    def fonk5(self):
        return 'Network'
    def fonk6(self, b17):
        self.b8.append(b17)
    def fonk7(self):
        for b17 in self.b8:
            b17.fonk3()
    def fonk8(self):
        print(threading.currentThread().getName() + ': Starting')
        while True:
            self.fonk7()
            if self.b9:
                print(threading.currentThread().getName() + ': Ending')
                return
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