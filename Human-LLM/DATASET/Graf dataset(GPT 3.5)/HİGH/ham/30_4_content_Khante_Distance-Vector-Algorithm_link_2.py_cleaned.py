import queue
import threading
class class1:
    def fonk1(self, b1, b2, b3, b4):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        print('Created link %s' % self.fonk5())
    def fonk2(self):
        return 'class1 %s-%d - %s-%d' % (self.b1, self.b2, self.b3, self.b4)
    def fonk3(self):
        for (node_a, node_a_intf, node_b, node_b_intf) in \
        [(self.b1, self.b2, self.b3, self.b4),
         (self.b3, self.b4, self.b1, self.b2)]:
            b5 = node_a.intf_L[node_a_intf]
            b6 = node_b.intf_L[node_b_intf]
            b7 = b5.get('out')
            if b7 is None:
                continue
            try:
                b6.put(b7, 'in')
                print('%s: direction %s-%s -> %s-%s: transmitting packet "%s"' % \
                    (self, node_a, node_a_intf, node_b, node_b_intf, b7))
            except queue.Full:
                print('%s: direction %s-%s -> %s-%s: packet lost' % \
                    (self, node_a, node_a_intf, node_b, node_b_intf))
                pass
class class2:
    def fonk4(self):
        self.b8 = []
        self.b9 = False
    def fonk5(self):
        return 'Network'
    def fonk6(self, link):
        self.b8.append(link)
    def fonk7(self):
        for link in self.b8:
            link.fonk3()
    def fonk8(self):
        print (threading.currentThread().getName() + ': Starting')
        while True:
            self.fonk7()
            if self.b9:
                print (threading.currentThread().getName() + ': Ending')
                return