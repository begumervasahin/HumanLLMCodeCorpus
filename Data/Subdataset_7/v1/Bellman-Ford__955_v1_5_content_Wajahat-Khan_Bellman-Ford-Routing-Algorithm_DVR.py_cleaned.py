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
            raise ValueError('Unknown protocol option: {}'.format(self.b8))
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
            raise ValueError('Unknown protocol field: {}'.format(b8))
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
        print('{}: SENDING PACKET "{}"'.format(self, b13))
        self.b11[0].fonk3(b13.fonk6(), 'out')
    def fonk11(self):
        b14 = self.b11[0].fonk2('in')
        if b14 is not None:
            print('{}: RECEIVED PACKET "{}"'.format(self, b14))
            if self.b10 = = 'H2':
                self.fonk10('H1', 'The way you look should be a sin, you my sensation')
    def fonk12(self):
        print('{}: Starting'.format(threading.currentThread().getName()))
        while True:
            self.fonk11()
            if self.b12:
                print('{}: Ending'.format(threading.currentThread().getName()))
                return
class class4:
    def fonk13(self, b15, cost_D, b38):
        self.b12 = False
        self.b15 = b15
        self.b11 = [class1(b38) for _ in range(len(cost_D))]
        self.b16 = cost_D
        self.b17 = cost_D.copy()
        self.b18 = defaultdict(dict)
        for neighbor_name, neighbor_info in self.b16.items():
            for interface, b25 in neighbor_info.items():
                self.b18[b15][neighbor_name] = [b25]
        print('{}: Initialized routing table'.format(self))
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
                    raise ValueError('Unknown b13 type in b13 {}'.format(b13))
    def fonk16(self, b13, i):
        try:
            b19 = self.b17.fonk2(str(b13.b6))
            for interface, b25 in b19.items():
                b20 = int(interface)
                break
            self.b11[b20].fonk3(b13.fonk6(), 'out', True)
            print('{}: forwarding b13 "{}" from interface {} to {}'.format(self, b13, i, b20))
        except queue.Full:
            print('{}: b13 "{}" lost on interface {}'.format(self, b13, i))
    def fonk17(self, i):
        print('sending routing table')
        b21 = '{}->'.format(self.b15)
        for k, b20 in self.b17.items():
            for b32, b25 in b20.items():
                b21 += '{}_{}_{} '.format(k, b32, b25)
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
        print('b25 table for {}:'.format(self))
        b30 = OrderedDict(sorted(self.b18.items()))
        b11 = []
        for item, neighbor_info in b30.items():
            for b32, cost_info in neighbor_info.items():
                if b32 not in b11:
                    b11.append(b32)
        b11 = sorted(b11)
        for interface in b11:
            print('{}\t'.format(interface), b31 = '')
            for item, neighbor_info in b30.items():
                for b32, cost_info in neighbor_info.items():
                    if b32 = = interface:
                        print('{}\t'.format(cost_info[0]), b31 = '')
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
    def fonk20(self):
        print('{}: Starting'.format(threading.currentThread().getName()))
        while True:
            self.fonk15()
            if self.b12:
                print('{}: Ending'.format(threading.currentThread().getName()))
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