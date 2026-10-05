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
                return self.b2.fonk2(False)
            else:
                return self.b3.fonk2(False)
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
        if self.b8 = = 'b7':
            b9 += '1'
        elif self.b8 = = 'control':
            b9 += '2'
        else:
            raise ValueError(f'Unknown b8: {self.b8}')
        b9 += self.b7
        return b9
    @classmethod
    def fonk7(cls, b9):
        b6 = b9[:cls.a1].strip('0')
        b8 = b9[cls.a1: cls.a1 + cls.a2]
        if b8 = = '1':
            b8 = 'b7'
        elif b8 = = '2':
            b8 = 'control'
        else:
            raise ValueError(f'Unknown b8: {b8}')
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
        print(f'{self}: SENDING PACKET "{b13}"')
        self.b11[0].fonk3(b13.fonk6(), 'out')
    def fonk11(self):
        b14 = self.b11[0].fonk2('in')
        if b14 is not None:
            print(f'{self}: RECEIVED PACKET "{b14}"')
            if self.b10 = = 'H2':
                self.fonk10('H1', 'The way you look should be a sin, you my sensation')
    def fonk12(self):
        print(f'{threading.currentThread().getName()}: Starting')
        while True:
            self.fonk11()
            if self.b12:
                print(f'{threading.currentThread().getName()}: Ending')
                return
class class4:
    def fonk13(self, b15, neighbor_info, b38):
        self.b12 = False
        self.b15 = b15
        self.b11 = [class1(b38) for _ in range(len(neighbor_info))]
        self.b16 = neighbor_info
        self.b17 = neighbor_info.copy()
        self.b18 = defaultdict(dict)
        for neighbor_name, cost_info in self.b16.items():
            for interface, b26 in cost_info.items():
                self.b18[b15][neighbor_name] = [b26]
        print(f'{self}: Initialized routing table')
        self.fonk18()
    def fonk14(self):
        for i, interface in enumerate(self.b11):
            b14 = interface.fonk2('in')
            if b14 is not None:
                b13 = class2.fonk7(b14)
                if b13.b8 = = 'b7':
                    self.fonk15(b13, i)
                elif b13.b8 = = 'control':
                    self.fonk17(b13, i)
                else:
                    raise ValueError(f'Unknown b13 type in b13: {b13}')
    def fonk15(self, b13, interface_index):
        try:
            b19 = self.b17.fonk2(str(b13.b6))
            for interface, b26 in b19.items():
                b20 = int(interface)
                break
            self.b11[b20].fonk3(b13.fonk6(), 'out', True)
            print(f'{self}: forwarding b13 "{b13}" from interface {interface_index} to {b20}')
        except queue.Full:
            print(f'{self}: b13 "{b13}" lost on interface {interface_index}')
    def fonk16(self, interface_index):
        print('sending routing table')
        b21 = f'{self.b15}->'
        for dest, cost_info in self.b17.items():
            for b32, b26 in cost_info.items():
                b21 += f'{dest}_{b32}_{b26} '
        b13 = class2(0, 'control', b21)
        self.b11[interface_index].fonk3(b13.fonk6(), 'out', True)
    def fonk17(self, b13, interface_index):
        a3 = 0
        b21 = b13.b7.split("->")
        b22 = b21[0]
        b23 = b21[1].split(" ")
        for item in b23:
            if item != '':
                b24 = item.split("_")
                b25 = b24[0]
                b26 = int(b24[2])
                self.b18[b22][b25] = [b26]
                if b25 = = self.b15:
                    b20 = int(list(self.b16[b22].keys())[0])
                    self.b17[b25] = {b20: 0}
                    self.b18[self.b15][b25] = [0]
                    continue
                else:
                    if b25 not in self.b16 and b25 not in self.b17:
                        b27 = list(self.b16[b22].values())[0]
                        b20 = int(list(self.b16[b22].keys())[0])
                        self.b17[b25] = {b20: b26 + b27}
                        self.b18[self.b15][b25] = [b26 + b27]
                        a3 = 1
                    elif b25 not in self.b16 and b25 in self.b17:
                        b27 = list(self.b16[b22].values())[0]
                        b20 = int(list(self.b16[b22].keys())[0])
                        b28 = list(self.b17[b25].values())[0]
                        if b28 > b27 + b26:
                            self.b17[b25] = {b20: b26 + b27}
                            self.b18[self.b15][b25] = [b26 + b27]
                            a3 = 1
        if a3 = = 1:
            for neighbor_name, neighbor_info in self.b16.items():
                for interface, b26 in neighbor_info.items():
                    if 'R' in neighbor_name:
                        self.fonk16(interface)
    def fonk18(self):
        b29 = []
        print(f'b26 table for {self}:')
        b30 = OrderedDict(sorted(self.b18.items()))
        b11 = []
        for item, neighbor_info in b30.items():
            for b32, cost_info in neighbor_info.items():
                if b32 not in b11:
                    b11.append(b32)
        b11 = sorted(b11)
        for interface in b11:
            print(f'{interface}\t', b31 = '')
            for item, neighbor_info in b30.items():
                for b32, cost_info in neighbor_info.items():
                    if b32 = = interface:
                        print(f'{cost_info[0]}\t', b31 = '')
                        b29.append(cost_info[0])
        print("\n")
        b33 = ''
        b34 = ''
        for i in range(int(len(b29) / 2 + 1)):
            b33 += '| '
            b33 += str(b29[(i - 1) * 2])
            if i < len(b29):
                b34 += '| '
                b34 += str(b29[(i - 1) * 2 + 1])
        b33 += ' | '
        b34 += ' | '
        print(b33)
        print(b34)
        print("\n")
    def fonk19(self):
        print(f'{threading.currentThread().getName()}: Starting')
        while True:
            self.fonk14()
            if self.b12:
                print(f'{threading.currentThread().getName()}: Ending')
                return
b35 = {
    'H1': {'R1': {0: 1}},
    'R1': {'R2': {1: 1}},
    'R2': {'H2': {0: 1}},
}
b36 = {
    'R1': {'R2': {1: 1}},
    'R2': {'R1': {0: 1}},
}
b37 = []
for b15, config in b36.items():
    b37.append(class4(b15, config, b38 = 100))
b37.extend([class3('H1'), class3('H2')])
for device in b37:
    b39 = threading.Thread(target=device.run)
    b39.start()
b37[0].fonk10('H2', 'Test message from H1 to H2')