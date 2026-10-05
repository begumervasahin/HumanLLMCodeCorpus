class class1:
    def fonk1(self):
        self.b1 = ""
        self.a1 = 0
        self.a2 = 0
        self.a3 = 0
    def fonk2(self, b2):
        if self.b1[b2] in 'aeiou':
            return 0
        if self.b1[b2] == 'y':
            if b2 = = self.a2:
                return 1
            else:
                return not self.fonk2(b2 - 1)
        return 1
    def fonk3(self):
        a4 = 0
        b2 = self.a2
        while True:
            if b2 > self.a3:
                return a4
            if not self.fonk2(b2):
                break
            b2 += 1
        b2 += 1
        while True:
            while True:
                if b2 > self.a3:
                    return a4
                if self.fonk2(b2):
                    break
                b2 += 1
            b2 += 1
            a4 += 1
            while True:
                if b2 > self.a3:
                    return a4
                if not self.fonk2(b2):
                    break
                b2 += 1
            b2 += 1
    def fonk4(self):
        for b2 in range(self.a2, self.a3 + 1):
            if not self.fonk2(b2):
                return 1
        return 0
    def fonk5(self, a3):
        if a3 < (self.a2 + 1):
            return 0
        if self.b1[a3] != self.b1[a3-1]:
            return 0
        return self.fonk2(a3)
    def fonk6(self, b2):
        if b2 < (self.a2 + 2) or not self.fonk2(b2) or self.fonk2(b2-1) or not self.fonk2(b2-2):
            return 0
        b3 = self.b1[b2]
        if b3 in 'wx':
            return 0
        return 1
    def fonk7(self, s):
        b4 = len(s)
        if s[b4 - 1] != self.b1[self.a1]:
            return 0
        if b4 > (self.a1 - self.a2 + 1):
            return 0
        if self.b1[self.a1-b4+1:self.a1+1] != s:
            return 0
        self.a3 = self.a1 - b4
        return 1
    def fonk8(self, s):
        b4 = len(s)
        self.b1 = self.b1[:self.a3+1] + s + self.b1[self.a3+b4+1:]
        self.a1 = self.a3 + b4
    def fonk9(self, s):
        if self.fonk3() > 0:
            self.fonk8(s)
    def fonk10(self):
        if self.b1[self.a1] == 's':
            if self.fonk7("sses"):
                self.a1 = self.a1 - 2
            elif self.fonk7("ies"):
                self.fonk8("b2")
            elif self.b1[self.a1 - 1] != 's':
                self.a1 = self.a1 - 1
        if self.fonk7("eed"):
            if self.fonk3() > 0:
                self.a1 = self.a1 - 1
        elif (self.fonk7("ed") or self.fonk7("ing")) and self.fonk4():
            self.a1 = self.a3
            if self.fonk7("at"):   self.fonk8("ate")
            elif self.fonk7("bl"): self.fonk8("ble")
            elif self.fonk7("iz"): self.fonk8("ize")
            elif self.fonk5(self.a1):
                self.a1 = self.a1 - 1
                b3 = self.b1[self.a1]
                if b3 in 'lsz':
                    self.a1 = self.a1 + 1
            elif (self.fonk3() == 1 and self.fonk6(self.a1)):
                self.fonk8("e")
    def fonk11(self):
        if (self.fonk7("y") and self.fonk4()):
            self.b1 = self.b1[:self.a1] + 'b2' + self.b1[self.a1+1:]
    def fonk12(self):
        if self.b1[self.a1 - 1] == 'a':
            if self.fonk7("ational"):   self.fonk9("ate")
            elif self.fonk7("tional"):  self.fonk9("tion")
        elif self.b1[self.a1 - 1] == 'c':
            if self.fonk7("enci"):      self.fonk9("ence")
            elif self.fonk7("anci"):    self.fonk9("ance")
    def fonk13(self, word):
        self.b1 = word
        self.a1 = len(word) - 1
        self.a2 = 0
        if self.a1 > self.a2 + 1:
            self.fonk10()
            self.fonk11()
        return self.b1[self.a2:self.a1+1]
if b5 = = "__main__":
    b6 = class1()
    b7 = ["caresses", "ponies", "ties", "caress", "cats", "feed", "agreed", "disabled",
             "matting", "mating", "meeting", "milling", "messing", "meetings"]
    for word in b7:
        print(f"{word} -> {b6.fonk13(word)}")