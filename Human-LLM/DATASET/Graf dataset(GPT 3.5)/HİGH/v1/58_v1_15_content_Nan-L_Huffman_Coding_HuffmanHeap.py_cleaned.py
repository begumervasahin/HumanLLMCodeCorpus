class class1(object):
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
    def fonk2(self):
        return self.b2
class class2(object):
    def fonk3(self, b4, b3 = None):
        self.b4 = b4
        self.b3 = b3 if b3 is not None else []
    def fonk4(self, b5):
        self.b3.append(b5)
    def fonk5(self):
        if len(self.b4) == 0 and len(self.b3) != 0:
            b5 = self.b3.pop(0)
        elif len(self.b3) == 0 and len(self.b4) != 0:
            b5 = self.b4.pop(0)
        elif len(self.b3) != 0 and len(self.b4) != 0:
            if self.b4[0].fonk2() >= self.b3[0].fonk2():
                b5 = self.b3.pop(0)
            else:
                b5 = self.b4.pop(0)
        else:
            print("b4 and b3 are both empty!")
            return None
        return b5
if b6 = = "__main__":
    b7 = [class1('a', 5), class1('b', 3)]
    b8 = [class1('c', 2), class1('d', 4)]
    b9 = class2(b7, b8)
    b9.fonk4(class1('e', 1))
    b10 = b9.fonk5()
    print("Smallest tree dequeued:", b10.b1, b10.b2)