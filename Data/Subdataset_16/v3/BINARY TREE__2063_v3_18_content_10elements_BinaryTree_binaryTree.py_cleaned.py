from collections import deque
class class1:
    def fonk1(self, b1 = -1, b2=None, b3=None):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
class class2:
    def fonk2(self, b4 = None):
        self.b5 = self.fonk4(b4) if b4 else None
    def fonk3(self):
        return self.fonk6()
    @staticmethod
    def fonk4(b4):
        if not isinstance(b4, str):
            raise TypeError('Input must be a string')
        if len(b4) < 3 or not (b4.startswith('[') and b4.endswith(']')):
            raise ValueError('Input must be surrounded by brackets and cannot be empty')
        b6 = b4[1:-1].split(', ')
        if b6[0] == 'null':
            return None
        b5 = class1(int(b6[0]))
        b7 = deque([b5])
        a1 = 1
        while a1 < len(b6):
            b8 = b7.popleft()
            if b6[a1] != 'null':
                b8.b2 = class1(int(b6[a1]))
                b7.append(b8.b2)
            a1 += 1
            if a1 < len(b6) and b6[a1] != 'null':
                b8.b3 = class1(int(b6[a1]))
                b7.append(b8.b3)
            a1 += 1
        return b5
    def fonk5(self):
        if not self.b5:
            return
        b9 = []
        b10 = self.b5
        while b9 or b10:
            while b10:
                b9.append(b10)
                b10 = b10.b2
            b10 = b9.pop()
            yield b10.b1
            b10 = b10.b3
    def fonk6(self):
        if not self.b5:
            return
        b9 = [self.b5]
        while b9:
            b8 = b9.pop()
            yield b8.b1
            if b8.b3:
                b9.append(b8.b3)
            if b8.b2:
                b9.append(b8.b2)
    def fonk7(self):
        if not self.b5:
            return
        b9, b11 = [self.b5], set()
        while b9:
            b8 = b9[-1]
            if (not b8.b2 or b8.b2 in b11) and (not b8.b3 or b8.b3 in b11):
                b9.pop()
                b11.add(b8)
                yield b8.b1
            else:
                if b8.b3 and b8.b3 not in b11:
                    b9.append(b8.b3)
                if b8.b2 and b8.b2 not in b11:
                    b9.append(b8.b2)
    def fonk8(self):
        if not self.b5:
            return
        b7 = deque([self.b5])
        while b7:
            b8 = b7.popleft()
            yield b8.b1
            if b8.b2:
                b7.append(b8.b2)
            if b8.b3:
                b7.append(b8.b3)
if b12 = = '__main__':
    b4 = "[1, 2, 3, null, null, 4, 5]"
    b13 = class2(b4)
    print("Pre-order traversal:")
    for value in b13.fonk6():
        print(value, b14 = ' ')
    print("\nIn-order traversal:")
    for value in b13.fonk5():
        print(value, b14 = ' ')
    print("\nPost-order traversal:")
    for value in b13.fonk7():
        print(value, b14 = ' ')
    print("\nBFS traversal:")
    for value in b13.fonk8():
        print(value, b14 = ' ')