class class1:
    def fonk1(self):
        self.b1 = []
        self.b2 = set()
    def fonk2(self, b3):
        self.b1.append(b3)
        self.b2.add(tuple(b3.b4))
    def fonk3(self):
        if not self.fonk4():
            b3 = self.b1.pop(0)
            self.b2.remove(tuple(b3.b4))
            return b3
        return None
    def fonk4(self):
        return len(self.b1) == 0
class class2:
    def fonk5(self, b4):
        self.b4 = b4
    def fonk6(self):
        return str(self.b4)
if b5 = = "__main__":
    b6 = class1()
    b6.fonk2(class2([1, 2, 3, 4, 5, 6, 7, 8, 0]))
    b6.fonk2(class2([1, 2, 3, 4, 5, 6, 0, 7, 8]))
    b6.fonk2(class2([1, 2, 3, 4, 5, 0, 6, 7, 8]))
    while not b6.fonk4():
        b2 = b6.fonk3()
        print("Dequeued:", b2)