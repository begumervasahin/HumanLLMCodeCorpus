class class1:
    def fonk1(self, b2, b1 = None, b3=None, b4=None):
        self.b2 = b2
        self.b1 = b1
        self.b3 = b3
        self.b4 = b4
    def fonk2(self):
        return self.b2
    def fonk3(self):
        return f"class1(b2 = {self.b2}, b1={self.b1})"
class class2:
    def fonk4(self, b6, b5 = None):
        self.b6 = b6 if b6 is not None else []
        self.b5 = b5 if b5 is not None else []
    def fonk5(self, b12):
        self.b5.append(b12)
        self.b5.sort(b7 = lambda x: x.fonk2())
    def fonk6(self):
        if len(self.b6) == 0 and len(self.b5) > 0:
            return self.b5.pop(0)
        elif len(self.b5) == 0 and len(self.b6) > 0:
            return self.b6.pop(0)
        elif len(self.b5) > 0 and len(self.b6) > 0:
            if self.b6[0].fonk2() >= self.b5[0].fonk2():
                return self.b5.pop(0)
            else:
                return self.b6.pop(0)
        else:
            print("Both b6 and b5 lists are empty!")
            return None
if b8 = = "__main__":
    b9 = [class1(b2=5), class1(b2=10)]
    b10 = [class1(b2=2), class1(b2=8)]
    b11 = class2(b9, b10)
    b11.fonk5(class1(b2 = 3))
    print("Dequeued:", b11.fonk6())
    print("Dequeued:", b11.fonk6())
    while True:
        b12 = b11.fonk6()
        if b12 is None:
            break
        print("Dequeued:", b12)