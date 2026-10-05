import queue
import threading
from collections import OrderedDict, defaultdict
class class1:
    def fonk1(self, b1 = 0):
        self.b2 = queue.Queue(b1)
        self.b3 = queue.Queue(b1)
    def fonk2(self, b4):
        try:
            if b4 = = 'in':
                b5 = self.b2.fonk2(False)
                return b5
            else:
                b5 = self.b3.fonk2(False)
                return b5
        except queue.Empty:
            return None
    def fonk3(self, pkt, b4, b6 = False):
        if b4 = = 'out':
            self.b3.fonk3(pkt, b6)
        else:
            self.b2.fonk3(pkt, b6)
class class2:
    a1 = 5
    a2 = 1
    def fonk4(self, b7, b9, b8):
        self.b7 = b7
        self.b8 = b8
        self.b9 = b9
    def fonk5(self):
        return self.fonk6()
    def fonk6(self):
        b10 = str(self.b7).zfill(self.a1)
        if self.b9 = = 'data':
            b10 += '1'
        elif self.b9 = = 'control':
            b10 += '2'
        else:
            raise Exception('%s: unknown b9 option: %s' %(self, self.b9))
        b10 += self.b8
        return b10
    @classmethod
    def fonk7(cls, b10):
        b7 = b10[0 : cls.a1].strip('0')
        b9 = b10[cls.a1 : cls.a1 + cls.a2]
        if b9 = = '1':
            b9 = 'data'
        elif b9 = = '2':
            b9 = 'control'
        else:
            raise Exception('%s: unknown b9 field: %s' %(cls, b9))
        b8 = b10[cls.a1 + cls.a2 : ]
        return cls(b7, b9, b8)
class class3:
    def fonk8(self, b11):
        self.b11 = b11
        self.b12 = [class1()]
        self.b13 = False
    def fonk9(self):
        return self.b11
    def fonk10(self, b7, b8):
        b14 = class2(b7, 'data', b8)
        print('%s: SENDING PACKET "%s"' % (self, b14))
        self.b12[0].fonk3(b14.fonk6(), 'out')
    def fonk11(self):
        b5 = self.b12[0].fonk2('in')
        if b5 is not None:
            print('%s: RECEIVED PACKET "%s"' % (self, b5))
            if self.b11 = = 'H2':
                self.fonk10('H1', 'The way you look should be a sin, you my sensation')
    def fonk12(self):
        print(threading.currentThread().getName() + ': Starting')
        while True:
            self.fonk11()
            if self.b13:
                print(threading.currentThread().getName() + ': Ending')
                return
class class4:
    def fonk13(self, b15, cost_D, b39):
        self.b13 = False
        self.b15 = b15
        self.b12 = [class1(b39) for _ in range(len(cost_D))]
        self.b16 = cost_D
        self.b17 = cost_D.copy()
        self.b18 = defaultdict(dict)
        for neighbor_name, neighbor_info in self.b16.items():
            for interface,cost in neighbor_info.items():
                self.b18[b15][neighbor_name] = [cost]
        print('%s: Initialized routing table' % self)
        self.fonk19()
    def fonk14(self):
        return self.b15
    def fonk15(self):
        for i in range(len(self.b12)):
            b5 = self.b12[i].fonk2('in')
            if b5 is not None:
                b14 = class2.fonk7(b5)
                if b14.b9 = = 'data':
                    self.fonk16(b14,i)
                elif b14.b9 = = 'control':
                    self.fonk18(b14, i)
                else:
                    raise Exception('%s: Unknown packet type in packet %s' % (self, b14))
    def fonk16(self, b14, i):
        try:
            b19 = self.b17.fonk2(str(b14.b7))
            for interface, cost in b19.items():
                b20 = int(interface)
                break
            self.b12[b20].fonk3(b14.fonk6(), 'out', True)
            print('%s: forwarding packet "%s" from interface %d to %d' % \
                (self, b14, i, b20))
        except queue.Full:
            print('%s: packet "%s" lost on interface %d' % (self, b14, i))
    def fonk17(self, i):
        print('sending_routes')
        b21 = self.b15 + "->"
        for k, b20 in self.b17.items():
            for b33, cost in b20.items():
                b21 += str(k) + "_" + str(b33) + "_" + str(cost) + " "
        b14 = class2(0, 'control', b21)
        self.b12[i].fonk3(b14.fonk6(), 'out', True)
    def fonk18(self, b14, i):
        a3 = 0
        b21 = b14.b8.split("->")
        b15 = b21[0]
        b22 = b21[1].split(" ")
        for i in b22:
            if i != '':
                b23 = i.split("_")
                b24 = b23[0]
                b25 = int(b23[2])
                self.b18[b15][b24] = [b25]
                if b24 = = self.b15:
                    b26 = int(list(self.b16[b15].keys())[0])
                    self.b17[b24] = {b26: 0}
                    self.b18[self.b15][b24] = [0]
                    continue
                else:
                    if b24 not in self.b16 and b24 not in self.b17:
                        b27 = list(self.b16[b15].values())[0]
                        b26 = int(list(self.b16[b15].keys())[0])
                        self.b17[b24] = {b26: b25 + b27}
                        self.b18[self.b15][b24] = [b25 + b27]
                        a3 = 1
                    elif b24 not in self.b16 and b24 in self.b17:
                        b27 = list(self.b16[b15].values())[0]
                        b26 = int(list(self.b16[b15].keys())[0])
                        b28 = list(self.b17[b24].values())[0]
                        if b28 > int(b27) + b25:
                            self.b17[b24] = {b26: b25 + b27}
                            self.b18[self.b15][b24] = [b25 + b27]
                            a3 = 1
        if a3 = = 1:
            for neighbor_name, neighbor_info in self.b16.items():
                for interface, cost in neighbor_info.items():
                    if 'R' in neighbor_name:
                        self.fonk17(interface)
    def fonk19(self):
        b29 = []
        print('cost table for %s: ' % self)
        b30 = OrderedDict(sorted(self.b18.items()))
        b31 = []
        for i, b20 in b30.items():
            for b33, cost in b20.items():
                if not b33 in b31:
                    b31.append(b33)
        b31 = sorted(b31)
        for interface in b31:
            print(str(interface) + "\t", b32 = '')
            for i, b20 in b30.items():
                for b33, cost in b20.items():
                    if b33 = = interface:
                        print(str(cost[0]) + "\t", b32 = '')
                        b29 += [cost[0]]
        print("\n")
        b34 = ''
        b35 = ''
        for i in range(int(len(b29) / 2 + 1)):
            b34 += '| '
            b34 += str(b29[(i - 1) * 2])
            if i < len(b29):
                b35 += '| '
                b35 += str(b29[(i - 1) * 2 + 1])
        b34 += ' | '
        b35 += ' | '
        print(b34)
        print(b35)
        print("\n")
    def fonk20(self):
        print(threading.currentThread().getName() + ': Starting')
        while True:
            self.fonk15()
            if self.b13:
                print(threading.currentThread().getName() + ': Ending')
                return
b36 = {
    'H1': {'R1': {0: 1}},
    'R1': {'R2': {1: 1}},
    'R2': {'H2': {0: 1}},
}
b37 = {
    'R1': {'R2': {1: 1}},
    'R2': {'R1': {0: 1}},
}
b38 = []
for b15, config in b37.items():
    b38.append(class4(b15, config, b39 = 100))
b38.extend([class3('H1'), class3('H2')])
for device in b38:
    b40 = threading.Thread(target=device.run)
    b40.start()
b38[0].fonk10('H2', 'Test message from H1 to H2')