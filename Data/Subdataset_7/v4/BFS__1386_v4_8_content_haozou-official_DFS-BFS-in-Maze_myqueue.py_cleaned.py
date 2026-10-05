class class1:
    def fonk1(self):
        self.b1 = []
    def fonk2(self, item):
        self.b1.insert(0, item)
    def fonk3(self):
        return self.b1.pop()
    def fonk4(self):
        return self.b1 = = []
    def fonk5(self):
        return len(self.b1)
def fonk6():
    b2 = class1()
    b2.fonk2(1)
    b2.fonk2(2)
    b2.fonk2(3)
    b2.fonk2(4)
    b2.fonk2(5)
    print("class1 size:", b2.fonk5())
    print("Dequeuing b1:")
    while not b2.fonk4():
        print(b2.fonk3())
    print("class1 size after dequeueing:", b2.fonk5())
if b3 = = '__main__':
    fonk6()