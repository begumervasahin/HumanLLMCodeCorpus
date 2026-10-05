class class1:
    def fonk1(self):
        self.b1 = []
    def fonk2(self, item):
        self.b1.append(item)
    def fonk3(self):
        return self.b1.pop(0)
    def fonk4(self):
        return len(self.b1) == 0
    def fonk5(self):
        return len(self.b1)
def fonk6():
    b2 = class1()
    for i in range(1, 6):
        b2.fonk2(i)
    print("class1 size:", b2.fonk5())
    print("Dequeuing b1:")
    while not b2.fonk4():
        print(b2.fonk3())
    print("class1 size after dequeueing:", b2.fonk5())
if b3 = = '__main__':
    fonk6()