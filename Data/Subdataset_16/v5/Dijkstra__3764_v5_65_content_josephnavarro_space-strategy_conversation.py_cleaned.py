from text import Text
class class1:
    def fonk1(self, b10, b1):
        self.b1 = b1
        self.b2 = []
        self.fonk2(b10)
        self.b3 = False
        self.a1 = 0
    def fonk2(self, strings):
        a2 = 3
        b4 = []
        for b6, string in enumerate(strings):
            b4.append(Text(string, b5 = True))
            if len(b4) >= a2 or b6 = = len(strings) - 1:
                while len(b4) < a2:
                    b4.append(Text('', b5 = True))
                self.b2.append(b4)
                b4 = []
    def fonk3(self, b12, b7 = None):
        if b7 is None:
            b7 = self.b1
        if self.b2:
            a3 = 0
            b8 = self.b2[self.a1]
            for text in b8:
                text.fonk3(b12, (b7[0], b7[1] + a3))
                if text.current_position < len(text.content):
                    break
                a3 += 16
if b9 = = "__main__":
    b10 = [
        "Hello!",
        "How are you?",
        "This is a long message that might span multiple lines.",
        "This is another message.",
        "Final message here."
    ]
    b1 = (10, 20)
    b11 = class1(b10, b1)
    b12 = []
    b11.fonk3(b12)
    for item in b12:
        print(item)