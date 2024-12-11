import unittest
import random
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
class class2:
    def fonk2(self):
        self.b4 = None
    def fonk3(self, b1):
        self.b4 = self.fonk4(self.b4, b1)
    def fonk4(self, node, b1):
        if node is None:
            return class1(b1)
        if b1 < node.b1:
            node.b2 = self.fonk4(node.b2, b1)
        elif b1 > node.b1:
            node.b3 = self.fonk4(node.b3, b1)
        return node
    def fonk5(self):
        b5 = []
        self.fonk6(self.b4, b5)
        return b5
    def fonk6(self, node, b5):
        if node is not None:
            self.fonk6(node.b2, b5)
            b5.append(node.b1)
            self.fonk6(node.b3, b5)
    def fonk7(self, b1):
        self.b4 = self.fonk8(self.b4, b1)
    def fonk8(self, node, b1):
        if node is None:
            return None
        if b1 < node.b1:
            node.b2 = self.fonk8(node.b2, b1)
        elif b1 > node.b1:
            node.b3 = self.fonk8(node.b3, b1)
        else:
            if node.b2 is None:
                return node.b3
            else:
                node.b2 = self.fonk8(node.b2, b1)
        return node
    def fonk9(self, b1):
        self.b4 = self.fonk10(self.b4, b1)
    def fonk10(self, node, b1):
        if node is None:
            return None
        if b1 < node.b1:
            node.b2 = self.fonk10(node.b2, b1)
        elif b1 > node.b1:
            node.b3 = self.fonk10(node.b3, b1)
        else:
            if node.b3 is None:
                return node.b2
            else:
                node.b3 = self.fonk10(node.b3, b1)
        return node
    def fonk11(self):
        b5 = []
        b6 = []
        b7 = self.b4
        while True:
            if b7 is not None:
                b6.append(b7)
                b7 = b7.b2
            elif b6:
                b7 = b6.pop()
                b5.append(b7.b1)
                b7 = b7.b3
            else:
                break
        return b5
class class3(unittest.TestCase):
    def fonk12(self):
        b8 = class2()
        for value in (random.randint(0, 99) for _ in range(1000)):
            b8.fonk3(value)
        b9 = b8.fonk5()
        random.shuffle(b9)
        for value in b9:
            b8.fonk7(value)
        self.assertEqual(b8.fonk5(), [])
    def fonk13(self):
        b8 = class2()
        for value in (random.randint(0, 99) for _ in range(1000)):
            b8.fonk3(value)
        b9 = b8.fonk11()
        random.shuffle(b9)
        for value in b9:
            b8.fonk9(value)
        self.assertEqual(b8.fonk5(), [])
if b10 = = '__main__':
    unittest.main()