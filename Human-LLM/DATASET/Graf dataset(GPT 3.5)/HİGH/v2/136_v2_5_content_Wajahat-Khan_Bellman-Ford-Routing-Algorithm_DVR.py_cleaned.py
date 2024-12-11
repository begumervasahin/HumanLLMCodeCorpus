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
    def fonk3(self, b13, b4, b5 = False):
        if b4 = = 'out':
            self.b3.fonk3(b13, b5)
        else:
            self.b2.fonk3(b13, b5)
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
            raise ValueError(f'Unknown b8 option: {self.b8}')
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
            raise ValueError(f'Unknown b8 field: {b8}')
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
        print(f'{self}: Starting')
        while True:
            self.fonk11()
            if self.b12:
                print(f'{self}: Ending')
                return
class class4:
    def fonk13(self, b15, cost_D, max_queue_size):
        self.b12 = False
        self.b15 = b15
        self.b11 = [class1(max_queue_size) for _ in range(len(cost_D))]
        self.b16 = cost_D
        self.b17 = cost_D.copy()
        self.b18 = defaultdict(dict)
        for neighbor_name, neighbor_info in self.b16.items():
            for interface, b25 in neighbor_info.items():
                self.b18[b15][neighbor_name] = [b25]
        print(f'{self}: Initialized routing table')
        self.fonk19()
    def fonk14(self):
        return self.b15
    def fonk15(self):
        for i in range(len(self.b11)):
            b14 = self.b11[i].fonk2('in')
            if b14 is not None:
                b13 = class2.fonk7(b14)
                if b13.b8 = = 'b7':
                    self.fonk16(b13, i)
                elif b13.b8 = = 'control':
                    self.fonk18(b13, i)
                else:
                    raise ValueError(f'Unknown b13 type in b13 {b13}')
    def fonk16(self, b13, i):
        try:
            b19 = self.b17.fonk2(str(b13.b6))
            for interface, b25 in b19.items():
                b20 = int(interface)
                break
            self.b11[b20].fonk3(b13.fonk6(), 'out', True)
            print(f'{self}: forwarding b13 "{b13}" from interface {i} to {b20}')
        except queue.Full:
            print(f'{self}: b13 "{b13}" lost on interface {i}')
    def fonk17(self, i):
        print('sending routing table')
        b21 = f'{self.b15}->'
        for k, b20 in self.b17.items():
            for link, b25 in b20.items():
                b21 += f'{k}_{link}_{b25} '
        b13 = class2(0, 'control', b21)
        self.b11[i].fonk3(b13.fonk6(), 'out', True)
    def fonk18(self, b13, i):
        a3 = 0
        b21 = b13.b7.split('->')
        b15 = b21[0]
        b22 = b21[1].split(' ')
        for item in b22:
            if item != '':
                b23 = item.split('_')
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
                        if b28 > b27 + b25:
                            self.b17[b24] = {b26: b25 + b27}
                            self.b18[self.b15][b24] = [b25 + b27]
                            a3 = 1
        if a3 = = 1:
            for neighbor_name, neighbor_info in self.b16.items():
                for interface, b25 in neighbor_info.items():
                    if 'R' in neighbor_name:
                        self.fonk17(interface)
    def fonk19(self):
        b29 = []
        print(f'b25 table for {self}:')
        b30 = OrderedDict(sorted(self.b18.items()))
        b11 = []
        for item, neighbor_info in b30.items():
            for link, cost_info in neighbor_info.items():
                if link not in b11:
                    b11.append(link)
        b11 = sorted(b11)
        for interface in b11:
            print(f'{interface}\t', b31 = '')
            for