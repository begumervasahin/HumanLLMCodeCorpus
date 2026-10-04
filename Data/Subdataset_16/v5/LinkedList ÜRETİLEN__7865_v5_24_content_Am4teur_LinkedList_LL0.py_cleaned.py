class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
class class2:
    def fonk2(self):
        self.b3 = None
    def fonk3(self, b1):
        b4 = class1(b1)
        if self.b3 is None:
            self.b3 = b4
        else:
            b5 = self.b3
            while b5.b2:
                b5 = b5.b2
            b5.b2 = b4
    def fonk4(self):
        b5 = self.b3
        while b5:
            yield b5
            b5 = b5.b2
    def fonk5(self):
        b6 = [str(node.b1) for node in self]
        return ' -> '.join(b6)
def fonk6():
    b7 = class2()
    b7.fonk3(0)
    b7.fonk3(1)
    b7.fonk3(2)
    print("Linked List:")
    print(b7)
if b8 = = "__main__":
    fonk6()