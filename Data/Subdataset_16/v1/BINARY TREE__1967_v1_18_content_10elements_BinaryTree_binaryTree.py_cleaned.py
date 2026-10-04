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
            try:
                self.b5 = class2.fonk4(b4)
            except Exception as e:
                raise e
    def fonk3(self):
        return self.fonk6()
    @staticmethod
    def fonk4(b4):
        if b4 is None:
            raise TypeError('input can not be None')
        if not isinstance(b4, str):
            raise TypeError('input must be str')
        if len(b4) < 3 or not b4.startswith('[') or not b4.endswith(']'):
            raise TypeError('input must be surrounded by brackets and can not be empty')
        b4 = b4[1:-1]
        b6 = b4.split(', ')
        if b6[0] == 'null':
            return None
        a1 = 1
        b7 = len(b6)
        b5 = class1(int(b6[0]))
        b8 = [b5]
        while a1 < b7:
            b9 = []
            for n in b8:
                if a1 < b7 and b6[a1] != 'null':
                    n.b2 = class1(int(b6[a1]))
                    b9.append(n.b2)
                a1 += 1
                if a1 < b7 and b6[a1] != 'null':
                    n.b3 = class1(int(b6[a1]))
                    b9.append(n.b3)
                a1 += 1
            b8 = b9
        return b5
    def fonk5(self):
        if self.b5:
            b10 = [self.b5]
            b11 = set()
            while b10:
                b12 = b10[-1]
                if not b12.b2 or b12.b2 in b11:
                    b10.pop()
                    b11.add(b12)
                    yield b12.b1
                    if b12.b3:
                        b10.append(b12.b3)
                else:
                    b10.append(b12.b2)
        raise StopIteration
    def fonk6(self):
        if self.b5:
            b10 = [self.b5]
            while b10:
                b12 = b10.pop()
                yield b12.b1
                if b12.b3:
                    b10.append(b12.b3)
                if b12.b2:
                    b10.append(b12.b2)
        raise StopIteration
    def fonk7(self):
        if self.b5:
            b10 = [self.b5]
            b11 = set()
            while b10:
                b12 = b10[-1]
                if (not b12.b2 or b12.b2 in b11) and (not b12.b3 or b12.b3 in b11):
                    b10.pop()
                    b11.add(b12)
                    yield b12.b1
                elif b12.b2 and b12.b2 not in b11:
                    b10.append(b12.b2)
                else:
                    b10.append(b12.b3)
        raise StopIteration
    def fonk8(self):
        if self.b5:
            b13 = deque([self.b5])
            while b13:
                b14 = b13.popleft()
                yield b14.b1
                if b14.b2:
                    b13.append(b14.b2)
                if b14.b3:
                    b13.append(b14.b3)
        raise StopIteration
if b15 = = '__main__':
    b4 = "[1, 2, 3, null, null, 4, 5]"
    b16 = class2(b4)
    print("Pre-order traversal:")
    for value in b16.fonk6():
        print(value, b17 = ' ')
    print("\nIn-order traversal:")
    for value in b16.fonk5():
        print(value, b17 = ' ')
    print("\nPost-order traversal:")
    for value in b16.fonk7():
        print(value, b17 = ' ')
    print("\nBFS traversal:")
    for value in b16.fonk8():
        print(value, b17 = ' ')