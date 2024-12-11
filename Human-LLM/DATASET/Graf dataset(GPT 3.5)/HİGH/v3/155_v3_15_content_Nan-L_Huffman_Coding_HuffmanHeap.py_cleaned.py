class class1:
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
    def fonk2(self):
        return self.b2
class class2:
    def fonk3(self, b4, b3 = None):
        self.b4 = b4
        self.b3 = b3 if b3 is not None else []
    def fonk4(self, tree):
        self.b3.append(tree)
    def fonk5(self):
        if not self.b4 and self.b3:
            b5 = self.b3.pop(0)
        elif not self.b3 and self.b4:
            b5 = self.b4.pop(0)
        elif self.b4 and self.b3:
            if self.b4[0].fonk2() >= self.b3[0].fonk2():
                b5 = self.b3.pop(0)
            else:
                b5 = self.b4.pop(0)
        else:
            print("Both old and new lists are empty!")
            return None
        return b5
if b6 = = "__main__":
    b4 = [class1('a', 5), class1('b', 3)]
    b3 = [class1('c', 2), class1('d', 4)]
    b7 = class2(b4, b3)
    b7.fonk4(class1('e', 1))
    b5 = b7.fonk5()
    if b5:
        print("Smallest tree dequeued:", b5.b1, b5.b2)