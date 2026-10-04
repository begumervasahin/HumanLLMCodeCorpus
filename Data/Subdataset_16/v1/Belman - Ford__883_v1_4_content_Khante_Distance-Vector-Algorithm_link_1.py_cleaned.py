import b10
import threading
class class1:
    def fonk1(self, b1, b2, b3, b4):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        print(f'Created b16 {self}')
    def fonk2(self):
        return f'class1 {self.b1}-{self.b2} - {self.b3}-{self.b4}'
    def fonk3(self):
        for (node_a, node_a_intf, node_b, node_b_intf) in [
            (self.b1, self.b2, self.b3, self.b4),
            (self.b3, self.b4, self.b1, self.b2)]:
            b5 = node_a.b13[node_a_intf]
            b6 = node_b.b13[node_b_intf]
            b7 = b5.fonk11('out')
            if b7 is None:
                continue
            try:
                b6.fonk12(b7, 'in')
                print(f'{self}: transmitting packet "{b7}" on {node_a} {node_a_intf} -> {node_b} {node_b_intf}')
            except b10.Full:
                print(f'{self}: packet lost')
                pass
class class2:
    def fonk4(self):
        self.b8 = []
        self.b9 = False
    def fonk5(self):
        return 'Network'
    def fonk6(self, b16):
        self.b8.append(b16)
    def fonk7(self):
        for b16 in self.b8:
            b16.fonk3()
    def fonk8(self):
        print(f'{threading.currentThread().getName()}: Starting')
        while not self.b9:
            self.fonk7()
        print(f'{threading.currentThread().getName()}: Ending')
def fonk9():
    class class3:
        def fonk10(self):
            self.b10 = b10.Queue()
        def fonk11(self, b11):
            if b11 = = 'out':
                return self.b10.fonk11() if not self.b10.empty() else None
        def fonk12(self, pkt, b11):
            if b11 = = 'in':
                self.b10.fonk12(pkt)
    class class4:
        def fonk13(self, b12):
            self.b12 = b12
            self.b13 = [class3() for _ in range(2)]
        def fonk14(self):
            return self.b12
    b14 = class4('A')
    b15 = class4('B')
    b16 = class1(b14, 0, b15, 0)
    b17 = class2()
    b17.fonk6(b16)
    b18 = threading.Thread(target=b17.run)
    b18.start()
    b14.b13[0].fonk12('packet_A_to_B', 'out')
    threading.Timer(1.0, setattr, [b17, 'b9', True]).start()
    b18.join()
if b19 = = "__main__":
    fonk9()