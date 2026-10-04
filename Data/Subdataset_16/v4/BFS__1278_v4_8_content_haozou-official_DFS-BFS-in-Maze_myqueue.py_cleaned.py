class class1:
    def fonk1(self):
        self.b1 = []
    def fonk2(self, item):
        self.b1.insert(0, item)
    def fonk3(self):
        if not self.fonk4():
            return self.b1.pop()
        else:
            raise IndexError("Dequeue from an empty queue.")
    def fonk4(self):
        return len(self.b1) == 0
    def fonk5(self):
        return len(self.b1)
def fonk6():
    b2 = class1()
    b2.fonk2(1)
    b2.fonk2(2)
    b2.fonk2(3)
    b2.fonk2(4)
    b2.fonk2(5)
    print("class1 size after enqueuing 5 b1:", b2.fonk5())
    print("Dequeuing b1:")
    while not b2.fonk4():
        print(b2.fonk3())
    print("class1 size after dequeuing all b1:", b2.fonk5())
if b3 = = '__main__':
    fonk6()