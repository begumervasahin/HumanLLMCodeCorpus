from collections import defaultdict
import operator
class class1:
    def fonk1(self, modules):
        self.b1 = modules
        self.b2 = []
        self.b3 = []
        self.fonk2()
    def fonk2(self):
        print('Modules\t|\t', b4 = '')
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
            self.fonk5(interval)
    def fonk5(self, interval):
        b8 = [module.getResult(interval) for module in self.b1]
        b9 = self.fonk6(b8)
        b10 = self.fonk7(b9)
        self.fonk8(interval, b8, b10)
        self.b3.append(b10)
        self.b2.append(interval)
        self.fonk9(b8, b10)
    def fonk6(self, b8):
        b9 = defaultdict(int)
        for res in b8:
            b9[res] += 1
        return b9
    def fonk7(self, b9):
        return max(b9.items(), b11 = operator.itemgetter(1))[0]
    def fonk8(self, interval, b8, b10):
        print(f'{interval}\t|\t', b4 = '')
        for res in b8:
            print(f'{res}\t', b4 = '')
        print(b10)
    def fonk9(self, b8, b10):
        for i, module in enumerate(self.b1):
            b12 = {'status': 'ok'} if b8[i] == b10 else {'status': 'error', 'goodValue': b10}
            module.receiveFeedback(b12)