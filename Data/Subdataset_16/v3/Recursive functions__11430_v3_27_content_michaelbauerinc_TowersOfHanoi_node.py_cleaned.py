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
def fonk9():
    b5 = class1(1)
    b6 = class1(2)
    b7 = class1(3)
    b5.fonk2(b6)
    b6.fonk4(b5)
    b6.fonk2(b7)
    b7.fonk4(b6)
    b5.fonk7('image1.png')
    b6.fonk7('image2.png')
    b7.fonk7('image3.png')
    b8 = b5
    while b8:
        print(f'class1 Value: {b8.fonk6()}')
        print(f'class1 Image: {b8.fonk8()}')
        b8 = b8.fonk3()
if b9 = = '__main__':
    fonk9()