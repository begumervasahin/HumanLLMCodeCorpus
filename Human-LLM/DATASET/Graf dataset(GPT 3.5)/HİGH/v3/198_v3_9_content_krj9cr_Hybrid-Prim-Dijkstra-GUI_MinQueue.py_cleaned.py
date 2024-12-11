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
        return any(node.b1 = = b1 for node in self.b3)
    def fonk5(self):
        b4 = min(self.b3, b1=lambda node: node.b1)
        self.b3.remove(b4)
        return b4.b2
if b5 = = "__main__":
    b3 = [class1(5, 0), class1(3, 1), class1(7, 2), class1(1, 3)]
    b6 = class2(b3)
    print("Initial queue length:", len(b6))
    print("Does queue contain node with b1 7?", b6.fonk4(7))
    print("Extracted minimum node index:", b6.fonk5())
    print("Queue length after extraction:", len(b6))