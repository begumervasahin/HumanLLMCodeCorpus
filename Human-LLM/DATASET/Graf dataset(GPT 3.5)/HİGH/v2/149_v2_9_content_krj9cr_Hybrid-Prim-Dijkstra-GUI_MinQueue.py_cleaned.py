import sys
class class1:
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
class class2:
    def fonk2(self, b3):
        self.b3 = b3[:]
    def fonk3(self):
        return len(self.b3)
    def fonk4(self, b1):
        for node in self.b3:
            if node.b1 = = b1:
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
    b3 = [class1(5, 0), class1(3, 1), class1(7, 2), class1(1, 3)]
    b7 = class2(b3)
    print("Initial queue length:", len(b7))
    print("Does queue contain node with b1 7?", b7.fonk4(7))
    print("Extracted minimum node index:", b7.fonk5())
    print("Queue length after extraction:", len(b7))