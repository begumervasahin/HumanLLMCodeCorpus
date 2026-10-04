from collections import defaultdict
import operator
class class1:
    def fonk1(self, b14):
        self.b1 = b14
        self.b2 = []
        self.b3 = []
        print('b14\t|\t', b4 = '')
        for i, m in enumerate(b14):
            print(f'{m}\t', b4 = '')
        print('Winner')
    def fonk2(self, i, b5 = None, interval=None):
        if i < len(self.b1):
            if b5 is not None:
                self.b1[i].b6 = b5
            if interval is not None:
                self.b1[i].b7 = interval
    def fonk3(self, intervals):
        for interval in intervals:
            b8 = [module.fonk6(interval) for module in self.b1]
            b9 = defaultdict(int)
            print(f'{interval}\t|\t', b4 = '')
            for res in b8:
                print(f'{res}\t', b4 = '')
                b9[res] += 1
            b10 = max(b9.items(), key=operator.itemgetter(1))[0]
            print(b10)
            self.b3.append(b10)
            self.b2.append(interval)
            for i, module in enumerate(self.b1):
                b11 = {'status': 'ok'} if b8[i] == b10 else {'status': 'error', 'goodValue': b10}
                module.fonk7(b11)
    def fonk4(self, interval):
        b8 = [module.fonk6(interval) for module in self.b1]
        b9 = defaultdict(int)
        print(f'{interval}\t|\t', b4 = '')
        for res in b8:
            print(f'{res}\t', b4 = '')
            b9[res] += 1
        b10 = max(b9.items(), key=operator.itemgetter(1))[0]
        print(b10)
        self.b3.append(b10)
        self.b2.append(interval)
        for i, module in enumerate(self.b1):
            b11 = {'status': 'ok'} if b8[i] == b10 else {'status': 'error', 'goodValue': b10}
            module.fonk7(b11)
if b12 = = "__main__":
    class class2:
        def fonk5(self, b13):
            self.b13 = b13
            self.b6 = None
            self.b7 = None
        def fonk6(self, interval):
            return interval % 3
        def fonk7(self, b11):
            pass
        def fonk8(self):
            return self.b13
    b14 = [class2("Module1"), class2("Module2"), class2("Module3")]
    b15 = class1(b14)
    b15.fonk3([1, 2, 3, 4, 5])
    b15.fonk4(6)