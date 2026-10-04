class class1:
    def fonk1(self, b2, b1 = False):
        self.b2 = b2
        self.b1 = b1
        self.a1 = 0
    def fonk2(self, b13, b11):
        b13.append(f"Drawing '{self.b2[self.a1:]}' at {b11}")
class class2:
    def fonk3(self, b10, b3):
        self.b3 = b3
        self.b4 = []
        self.fonk4(b10)
        self.b5 = False
        self.a1 = 0
    def fonk4(self, b10):
        b6 = []
        a2 = 0
        for b7 in range(len(b10)):
            b6.append(class1(b10[b7], b1 = True))
            a2 += 1
            if a2 >= 3 or b7 = = len(b10) - 1:
                b8 = len(b6)
                for i in range(3 - b8):
                    b6.append(class1('', b1 = True))
                self.b4.append(b6)
                a2 = 0
                b6 = []
    def fonk5(self, b13, b3 = None):
        if b3 is None:
            b3 = self.b3
        a2 = 0
        if len(self.b4) > 0:
            for b2 in self.b4[self.a1]:
                b2.fonk5(b13, (b3[0], b3[1] + a2 * 16))
                if b2.a1 < len(b2.b2):
                    break
                else:
                    a2 += 1
if b9 = = "__main__":
    b10 = ["Hello!", "How are you?", "This is a long message that might span multiple lines.",
               "This is another message.", "Final message here."]
    b11 = (10, 20)
    b12 = class2(b10, b11)
    b13 = []
    b12.fonk5(b13)
    for item in b13:
        print(item)