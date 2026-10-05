class class1:
    def fonk1(self, b1 = None, b2=None, b3=None):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
b4 = class1(b1="resize", b2="rectangle", b3=1)
print("Operation Type:", b4.b1)
print("Shape:", b4.b2)
print("Index:", b4.b3)