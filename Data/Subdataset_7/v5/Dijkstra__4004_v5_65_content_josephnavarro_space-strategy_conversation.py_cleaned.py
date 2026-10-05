from text import Text
class class1:
    def fonk1(self, strings, b1):
        self.b1 = b1
        self.b2 = self.fonk2(strings)
        self.b3 = False
        self.a1 = 0
    def fonk2(self, strings):
        b4 = []
        b5 = []
        a2 = 0
        for b7 in strings:
            b5.append(Text(b7, b6 = True))
            a2 += 1
            if a2 >= 3 or b7 = = strings[-1]:
                b8 = 3 - len(b5)
                for _ in range(b8):
                    b5.append(Text('', b6 = True))
                b4.append(b5)
                a2 = 0
                b5 = []
        return b4
    def fonk3(self, surface, b1 = (0, 0)):
        a2 = 0
        if self.b2:
            for text in self.b2[self.a1]:
                text.fonk3(surface, (b1[0], b1[1] + a2 * 16))
                if text.a1 < len(text.text):
                    break
                else:
                    a2 += 1