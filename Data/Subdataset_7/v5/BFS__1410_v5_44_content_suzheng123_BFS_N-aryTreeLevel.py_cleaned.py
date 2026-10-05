from collections import deque
class class1:
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
class class2:
    def fonk2(self, root):
        if not root:
            return []
        b3 = deque([root])
        b4 = []
        while b3:
            b5 = []
            for _ in range(len(b3)):
                b6 = b3.popleft()
                b5.append(b6.b1)
                for child in b6.b2:
                    b3.append(child)
            b4.append(b5)
        return b4
