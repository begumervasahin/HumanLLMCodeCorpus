import threading
import queue
from collections import defaultdict, OrderedDict
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
    def fonk10(self, b6, b7):
        b13 = class2(b6, 'b7', b7)
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
    def fonk13(self, b14, b15, b34):
        self.b12 = False
        self.b14 = b14
        self.b11 = [class1(b34) for _ in range(len(b15))]
        self.b15 = b15
        self.b16 = b15.copy()
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
            b13 = interface.fonk2('in')
            if b13 is not None:
                b18 = class2.fonk7(b13)
                if b18.b8 = = 'b7':
                    self.fonk16(b18, i)
                elif b18.b8 = = 'control':
                    self.fonk18(b18, i)
                else:
                    raise ValueError('%s: Unknown b13 type in b13 %s' % (self, b18))
    def fonk16(self, b18, interface_index):
        try:
            b19 = self.b16.fonk2(str(b18.b6))
            b20 = next(iter(b19))
            self.b11[b20].fonk3(b18.fonk6(), 'out', True)
            print('%s: forwarding b13 "%s" from interface %d to %d' % (self, b18, interface_index, b20))
        except queue.Full:
            print('%s: b13 "%s" lost on interface %d' % (self, b18, interface_index))
    def fonk17(self, interface_index):
        print('sending_routing_table')
        b21 = f"{self.b14}->"
        for node, b15 in self.b16.items():
            for b30, cost in b15.items():
                b21 += f"{node}_{b30}_{cost} "
        b13 = class2(0, 'control', b21)
        self.b11[interface_index].fonk3(b13.fonk6(), 'out', True)
    def fonk18(self, b18, interface_index):
        a3 = 0
        source_node, b22 = b18.b7.split("->")
        for b19 in b22.split():
            if b19:
                b24, _, b23 = b19.split("_")
                b23 = int(b23)
                self.b17[source_node][b24] = [b23]
                if b24 = = self.b14:
                    b25 = next(iter(self.b15[source_node]))
                    self.b16[b24] = {b25: 0}
                    self.b17[self.b14][b24] = [0]
                    continue
                else:
                    if b24 not in self.b15 and b24 not in self.b16:
                        b26 = next(iter(self.b15[source_node].values()))
                        b25 = next(iter(self.b15[source_node].keys()))
                        self.b16[b24] = {b25: b23 + b26}
                        self.b17[self.b14][b24] = [b23 + b26]
                        a3 = 1
                    elif b24 not in self.b15 and b24 in self.b16:
                        b26 = next(iter(self.b15[source_node].values()))
                        b25 = next(iter(self.b15[source_node].keys()))
                        b27 = next(iter(self.b16[b24].values()))
                        if b27 > b26 + b23:
                            self.b16[b24] = {b25: b23 + b26}
                            self.b17[self.b14][b24] = [b23 + b26]
                            a3 = 1
        if a3 = = 1:
            for neighbor_name, neighbor_info in self.b15.items():
                for interface_index, cost in neighbor_info.items():
                    if 'R' in neighbor_name:
                        self.fonk17(interface_index)
    def fonk19(self):
        print(f'Routing table for {self}:')
        b28 = OrderedDict(sorted(self.b17.items()))
        b11 = sorted(set(interface for node in b28.values() for interface in node))
        for interface in b11:
            print(interface, b29 = '\t')
            for node, b15 in b28.items():
                for b30, cost in b15.items():
                    if b30 = = interface:
                        print(cost[0], b29 = '\t')
        print("\n")
    def fonk20(self):
        print(threading.currentThread().getName() + ': Starting')
        while True:
            self.fonk15()
            if self.b12:
                print(threading.currentThread().getName() + ': Ending')
                return
b31 = {
    'H1': {'R1': {0: 1}},
    'R1': {'R2': {1: 1}},
    'R2': {'H2': {0: 1}},
}
b32 = {
    'R1': {'R2': {1: 1}},
    'R2': {'R1': {0: 1}},
}
b33 = []
for b14, config in b32.items():
    b33.append(class4(b14, config, b34 = 100))
b33.extend([class3('H1'), class3('H2')])
for device in b33:
    b35 = threading.Thread(target=device.run)
    b35.start()
b33[0].fonk10('H2', 'Test message from H1 to H2')