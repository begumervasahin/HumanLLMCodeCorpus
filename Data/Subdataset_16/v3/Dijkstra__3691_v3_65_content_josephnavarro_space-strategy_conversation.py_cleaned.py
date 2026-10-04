class class1:
    def fonk1(self, b2, b1 = False):
        self.b2 = b2
        self.b1 = b1
        self.a1 = 0
    def fonk2(self, b13, b8):
        b13.append(f"Drawing '{self.b2[self.a1:]}' at {b8}")
class class2:
    def fonk3(self, texts, b3):
        self.b3 = b3
        self.b4 = []
        self.fonk4(texts)
        self.b5 = False
        self.a2 = 0
    def fonk4(self, texts):
        a3 = 3
        b6 = []
        for b7, text in enumerate(texts):
            b6.append(class1(text, b1 = True))
            if len(b6) >= a3 or b7 = = len(texts) - 1:
                while len(b6) < a3:
                    b6.append(class1('', b1 = True))
                self.b4.append(b6)
                b6 = []
    def fonk5(self, b13, b8 = None):
        if b8 is None:
            b8 = self.b3
        if self.b4:
            a4 = 0
            b9 = self.b4[self.a2]
            for text in b9:
                text.fonk5(b13, (b8[0], b8[1] + a4))
                if text.a1 < len(text.b2):
                    break
                a4 += 16
if b10 = = "__main__":
    b11 = [
        "Hello!",
        "How are you?",
        "This is a long message that might span multiple lines.",
        "This is another message.",
        "Final message here."
    ]
    b3 = (10, 20)
    b12 = class2(b11, b3)
    b13 = []
    b12.fonk5(b13)
    for item in b13:
        print(item)