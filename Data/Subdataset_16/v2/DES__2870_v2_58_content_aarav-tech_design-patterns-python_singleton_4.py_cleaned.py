
class class1(type):
    b1 = {}
    def fonk1(cls, *args, **kwargs):
        if cls not in cls.b1:
            cls.b1[cls] = super().fonk1(*args, **kwargs)
        return cls.b1[cls]
class class2(b2 = class1):
    def fonk2(self):
        self.b3 = "Not Connected"
    def fonk3(self):
        self.b3 = "Disconnected"
    def fonk4(self):
        self.b3 = "Connected"
def fonk5():
    b4 = class2()
    print("Client 1:", b4)
    print("Client 1 b3:", b4.b3)
    b5 = class2()
    print("Client 2:", b5)
    b5.fonk4()
    print("Client 1 b3 after b5 connects:", b4.b3)
    b4.fonk3()
    print("Client 2 b3 after b4 disconnects:", b5.b3)
if b6 = = "__main__":
    fonk5()