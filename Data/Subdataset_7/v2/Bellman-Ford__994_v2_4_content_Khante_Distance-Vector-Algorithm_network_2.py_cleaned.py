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
            raise ValueError(f'Unknown b9 option: {self.b9}')
        b10 += self.b8
        return b10
    @classmethod
    def fonk7(cls, b10):
        b7 = b10[:cls.a1].strip('0')
        b9 = b10[cls.a1: cls.a1 + cls.a2]
        if b9 = = '1':
            b9 = 'data'
        elif b9 = = '2':
            b9 = 'control'
        else:
            raise ValueError(f'Unknown b9 field: {b9}')
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
        b14 = class2(b7, 'data', b8)
        print(f'{self}: SENDING PACKET "{b14}"')
        self.b12[0].fonk3(b14.fonk6(), 'out')
    def fonk11(self):
        b15 = self.b12[0].fonk2('in')
        if b15 is not None:
            print(f'{self}: RECEIVED PACKET "{b15}"')
            if self.b11 = = 'H2':
                self.fonk10('H1', 'The way you look should be a sin, you my sensation')
    def fonk12(self):
        print(f'{threading.currentThread().getName()}: Starting')
        while True:
            self.fonk11()
            if self.b13:
                print(f'{threading.currentThread().getName()}: Ending')
                return
class class4:
    def fonk13(self, b16, cost_D, b40):
        self.b13 = False
        self.b16 = b16
        self.b12 = [class1(b40) for _ in range(len(cost_D))]
        self.b17 = cost_D
        self.b18 = cost_D.copy()
        self.b19 = defaultdict(dict)
        for neighbor_name, neighbor_info in self.b17.items():
            for interface, cost in neighbor_info.items():
                self.b19[b16][neighbor_name] = [cost]
        print(f'{self}: Initialized routing table')
        self.fonk19()
    def fonk14(self):
        return self.b16
    def fonk15(self):
        for i in range(len(self.b12)):
            b15 = self.b12[i].fonk2('in')
            if b15 is not None:
                b14 = class2.fonk7(b15)
                if b14.b9 = = 'data':
                    self.fonk16(b14, i)
                elif b14.b9 = = 'control':
                    self.fonk18(b14, i)
                else:
                    raise ValueError(f'Unknown b14 type in b14 {b14}')
    def fonk16(self, b14, i):
        try:
            b20 = self.b18.fonk2(str(b14.b7))
            for interface, cost in b20.items():
                b21 = int(interface)
                break
            self.b12[b21].fonk3(b14.fonk6(), 'out', True)
            print(f'{self}: forwarding b14 "{b14}" from interface {i} to {b21}')
        except queue.Full:
            print(f'{self}: b14 "{b14}" lost on interface {i}')
    def fonk17(self, i):
        print('sending_routes')
        b22 = f'{self.b16}->'
        for k, b21 in self.b18.items():
            for b34, cost in b21.items():
                b22 += f'{k}_{b34}_{cost} '
        b14 = class2(0, 'control', b22)
        self.b12[i].fonk3(b14.fonk6(), 'out', True)
    def fonk18(self, b14, i):
        a3 = 0
        b22 = b14.b8.split("->")
        b16 = b22[0]
        b23 = b22[1].split(" ")
        for item in b23:
            if item != '':
                b24 = item.split("_")
                b25 = b24[0]
                b26 = int(b24[2])
                self.b19[b16][b25] = [b26]
                if b25 = = self.b16:
                    b27 = int(list(self.b17[b16].keys())[0])
                    self.b18[b25] = {b27: 0}
                    self.b19[self.b16][b25] = [0]
                    continue
                else:
                    if b25 not in self.b17 and b25 not in self.b18:
                        b28 = list(self.b17[b16].values())[0]
                        b27 = int(list(self.b17[b16].keys())[0])
                        self.b18[b25] = {b27: b26 + b28}
                        self.b19[self.b16][b25] = [b26 + b28]
                        a3 = 1
                    elif b25 not in self.b17 and b25 in self.b18:
                        b28 = list(self.b17[b16].values())[0]
                        b27 = int(list(self.b17[b16].keys())[0])
                        b29 = list(self.b18[b25].values())[0]
                        if b29 > int(b28) + b26:
                            self.b18[b25] = {b27: b26 + b28}
                            self.b19[self.b16][b25] = [b26 + b28]
                            a3 = 1
        if a3 = = 1:
            for neighbor_name, neighbor_info in self.b17.items():
                for interface, cost in neighbor_info.items():
                    if 'R' in neighbor_name:
                        self.fonk17(interface)
    def fonk19(self):
        b30 = []
        print(f'cost table for {self}:')
        b31 = OrderedDict(sorted(self.b19.items()))
        b32 = []
        for item, b21 in b31.items():
            for b34, cost in b21.items():
                if b34 not in b32:
                    b32.append(b34)
        b32 = sorted(b32)
        for interface in b32:
            print(f'{interface}\t', b33 = '')
            for item, b21 in b31.items():
                for b34, cost in b21.items():
                    if b34 = = interface:
                        print(f'{cost[0]}\t', b33 = '')
                        b30.append(cost[0])
        print("\n")
        b35 = ''
        b36 = ''
        for i in range(int(len(b30) / 2 + 1)):
            b35 += '| '
            b35 += str(b30[(i - 1) * 2])
            if i < len(b30):
                b36 += '| '
                b36 += str(b30[(i - 1) * 2 + 1])
        b35 += ' | '
        b36 += ' | '
        print(b35)
        print(b36)
        print("\n")
    def fonk20(self):
        print(f'{threading.currentThread().getName()}: Starting')
        while True:
            self.fonk15()
            if self.b13:
                print(f'{threading.currentThread().getName()}: Ending')
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
for b16, config in b38.items():
    b39.append(class4(b16, config, b40 = 100))
b39.extend([class3('H1'), class3('H2')])
for device in b39:
    b41 = threading.Thread(target=device.run)
    b41.start()
b39[0].fonk10('H2', 'Test message from H1 to H2')