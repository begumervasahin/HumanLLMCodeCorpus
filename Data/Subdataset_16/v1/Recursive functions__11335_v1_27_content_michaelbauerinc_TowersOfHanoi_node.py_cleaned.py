class class1:
    def fonk1(self, b2, b1 = None):
        self.b2 = b2
        self.b1 = b1
        self.b3 = None
        self.b4 = None
    def fonk2(self, b1):
        self.b1 = b1
    def fonk3(self):
        return self.b1
    def fonk4(self, b3):
        self.b3 = b3
    def fonk5(self):
        return self.b3
    def fonk6(self):
        return self.b2
    def fonk7(self, b4):
        self.b4 = b4
    def fonk8(self):
        return self.b4
if b5 = = '__main__':
    b6 = class1(1)
    b7 = class1(2)
    b8 = class1(3)
    b6.fonk2(b7)
    b7.fonk4(b6)
    b7.fonk2(b8)
    b8.fonk4(b7)
    b6.fonk7('image1.png')
    b7.fonk7('image2.png')
    b8.fonk7('image3.png')
    b9 = b6
    while b9 is not None:
        print(f'class1 Value: {b9.fonk6()}')
        print(f'class1 Image: {b9.fonk8()}')
        b9 = b9.fonk3()