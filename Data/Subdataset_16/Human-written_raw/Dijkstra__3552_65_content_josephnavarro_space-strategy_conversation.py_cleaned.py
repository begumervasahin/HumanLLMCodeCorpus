from text import Text
class class1:
    def fonk1(self, strings, b1):
        self.b1 = b1
        self.b2 = []
        b3 = []
        a1 = 0
        for b5 in range(len(strings)):
            b3.append(Text(strings[b5], b4 = True))
            a1 += 1
            if a1 >= 3 or b5 = = len(strings)-1:
                b6 = len(b3)
                for i in range(3-b6):
                    b3.append(Text('', b4 = True))
                self.b2.append(b3)
                a1 = 0
                b3 = []
        self.b7 = False
        self.a2 = 0
    def fonk2(self, surface, b1 = (0,0)):
        a1 = 0
        if len(self.b2) > 0:
            for text in self.b2[self.a2]:
                text.fonk2(surface, (b1[0],b1[1]+a1*16))
                if text.a2 < len(text.text):
                    break
                else:
                    a1 += 1