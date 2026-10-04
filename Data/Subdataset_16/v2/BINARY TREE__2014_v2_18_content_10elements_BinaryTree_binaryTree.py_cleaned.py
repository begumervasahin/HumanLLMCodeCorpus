from collections import deque
class class1:
    def fonk1(self, b1 = -1, b2=None, b3=None):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
class class2:
    def fonk2(self, b4 = None):
        if b4 is None:
            self.b5 = None
        else:
            self.b5 = self.fonk4(b4)
    def fonk3(self):
        return self.fonk6()
    @staticmethod
    def fonk4(b4):
        if not isinstance(b4, str):
            raise TypeError('Input must be a string')
        if len(b4) < 3 or not (b4.startswith('[') and b4.endswith(']')):
            raise ValueError('Input must be surrounded by brackets and cannot be empty')
        b4 = b4[1:-1].split(', ')
        if b4[0] == 'null':
            return None
        b5 = class1(int(b4[0]))
        b6 = deque([b5])
        a1 = 1
        while a1 < len(b4):
            b7 = b6.popleft()
            if b4[a1] != 'null':
                b7.b2 = class1(int(b4[a1]))
                b6.append(b7.b2)
            a1 += 1
            if a1 < len(b4) and b4[a1] != 'null':
                b7.b3 = class1(int(b4[a1]))
                b6.append(b7.b3)
            a1 += 1
        return b5
    def fonk5(self):
        if self.b5:
            b10, b8 = [], set()
            b9 = self.b5
            while b10 or b9:
                while b9:
                    b10.append(b9)
                    b9 = b9.b2
                b9 = b10.pop()
                yield b9.b1
                b9 = b9.b3
    def fonk6(self):
        if self.b5:
            b10 = [self.b5]
            while b10:
                b9 = b10.pop()
                yield b9.b1
                if b9.b3:
                    b10.append(b9.b3)
                if b9.b2:
                    b10.append(b9.b2)
    def fonk7(self):
        if self.b5:
            b10, b8 = [self.b5], set()
            while b10:
                b9 = b10[-1]
                if (not b9.b2 or b9.b2 in b8) and (not b9.b3 or b9.b3 in b8):
                    b10.pop()
                    b8.add(b9)
                    yield b9.b1
                else:
                    if b9.b3 and b9.b3 not in b8:
                        b10.append(b9.b3)
                    if b9.b2 and b9.b2 not in b8:
                        b10.append(b9.b2)
    def fonk8(self):
        if self.b5:
            b6 = deque([self.b5])
            while b6:
                b9 = b6.popleft()
                yield b9.b1
                if b9.b2:
                    b6.append(b9.b2)
                if b9.b3:
                    b6.append(b9.b3)
if b11 = = '__main__':
    b4 = "[1, 2, 3, null, null, 4, 5]"
    b12 = class2(b4)
    print("Pre-order traversal:")
    for value in b12.fonk6():
        print(value, b13 = ' ')
    print("\nIn-order traversal:")
    for value in b12.fonk5():
        print(value, b13 = ' ')
    print("\nPost-order traversal:")
    for value in b12.fonk7():
        print(value, b13 = ' ')
    print("\nBFS traversal:")
    for value in b12.fonk8():
        print(value, b13 = ' ')