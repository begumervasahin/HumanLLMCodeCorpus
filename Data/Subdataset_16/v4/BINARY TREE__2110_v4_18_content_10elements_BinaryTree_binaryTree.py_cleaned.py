from .treeNode import treeNode
from collections import deque
class class1(object):
    def fonk1(self, b1 = None):
        if b1 is None:
            self.b2 = None
        else:
            try:
                self.b2 = class1.fonk3(b1)
            except Exception as e:
                raise e
    def fonk2(self):
        return self.fonk5()
    @staticmethod
    def fonk3(b1):
        if b1 is None:
            raise TypeError('Input cannot be None')
        if not isinstance(b1, str):
            raise TypeError('Input must be a string')
        if len(b1) < 3 or not b1.startswith('[') or not b1.endswith(']'):
            raise TypeError('Input must be surrounded by brackets and cannot be empty')
        b1 = b1[1:-1]
        b3 = b1.split(', ')
        if b3[0] == 'null':
            return None
        b2 = treeNode(b3[0])
        b4 = [b2]
        a1 = 1
        b5 = len(b3)
        while a1 < b5:
            b6 = []
            for node in b4:
                if a1 < b5 and b3[a1] != 'null':
                    node.b7 = treeNode(b3[a1])
                    b6.append(node.b7)
                a1 += 1
                if a1 < b5 and b3[a1] != 'null':
                    node.b8 = treeNode(b3[a1])
                    b6.append(node.b8)
                a1 += 1
            b4 = b6
        return b2
    def fonk4(self):
        if self.b2:
            b9 = [self.b2]
            b10 = {}
            while b9:
                b11 = b9[-1]
                if not b11.b7 or b11.b7 in b10:
                    b9.pop()
                    b10[b11] = True
                    yield b11.val
                    if b11.b8:
                        b9.append(b11.b8)
                else:
                    b9.append(b11.b7)
        raise StopIteration
    def fonk5(self):
        if self.b2:
            b9 = [self.b2]
            while b9:
                b11 = b9.pop()
                yield b11.val
                if b11.b8:
                    b9.append(b11.b8)
                if b11.b7:
                    b9.append(b11.b7)
        raise StopIteration
    def fonk6(self):
        if self.b2:
            b9 = [self.b2]
            b10 = {}
            while b9:
                b11 = b9[-1]
                if (not b11.b7 or b11.b7 in b10) and (not b11.b8 or b11.b8 in b10):
                    b9.pop()
                    b10[b11] = True
                    yield b11.val
                elif b11.b7 and b11.b7 not in b10:
                    b9.append(b11.b7)
                else:
                    b9.append(b11.b8)
        raise StopIteration
    def fonk7(self):
        if self.b2:
            b12 = deque([self.b2])
            while b12:
                b13 = b12.popleft()
                yield b13.val
                if b13.b7:
                    b12.append(b13.b7)
                if b13.b8:
                    b12.append(b13.b8)
        raise StopIteration