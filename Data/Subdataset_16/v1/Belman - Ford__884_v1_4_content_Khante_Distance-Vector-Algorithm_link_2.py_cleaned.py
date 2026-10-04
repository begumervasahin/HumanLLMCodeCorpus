import b11
import threading
class class1:
    def fonk1(self, b1, b2, b3, b4):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        print(f'Created b17 {self}')
    def fonk2(self):
        return f'class1 {self.b1}-{self.b2} - {self.b3}-{self.b4}'
    def fonk3(self):
        b5 = [
            (self.b1, self.b2, self.b3, self.b4),
            (self.b3, self.b4, self.b1, self.b2)
        ]
        for (node_a, node_a_intf, node_b, node_b_intf) in b5:
            b6 = node_a.b14[node_a_intf]
            b7 = node_b.b14[node_b_intf]
            b8 = b6.fonk11('out')
            if b8 is None:
                continue
            try:
                b7.fonk12(b8, 'in')
                print(f'{self}: b12 {node_a}-{node_a_intf} -> {node_b}-{node_b_intf}: transmitting packet "{b8}"')
            except b11.Full:
                print(f'{self}: b12 {node_a}-{node_a_intf} -> {node_b}-{node_b_intf}: packet lost')
class class2:
    def fonk4(self):
        self.b9 = []
        self.b10 = False
    def fonk5(self):
        return 'Network'
    def fonk6(self, b17):
        self.b9.append(b17)
    def fonk7(self):
        for b17 in self.b9:
            b17.fonk3()
    def fonk8(self):
        print(f'{threading.currentThread().getName()}: Starting')
        while not self.b10:
            self.fonk7()
        print(f'{threading.currentThread().getName()}: Ending')
def fonk9():
    class class3:
        def fonk10(self):
            self.b11 = b11.Queue()
        def fonk11(self, b12):
            if b12 = = 'out':
                return self.b11.fonk11() if not self.b11.empty() else None
        def fonk12(self, pkt, b12):
            if b12 = = 'in':
                self.b11.fonk12(pkt)
    class class4:
        def fonk13(self, b13):
            self.b13 = b13
            self.b14 = [class3() for _ in range(2)]
        def fonk14(self):
            return self.b13
    b15 = class4('A')
    b16 = class4('B')
    b17 = class1(b15, 0, b16, 0)
    b18 = class2()
    b18.fonk6(b17)
    b19 = threading.Thread(target=b18.run)
    b19.start()
    b15.b14[0].fonk12('packet_A_to_B', 'out')
    threading.Timer(1.0, setattr, [b18, 'b10', True]).start()
    b19.join()
if b20 = = "__main__":
    fonk9()