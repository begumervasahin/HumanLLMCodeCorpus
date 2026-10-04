from collections import defaultdict
import operator
class class1:
    def fonk1(self, b14):
        self.b1 = b14
        self.b2 = []
        self.b3 = []
        self.fonk2()
    def fonk2(self):
        print('Interval\t|\t', b4 = '')
        for module in self.b1:
            print(f'{module}\t', b4 = '')
        print('Winner')
    def fonk3(self, index, b5 = None, interval=None):
        if index < len(self.b1):
            if b5 is not None:
                self.b1[index].b6 = b5
            if interval is not None:
                self.b1[index].b7 = interval
    def fonk4(self, intervals):
        for interval in intervals:
            self.fonk6(interval)
    def fonk5(self, interval):
        self.fonk6(interval)
    def fonk6(self, interval):
        b8 = [module.fonk9(interval) for module in self.b1]
        b9 = defaultdict(int)
        print(f'{interval}\t|\t', b4 = '')
        for result in b8:
            print(f'{result}\t', b4 = '')
            b9[result] += 1
        b10 = max(b9.items(), key=operator.itemgetter(1))[0]
        print(b10)
        self.b3.append(b10)
        self.b2.append(interval)
        self.fonk7(b8, b10)
    def fonk7(self, b8, b10):
        for i, module in enumerate(self.b1):
            b11 = {'status': 'ok'} if b8[i] == b10 else {'status': 'error', 'goodValue': b10}
            module.fonk10(b11)
if b12 = = "__main__":
    class class2:
        def fonk8(self, b13):
            self.b13 = b13
            self.b6 = None
            self.b7 = None
        def fonk9(self, interval):
            return interval % 3
        def fonk10(self, b11):
            pass
        def fonk11(self):
            return self.b13
    b14 = [class2("Module1"), class2("Module2"), class2("Module3")]
    b15 = class1(b14)
    b15.fonk4([1, 2, 3, 4, 5])
    b15.fonk5(6)