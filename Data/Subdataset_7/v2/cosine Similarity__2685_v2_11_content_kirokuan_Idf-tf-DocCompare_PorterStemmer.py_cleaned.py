class class1:
    def fonk1(self):
        self.b1 = ""
        self.a1 = 0
        self.a2 = 0
        self.a3 = 0
    def fonk2(self, b3):
        b2 = 'aeiou'
        if self.b1[b3] in b2:
            return False
        if self.b1[b3] == 'y':
            if b3 = = self.a2:
                return True
            else:
                return not self.fonk2(b3 - 1)
        return True
    def fonk3(self):
        a4 = 0
        b3 = self.a2
        while True:
            if b3 > self.a1:
                return a4
            if not self.fonk2(b3):
                break
            b3 += 1
        b3 += 1
        while True:
            while True:
                if b3 > self.a1:
                    return a4
                if self.fonk2(b3):
                    break
                b3 += 1
            b3 += 1
            a4 += 1
            while True:
                if b3 > self.a1:
                    return a4
                if not self.fonk2(b3):
                    break
                b3 += 1
            b3 += 1
    def fonk4(self):
        for b3 in range(self.a2, self.a1 + 1):
            if not self.fonk2(b3):
                return True
        return False
    def fonk5(self, j):
        if j < (self.a2 + 1):
            return False
        if self.b1[j] != self.b1[j - 1]:
            return False
        return self.fonk2(j)
    def fonk6(self, b3):
        if b3 < (self.a2 + 2) or not self.fonk2(b3) \
                or self.fonk2(b3 - 1) or not self.fonk2(b3 - 2):
            return False
        b4 = self.b1[b3]
        if b4 in 'wx':
            return False
        return True
    def fonk7(self, suffix):
        b5 = len(suffix)
        if suffix[b5 - 1] != self.b1[self.a3]:
            return False
        if b5 > (self.a3 - self.a2 + 1):
            return False
        if self.b1[self.a3 - b5 + 1:self.a3 + 1] != suffix:
            return False
        self.a1 = self.a3 - b5
        return True
    def fonk8(self, replacement):
        b5 = len(replacement)
        self.b1 = self.b1[:self.a1 + 1] + replacement + self.b1[self.a1 + b5 + 1:]
        self.a3 = self.a1 + b5
    def fonk9(self, suffix, replacement):
        if self.fonk7(suffix):
            self.fonk8(replacement)
    def fonk10(self):
        if self.b1[self.a3] == 's':
            if self.fonk7("sses"):
                self.a3 -= 2
            elif self.fonk7("ies"):
                self.fonk8("i")
            elif self.b1[self.a3 - 1] != 's':
                self.a3 -= 1
        if self.fonk7("eed"):
            if self.fonk3() > 0:
                self.a3 -= 1
        elif (self.fonk7("ed") or self.fonk7("ing")) and self.fonk4():
            self.a3 = self.a1
            if self.fonk7("at"):
                self.fonk8("ate")
            elif self.fonk7("bl"):
                self.fonk8("ble")
            elif self.fonk7("iz"):
                self.fonk8("ize")
            elif self.fonk5(self.a3):
                self.a3 -= 1
                b4 = self.b1[self.a3]
                if b4 in 'lsz':
                    self.a3 += 1
            elif (self.fonk3() == 1 and self.fonk6(self.a3)):
                self.fonk8("e")
    def fonk11(self):
        if (self.fonk7("y") and self.fonk4()):
            self.b1 = self.b1[:self.a3] + 'i' + self.b1[self.a3 + 1:]
    def fonk12(self):
        if self.b1[self.a3 - 1] == 'a':
            self.fonk9("ational", "ate")
            self.fonk9("tional", "tion")
        elif self.b1[self.a3 - 1] == 'c':
            self.fonk9("enci", "ence")
            self.fonk9("anci", "ance")
    def fonk13(self, b1):
        self.b1 = b1
        self.a3 = len(b1) - 1
        self.a2 = 0
        if self.a3 > self.a2 + 1:
            self.fonk10()
            self.fonk11()
        return self.b1[self.a2:self.a3 + 1]
if b6 = = "__main__":
    b7 = class1()
    b8 = ["caresses", "ponies", "ties", "caress", "cats", "feed", "agreed", "disabled",
             "matting", "mating", "meeting", "milling", "messing", "meetings"]
    for b1 in b8:
        print(f"{b1} -> {b7.fonk13(b1)}")