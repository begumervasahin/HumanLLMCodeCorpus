from collections import deque
from .treeNode import treeNode
class class1:
    def fonk1(self, b1 = None):
        self.b2 = self.fonk3(b1) if b1 else None
    def fonk2(self):
        return self.fonk5()
    @staticmethod
    def fonk3(b1):
        if not isinstance(b1, str):
            raise TypeError('Input must be a string')
        if not b1.startswith('[') or not b1.endswith(']'):
            raise ValueError('Input must be surrounded by brackets and cannot be empty')
        b1 = b1[1:-1].split(', ')
        if b1[0] == 'null':
            return None
        b2 = treeNode(b1[0])
        b3 = [b2]
        a1 = 1
        while a1 < len(b1):
            b4 = []
            for node in b3:
                if a1 < len(b1) and b1[a1] != 'null':
                    node.b5 = treeNode(b1[a1])
                    b4.append(node.b5)
                a1 += 1
                if a1 < len(b1) and b1[a1] != 'null':
                    node.b6 = treeNode(b1[a1])
                    b4.append(node.b6)
                a1 += 1
            b3 = b4
        return b2
    def fonk4(self):
        if not self.b2:
            return
        b9, b7 = [self.b2], set()
        while b9:
            b8 = b9[-1]
            if not b8.b5 or b8.b5 in b7:
                b9.pop()
                b7.add(b8)
                yield b8.val
                if b8.b6:
                    b9.append(b8.b6)
            else:
                b9.append(b8.b5)
        raise StopIteration
    def fonk5(self):
        if not self.b2:
            return
        b9 = [self.b2]
        while b9:
            b8 = b9.pop()
            yield b8.val
            if b8.b6:
                b9.append(b8.b6)
            if b8.b5:
                b9.append(b8.b5)
        raise StopIteration
    def fonk6(self):
        if not self.b2:
            return
        b9, b7 = [self.b2], set()
        while b9:
            b8 = b9[-1]
            if (not b8.b5 or b8.b5 in b7) and (not b8.b6 or b8.b6 in b7):
                b9.pop()
                b7.add(b8)
                yield b8.val
            elif b8.b5 and b8.b5 not in b7:
                b9.append(b8.b5)
            else:
                b9.append(b8.b6)
        raise StopIteration
    def fonk7(self):
        if not self.b2:
            return
        b10 = deque([self.b2])
        while b10:
            b11 = b10.popleft()
            yield b11.val
            if b11.b5:
                b10.append(b11.b5)
            if b11.b6:
                b10.append(b11.b6)
        raise StopIteration