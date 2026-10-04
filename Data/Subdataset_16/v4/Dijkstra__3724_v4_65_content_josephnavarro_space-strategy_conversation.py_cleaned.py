from text import Text
class class1:
    def fonk1(self, strings, b1):
        self.b1 = b1
        self.b2 = []
        self.fonk2(strings)
        self.b3 = False
        self.a1 = 0
    def fonk2(self, strings):
        a2 = 3
        b4 = []
        a3 = 0
        for string in strings:
            b4.append(Text(string, b5 = True))
            a3 += 1
            if a3 >= a2 or len(b4) == len(strings):
                while len(b4) < a2:
                    b4.append(Text('', b5 = True))
                self.b2.append(b4)
                b4 = []
                a3 = 0
    def fonk3(self, b10, b6 = None):
        if b6 is None:
            b6 = self.b1
        if self.b2:
            a4 = 0
            for text in self.b2[self.a1]:
                text.fonk3(b10, (b6[0], b6[1] + a4))
                if text.current_position < len(text.content):
                    break
                a4 += 16
if b7 = = "__main__":
    b8 = [
        "Hello!",
        "How are you?",
        "This is a long message that might span multiple lines.",
        "This is another message.",
        "Final message here."
    ]
    b1 = (10, 20)
    b9 = class1(b8, b1)
    b10 = []
    b9.fonk3(b10)
    for item in b10:
        print(item)