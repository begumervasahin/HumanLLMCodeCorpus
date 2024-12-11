class class1:
    def fonk1(self):
        self.b1 = ""
        self.a1 = 0
        self.a2 = 0
        self.a3 = 0
    def fonk2(self, b2):
        if self.b1[b2] in 'aeiou':
            return False
        if self.b1[b2] == 'y':
            if b2 = = self.a2:
                return True
            else:
                return not self.fonk2(b2 - 1)
        return True
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
                return True
        return False
    def fonk5(self, a3):
        if a3 < (self.a2 + 1):
            return False
        if self.b1[a3] != self.b1[a3 - 1]:
            return False
        return self.fonk2(a3)
    def fonk6(self, b2):
        if b2 < (self.a2 + 2) or not self.fonk2(b2) or self.fonk2(b2 - 1) or not self.fonk2(b2 - 2):
            return False
        b3 = self.b1[b2]
        if b3 in 'wx':
            return False
        return True
    def fonk7(self, s):
        b4 = len(s)
        if s[b4 - 1] != self.b1[self.a1]:
            return False
        if b4 > (self.a1 - self.a2 + 1):
            return False
        if self.b1[self.a1 - b4 + 1:self.a1 + 1] != s:
            return False
        self.a3 = self.a1 - b4
        return True
    def fonk8(self, s):
        b4 = len(s)
        self.b1 = self.b1[:self.a3 + 1] + s + self.b1[self.a3 + b4 + 1:]
        self.a1 = self.a3 + b4
    def fonk9(self, s):
        if self.fonk3() > 0:
            self.fonk8(s)
    def fonk10(self):
        if self.b1[self.a1] == 's':
            if self.fonk7("sses"):
                self.a1 -= 2
            elif self.fonk7("ies"):
                self.fonk8("b2")
            elif self.b1[self.a1 - 1] != 's':
                self.a1 -= 1
        if self.fonk7("eed"):
            if self.fonk3() > 0:
                self.a1 -= 1
        elif (self.fonk7("ed") or self.fonk7("ing")) and self.fonk4():
            self.a1 = self.a3
            if self.fonk7("at"):
                self.fonk8("ate")
            elif self.fonk7("bl"):
                self.fonk8("ble")
            elif self.fonk7("iz"):
                self.fonk8("ize")
            elif self.fonk5(self.a1):
                self.a1 -= 1
                b3 = self.b1[self.a1]
                if b3 in 'lsz':
                    self.a1 += 1
            elif (self.fonk3() == 1 and self.fonk6(self.a1)):
                self.fonk8("e")
    def fonk11(self):
        if self.fonk7("y") and self.fonk4():
            self.b1 = self.b1[:self.a1] + 'b2' + self.b1[self.a1 + 1:]
    def fonk12(self):
        if self.b1[self.a1 - 1] == 'b5':
            if self.fonk7("ational"):
                self.fonk9("ate")
            elif self.fonk7("tional"):
                self.fonk9("tion")
        elif self.b1[self.a1 - 1] == 'c':
            if self.fonk7("enci"):
                self.fonk9("ence")
            elif self.fonk7("anci"):
                self.fonk9("ance")
    def fonk13(self):
        if self.b1[self.a1] == 'e':
            if self.fonk7("icate"):
                self.fonk9("ic")
            elif self.fonk7("ative"):
                self.fonk9("")
            elif self.fonk7("alize"):
                self.fonk9("al")
    def fonk14(self):
        if self.b1[self.a1 - 1] == 'b5':
            if self.fonk7("al"):
                pass
        elif self.b1[self.a1 - 1] == 'c':
            if self.fonk7("ance") or self.fonk7("ence"):
                pass
    def fonk15(self):
        self.a3 = self.a1
        if self.b1[self.a1] == 'e':
            b5 = self.fonk3()
            if b5 > 1 or (b5 = = 1 and not self.fonk6(self.a1 - 1)):
                self.a1 -= 1
        if self.b1[self.a1] == 'l' and self.fonk5(self.a1) and self.fonk3() > 1:
            self.a1 -= 1
    def fonk16(self, p, b2, a3):
        self.b1 = p
        self.a1 = a3
        self.a2 = b2
        if self.a1 <= self.a2 + 1:
            return self.b1
        self.fonk10()
        self.fonk11()
        self.fonk12()
        self.fonk13()
        self.fonk14()
        self.fonk15()
        return self.b1[self.a2:self.a1 + 1]