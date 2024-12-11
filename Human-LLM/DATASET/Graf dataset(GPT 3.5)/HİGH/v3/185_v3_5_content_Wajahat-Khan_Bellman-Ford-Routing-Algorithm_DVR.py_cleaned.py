import queue
import threading
from collections import defaultdict
class class1:
    def fonk1(self, b1 = 0):
        self.b2 = queue.Queue(b1)
        self.b3 = queue.Queue(b1)
    def fonk2(self, b4):
        try:
            return self.b2.fonk2(False) if b4 = = 'in' else self.b3.fonk2(False)
        except queue.Empty:
            return None
    def fonk3(self, b14, b4, b5 = False):
        b6 = self.b3 if b4 == 'out' else self.b2
        b6.fonk3(b14, b5)
class class2:
    a1 = 5
    a2 = 1
    def fonk4(self, b7, b8, b9):
        self.b7 = b7
        self.b8 = b8
        self.b9 = b9
    def fonk5(self):
        return self.fonk6()
    def fonk6(self):
        b10 = str(self.b7).zfill(self.a1)
        b10 += '1' if self.b8 = = 'b9' else '2'
        b10 += self.b9
        return b10
    @classmethod
    def fonk7(cls, b10):
        b7 = b10[:cls.a1].strip('0')
        b8 = 'b9' if b10[cls.a1] == '1' else 'control'
        b9 = b10[cls.a1 + cls.a2:]
        return cls(b7, b8, b9)
class class3:
    def fonk8(self, b11):
        self.b11 = b11
        self.b12 = [class1()]
        self.b13 = False
    def fonk9(self):
        return self.b11
    def fonk10(self, b7, b9):
        b14 = class2(b7, 'b9', b9)
        print(f'{self}: SENDING PACKET "{b14}"')
        self.b12[0].fonk3(b14.fonk6(), 'out')
    def fonk11(self):
        b15 = self.b12[0].fonk2('in')
        if b15:
            print(f'{self}: RECEIVED PACKET "{b15}"')
            if self.b11 = = 'H2':
                self.fonk10('H1', 'The way you look should be a sin, you my sensation')
    def fonk12(self):
        print(f'{self}: Starting')
        while True:
            self.fonk11()
            if self.b13:
                print(f'{self}: Ending')
                return
class class4:
    def fonk13(self, b16, neighbor_costs, max_queue_size):
        self.b13 = False
        self.b16 = b16
        self.b12 = [class1(max_queue_size) for _ in range(len(neighbor_costs))]
        self.b17 = neighbor_costs
        self.b18 = defaultdict(dict)
        self.b19 = defaultdict(dict)
        self.fonk14()
        print(f'{self}: Initialized routing table')
        self.fonk20()
    def fonk14(self):
        for neighbor_name, neighbor_info in self.b17.items():
            for interface, b21 in neighbor_info.items():
                self.b19[self.b16][neighbor_name] = [b21]
    def fonk15(self):
        return self.b16
    def fonk16(self):
        for i, interface in enumerate(self.b12):
            b15 = interface.fonk2('in')
            if b15:
                b14 = class2.fonk7(b15)
                if b14.b8 = = 'b9':
                    self.fonk17(b14, i)
                elif b14.b8 = = 'control':
                    self.fonk19(b14, i)
                else:
                    raise ValueError(f'Unknown b14 type in b14 {b14}')
    def fonk17(self, b14, i):
        try:
            b20 = self.b18.fonk2(str(b14.b7))
            interface, b21 = next(iter(b20.items()))
            self.b12[int(interface)].fonk3(b14.fonk6(), 'out', True)
            print(f'{self}: forwarding b14 "{b14}" from interface {i} to {interface}')
        except queue.Full:
            print(f'{self}: b14 "{b14}" lost on interface {i}')
    def fonk18(self, i):
        print('sending routing table')
        b22 = f'{self.b16}->'
        for k, j in self.b18.items():
            for b30, b21 in j.items():
                b22 += f'{k}_{b30}_{b21} '
        b14 = class2(0, 'control', b22)
        self.b12[i].fonk3(b14.fonk6(), 'out', True)
    def fonk19(self, b14, i):
        a3 = 0
        b16, b23 = b14.b9.split('->')
        for item in b23.split(' '):
            if item:
                b24, _, b21 = item.split('_')
                b21 = int(b21)
                self.b19[b16][b24] = [b21]
                if b24 = = self.b16:
                    b25 = int(list(self.b17[b16].keys())[0])
                    self.b18[b24] = {b25: 0}
                    self.b19[self.b16][b24] = [0]
                    continue
                else:
                    if b24 not in self.b17 and b24 not in self.b18:
                        b26 = list(self.b17[b16].values())[0]
                        b25 = int(list(self.b17[b16].keys())[0])
                        self.b18[b24] = {b25: b21 + b26}
                        self.b19[self.b16][b24] = [b21 + b26]
                        a3 = 1
                    elif b24 not in self.b17 and b24 in self.b18:
                        b26 = list(self.b17[b16].values())[0]
                        b25 = int(list(self.b17[b16].keys())[0])
                        b27 = list(self.b18[b24].values())[0]
                        if b27 > b26 + b21:
                            self.b18[b24] = {b25: b21 + b26}
                            self.b19[self.b16][b24] = [b21 + b26]
                            a3 = 1
        if a3 = = 1:
            for neighbor_name, neighbor_info in self.b17.items():
                for interface, b21 in neighbor_info.items():
                    if 'R' in neighbor_name:
                        self.fonk18(interface)
    def fonk20(self):
        print(f'b21 table for {self}:')
        b28 = OrderedDict(sorted(self.b19.items()))
        b12 = sorted(set(b30 for neighbor_info in b28.values() for b30 in neighbor_info.keys()))
        for interface in b12:
            print(f'{interface}\t', b29 = '')
            for item, neighbor_info in b28.items():
                for b30, cost_info in neighbor_info.items():
                    if b30 = = interface:
                        print(f'{cost_info[0]}\t', b29 = '')
        print('\n')
    def fonk21(self):
        print(f'{self}: Starting')
        while True:
            self.fonk16()
            if self.b13:
                print(f'{self}: Ending')
                return
b31 = {
    'H1': {'R1': {0: 1}},
    'R1': {'R2': {1: 1}},
    'R2