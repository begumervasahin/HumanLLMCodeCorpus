import threading
import queue
from collections import defaultdict, OrderedDict
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
    def fonk3(self, b5, b4, b6 = False):
        if b4 = = 'out':
            self.b3.fonk3(b5, b6)
        else:
            self.b2.fonk3(b5, b6)
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
        if self.b9 = = 'b8':
            b10 += '1'
        elif self.b9 = = 'control':
            b10 += '2'
        else:
            raise ValueError('%s: unknown b9 option: %s' % (self, self.b9))
        b10 += self.b8
        return b10
    @classmethod
    def fonk7(cls, b10):
        b7 = b10[0:cls.a1].strip('0')
        b9 = b10[cls.a1:cls.a1 + cls.a2]
        if b9 = = '1':
            b9 = 'b8'
        elif b9 = = '2':
            b9 = 'control'
        else:
            raise ValueError('%s: unknown b9 field: %s' % (cls, b9))
        b8 = b10[cls.a1 + cls.a2:]
        return cls(b7, b9, b8)
class class3:
    def fonk8(self, b11):
        self.b11 = b11
        self.b12 = [class1()]
        self.b13 = False
    def fonk9(self):
        return self.b11
    def fonk10(self, b7, b8):
        b14 = class2(b7, 'b8', b8)
        print('%s: SENDING PACKET "%s"' % (self, b14))
        self.b12[0].fonk3(b14.fonk6(), 'out')
    def fonk11(self):
        b14 = self.b12[0].fonk2('in')
        if b14 is not None:
            print('%s: RECEIVED PACKET "%s"' % (self, b14))
    def fonk12(self):
        print(threading.currentThread().getName() + ': Starting')
        while True:
            self.fonk11()
            if self.b13:
                print(threading.currentThread().getName() + ': Ending')
                return
class class4:
    def fonk13(self, b15, b16, b40):
        self.b13 = False
        self.b15 = b15
        self.b12 = [class1(b40) for _ in range(len(b16))]
        self.b16 = b16
        self.b17 = b16.copy()
        self.b18 = defaultdict(dict)
        for neighbor_name, neighbor_info in self.b16.items():
            for interface, cost in neighbor_info.items():
                self.b18[b15][neighbor_name] = [cost]
        print('%s: Initialized routing table' % self)
        self.fonk19()
    def fonk14(self):
        return self.b15
    def fonk15(self):
        for i in range(len(self.b12)):
            b14 = self.b12[i].fonk2('in')
            if b14 is not None:
                b19 = class2.fonk7(b14)
                if b19.b9 = = 'b8':
                    self.fonk16(b19, i)
                elif b19.b9 = = 'control':
                    self.fonk18(b19, i)
                else:
                    raise ValueError('%s: Unknown b14 type in b14 %s' % (self, b19))
    def fonk16(self, b19, interface_index):
        try:
            b20 = self.b17.fonk2(str(b19.b7))
            for interface, cost in b20.items():
                b21 = int(interface)
                break
            self.b12[b21].fonk3(b19.fonk6(), 'out', True)
            print('%s: forwarding b14 "%s" from interface %d to %d' % (self, b19, interface_index, b21))
        except queue.Full:
            print('%s: b14 "%s" lost on interface %d' % (self, b19, interface_index))
    def fonk17(self, interface_index):
        print('sending_routing_table')
        b22 = self.b15 + "->"
        for node, b16 in self.b17.items():
            for b34, cost in b16.items():
                b22 += str(node) + "_" + str(b34) + "_" + str(cost) + " "
        b14 = class2(0, 'control', b22)
        self.b12[interface_index].fonk3(b14.fonk6(), 'out', True)
    def fonk18(self, b19, interface_index):
        a3 = 0
        b22 = b19.b8.split("->")
        b23 = b22[0]
        b24 = b22[1].split(" ")
        for b20 in b24:
            if b20 != '':
                b25 = b20.split("_")
                b26 = b25[0]
                b27 = int(b25[2])
                self.b18[b23][b26] = [b27]
                if b26 = = self.b15:
                    b28 = int(list(self.b16[b23].keys())[0])
                    self.b17[b26] = {b28: 0}
                    self.b18[self.b15][b26] = [0]
                    continue
                else:
                    if b26 not in self.b16 and b26 not in self.b17:
                        b29 = list(self.b16[b23].values())[0]
                        b28 = int(list(self.b16[b23].keys())[0])
                        self.b17[b26] = {b28: b27 + b29}
                        self.b18[self.b15][b26] = [b27 + b29]
                        a3 = 1
                    elif b26 not in self.b16 and b26 in self.b17:
                        b29 = list(self.b16[b23].values())[0]
                        b28 = int(list(self.b16[b23].keys())[0])
                        b30 = list(self.b17[b26].values())[0]
                        if b30 > b29 + b27:
                            self.b17[b26] = {b28: b27 + b29}
                            self.b18[self.b15][b26] = [b27 + b29]
                            a3 = 1
        if a3 = = 1:
            for neighbor_name, neighbor_info in self.b16.items():
                for interface_index, cost in neighbor_info.items():
                    if 'R' in neighbor_name:
                        self.fonk17(interface_index)
    def fonk19(self):
        b31 = []
        print('routing table for %s: ' % self)
        b32 = OrderedDict(sorted(self.b18.items()))
        b12 = []
        for node, b16 in b32.items():
            for b34, cost in b16.items():
                if b34 not in b12:
                    b12.append(b34)
        b12 = sorted(b12)
        for interface in b12:
            print(str(interface) + "\t", b33 = '')
            for node, b16 in b32.items():
                for b34, cost in b16.items():
                    if b34 = = interface:
                        print(str(cost) + "\t", b33 = '')
                        b31 += [cost]
        print("\n")
        b35 = ''
        b36 = ''
        for i in range(int(len(b31) / 2 + 1)):
            b35 += '| '
            b35 += str(b31[(i - 1) * 2])
            if i < len(b31):
                b36 += '| '
                b36 += str(b31[(i - 1) * 2 + 1])
        b35 += ' | '
        b36 += ' | '
        print(b35)
        print(b36)
        print("\n")
    def fonk20(self):
        print(threading.currentThread().getName() + ': Starting')
        while True:
            self.fonk15()
            if self.b13:
                print(threading.currentThread().getName() + ': Ending')
                return
b37 = {
    'H1': {'R1': {0: 1}},
    'R1': {'R2': {1: 1}},
    'R2': {'H2': {0: 1}},
}
b38 = {
    'R1': {'R2': {1: 1}},
    'R2': {'R1': {0: 1}},
}
b39 = []
for b15, config in b38.items():
    b39.append(class4(b15, config, b40 = 100))
b39.append(class3('H1'))
b39.append(class3('H2'))
for device in b39:
    b41 = threading.Thread(target=device.run)
    b41.start()
b39[0].fonk10('H2', 'Test message from H1 to H2')