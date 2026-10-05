import sys
class class1:
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
class class2:
    def fonk2(self, n):
        self.b3 = n[:]
    def fonk3(self):
        return len(self.b3)
    def fonk4(self, x):
        if x in self.b3:
            return True
        return False
    def fonk5(self):
        b4 = sys.maxsize
        b5 = None
        for node in self.b3:
            if node.b1 < b4:
                b4 = node.b1
                b5 = node
        self.b3.remove(b5)
        return b5.b2
if b6 = = "__main__":
    b7 = [class1(5, 0), class1(3, 1), class1(7, 2), class1(1, 3)]
    b8 = class2(b7)
    print("Initial queue length:", len(b8))
    print("Does queue contain node with b1 7?", b8.fonk4(7))
    print("Extracted minimum node index:", b8.fonk5())
    print("Queue length after extraction:", len(b8))