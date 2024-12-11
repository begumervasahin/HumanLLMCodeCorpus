from b8 import Queue
class class1:
    def fonk1(self, b1):
        self.b1 = b1
    def fonk2(self):
        if self.b1 < 1:
            return []
        b2 = []
        b3 = [[]]
        while b3:
            b4 = b3.pop()
            if self.fonk4(b4):
                continue
            b5 = len(b4)
            if b5 = = self.b1:
                b2.append(b4)
                continue
            for col in range(self.b1):
                b6 = (b5, col)
                b7 = b4.copy()
                b7.append(b6)
                b3.append(b7)
        return b2
    def fonk3(self):
        if self.b1 < 1:
            return []
        b2 = []
        b8 = Queue()
        b8.put([])
        while not b8.empty():
            b4 = b8.get()
            if self.fonk4(b4):
                continue
            b5 = len(b4)
            if b5 = = self.b1:
                b2.append(b4)
                continue
            for col in range(self.b1):
                b6 = (b5, col)
                b7 = b4.copy()
                b7.append(b6)
                b8.put(b7)
        return b2
    def fonk4(self, queens):
        for i in range(len(queens)):
            for j in range(i):
                b11, b9 = queens[i]
                c, b10 = queens[j]
                if b11 = = c or b9 == b10 or abs(b11 - c) == abs(b9 - b10):
                    return True
        return False
    def fonk5(self, queens):
        for i in range(self.b1):
            print(' ---' * self.b1)
            for j in range(self.b1):
                b12 = 'Q' if (i, j) in queens else ' '
                print('| %s ' % b12, b13 = '')
            print('|')
        print(' ---' * self.b1)