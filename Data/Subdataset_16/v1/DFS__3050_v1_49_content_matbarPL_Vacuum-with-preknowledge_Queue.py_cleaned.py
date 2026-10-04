class class1:
    def fonk1(self):
        self.b1 = []
    def fonk2(self):
        return self.b1 = = []
    def fonk3(self, item):
        self.b1.insert(0, item)
    def fonk4(self):
        if not self.fonk9():
            return self.b1.pop()
        else:
            raise IndexError("dequeue from empty queue")
    def fonk5(self):
        if not self.fonk9():
            return self.b1[0]
        else:
            raise IndexError("first from empty queue")
    def fonk6(self):
        return len(self.b1)
    def fonk7(self, b1):
        for el in b1:
            self.fonk10(el)
class class2:
    def fonk8(self):
        self.b1 = []
    def fonk9(self):
        return self.b1 = = []
    def fonk10(self, item):
        self.b1.append(item)
    def fonk11(self):
        if not self.fonk9():
            return self.b1.pop()
        else:
            raise IndexError("dequeue from empty queue")
    def fonk12(self):
        return len(self.b1)
def fonk13():
    b2 = class1()
    b2.fonk10(1)
    b2.fonk10(2)
    b2.fonk10(3)
    print("class1 b1:", b2.b1)
    print("Dequeue from class1:", b2.fonk11())
    print("First item in class1:", b2.fonk5())
    print("class1 size:", b2.fonk12())
    b3 = class2()
    b3.fonk10(1)
    b3.fonk10(2)
    b3.fonk10(3)
    print("class2 b1:", b3.b1)
    print("Dequeue from class2:", b3.fonk11())
    print("class2 size:", b3.fonk12())
if b4 = = "__main__":
    fonk13()