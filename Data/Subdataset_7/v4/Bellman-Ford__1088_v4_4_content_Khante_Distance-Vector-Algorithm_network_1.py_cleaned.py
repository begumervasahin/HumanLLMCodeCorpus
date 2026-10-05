import queue
import threading
from collections import OrderedDict, defaultdict
class class1:
    def fonk1(self, b1 = 0):
        self.b2 = queue.Queue(b1)
        self.b3 = queue.Queue(b1)
    def fonk2(self, b4):
        try:
            return self.b2.fonk2(False) if b4 = = 'in' else self.b3.fonk2(False)
        except queue.Empty:
            return None
    def fonk3(self, pkt, b4, b5 = False):
        if b4 = = 'out':
            self.b3.fonk3(pkt, b5)
        else:
            self.b2.fonk3(pkt, b5)
class class2:
    a1 = 5
    a2 = 1
    def fonk4(self, b6, b8, b7):
        self.b6 = b6
        self.b7 = b7
        self.b8 = b8
    def fonk5(self):
        return self.fonk6()
    def fonk6(self):
        b9 = str(self.b6).zfill(self.a1)
        b9 += '1' if self.b8 = = 'b7' else '2'
        b9 += self.b7
        return b9
    @classmethod
    def fonk7(cls, b9):
        b6 = b9[:cls.a1].strip('0')
        b8 = 'b7' if b9[cls.a1:cls.a1 + cls.a2] == '1' else 'control'
        b7 = b9[cls.a1 + cls.a2:]
        return cls(b6, b8, b7)
class class3:
    def fonk8(self, b10):
        self.b10 = b10
        self.b11 = [class1()]
        self.b12 = False
    def fonk9(self):
        return self.b10
    def fonk10(self, destination, b7):
        b13 = class2(destination, 'b7', b7)
        print('%s: SENDING PACKET "%s"' % (self, b13))
        self.b11[0].fonk3(b13.fonk6(), 'out')
    def fonk11(self):
        b13 = self.b11[0].fonk2('in')
        if b13 is not None:
            print('%s: RECEIVED PACKET "%s"' % (self, b13))
    def fonk12(self):
        print(threading.currentThread().getName() + ': Starting')
        while True:
            self.fonk11()
            if self.b12:
                print(threading.currentThread().getName() + ': Ending')
                return
class class4:
    def fonk13(self, b14, cost_dict, b39):
        self.b12 = False
        self.b14 = b14
        self.b11 = [class1(b39) for _ in range(len(cost_dict))]
        self.b15 = cost_dict
        self.b16 = cost_dict.copy()
        self.b17 = defaultdict(dict)
        for neighbor_name, neighbor_info in self.b15.items():
            for interface, cost in neighbor_info.items():
                self.b17[b14][neighbor_name] = [cost]
        print('%s: Initialized routing table' % self)
        self.fonk19()
    def fonk14(self):
        return self.b14
    def fonk15(self):
        for i, interface in enumerate(self.b11):
            b18 = interface.fonk2('in')
            if b18 is not None:
                b13 = class2.fonk7(b18)
                if b13.b8 = = 'b7':
                    self.fonk16(b13, i)
                elif b13.b8 = = 'control':
                    self.fonk18(b13, i)
                else:
                    raise Exception('%s: Unknown b13 type in b13 %s' % (self, b13))
    def fonk16(self, b13, interface_index):
        try:
            b19 = self.b16.fonk2(str(b13.b6))
            b20 = next(iter(b19))
            self.b11[b20].fonk3(b13.fonk6(), 'out', True)
            print('%s: forwarding b13 "%s" from interface %d to %d' % (self, b13, interface_index, b20))
        except queue.Full:
            print('%s: b13 "%s" lost on interface %d' % (self, b13, interface_index))
    def fonk17(self, interface_index):
        print('sending_routing_table')
        b21 = f"{self.b14}->"
        for node, b15 in self.b16.items():
            for b33, cost in b15.items():
                b21 += f"{node}_{b33}_{cost} "
        b13 = class2(0, 'control', b21)
        self.b11[interface_index].fonk3(b13.fonk6(), 'out', True)
    def fonk18(self, b13, interface_index):
        a3 = 0
        b21 = b13.b7.split("->")
        b22 = b21[0]
        b23 = b21[1].split(" ")
        for b19 in b23:
            if b19 != '':
                b24 = b19.split("_")
                b25 = b24[0]
                b26 = int(b24[2])
                self.b17[b22][b25] = [b26]
                if b25 = = self.b14:
                    b27 = next(iter(self.b15[b22]))
                    self.b16[b25] = {b27: 0}
                    self.b17[self.b14][b25] = [0]
                    continue
                else:
                    if b25 not in self.b15 and b25 not in self.b16:
                        b28 = next(iter(self.b15[b22].values()))
                        b27 = next(iter(self.b15[b22].keys()))
                        self.b16[b25] = {b27: b26 + b28}
                        self.b17[self.b14][b25] = [b26 + b28]
                        a3 = 1
                    elif b25 not in self.b15 and b25 in self.b16:
                        b28 = next(iter(self.b15[b22].values()))
                        b27 = next(iter(self.b15[b22].keys()))
                        b29 = next(iter(self.b16[b25].values()))
                        if b29 > b28 + b26:
                            self.b16[b25] = {b27: b26 + b28}
                            self.b17[self.b14][b25] = [b26 + b28]
                            a3 = 1
        if a3 = = 1:
            for neighbor_name, neighbor_info in self.b15.items():
                for interface_index, cost in neighbor_info.items():
                    if 'R' in neighbor_name:
                        self.fonk17(interface_index)
    def fonk19(self):
        b30 = []
        print('Routing table for %s:' % self)
        b31 = OrderedDict(sorted(self.b17.items()))
        b11 = sorted(set(interface for node in b31.values() for interface in node))
        for interface in b11:
            print(interface, b32 = '\t')
            for node, b15 in b31.items():
                for b33, cost in b15.items():
                    if b33 = = interface:
                        print(cost[0], b32 = '\t')
                        b30.append(cost[0])
        print("\n")
        b34 = ''
        b35 = ''
        for i in range(0, len(b30), 2):
            b34 += f'| {b30[i]}'
            if i + 1 < len(b30):
                b35 += f'| {b30[i+1]}'
        b34 += ' |'
        b35 += ' |'
        print(b34)
        print(b35)
        print("\n")
    def fonk20(self):
        print(threading.currentThread().getName() + ': Starting')
        while True:
            self.fonk15()
            if self.b12:
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
for b14, config in b37.items():
    b38.append(class4(b14, config, b39 = 100))
b38.extend([class3('H1'), class3('H2')])
for device in b38:
    b40 = threading.Thread(target=device.run)
    b40.start()
b38[0].fonk10('H2', 'Test message from H1 to H2')